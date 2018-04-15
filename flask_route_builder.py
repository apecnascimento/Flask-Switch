import pkgutil

from flask import current_app


class RouterBuilder(object):
    def __init__(self, app=None, blueprints_package=None):
        self._app = app

        #: The name where blueprints are.
        self._blueprints_package = blueprints_package or 'blueprints'

        if app is not None:
            self.init_app(app)

    def _format_route(self, blueprint, blueprints_package):
        return '{0}.{1}.main'.format(blueprints_package, blueprint), blueprint

    def init_app(self, app):
        app.config.setdefault('ROUTER_BUILDER_URL_PREFIX', None)

        #: List all blueprints in the application blueprints package and return a list of tuples with (url, module_name)
        blueprints = [self._format_route(module_name, self._blueprints_package) for _, module_name, _ in
                      pkgutil.iter_modules(['blueprints'])]

        for module_namespace, module_name in blueprints:
            blueprint = __import__(module_namespace, globals(), locals(), [module_name], 0)
            if current_app.config['ROUTER_BUILDER_URL_PREFIX'] is not None:
                self._flask_app.register_blueprint(getattr(blueprint, module_name),
                                                   url_prefix='/{0}/{1}'.format(
                                                       current_app.config['ROUTER_BUILDER_URL_PREFIX'], module_name))
            else:
                self._flask_app.register_blueprint(getattr(blueprint, module_name),
                                                   url_prefix='/{0}'.format(module_name))

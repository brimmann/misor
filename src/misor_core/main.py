from django.http import HttpResponse
from django.urls import path
from .utils import create_model, view_model, parse_subpath
import logging
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator

logger = logging.getLogger("misor")


class _Misor:
    def __init__(self):
        self.models = None
        self._urls = []

    def register(self, *models):
        self.models = models

    def get_tables(self):
        return self.models

    def handle(self):
        self.generate_urls()

    def get_models_dict(self):
        return {model.__name__.lower(): model for model in self.models}
    
    @method_decorator(never_cache)
    def view(self, request, subpath):
        logger.info("---------------------------------------------")
        logger.info("##### VIEW CALLED #####")
        action, model_name = parse_subpath(subpath)
        model = self.get_models_dict().get(model_name)

        if action == "create":
            return create_model(model, request)
        elif action == "view":
            return view_model(model, request)
        else:
            # TODO: implement 404
            return HttpResponse("Hey there")

    def get_urls(self):
        return self._urls

    def generate_urls(self):
        for model in self.models:
            temp_path = path(model.__name__.lower(), self.view)
            self._urls.append(temp_path)


misor = _Misor()

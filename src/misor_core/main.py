from django.http import HttpResponse
from django.urls import path
from .utils import create_model, view_model, parse_subpath, dashboard
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
    def view(self, request, subpath=None):
        logger.info("---------------------------------------------")
        logger.info("##### VIEW CALLED #####")
        model_name = ""
        if subpath:
            action, model_name = parse_subpath(subpath)
        else:
            response = dashboard(request)
            response.context_data["model_names"] = self.get_models_dict().keys()
            response.context_data["current_model"] = model_name
            return response
        model = self.get_models_dict().get(model_name)
        if action == "create":
            response = create_model(model, request)
            response.context_data["model_names"] = self.get_models_dict().keys()
            response.context_data["current_model"] = model_name
            return response
        elif action == "view":
            response = view_model(model, request)
            response.context_data["model_names"] = self.get_models_dict().keys()
            response.context_data["current_model"] = model_name
            return response
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

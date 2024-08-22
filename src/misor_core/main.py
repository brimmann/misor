from django.http import HttpResponse
from django.urls import path
from .utils import get_model_to_pass, create_model, view_model


class _Misor:
    def __init__(self):
        self.models = None
        self._urls = []

    def set_misor(self, *models):
        self.models = models

    def get_tables(self):
        return self.models

    def handle(self):
        self.generate_urls()
        # print(self._urls)

    def view(self, request, subpath):
        print("view", request, subpath)
        path_components = subpath.strip('/').split('/')
        action = path_components[1] if len(path_components) > 1 else "view"

        if action == "create":
            return create_model(get_model_to_pass(self.models, path_components[0]), request)
        elif action == "view":
            return view_model(get_model_to_pass(self.models, path_components[0]), request)
        else:
            return HttpResponse("Hey there")

    def get_urls(self):
        return self._urls

    def generate_urls(self):
        for model in self.models:
            temp_path = path(model.__name__.lower(), self.view)
            self._urls.append(temp_path)


misor = _Misor()

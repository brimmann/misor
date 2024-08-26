from django.http import HttpResponse
from django.template import loader
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field, Button, Row, Column, HTML, ButtonHolder, Div, Hidden
from crispy_forms.bootstrap import InlineField
from django import forms
from django.shortcuts import redirect, render
import logging
logger = logging.getLogger("misor")


# TODO: Remove this class later
class ProductFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.template = 'formset_table.html'


def view_model(model, request):
    helper = FormHelper()

    ModelFormset = forms.modelformset_factory(model, fields='__all__', extra=0)
    model_formset = ModelFormset(queryset=model.objects.all())

    if model_formset.__len__() > 0:
        for form in model_formset:
            form.helper = FormHelper()
            form.helper.field_template = "field.html"
            form.helper.form_show_labels = False
            for field in form.fields.values():
                field.disabled = True

    return render(request, 'view.html', {"formset": model_formset})


def create_model(model, request):
    # TODO: Unify the logic for both create and other views
    # helper = FormHelper()
    # helper.add_input(Submit("submit", "Save"))
    ModelFormset = forms.modelformset_factory(model, fields='__all__', extra=1)
    if request.method == "POST":
        model_formset = ModelFormset(request.POST)
        logger.debug(f"_thevom {model_formset}")
        # helper.form_show_labels = False
        # TODO: Remove this line later
        # helper.form_class = "row g-3 align-items-center"
        logger.debug("form isn't valid 1")
        model_formset.save()
        return redirect(f'/mis/{model.__name__.lower()}')
        for form in model_formset:
            form.helper = FormHelper()
            form.helper.field_template = "field.html"
            form.helper.form_show_labels = False
            logger.debug("form isn't valid")
            logger.debug("form is valid")
            

    else:
        model_formset = ModelFormset(queryset=model.objects.none())
        # TODO: Remove this line later
        # helper.form_class = "row g-3 align-items-center"
        for form in model_formset:
            form.helper = FormHelper()
            form.helper.field_template = "field.html"
            form.helper.form_show_labels = False

    return render(request, 'create.html', {"formset": model_formset})


# TODO: remove it later, i think there is not need for it anymore
def get_model_to_pass(models, model_name):
    models_dict = {model.__name__.lower(): model for model in models}
    return models_dict.get(model_name)


def parse_subpath(subpath):
    path_components = subpath.strip('/').split('/')
    return path_components[1] if len(path_components) > 1 else "view", path_components[0]

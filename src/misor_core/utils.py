from django.http import HttpResponse
from django.template import loader
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from django import forms
from django.shortcuts import redirect, render


class ProductFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.template = 'formset_table.html'


def view_model(model, request):
    helper = ProductFormHelper()

    ModelFormset = forms.modelformset_factory(model, fields='__all__', extra=0)
    model_formset = ModelFormset(queryset=model.objects.all())
    print(model_formset.__len__())
    if model_formset.__len__() > 0:
        helper.layout = Layout(
            *[Field(field_name, disabled=True) for field_name in model_formset.forms[0].fields]
        )
        print(*[field_name for field_name in model_formset.forms[0].fields])
    return render(request, 'create.html', {"formset": model_formset, "helper": helper})


def create_model(model, request):
    helper = ProductFormHelper()
    helper.add_input(Submit("submit", "Save"))
    ModelFormset = forms.modelformset_factory(model, fields='__all__', extra=1)
    if request.method == "POST":
        model_formset = ModelFormset(request.POST)
        if model_formset.is_valid():
            model_formset.save()
            return redirect(f'/mis/{model.__name__.lower()}')
    else:
        model_formset = ModelFormset(queryset=model.objects.none())

    return render(request, 'create.html', {"formset": model_formset, "helper": helper})


def get_model_to_pass(models, model_name):
    models_dict = {model.__name__.lower(): model for model in models}
    return models_dict.get(model_name)

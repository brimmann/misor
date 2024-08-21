from django import forms
from .models import Product
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price']


ProductFormSet = forms.modelformset_factory(Product, form=ProductForm, extra=3)


class ProductFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.layout = Layout(
            'price',
            'name'
        )
        self.add_input(Submit("submit", "Save"))
        self.template = 'formset_table.html'
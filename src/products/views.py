from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader
from .models import Product
from .forms import ProductFormSet, ProductFormHelper


# print("Loader", loader.get_template("products/product_list.html"))
def product_list(request):
    products = Product.objects.all()
    try:
        template = loader.get_template("product_list.html")
        rendered_template = template.render({"products": products}, request)
        return HttpResponse(rendered_template)
    except Exception as e:
        print(f"error is: {e.chain}")

    return HttpResponse("Template not found!")


def create_multiple_products(request):
    helper = ProductFormHelper()
    if request.method == "POST":
        formset = ProductFormSet(request.POST)
        if formset.is_valid():
            formset.save()
            return redirect('product_list')
    else:
        formset = ProductFormSet(queryset=Product.objects.none())

    return render(request, 'product_formset.html', {"formset": formset, "helper": helper})

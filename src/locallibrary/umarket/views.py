from django.shortcuts import render
from umarket.models import Profile, Product
from django.views import generic


# Create your views here.
def index(request):
    context={}
    return render(request, 'home_page.html', context=context)


class UserDetailView(generic.DetailView):
    model = Profile
    template_name = "user_page.html"

class BrowserView(generic.ListView):
    model = Product
    template_name = "browser_page.html"
    context_object_name = 'browser_list'
    paginate_by = 10

class ProductListView2(generic.ListView):
    model = Product
    template_name = "user_page.html"
    context_object_name = 'user_list'
    paginate_by = 10



class ProductDetailView(generic.DetailView):
	model = Product
	template_name = "product_page.html"



# def product_detail_view(request, primary_key):
#     try:
#         product = Product.objects.get(pk=primary_key)
#     except product.DoesNotExist:
#         raise Http404('Book does not exist')
#
#     return render(request, 'product_page.html', context={'product': product})

def product_detail_view(request, primary_key):
    product = Product()
    try:
        products = Product.objects.all()
        for p in products:
            if primary_key in p.productID:
                product = p

    except product.DoesNotExist:
        raise Http404('Book does not exist')

    return render(request, 'product_page.html', context={'product': product})

def about (request):
	context={}
	return render(request, 'about_page.html', context=context)

def logout(request):
    context={}
    return render(request, 'logged_out.html', context=context)

def product(request):
    context={}
    return render(request, 'product_add_page.html', context=context)

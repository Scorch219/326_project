from django.shortcuts import render
from umarket.models import UserAccount, Product
from django.views import generic

# Create your views here.
def index(request):
    context={}
    return render(request, 'home_page.html', context=context)

class UserDetailView(generic.DetailView):
    model = UserAccount
    template_name = "user_page.html"

class ProductListView(generic.ListView):
	model = Product
	template_name = "browser_page.html"
	template_name2 = "user_page.html"
	paginate_by = 10


class ProductDetailView(generic.DetailView):
	model = Product
	template_name = "product_page.html"

def product_detail_view(request, primary_key):
    try:
        product = Product.objects.get(pk=primary_key)
    except product.DoesNotExist:
        raise Http404('Book does not exist')

    return render(request, 'product_page.html', context={'product': product})

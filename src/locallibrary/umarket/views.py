from django.shortcuts import render
from umarket.models import Profile, Product
from django.views import generic
from django.views.generic.edit import CreateView, ModelFormMixin
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


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

    def get_queryset(self): return ( Product.objects.filter(seller=self.request.user.profile) )
    def get_context_data(self, **kwargs):
        context = super(ProductListView2, self).get_context_data(**kwargs)
        context['favorited'] = Product.objects.filter(favorited=self.request.user.profile)
        # Add any other variables to the context here
        ...
        return context

class ProductAdd(CreateView):
    model = Product
    template_name = "product_add_page.html"
    fields = ['name', 'picture', 'description', 'price', 'category']
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.seller_rating = self.request.user.profile.rating
        self.object.seller = self.request.user.profile
        self.object.save()

        return super(ModelFormMixin, self).form_valid(form)

#requires guest/unauthorized user to login if they press "I'm Interested" for wishlist.
@login_required
def favorite(request, product_id):
    if product_id:
        product = Product.objects.get(id=product_id)
        product.favorited = request.user.profile
        product.save()
        return HttpResponseRedirect('/umarket/products/%s' % product_id)
    else:
        return HttpResponseRedirect('/browser_page')

class ProductDetailView(generic.DetailView):
	model = Product
	template_name = "product_page.html"

# def product_detail_view(request, primary_key):
#     product = Product()
#     try:
#         products = Product.objects.all()
#         for p in products:
#             if primary_key in p.productID:
#                 product = p
#
#     except product.DoesNotExist:
#         raise Http404('Book does not exist')
#
#     return render(request, 'product_page.html', context={'product': product})

def about (request):
	context={}
	return render(request, 'about_page.html', context=context)

def logout(request):
    context={}
    return render(request, 'logged_out.html', context=context)

def product(request):
    context={}
    return render(request, 'product_add_page.html', context=context)

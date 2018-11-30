from django.urls import path
from umarket import views
from django.conf.urls import url

urlpatterns = [
	path('', views.index, name="home-page"),
	path('products/<int:pk>', views.ProductDetailView.as_view(), name="product-detail"),
	path('user/<int:pk>', views.UserDetailView.as_view(), name="user-detail"),
	path("browser_page/", views.BrowserView.as_view(), name="browser-page"),
	path("user/", views.ProductListView2.as_view(), {'user_page.html': '/umarket/templates/'}, name="user"),
	path("about_page/", views.about, name="about-page"),
	path("new_product/", views.ProductAdd.as_view(), name="new-product"),
	url(r'^products/(?P<product_id>\d+)/$', views.favorite, name='favorite')
]

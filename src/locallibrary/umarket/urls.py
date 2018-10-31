from django.urls import path
from umarket import views

urlpatterns = [
	path('', views.index, name="home_page"),
	#path('products/', views.ProductBrowsing.as_view(), name="product-browsing"),
	path('products/<int:pk>', views.ProductDetailView.as_view(), name="product-detail"),
	path('user/<int:pk', views.UserDetailView.as_view(), name="user-detail"),
	path("browser_page/", views.ProductListView.as_view(), name="products"),
	path("user/", views.ProductListView.as_view(), {'user_page.html': '/umarket/templates/'}, name="user"),
]

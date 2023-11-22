from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


from accounts.views import signup, logout_user, login_user
from configomatic.views import configomatic
from djangotests import settings
from store.views import index, product_detail, add_to_cart, cart, delete_cart, produits, search_products, tri

urlpatterns = [
    path('', index, name="index"),
    path('admin/', admin.site.urls),
    path('signup/', signup, name="signup"),
    path('login/', login_user, name="login"),
    path('logout/', logout_user, name="logout"),
    path('cart/', cart, name="cart"),
    path('product/<str:slug>', product_detail, name="product"),
    path('product/<str:slug>/add-to-cart', add_to_cart, name="add-to-cart"),
    path('cart/delete/', delete_cart, name="delete-cart"),
    path('store/produits.html', produits, name='produits'),
    path('configomatic.html', configomatic, name='configomatic'),
    path('search/', search_products, name='search_products'),
    path('tri/', tri, name='tri'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

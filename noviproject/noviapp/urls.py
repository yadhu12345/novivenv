from django.urls import path
from . import views
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register/', register, name="register"),
    path('login/', loginPage, name="login"),
    path('logout/', logoutUser, name="logout"),
    path('', home, name="home"),
    path('cart/', cart, name="cart"),
    path('add_to_cart/<int:id>', views.cart_add, name="add_to_cart"),
    path('remove-from-cart/<int:cart_id>/', remove_from_cart, name="remove_from_cart"),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
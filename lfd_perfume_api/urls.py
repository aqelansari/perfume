from django.contrib import admin
from django.urls import path,include
from user_management.views import CustomAuthLogin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-token-auth/', CustomAuthLogin.as_view(), name='api-token-auth/'),
    path('user_management/', include('user_management.urls')),
    path('company/', include('company.urls')),
    path('order/', include('customer_order.urls')),
    path('ingredient/', include('ingredient.urls')),
    path('inventory/', include('inventory.urls')),
    path('recipe/', include('recipe.urls')),
    path('container/', include('container.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

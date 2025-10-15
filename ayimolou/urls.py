from django.contrib import admin
from django.urls import path, include
from accounts.views import RegisterView, LoginView

urlpatterns = [
    path('admin/', admin.site.urls),

    # Authentification
    path('api/accounts/register/', RegisterView.as_view(), name='register'),
    path('api/accounts/login/', LoginView.as_view(), name='login'),

    # Vendors
    path('api/vendors/', include('vendors.urls')),
]

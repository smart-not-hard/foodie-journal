from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/v1/', include('recipes.urls')),
    path('api/v1/recipes/', include('recipes.urls')),
    # path('', include('django.contrib.auth.urls')),
    path('custom-users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('api-auth/', include('rest_framework.urls')), 
    path('/api-auth/login/', include('users.urls'), name='home'),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]

# urlpatterns = [
#     path('', TemplateView.as_view(template_name='home.html'),name='home'),
#     path('admin/', admin.site.urls),
#     path('users/', include('users.urls')),
#     path('users/', include('django.contrib.auth.urls')),
# ]
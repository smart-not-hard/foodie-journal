from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include('recipes.urls')),

    # path('', include('django.contrib.auth.urls')),

    path('users/', include('users.urls')),

    # path('users/', include('django.contrib.auth.urls')),

    path('api-auth/', include('rest_framework.urls')), 
    
    # path('/api-auth/login/', include('users.urls')),

    path('api/token/', jwt_views.TokenObtainPairView.as_view()),

    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view()),
]
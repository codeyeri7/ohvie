from django.urls import path, include
from . import views
from rest_framework_jwt.views import obtain_jwt_token
# from django.conf.urls import url

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup),
    path('api-token-auth/', obtain_jwt_token),
    path('myprofile/', views.my_profile),
    # path('login/', views.login),
    # path('logout/', views.logout),
    # ...,
    # path('rest-auth/', include('rest_auth.urls')),
    # path('rest-auth/registration/', include('rest_auth.registration.urls')),

    # url(r'^rest-auth/', include('rest_auth.urls')),

    # url(r'^rest-auth/registration/', include('rest_auth.registration.urls'))

    # path('api-auth/', include('rest_framework.urls')),
    # path('api/rest-auth/', include('rest_auth.urls')),

]

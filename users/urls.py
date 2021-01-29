from django.urls import path
from users.views import home

urlpatterns = [
    path('', home, name='home'),
    # path('sesion/crear/', create_account, name='create_account'),
    # path('sesion/entrar/', log_in, name='log_in'),
    # path('sesion/cerrar/', sign_off, name='sign_off'),
]

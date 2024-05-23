from django.contrib import admin
from django.urls import path, include
from produtos.views import consultar_produto

urlpatterns = [
    path('', consultar_produto),
    path('admin/', admin.site.urls),
    path('produtos/', include('produtos.urls'))
]

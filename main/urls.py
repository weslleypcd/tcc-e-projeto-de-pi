"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from modernize_se_mercado.views import index, cadastro, login_views, mercados_parceiros, perfil_mercado, perfil_mercado_editar, minhas_ofertas, adicionar_ofertas, gerenciador_perfil_mercado, deletar_oferta, editar_oferta, editar_oferta

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('cadastro/', cadastro, name='cadastro'),
    path('login/', login_views, name='login'),
    path('mercados_parceiros/', mercados_parceiros, name='mercados_parceiros'),
    path('perfil_mercado/', perfil_mercado, name='perfil_mercado'),
    path('minhas_ofertas', minhas_ofertas, name='minhas_ofertas'),
    path('adicionar_ofertas/', adicionar_ofertas, name='adicionar_ofertas'),
    path('minhas_ofertas/<int:oferta_id>/', deletar_oferta, name='deletar_oferta'),
    path('minhas_ofertas/editar/<int:oferta_id>/', editar_oferta, name="editar_oferta"),
    path('perfil_mercado_editar', perfil_mercado_editar, name='perfil_mercado_editar'),
    path('gerenciador_perfil_mercado', gerenciador_perfil_mercado, name='gerenciador_perfil_mercado')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
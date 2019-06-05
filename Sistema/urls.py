from django.conf.urls import url,include
from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.conf.urls.static import static


urlpatterns=[
    url(r'^$',views.inicio,name="inicio"),
    url(r'^registro/$',views.registroCliente,name="registroCliente"),
    url(r'^login/',views.loginCliente,name="login"),
	url(r'^logout/', views.logoutCliente, name="logout"),
    url(r'^productos/$',views.gestionProducto,name="gestionProducto"),
    url(r'^productos/editar/(?P<pk>[0-9]+)/$',views.editarProducto,name="editarProducto"),
    url(r'^productos/eliminar/(?P<pk>[0-9]+)/$',views.eliminarProducto,name="eliminarProducto"),
    url(r'^lista/$',views.verProductos,name="verProductos"),
    url(r'^lista/añadir/(?P<pk>[0-9]+)/$',views.añadirProducto,name="añadirProducto"),
    url(r'^lista/eliminar/(?P<pk>[0-9]+)/$',views.eliminarPedido,name="eliminarPedido"),
   

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



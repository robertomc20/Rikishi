from django.contrib import admin
from .models import Perfil,Producto,Pedido,Detalle_Pedido,Compra
# Register your models here.
admin.site.register(Perfil) 
admin.site.register(Producto)
admin.site.register(Pedido)
admin.site.register(Detalle_Pedido)
admin.site.register(Compra)
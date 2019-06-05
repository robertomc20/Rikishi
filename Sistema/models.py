from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

# Create your models here.
class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    '''rut = models.CharField(primary_key=True, max_length=20, blank=True)'''

    # Python 3
    def __str__(self): 
        return self.usuario.username

@receiver(post_save, sender=User)
def crear_usuario_perfil(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(usuario=instance)

@receiver(post_save, sender=User)
def guardar_usuario_perfil(sender, instance, **kwargs):
    instance.perfil.save()


class Producto(models.Model):
    codigoProducto=models.AutoField(primary_key=True)
    fotoProducto=models.ImageField(upload_to='./media/')
    nombreProducto=models.CharField(max_length=30, blank=True)
    precioProducto=models.CharField(max_length=30, blank=True)
    descripcion=models.CharField(max_length=30, blank=True)
    stockProducto=models.CharField(max_length=30, blank=True)


#Una vez que el usuario seleccione 1 producto para añadir al carrito, se crea un Pedido(Codigo de pedido), sucesivamente se 
#y el producto seleccionado se crea en Detalle_Pedido relacionandola con la pk recién creada(Codigo de pedido).


class Detalle_Pedido(models.Model):
    codigoPedido=models.AutoField(primary_key=True)
    codigoProducto=models.ForeignKey(Producto, on_delete=models.CASCADE)
    nombreProducto=models.CharField(max_length=30, blank=True)
    precioProducto=models.CharField(max_length=30, blank=True)
    cliente=models.CharField(max_length=30, blank=True)
    fecha=models.DateField(default=timezone.now)

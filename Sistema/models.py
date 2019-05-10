from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

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
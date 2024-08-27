from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    rol = models.CharField(max_length=50, choices=[('cliente', 'Cliente'), ('repartidor', 'Repartidor'), ('restaurante', 'Restaurante')])

    def __str__(self):
        return self.username

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    cliente = models.ForeignKey('Usuario', on_delete=models.CASCADE, related_name='pedidos')
    restaurante = models.ForeignKey('Usuario', on_delete=models.CASCADE, related_name='pedidos_restaurante')
    repartidor = models.ForeignKey('Usuario', on_delete=models.CASCADE, related_name='pedidos_repartidor', null=True, blank=True)
    productos = models.ManyToManyField(Producto, through='PedidoProducto')
    estado = models.CharField(max_length=50)  # pendiente, en camino, entregado
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    fecha_entrega = models.DateTimeField(null=True, blank=True)

class PedidoProducto(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

    def __str__(self):
        return f'{self.cantidad} x {self.producto.nombre}'

class Feedback(models.Model):
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    comentario = models.TextField()
    calificacion = models.IntegerField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Feedback by {self.usuario.nombre}'

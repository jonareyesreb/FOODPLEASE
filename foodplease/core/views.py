from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from .models import Usuario, Producto

@login_required
def seleccionar_rol(request):
    if request.method == 'POST':
        rol = request.POST['rol']
        return redirect('mostrar_contenido', rol=rol)
    return render(request, 'core/seleccionar_rol.html')

@login_required
def mostrar_contenido(request, rol):
    if rol == 'cliente':
        return render(request, 'core/contenido_cliente.html')
    elif rol == 'repartidor':
        return render(request, 'core/contenido_repartidor.html')
    elif rol == 'restaurante':
        return redirect('menu_restaurante')  # Redirigir a la gestión del menú
    else:
        return redirect('seleccionar_rol')

def inicio(request):
    return render(request, 'core/inicio.html')

@login_required
def menu_restaurante(request):
    productos = Producto.objects.all()
    return render(request, 'core/menu_restaurante.html', {'productos': productos})

@login_required
def agregar_producto(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        precio = request.POST['precio']
        disponible = request.POST.get('disponible') == 'on'  # Manejo de la disponibilidad
        Producto.objects.create(nombre=nombre, descripcion=descripcion, precio=precio, disponible=disponible)
        return redirect('menu_restaurante')
    return render(request, 'core/agregar_producto.html')

@login_required
def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        producto.nombre = request.POST['nombre']
        producto.descripcion = request.POST['descripcion']
        producto.precio = request.POST['precio']
        producto.disponible = request.POST.get('disponible') == 'on'  # Manejo de la disponibilidad
        producto.save()
        return redirect('menu_restaurante')
    return render(request, 'core/editar_producto.html', {'producto': producto})

@login_required
def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        producto.delete()
        return redirect('menu_restaurante')
    return render(request, 'core/eliminar_producto.html', {'producto': producto})

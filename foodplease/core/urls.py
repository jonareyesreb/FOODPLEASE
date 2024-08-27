from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('seleccionar_rol/', views.seleccionar_rol, name='seleccionar_rol'),
    path('mostrar_contenido/<str:rol>/', views.mostrar_contenido, name='mostrar_contenido'),
    path('menu_restaurante/', views.menu_restaurante, name='menu_restaurante'),
    path('agregar_producto/', views.agregar_producto, name='agregar_producto'),
    path('editar_producto/<int:producto_id>/', views.editar_producto, name='editar_producto'),
    path('eliminar_producto/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),
]

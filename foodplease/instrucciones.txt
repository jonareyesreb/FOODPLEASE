
### Instrucciones para configurar el proyecto FoodPlease ###

1. Extrae el archivo ZIP en tu máquina local

2. Crea y activa un entorno virtual (si es del caso):
    - En sistemas Unix o MacOS:
        
        python3 -m venv venv
        source venv/bin/activate
        
    - En Windows:
        
        python -m venv venv
        .\\venv\\Scripts\\activate
        

3. Instala las dependencias (creadas desde MacOS):
    
    pip install -r requirements.txt
    

4. Configura la base de datos:

    - Edita el archivo `settings.py` # es necesario para conectar la base de datos si se tiene una 

	Crea una base de datos en blanco llamada menu (`settings.py` configurado con ese nombre)


5. Realiza las migraciones de la base de datos (aqui depende de la version de python instalada en mi caso es python3):
    
    python manage.py makemigrations
    python manage.py migrate
    

6. Ejecuta el servidor de desarrollo (aqui depende de la version de python instalada en mi caso es python3 y revisar el puerto [8000]):
    
    python manage.py runserver
    

7. Accede a la aplicación :
    Abre un navegador y ve a `http://127.0.0.1:8000/`


**Nota:** 

No olvides crear un superusuario si necesitas acceder al panel de administración:

python manage.py createsuperuser

### seguir instrucciones de creación :

pide un nombre de usuario: xxxxxxx
pide un correo: xxxxxx@xxxxxxx.com  (no es necesario que sea real)
pide una contraseña: (se debe repetir dos veces y debe ser segura o de lo contrario alerta y pregunta  *** y/n *** si quiere crearla

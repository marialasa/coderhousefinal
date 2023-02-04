# 💻 Proyecto final de CoderHouse
El presente repositorio contiene el proyecto final del Curso de Python #47635 de CoderHouse.

# Alumna
María de los Ángeles Lasa

# 🗣️ BlaBlaBlog
🗣️ BlaBlaBlog es una plataforma colaborativa de blogging que permite que un usuario:

- Cree su cuenta de registro e inicie sesión desde la homepage
- Modifique o elimine su usuario
- Busca y acceda a todos los posts publicados por otros usuarios
- Cree, edite y/o borre posts
- Complete y envíe un formulario de contacto
- Deje una reseña en "Sobre BlaBlaBlog"

# Tech Stack
- Pyhon
- Django
- HTML
- CSS
- JavaScript
- Bootstrap

# Requisitos para correr el proyecto
## Instalar:
```python
python version 3.10.8 
django version 4.0.3
pillow version 9.3.6
whitenoise version 6.2.0
```
## Correr los siguientes comandos en Visual Studio Code: 
```python
> python manage.py makemigrations
> python manage.py migrate
> python manage.py collectstatic (yes)
> python manage.py runserver
```
## Visualización:
- Ingresar a http://127.0.0.1:8000/ en el navegador.
## Panel reservado a usuario administrador:
- Ingresar a http://127.0.0.1:8000/admin/ en el navegador.
```python
User: admin
Correo electrónico: admin@blablablog.com
Password: blablablogadmin123
```
- El administrador tiene todos los accesos previstos para un usuario regular pero se suman funciones adicionales, como ser la edición y/o eliminación de reseñas, la gestión de formularios y el overview general de posts generados en la web.
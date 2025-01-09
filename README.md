# Plantilla de django fullstack

0. [Cambios recientes](#Cambios)
1. [Características](#caracteristicas)
2. [Instalación](#Instalación)
3. [Desarrollo](#desarrollo)
4. [Operaciones con Make](#make)

## Cambios recientes<a name="Cambios"></a>

* Se cambio el sistema de plantillas para usar cookiecutter
* Se añadió pyproject.toml para usar **uv** como sistema de gestión de entorno y dependencias
* Se vuelve a recomendar el trabajo por entornos en vez de por contenedores

## Características<a name="caracteristicas"></a>

### Settings divididos

Los settings están divididos para una mayor comodidad y gestión de estos.

### Settings usando variables de entorno

No sólo se usan las variables de entorno y el archivo `.env` si no que además dejamos que la librería haga el **casting** de tipos por nosotros.

### Docker optimizado para cache

La imagen de docker está construida de tal forma que se reaprovechan la mayoría de capas de cache.

### Makefile como centro de operaciones

Con el makefile tienes toda la operativa básica para solucionar la mayoría de problemas.

### Apps en subcarpetas

Esto permite que el código pueda crecer y seguir teniendo una estructura ordenada.

### Whitenoise para gestión de estáticos

Usando whitenoise la app puede servir estáticos de forma eficiente sin necesidad de delegar este trabajo a Nginx/Traefik.

### App "core"

La app `core` sirve para poder centralizar ahí todas las funcionalidades/utilidades/modelos/vistas que tengan un uso transversal a toda el proyecto.

!Nuevo: Se ha añadido en core también templatetags útiles para las plantillas

### App "users" directamente editable

Ya tenemos una app `users` que nos permite adaptar el usuario a nuestras necesidades sin tener que generar "modelos sidecar".

!Nuevo: Se han añadido las vistas de cambiar usuario y cambiar contraseña así como sus formularios y la función de logout

### Gunicorn configurado

Gunicorn viene ya configurado para ser productivo y, además, *trae una configuración extra para desarrollo*

### Requirements actualizados

Tanto los requirements como la versión de python están actualmente en su última versión.

### Tailwind preinstalado

Puedes usar tailwind, o no, depende del proyecto. Para usarlo sólo necesitas hacer `make cssdev`.

### Gunicorn con Hot Reloading para desarrollo

Podrás usar gunicorn para estar en un entorno prácticamente idéntico a producción.

### Celery preinstalado

Sólo faltaría configurar los detalles de Celery

### Celery con colas de prioridad

Este template te da un sistema de prioridades de colas para que puedas ejecutar antes lo que más apremie.

### Email configurado

El email está configurado por defecto para desarrollo, se puede configurar con variables de entorno y hay un pequeño test de ejemplo.

### !Nuevo: Gestión de errores

Los errores se enviarán al correo una vez se añadan los `ADMINS` en `settings/base.py`

### !Nuevo: Añadidos paquetes de utilidades

Se han añadido:
*  Django extensions: Te permite tener una consola interactiva más útil entre otras tantas utilidades
*  Django widget tweaks: Te permite modificar las clases y atributos a los widgets desde la plantilla (ejemplo en `components/field.html`)
*  Django filter: Es un must para generar filtros tanto en Django como DRF

### !Nuevo: Plantillas de ejemplo

* En `templates/base.html` podrás encontrar un ejemplo de cómo usar la plantilla, esta plantilla está pensada para poderse usar con HTMX teniendo #page como objetivo para cambiar sólo el contenido necesario. Esta plantilla de ejemplo hace uso de **dos componentes de ejemplo**, `top-bar` y `messages`. Esta plantilla lleva configurado el `token CSRF` por lo tanto no hará falta usarlo en formularios que usen HTMX.

* En `templates/components/top-bar.html` encontrarás un ejemplo de cómo tener una plantilla usando tailwind (copypaste de Flowbite) teniendo un dropdown y marcando el elemento activo por ruta.

* En `templates/components/messages.html` tendrás un ejemplo de mensaje de alerta que desaparece automáticamente y cuyo color se adapta al mensaje concreto. Esto hace uso del framework de mensajes de django y está integrado en `base.html`

* En `templates/components/field.html` podrás ver un ejemplo de campo reutilizable a través de los formularios de django con manejo de errores y representación de si es requerido o no. Su uso sería a través de un `include` desde field añadiendo como parámetro `field` el campo del formulario en cuestión.

### !Nuevo: django-components para gestionar componentes + ejemplo

Se ha tomado la decisión de añadir django-components al proyecto porque aporta una mayor organización y control sobre el código y la interfaz.

* _Timer_ se ha pasado a componente con django-component para tener un ejemplo de uso 

__________


## Instalación<a name="instalación"></a>

Para instalar usaremos cookiecutter. 
```
pip install cookiecutter
```

Una vez instalado procedemos a crear el proyecto respondiendo a las preguntas que nos haga
```
cookiecutter https://github.com/FJLendinez/django-template.git
```

Si la url no funciona (por permisos o whatever), descarga el zip desde gitlab y haz

```
cookiecutter ./path/to/django-template-master.zip
```

Una vez hecho, iremos a la carpeta del proyecto

```
cd <project_name>
```

y aquí construiremos la imagen para empezar a trabajar

```
make build
```

Mientras no se añadan dependencias ni se toque la forma de construir/desplegar, esta **imagen será suficiente para desarrollar**.

__________
## Desarrollo <a name="desarrollo"></a>

### Modificar las variables de entorno

En el archivo `.env` vienen unas variables de entorno de ejemplo que **deben ser modificadas**. En este punto es bueno saber qué base de datos usaremos, entre otras cosas, para dejarlo configurado.

### Levantar dependencias de docker (postgres y redis)
Edita el docker compose de dependencias en `docker/docker-compose.dev.yml` para modificar la receta a tu gusto. Recomendamos exponer puertos para poderlos usar desde fuera de docker en nuestro entorno de desarrollo.

Una vez editado, ejecutamos:

```
make rundeps
```


### Crear entorno virtual e instalar paquetes
En la terminal, con **uv instalado**, haz:
```
uv sync
```
Esto **creará el entorno virtual e instalará las dependencias por ti**


### Cómo añadir una aplicación
Debido a que el orden de este proyecto no es el orden por defecto de django, tenemos que hacer unos pequeños cambios.
Asumiremos que vamos a instalar una aplicación que sea `facturas`.

Ejecutamos:
```
mkdir apps/facturas && python manage.py startapp facturas apps/facturas
```

En `apps/facturas/apps.py`, añade `name = 'apps.facturas'`

En `config/settings/apps.py`, en `INSTALLED_APPS`, añade `apps.facturas`

__________

## Operaciones con make<a name="make"></a>

`make rundeps` : Levanta las dependencias de desarrollo. Por defecto son **postgres** y **redis**

_______

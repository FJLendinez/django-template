# Plantilla de django fullstack

1. [Instalación](#Instalación)
2. [Desarrollo](#desarrollo)
3. [Características](#caracteristicas)
4. [Operaciones con Make](#make)

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

# Desarrollo (Básico) <a name="desarrollo"></a>

## Quickstart

Para **iniciar** el proyecto creando un entorno virtual e instalando sus dependencias en él, usa el siguiente comando:

```bash
uv sync
```

Una vez lo tengamos, podemos configurar la base de datos y una vez hecho podremos hacer:

```bash
uv run manage.py migrate
```

Con la base de datos lista, creamos el primer superusuario.

```bash
uv run manage.py createsuperuser
```

Ya tenemos todo listo. Podemos ejecutar ya el servidor pero antes vamos a revisar que están los estilos necesarios.

```bash
make cssdev
```

Con todo descargado y ejecutado, terminamos el servidor de css (o lo dejamos abierto y abrimos otra terminal) y arrancamos el server de django:

```bash
uv run manage.py runserver
```

## Cómo añadir una aplicación
Debido a que el orden de este proyecto no es el orden por defecto de django, tenemos que hacer unos pequeños cambios.
Asumiremos que vamos a instalar una aplicación que sea `facturas`.

### 1. Crear una carpeta
Dentro de apps habrá que crear una carpeta que se llame `facturas`

### 2. Ejecutar el comando

```python manage.py startapp facturas apps/facturas```

#### 3. Edita el apps.py

Añade `name = 'apps.facturas'` en la configuración de la app.

#### 4. Instálala en las settings

En `config/settings/apps.py`, en `INSTALLED_APPS`, añade `apps.facturas`

# Características<a name="caracteristicas"></a>

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

~~!Nuevo: Se ha añadido en core también templatetags útiles para las plantillas~~

!Nuevo: En la app core se han añadido los componentes de django-cotton compatidos en todo el proyecto. Se pueden usar en el resto de apps para extender su funcionalidad.

!Nuevo: Se ha añadido un bloque (conjunto de componentes con una utilidad específica) de alertas y una vista para ser mostradas en interfaz usando el sistema de mensajes de django.

### App "users" directamente editable

Ya tenemos una app `users` que nos permite adaptar el usuario a nuestras necesidades sin tener que generar "modelos sidecar".

~~!Nuevo: Se han añadido las vistas de cambiar usuario y cambiar contraseña así como sus formularios y la función de logout~~
!Nuevo: Se han movido las vistas a la propia aplicación. Se ha añadido todo el flujo de password-reset de django.

### Gunicorn configurado

Gunicorn viene ya configurado para ser productivo ~~y, además, *trae una configuración extra para desarrollo*~~ (se recomienda montar un entorno)

### Requirements actualizados

Tanto los requirements como la versión de python están actualmente en su última versión.

### Tailwind preinstalado

Puedes usar tailwind, o no, depende del proyecto. Para usarlo sólo necesitas hacer `make cssdev`

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
~~*  Django extensions: Te permite tener una consola interactiva más útil entre otras tantas utilidades~~
*  Django cotton: Se ha preferido frente a django-extensions por ofrecer un mejor desacople lógica-interfaz.
*  Django widget tweaks: Te permite modificar las clases y atributos a los widgets desde la plantilla
*  Django filter: Es un must para generar filtros tanto en Django como DRF

### !Nuevo: Plantillas de ejemplo

* En `apps/core/templates/bases/base.html` podrás encontrar un ejemplo de cómo usar la plantilla, esta plantilla está pensada para poderse usar con HTMX teniendo #app como objetivo para cambiar sólo el contenido necesario. Esta plantilla de ejemplo hace uso de **dos componentes de ejemplo**, `header` y `toast`. Esta plantilla lleva configurado el `token CSRF` por lo tanto no hará falta usarlo en formularios que usen HTMX.

* En `apps/core/templates/cotton/header.html` encontrarás un ejemplo de cómo tener una plantilla usando tailwind, django-cotton y daisyUI.

* En `apps/core/blocks/alerts.html` tendrás un ejemplo de bloque para los mensajes de alerta que desaparecen automáticamente y cuyo color se adapta al mensaje concreto. Esto hace uso del framework de mensajes de django y está integrado en `base.html` a través del componente `toast`

~~* En `templates/components/field.html` podrás ver un ejemplo de campo reutilizable a través de los formularios de django con manejo de errores y representación de si es requerido o no. Su uso sería a través de un `include` desde field añadiendo como parámetro `field` el campo del formulario en cuestión.~~

### !Nuevo: django-cotton para gestionar componentes + ejemplo

Se ha tomado la decisión de añadir django-cotton al proyecto porque aporta una mayor organización y control sobre el código y la interfaz.

__________

## Operaciones con make<a name="make"></a>

`make build` : Construye la imagen que usaremos para desarrollar.

`make run` : Ejecuta la app y sus workers

`make rundeps` : Levanta las dependencias de desarrollo. Por defecto son **postgres** y **redis**

`make rundev` : Hace lo mismo que `rundeps` y, además, levanta la app

`make exec` : Te permite levantar una shell de django dentro del contenedor de Desarrollo

`make bash` : Te permite levantar una bash dentro del contenedor de desarrollo

`make cssdev` : Instala tailwind y daisyUI, levanta un proceso que escucha los cambios en las templates y construye el css minificado necesario para que toda la aplicación funcione correctamente.

`make tests`: Ejecuta ruff y los tests de la aplicación

`make htmxupgrade`: Utilidad para descargar HTMX y añadirlo a los estáticos de forma que la aplicación pueda hacer uso de la lib.

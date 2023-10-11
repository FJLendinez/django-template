# Django Template

1. [Instalación](#instalacion)
2. [Desarrollo](#desarrollo)
3. [Características](#caracteristicas)
4. [Operaciones con Make](#make)

## Instalación<a name="instalacion"></a>

Usaremos el comando `startproject` de django como utilidad para generar nuestro proyecto. Se puede generar con cualquier django-admin de cualquier entorno.

```
django-admin startproject --template https://github.com/FJLendinez/django-template/archive/refs/heads/main.zip -e py,yml,toml <project_name> .
```

Si la url no funciona (por permisos o whatever), descarga el zip desde github y haz

```
django-admin startproject --template ~/Descargas/django-template-main.zip -e py,yml,toml <project_name> .
```

Una vez hecho, iremos a la carpeta del proyecto

```
cd <project_name>
```

y aquí construiremos la imagen para empezar a trabajar

```
make build
```

Mientras no se añadan dependencias ni se toque la forma de construir/desplegar, esta imagen será suficiente para desarrollar.

__________
## Desarrollo (Básico) <a name="desarrollo"></a>

Copia el `.env` de ejemplo:

```
cp .env.example .env
```

y ejecuta:

```
make rundev
```

Esto levantará las dependencias y el poyecto con gunicorn de tal forma que podrás trabajar de una manera cercana a producción pero con hot reloading

### Cómo añadir una aplicación
Debido a que el orden de este proyecto no es el orden por defecto de django, tenemos que hacer unos pequeños cambios.
Asumiremos que vamos a instalar una aplicación que sea `facturas`.

#### 1. Crear una carpeta
Dentro de apps habrá que crear una carpeta que se llame `facturas`

#### 2. Ejecutar el comando

```python manage.py startapp facturas apps/facturas```

#### 3. Edita el apps.py

Añade `name = 'apps.facturas'` en la configuración de la app.

#### 4. Instálala en las settings

En `config/settings/apps.py`, en `INSTALLED_APPS`, añade `apps.facturas`
__________

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

### App "users" directamente editable

Ya tenemos una app `users` que nos permite adaptar el usuario a nuestras necesidades sin tener que generar "modelos sidecar".

### Gunicorn configurado

Gunicorn viene ya configurado para ser productivo y, además, *trae una configuración extra para desarrollo*

### Requirements actualizados

Tanto los requirements como la versión de python están actualmente en su última versión.

### Tailwind preinstalado

Puedes usar tailwind, o no, depende del proyecto. Para usarlo sólo necesitas hacer `make cssdev`

### Gunicorn con Hot Reloading para desarrollo

Podrás usar gunicorn para estar en un entorno prácticamente idéntico a producción.

### Celery preinstalado

Sólo faltaría configurar los detalles de Celery

### Celery con colas de prioridad

Este template te da un sistema de prioridades de colas para que puedas ejecutar antes lo que más apremie.

__________

## Operaciones con make<a name="make"></a>

`make build` : Construye la imagen que usaremos para desarrollar.

`make run` : Ejecuta la app y sus workers

`make rundeps` : Levanta las dependencias de desarrollo. Por defecto son **postgres** y **redis**

`make rundev` : Hace lo mismo que `rundeps` y, además, levanta la app

`make exec` : Te permite levantar una shell de django dentro del contenedor de Desarrollo

`make bash` : Te permite levantar una bash dentro del contenedor de desarrollo

`make cssdev` : Instala tailwind en el contenedor y levanta un proceso que escucha los cambios en las templates para construir sus estilos

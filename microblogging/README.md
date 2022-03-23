# Microblogging

Este proyecto es un simple CRUD para mostrar el funcionamiento e integración de las tecnologías Django-Inertia-VueJs.

## Pasos iniciales

### Clone el repositorio

```bash
git clone git@github.com:bitmotto/dev_onboarding_inertia_django.git
```

### Cree un entorno de desarrollo e instale los paquetes de Django

```bash
virtualenv venv --python=python3.9
pip install -r requirements.txt
```

### Corra las migraciones

```bash
python manage.py migrate
```

### Actualizamos las rutas de nuestro proyecto

```bash
python manage.py dump_routes_resolver --format=default --output=static/js/routes/resolver.js
```

### Instale los paquetes del frontend

```bash
cd frontend
npm install
```

### Actualizamos el tailwind.css

```bash
cd frontend
npm run tailwind
```

## Uso

En una terminal y en el directorio principal del proyecto levante el servidor de Django.

```bash
python manage.py runserver 0.0.0.0:8000
```

En otra terminal y en el directorio frontend genere el bundle .css y .js del proyecto.

```bash
npm run start
```

hello

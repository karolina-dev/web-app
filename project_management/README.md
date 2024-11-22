# web-app
Aplicación de prueba



```markdown
# Panel de Administración de Proyectos de Desarrollo

Este proyecto es una aplicación web diseñada para gestionar el progreso de diferentes proyectos de desarrollo. Está orientada a gestionar **historias de usuario**, **tickets de desarrollo** y **proyectos** en general. La aplicación permite a los usuarios crear y gestionar proyectos de desarrollo, asociar historias de usuario a los proyectos, y crear tickets relacionados con cada historia de usuario para seguir el progreso de las tareas de desarrollo.

## Funcionalidades

### 1. **Crear una cuenta de usuario**
   Los usuarios pueden crear una cuenta e iniciar sesión para acceder a las funcionalidades de la plataforma.

### 2. **Gestionar proyectos**
   Los usuarios pueden crear, editar y ver los proyectos disponibles. Cada proyecto puede contener varias historias de usuario.

### 3. **Gestionar historias de usuario**
   Los usuarios pueden crear historias de usuario, que son funcionalidades globales asociadas a un proyecto. Cada historia de usuario puede contener uno o más tickets.

### 4. **Gestionar tickets**
   Los usuarios pueden crear, editar y cancelar tickets de desarrollo relacionados a las historias de usuario. Los tickets permiten gestionar tareas específicas relacionadas con el desarrollo del proyecto.
5. **Ver el estado de los tickets**
   Los usuarios pueden ver el historial de tickets asociados a un proyecto y su estado actual (activo, cerrado, cancelado, etc.).

### 6. **Autenticación y Autorización**
   La plataforma soporta autenticación de usuarios para permitir el acceso a las funcionalidades según el tipo de usuario.

## Requisitos

- Python 3.8 o superior
- Django 5.1.3
- Bootstrap 5 (para estilos y diseño de la interfaz)

## Instalación

1. Clona el repositorio a tu máquina local:

   ```bash
   git clone https://github.com/usuario/repositorio.git
   cd repositorio
   ```

2. Crea un entorno virtual (opcional pero recomendado):

   ```bash
   python -m venv .venv
   ```

3. Activa el entorno virtual:

   - En Windows:

     ```bash
     .venv\Scripts\activate
     ```

   - En macOS/Linux:

     ```bash
     source .venv/bin/activate
     ```

4. Instala las dependencias del proyecto:

   ```bash
   pip install -r requirements.txt
   ```

5. Configura la base de datos (si es necesario, ajusta la configuración en `settings.py`):

   ```bash
   python manage.py migrate
   ```

6. Ejecuta el servidor de desarrollo:

   ```bash
   python manage.py runserver
   ```

7. Accede a la aplicación a través de tu navegador en `http://127.0.0.1:8000/`.

## Estructura del Proyecto

El proyecto se organiza de la siguiente manera:

```
project_management/
├── project_management/       # Configuración general de Django
│   ├── settings.py           # Configuración de Django (base de datos, etc.)
│   ├── urls.py               # Rutas de la aplicación
│   └── wsgi.py               # Configuración del servidor WSGI
│
├── projects/                 # Aplicación principal del proyecto
│   ├── migrations/           # Migraciones de la base de datos
│   ├── models.py             # Modelos para proyectos, historias de usuario, y tickets
│   ├── views.py              # Lógica de las vistas
│   ├── urls.py               # Rutas para la aplicación de proyectos
│   ├── forms.py              # Formularios para crear y editar proyectos, historias de usuario y tickets
│   └── templates/            # Plantillas HTML (con Bootstrap para estilos)
│       └── projects/
│           ├── base.html     # Plantilla base para el diseño común
│           ├── home.html     # Página de inicio
│           ├── project_list.html # Listado de proyectos
│           ├── create_project.html # Formulario para crear proyectos
│           └── ...
├── static/                   # Archivos estáticos (CSS, JS, imágenes)
├── manage.py                 # Script para ejecutar comandos de Django
└── requirements.txt          # Dependencias del proyecto
```

### Descripción de los Archivos Importantes

- **`models.py`**: Define los modelos de la base de datos, incluyendo `Project`, `UserStory`, y `Ticket`. Estos modelos representan las entidades centrales del proyecto.
  
- **`views.py`**: Contiene las vistas que controlan la lógica detrás de las operaciones de la aplicación, como crear proyectos, ver tickets, y gestionar historias de usuario.
  
- **`forms.py`**: Define los formularios utilizados para crear y editar proyectos, tickets, y historias de usuario.

- **`templates/`**: Contiene las plantillas HTML que definen la interfaz de usuario. Estas plantillas utilizan la extensión de base `base.html` para mantener una estructura común.

- **`static/`**: Contiene los archivos estáticos, como hojas de estilo CSS y scripts JS. El proyecto usa Bootstrap 5 para facilitar el diseño responsivo y moderno.

## Contribución

Si deseas contribuir a este proyecto, puedes hacerlo siguiendo estos pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama para tus cambios.
3. Realiza los cambios y asegúrate de que el proyecto sigue funcionando correctamente.
4. Realiza un pull request con tus cambios.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.

---

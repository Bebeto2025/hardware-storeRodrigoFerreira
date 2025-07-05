Rodrigo Fabian Ferreira Martinez

# Hardware Store

Descripción:

Este proyecto es una plataforma web para la compra y venta de hardware entre usuarios. Los usuarios pueden publicar componentes con sus características principales y, en caso de que alguien desee más información sobre un producto, puede comunicarse directamente con el vendedor a través de un sistema de mensajería privada integrado. 

La aplicación incluye funcionalidades completas de gestión de usuarios (registro, login, perfiles con edición y cambio de contraseña), administración de publicaciones de hardware (creación, edición, eliminación y visualización detallada) y mensajería interna para facilitar la comunicación entre compradores y vendedores. Además, cuenta con un diseño responsivo basado en Bootstrap y utiliza CKEditor para la edición enriquecida de texto.

Este proyecto refleja buenas prácticas en Django, incluyendo el uso de vistas basadas en clases, señales, mixins, decoradores y manejo avanzado de formularios con soporte para carga de imágenes.

# Autor

- Soy uruguayo, tecnólogo químico, diplomado en IA y estudiante de Python en Coderhouse.
- Entusiasta de la tecnología accesible para todos, por eso este proyecto orientado a la venta de hardware barato, potente y accesible.

# Tecnologías utilizadas

- **Python 3**
- **Django 5**
- **HTML + CSS**
- **SQLite** 
- **CKEditor** 
- **Bootstrap** 

# Funcionalidades

# Usuarios
- Registro, login y logout
- Edición de perfil
- Cambio de contraseña

# Gestión de hardware
- Listado de productos
- Detalle de cada producto
- Crear nuevo producto (solo usuarios autenticados)
- Editar/eliminar productos propios

# Mensajería
- Inbox de mensajes entre usuarios
- Envío y recepción de mensajes

---

# Cómo ejecutar el proyecto

1. Cloná el repositorio o descargá el ZIP.
2. Asegurate de tener Python y pip instalados.
3. Creá un entorno virtual:
   ```bash
   python -m venv env
   source env/bin/activate   # en Linux/Mac
   env\Scripts\activate      # en Windows
4. Instalá las dependencias:
    pip install -r requirements.txt
5. Ejecutá las migraciones:
    python manage.py migrate
6. Corré el servidor:
    python manage.py runserver
7. Abrí en el navegador: 
    http://localhost:8000


Estructura basica del proyecto

hardware_store/
├── accounts/         # Registro, login, perfil
├── core/             # Home y About
├── store/            # Gestión de páginas de productos
├── messenger/        # Mensajería entre usuarios
├── templates/        # HTML base y específicos
├── static/           # Archivos estáticos
├── media/            # Imágenes cargadas por usuarios
├── config/           # Configuración general del proyecto
├── manage.py         # Comando principal de Django
├── README.md         # Este archivo

Video de la presentacion

rodrigoferreira.mkv

Link video drive

https://drive.google.com/file/d/1taT-GgLnu4-oDBLatRLLiDUmDulAsvde/view?usp=drive_link 

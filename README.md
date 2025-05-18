# Integración de Pagos con Khipu

Este proyecto implementa una integración con la API de pagos de Khipu utilizando Flask para crear una aplicación web que permite procesar pagos a través del servicio de Khipu.

## Requisitos

- Python 3.7+
- Flask
- Cuenta de desarrollador en Khipu

## Configuración del entorno

1. Clona este repositorio:

   ```bash
   git clone https://github.com/tu-usuario/khipu-integration.git
   cd khipu-integration
   ```

2. Crea un entorno virtual e instala las dependencias:

   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Configura las credenciales de Khipu:
   ```bash
   # Archivo .env
   KHIPU_RECEIVER_ID=tu_id_de_receptor
   KHIPU_SECRET=tu_clave_secreta
   ```

## Ejecución

Para iniciar la aplicación:

```bash
python app.py
```

La aplicación estará disponible en http://127.0.0.1:5000/

## Implementación

Esta integración utiliza el entorno de Khipu, permitiendo procesar pagos de forma rápida y segura. Para el desarrollo y pruebas, se utiliza el entorno de pruebas con DemoBank.

### Características principales

- Creación de pagos mediante llamadas a la API de Khipu
- Implementación del modal de pago para una experiencia de usuario fluida
- Verificación del estado del pago en tiempo real
- Manejo de diferentes estados de transacción

### Flujo de pago implementado

1. El usuario ingresa el monto, motivo y correo
2. La aplicación crea un pago a través de la API de Khipu
3. Se muestra el modal de pago de Khipu
4. El usuario completa el proceso de pago
5. La aplicación recibe y procesa la notificación de pago completado

## Estructura del proyecto

```
├── app.py                 # Aplicación principal de Flask
├── .env                   # Archivo de credenciales (no incluido en el repositorio)
├── requirements.txt       # Dependencias del proyecto
├── static/                # Archivos estáticos
│   ├── pago.js            # JavaScript para el formulario de pago
│   └── styles.css         # Estilos CSS
└── templates/             # Plantillas HTML
    ├── index.html         # Página principal con formulario de pago
    ├── estado.html        # Página de estado del pago
    └── exito.html         # Página de confirmación de pago exitoso
```

## Recursos y documentación

Para más información sobre la API de Khipu y sus funcionalidades, consulta:

- [Documentación oficial de Khipu](https://docs.khipu.com/portal/es/)

## Capturas del proceso

##### 1. Inicio (index.html)

![Página de inicio](/img/img001.png)

##### 2. Relleno de formulario

Al rellenar el formulario y hacer click en el botón "Pagar ahora", se redirige a _estado.html_

![Relleno de formulario](/img/img002.png)

##### 3. Estado de pago

La página de estado verifica mediante ajax la respuesta de API Kiphu, de ser exitosa, se abre el sistema de pago Kiphu.

![estado.html](/img/img003.png)

##### 4. Ingreso de credenciales DemoBank creado en modo desarrollador de Kiphu

![credenciales](/img/img004.png)

##### 5. Ingreso de coordenadas DemoBank

Ajax sigue verificando el _status_ de la transacción

![ingreso de credenciales](/img/img005.png)

##### 6. Pago correcto

Si el status del pago es correcto ajax actualiza el contenido de la pagina y comienza un countdown que redirigirá a exito.html.

![Página de inicio](/img/img006.png)

El usuario es redirigido a _exito.html_ con la opción de volver a página principal.

![Página de inicio](/img/img009.png)

##### 6. Pago incorrecto o cancelado

En caso de ser una transacción fallida o cancelada por el usuario, ajax nos envía un mensaje de error y volvemos a inicio.

![Página de inicio](/img/img007.png)

![Página de inicio](/img/img008.png)

# Fin

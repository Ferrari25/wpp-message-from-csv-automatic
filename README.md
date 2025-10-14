# Bot de Mensajes Masivos para WhatsApp

Este es un script de Python diseñado para automatizar el envío de mensajes personalizados de WhatsApp a una lista de contactos extraída de un archivo CSV. El script utiliza Selenium para controlar un navegador web, simular el comportamiento humano y enviar los mensajes de forma robusta.

## ✨ Características Principales

* **Lectura desde CSV:** Obtiene los datos de los destinatarios (nombre, teléfono, etc.) de un archivo `alumnos.csv`.
* **Mensajes Personalizados:** Utiliza una plantilla de mensaje que se personaliza automáticamente con el nombre de cada destinatario (ej. "Hola {nombre}, ...").
* **Barra de Progreso:** Muestra una barra de progreso en la terminal (`tqdm`) para visualizar el avance de los envíos en tiempo real.
* **Reporte Final Detallado:** Al finalizar, genera un resumen en la consola listando los envíos exitosos y los fallidos, incluyendo el tiempo que tardó cada operación.
* **Creación de Ejecutable:** Incluye instrucciones para empaquetar el script en un archivo `.exe` utilizando PyInstaller, permitiendo su uso en cualquier computadora con Windows sin necesidad de instalar Python.

---

## ⚠️ Advertencia: Úsese con Responsabilidad

Este script ha sido desarrollado con fines educativos y para facilitar la comunicación legítima (por ejemplo, notificaciones a alumnos, recordatorios a clientes, etc.).

* **NO USAR PARA SPAM:** El envío masivo de mensajes no solicitados va en contra de las políticas de WhatsApp y puede resultar en el **bloqueo permanente de tu número de teléfono**.
* **Simulación Humana:** El script incluye pausas (`time.sleep`) para simular un comportamiento más humano y reducir el riesgo de bloqueo, pero el riesgo siempre existe. Úsalo con moderación.
* **El autor no se hace responsable** del mal uso de esta herramienta ni de sus consecuencias.

---

## 🔧 Requisitos Previos

Para ejecutar el script desde el código fuente, necesitarás:

* **Python 3.x** instalado en tu sistema.
* El navegador **Google Chrome** actualizado.

---

## ⚙️ Instalación y Configuración

Sigue estos pasos para poner en marcha el proyecto:

**1. Clona o descarga este repositorio:**


## ⚙️ Estructura de la Carpeta
/TuProyecto/
  ├── script.py          # El script principal de Python
  ├── chromedriver.exe   # El controlador de Chrome
  └── alumnos.csv        # Tu base de datos de contactos

## ⚙️ Instala las dependencias de Python:
bash
pip install selenium tqdm pyinstaller
```bash

## ⚙️ Uso del Script
python script.py

git clone [URL_DEL_REPOSITORIO]
# O simplemente descarga el ZIP y descomprímelo.

# Bot de Mensajes Masivos para WhatsApp

Este es un script de Python diseñado para automatizar el envío de mensajes personalizados de WhatsApp a una lista de contactos extraída de un archivo CSV. El script utiliza Selenium para controlar un navegador web.

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

## ⚙️ Estructura de la Carpeta
```
/TuProyecto/
  ├── script.exe          # El script principal de Python
  ├── chromedriver.exe   # El controlador de Chrome
  └── alumnos.csv        # Tu base de datos de contactos
```

## ⚙️ Instala las dependencias de Python:
bash
pip install selenium tqdm pyinstaller
bash

## ⚙️ Uso del Script
python script.py

git clone [URL_DEL_REPOSITORIO]
ó simplemente descarga el ZIP y descomprímelo.

---

## ⚠️ Debilidades

Este script de repente deja de funcionar, no reconoce numeros de telefono con un pop up que dice "El numero de telefono compartido a traves de la direccion URL no es valido"

La causa más probable de este problema repentino es una actualización silenciosa en las medidas anti-automatización (anti-bots) de WhatsApp.

Cuando ejecutas el script (o incluso cuando pruebas los links wa.me manualmente uno tras otro), el sistema de WhatsApp detecta una serie de solicitudes para verificar números desde tu misma red (tu conexión a internet). Un sistema de seguridad puede interpretar esta actividad como "sospechosa" o "parecida a un bot" y, como medida de protección, empieza a responder con el error "Número no válido" para todo, incluso para números que sabe que son correctos.

Es una especie de bloqueo temporal y preventivo para desalentar a los spammers de verificar listas de números masivamente. Tú, sin quererlo, has activado esta defensa. Por eso, lo que antes funcionaba, ahora no.

¿Qué Hacemos Ahora? Un Plan de Acción

# Paso 1: Período de "Enfriamiento" (El más importante)

Te pido que hagas una pausa. Cierra el navegador que controla Selenium, no ejecutes el script y no intentes abrir links de wa.me manualmente por al menos unas cuantas horas. Necesitamos dejar que el sistema de WhatsApp "se olvide" de tu actividad y quite el bloqueo temporal de tu red.

# Paso 2: Hacer el Script Más "Humano" (Más lento)

Si el paso 2 funcionó, significa que el problema es la velocidad. Para evitar volver a ser bloqueados, debemos hacer que nuestro script sea más lento y parezca menos un robot.

Abre tu script.py, ve a la función main y busca la línea time.sleep(8) que está dentro del bucle. Vamos a aumentar esa pausa considerablemente para darle más aire a WhatsApp entre cada mensaje.

---



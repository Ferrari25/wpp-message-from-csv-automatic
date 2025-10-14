import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service
from tqdm import tqdm # librería para la barra de progreso

# --- CONFIGURACIÓN ---
NOMBRE_ARCHIVO_CSV = 'alumnos.csv'
MENSAJE_PLANTILLA = """
Buenos días/tardes, {nombre}.

Mi nombre es Santiago Ferrari y te escribo desde la Secretaría de Asuntos Estudiantiles (Asest) de la UTN Facultad Regional Delta.


Me comunico con vos porque figuras como beneficiario/a del programa de Becas Progresar y he sido asignado/a como tu tutor/a para acompañarte durante esta última parte del año. El objetivo es apoyarte en tu trayectoria académica y asegurar que cumplas con los requisitos para mantener y renovar la beca.


Para poder hacer este seguimiento, es de carácter obligatorio que actualices tu información académica. Te ofrecemos dos maneras de hacerlo:

Opción Online: Completando el siguiente formulario de Google. No te tomará más de unos minutos.
Link al formulario: https://forms.gle/byZPdtF45Se8joWg9

Opción Presencial: Acercándote a la oficina de Asest en la facultad para que podamos conversar y completar la información juntos.

Es fundamental que respondas a la brevedad. Mantener tus datos actualizados es una de las obligaciones que asumiste con el programa.

Te recordamos que, según el reglamento de Progresar, existen varias causales que pueden llevar al cese o pérdida de la beca, entre ellas:

* La pérdida de la condición de alumno/a regular.

* Estar excedido/a dos o más años en la duración de la carrera.

* El incumplimiento de cualquiera de las obligaciones del programa.

Este seguimiento es una herramienta para ayudarte a evitar estos inconvenientes y asegurar la correcta renovación de tu beca el próximo año.

Quedo a tu disposición por cualquier consulta.

Saludos cordiales,

Santiago Ferrari,
Tutor/a de Becas Progresar
Secretaría de Asuntos Estudiantiles (Asest)
UTN Facultad Regional Delta
"""
# --- FIN DE LA CONFIGURACIÓN ---


def leer_alumnos_del_csv(nombre_archivo):
    alumnos = []
    try:
        with open(nombre_archivo, mode='r', encoding='utf-8') as archivo_csv:
            lector_csv = csv.reader(archivo_csv)
            for fila in lector_csv:
                if len(fila) >= 6:
                    nombre_completo = fila[2].strip()
                    telefono = fila[5].strip()
                    if nombre_completo and telefono:
                        alumnos.append({'nombre': nombre_completo, 'telefono': telefono})
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{nombre_archivo}'.")
        return None
    return alumnos

def enviar_mensaje_whatsapp(driver, alumno, mensaje_template):
    """
    Envía un mensaje de WhatsApp y devuelve un estado (éxito/fallo) y la duración.
    """
    start_time = time.time() # Guardamos el tiempo de inicio
    
    nombre = alumno['nombre'] # Usaremos el nombre completo para el reporte
    primer_nombre = nombre.split(' ')[0]
    telefono = ''.join(filter(str.isdigit, alumno['telefono']))
    
    if not telefono.startswith('549'):
        telefono_completo = '549' + telefono
    else:
        telefono_completo = telefono

    mensaje_personalizado = mensaje_template.format(nombre=primer_nombre)
    url = f"https://web.whatsapp.com/send?phone={telefono_completo}"
    
    driver.get(url)
    
    try:
        # XPATH PERSONALIZADO (TU DESCUBRIMIENTO)
        caja_mensaje_xpath = '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div/div[3]/div[1]/p'
        
        caja_mensaje = WebDriverWait(driver, 40).until(
            EC.presence_of_element_located((By.XPATH, caja_mensaje_xpath))
        )
        time.sleep(1)

        for linea in mensaje_personalizado.split('\n'):
            caja_mensaje.send_keys(linea)
            caja_mensaje.send_keys(webdriver.common.keys.Keys.SHIFT + webdriver.common.keys.Keys.ENTER)
            time.sleep(0.3)

        # XPATH PERSONALIZADO (TU DESCUBRIMIENTO)
        boton_enviar_xpath = '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div/div[4]/div/span/div/div/div[1]'
        
        boton_enviar = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, boton_enviar_xpath))
        )
        boton_enviar.click()
        
        # Damos tiempo a que el mensaje se marque como enviado (doble tick)
        time.sleep(5)
        
        end_time = time.time() # Guardamos el tiempo de finalización
        duracion = round(end_time - start_time, 1)
        return True, duracion, nombre # Devolvemos Éxito, duración y nombre
        
    except TimeoutException:
        end_time = time.time()
        duracion = round(end_time - start_time, 1)
        return False, duracion, nombre # Devolvemos Fallo, duración y nombre
    except Exception as e:
        print(f"\n[ERROR INESPERADO con {nombre}: {e}]")
        end_time = time.time()
        duracion = round(end_time - start_time, 1)
        return False, duracion, nombre # Devolvemos Fallo, duración y nombre

def main():
    print("--- Iniciando Script de Envío Masivo de WhatsApp (Versión Mejorada) ---")
    
    lista_alumnos = leer_alumnos_del_csv(NOMBRE_ARCHIVO_CSV)
    
    if not lista_alumnos:
        print("No se encontraron alumnos válidos. Finalizando.")
        return

    # Listas para guardar el reporte final
    enviados_correctamente = []
    errores_envio = []

    # Inicia el navegador Chrome de forma robusta
    try:
        servicio = Service('./chromedriver.exe')
        driver = webdriver.Chrome(service=servicio)
    except Exception as e:
        print("Error al iniciar WebDriver. Asegúrate de que 'chromedriver.exe' está en la carpeta y es compatible.")
        print(f"Error detallado: {e}")
        return
        
    driver.get("https://web.whatsapp.com")
    
    print("\n************************************************************")
    print("1. Escanea el código QR para iniciar sesión en WhatsApp Web.")
    print("2. Espera a que tus chats carguen completamente.")
    print("************************************************************\n")
    input(">>> Cuando estés listo, presiona ENTER aquí para comenzar los envíos...")

    # Usamos tqdm para crear la barra de progreso
    print("\n--- Iniciando secuencia de envíos ---")
    for alumno in tqdm(lista_alumnos, desc="Progreso de envíos"):
        
        exito, duracion, nombre_alumno = enviar_mensaje_whatsapp(driver, alumno, MENSAJE_PLANTILLA)
        
        # Añadimos la información a nuestras listas de reporte
        if exito:
            enviados_correctamente.append(f"{nombre_alumno} (tardó {duracion}s)")
        else:
            errores_envio.append(f"{nombre_alumno} (falló tras {duracion}s)")

    print("\n--- Proceso finalizado. Cerrando navegador en 10 segundos... ---")
    time.sleep(10)
    driver.quit()

    # --- Mostramos el reporte final ---
    print("\n==================== REPORTE FINAL DE ENVÍOS ====================")
    print(f"\n✔ Envíos Exitosos: {len(enviados_correctamente)} de {len(lista_alumnos)}")
    for reporte in enviados_correctamente:
        print(f"  - {reporte}")
        
    if errores_envio:
        print(f"\n❌ Envíos Fallidos: {len(errores_envio)} de {len(lista_alumnos)}")
        for reporte in errores_envio:
            print(f"  - {reporte}")
    
    print("\n=================================================================\n")

if __name__ == "__main__":

    main()


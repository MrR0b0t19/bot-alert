from plyer import accelerometer
from time import sleep
from threading import Thread
from core.gps import obtener_ubicacion
from core.alert import enviar_alerta_telegram

def iniciar_detector(token, chat_id, threshold=25):
    def detectar():
        accelerometer.enable()
        print("[!] Detector de movimiento activado...")

        while True:
            try:
                val = accelerometer.acceleration
                if val != (None, None, None):
                    x, y, z = val
                    total = abs(x) + abs(y) + abs(z)

                    if total > threshold:
                        print(f"[!] Movimiento fuerte detectado: {total}")
                        lat, lon, direccion = obtener_ubicacion()
                        enviar_alerta_telegram(lat, lon, direccion, token, chat_id)
                        sleep(10)  # Evita múltiples alertas seguidas
            except Exception as e:
                print(f"[X] Error acelerómetro: {e}")
            sleep(1)

    Thread(target=detectar, daemon=True).start()

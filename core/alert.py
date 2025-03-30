from telegram import Bot

def enviar_alerta_telegram(lat, lon, direccion, token, chat_id):
    try:
        bot = Bot(token=token)
        url = f"https://maps.google.com/?q={lat},{lon}"
        mensaje = f"""
🚨 *Ubicación de Prueba* 🚨

📍 Coordenadas: `{lat}, {lon}`
📌 Dirección: _{direccion}_
🗺️ [Ver en Google Maps]({url})
        """
        bot.send_message(chat_id=chat_id, text=mensaje, parse_mode='Markdown')
        print("Mensaje enviado.")
    except Exception as e:
        print(f"Error enviando mensaje: {e}")

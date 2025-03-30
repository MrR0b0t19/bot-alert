from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from core.gps import obtener_ubicacion
from core.alert import enviar_alerta_telegram
from core.trigger import iniciar_detector
from kivy.lang import Builder

Builder.load_file("ui/styles.kv")

class MenuInicial(BoxLayout):
    def __init__(self, **kwargs):
        super(MenuInicial, self).__init__(orientation='vertical', padding=20, spacing=15, **kwargs)

        self.token_input = TextInput(hint_text="Ingresa tu Telegram Bot Token", multiline=False)
        self.chat_input = TextInput(hint_text="Ingresa tu Chat ID o @grupo", multiline=False)
        self.boton = Button(text="📍 Enviar ubicación de prueba")
        self.oculto = Button()  # Invisible, pero se definirá en KV

        self.boton.bind(on_press=self.enviar_prueba)
        self.oculto.bind(on_press=self.alerta_oculta)

        self.add_widget(Label(text="Configuración Inicial"))
        self.add_widget(self.token_input)
        self.add_widget(self.chat_input)
        self.add_widget(self.boton)
        self.add_widget(Label(text=" "))  # Espacio
        self.add_widget(Label(text=" "))  # Espacio
        self.add_widget(self.oculto)  # Botón oculto

    def enviar_prueba(self, instance):
        token = self.token_input.text
        chat_id = self.chat_input.text

        lat, lon, direccion = obtener_ubicacion()
        enviar_alerta_telegram(lat, lon, direccion, token, chat_id)

        iniciar_detector(token, chat_id)  # Iniciar sensor luego de prueba

        self.mostrar_popup("Alerta enviada y sensores activados.")

    def alerta_oculta(self, instance):
        token = self.token_input.text
        chat_id = self.chat_input.text
        lat, lon, direccion = obtener_ubicacion()
        enviar_alerta_telegram(lat, lon, direccion, token, chat_id)
        self.mostrar_popup("¡Alerta enviada desde botón oculto!")

    def mostrar_popup(self, mensaje):
        popup = Popup(title="Info", content=Label(text=mensaje), size_hint=(0.8, 0.3))
        popup.open()

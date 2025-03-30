from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from core.gps import obtener_ubicacion
from core.alert import enviar_alerta_telegram

class MenuInicial(BoxLayout):
    def __init__(self, **kwargs):
        super(MenuInicial, self).__init__(orientation='vertical', padding=20, spacing=15, **kwargs)

        self.token_input = TextInput(hint_text="Ingresa tu Token de bot telegram", multiline=False)
        self.chat_input = TextInput(hint_text="Ingresa tu Chat ID o @grupo", multiline=False)
        self.boton = Button(text="📍 Enviar ubicación de prueba")

        self.boton.bind(on_press=self.enviar_prueba)

        self.add_widget(Label(text="Configuración Inicial"))
        self.add_widget(self.token_input)
        self.add_widget(self.chat_input)
        self.add_widget(self.boton)

    def enviar_prueba(self, instance):
        token = self.token_input.text
        chat_id = self.chat_input.text

        lat, lon, direccion = obtener_ubicacion()
        enviar_alerta_telegram(lat, lon, direccion, token, chat_id)

from kivy.app import App
from ui.views import MenuInicial

class BotEmergenciaApp(App):
    def build(self):
        return MenuInicial()

if __name__ == '__main__':
    BotEmergenciaApp().run()

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.switch import Switch
from kivy.uix.slider import Slider
from kivy.core.window import Window

Window.clearcolor = (0.04, 0.05, 0.08, 1)

class ModMenu(App):
    def build(self):
        self.root = BoxLayout(
            orientation="vertical",
            padding=15,
            spacing=12
        )

        titulo = Label(
            text="GAMING CONTROL",
            font_size=26,
            bold=True,
            size_hint_y=None,
            height=60
        )
        self.root.add_widget(titulo)

        self.estado = Label(
            text="MENU INDEPENDIENTE",
            font_size=15,
            size_hint_y=None,
            height=35
        )
        self.root.add_widget(self.estado)

        for nombre in ["VISUAL", "AIM DEMO", "CONFIG"]:
            boton = Button(
                text=nombre,
                size_hint_y=None,
                height=50
            )
            boton.bind(on_press=self.cambiar)
            self.root.add_widget(boton)

        self.root.add_widget(
            Label(text="Mira de demostración")
        )

        self.mira = Switch(active=True)
        self.root.add_widget(self.mira)

        self.root.add_widget(
            Label(text="Tamaño de la mira")
        )

        self.slider = Slider(
            min=5,
            max=40,
            value=15
        )
        self.root.add_widget(self.slider)

        self.root.add_widget(
            Label(text="Configuración de demostración")
        )

        return self.root

    def cambiar(self, boton):
        self.estado.text = "Pestaña: " + boton.text

ModMenu().run()
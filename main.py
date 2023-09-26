import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.camera import Camera
from kivy.uix.button import Button

kivy.require('2.2.1')

class CameraApp(App):

    def build(self):
        layout = BoxLayout(orientation='vertical')

        # Câmera
        self.camera = Camera(play=True)
        layout.add_widget(self.camera)

        # Botão para tirar a foto
        self.capture_button = Button(text="Capturar", size_hint=(None, None), size=(100, 50))
        self.capture_button.bind(on_press=self.take_picture)
        layout.add_widget(self.capture_button)

        return layout

    def take_picture(self, *args):
        # Captura a imagem
        self.camera.export_to_png('image.png')
        print("Imagem capturada e salva como image.png")

if __name__ == '__main__':
    CameraApp().run()

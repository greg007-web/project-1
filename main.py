from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.camera import Camera
from kivy.uix.button import Button
from kivy.utils import platform
from android.permissions import request_permissions, Permission

class CameraApp(App):
    def build(self):
        # Verificar a plataforma
        if platform == 'android':
            self.request_android_permissions()

        layout = BoxLayout(orientation='vertical')

        # Criar instância da câmera
        self.cam = Camera(resolution=(640, 480), play=True)

        # Criar botão para capturar
        self.capture_btn = Button(
            text="Capture",
            size_hint=(1, 0.2),
            font_size=35,
            background_color='green',
            on_press=self.capture_image
        )

        layout.add_widget(self.cam)
        layout.add_widget(self.capture_btn)
        return layout

    def request_android_permissions(self):
        permissions = [
            Permission.CAMERA,
            Permission.WRITE_EXTERNAL_STORAGE
        ]
        request_permissions(permissions)

    def capture_image(self, *args):
        # Salvar a imagem capturada
        self.cam.export_to_png('captured_image.png')

if __name__ == '__main__':
    CameraApp().run()

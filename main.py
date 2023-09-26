import os
from kivy.app import App
from kivy.uix.camera import Camera
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class CameraApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        # Create camera instance
        self.cam = Camera(resolution=(640, 480), play=True)

        # Create button
        self.btn = Button(
            text="Capture",
            size_hint=(1, 0.2),
            font_size=35,
            background_color='green',
            on_press=self.capture_image)

        # Create label
        self.lbl = Label(
            text="Press the button to capture",
            size_hint=(1, 0.2))

        # Add widgets to layout
        layout.add_widget(self.cam)
        layout.add_widget(self.btn)
        layout.add_widget(self.lbl)

        return layout

    def capture_image(self, *args):
        # Save captured image
        self.cam.export_to_png(os.path.join(os.getcwd(), 'img.png'))
        self.lbl.text = "Image saved as img.png"

if __name__ == '__main__':
    CameraApp().run()

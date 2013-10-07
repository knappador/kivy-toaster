from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class ToastUI(BoxLayout):
    pass
    

class ToastApp(App):
    def __init__(self, *args, **kwargs):
        super(ToastApp, self).__init__(*args, **kwargs)
        global app
        app = self

    def build(self):
        return ToastUI()


if __name__ == '__main__':
    ToastApp().run()

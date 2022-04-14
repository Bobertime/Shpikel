from kivy.app import App
from kivy.uix.label import Label, Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

class screen_1(Widget):
    pass


class screen_2(Widget):
    pass


class Main_screenApp(App):
    def build(self):
        # main = BoxLayout(orientation="vertical")
        # logo = Label(text="Spikel", font_size="20px")
        # main.add_widget(logo)

        return screen_1()


if __name__ == '__main__':
    Main_screenApp().run()

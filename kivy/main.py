from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty


class WidgetsExample(GridLayout):
    my_text = StringProperty("Hello!")
    count = 0
    state = BooleanProperty(False)

    def on_button_click(self):
        #print("Button clicked")
        if self.state:
            self.count += 1
            self.my_text = str(self.count)

    def on_toggle_button_state(self, widget):
        print("Toggle state: " + widget.state)
        if widget.state == "normal":
            widget.text = "OFF"
            self.state = False
        else:
            widget.text = "UPP"
            self.state = True


class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #self.orientation = "lr-bt"
        for i in range(100):
            #size = dp(100) + i*10
            size = dp(100)
            b = Button(text=str(i+1), size_hint=(None, None),
                       size=(size, size))
            self.add_widget(b)


# class GridLayoutExample(GridLayout):
# pass


class AnchorLayoutExample(AnchorLayout):
    pass


class BoxLayoutExample(BoxLayout):
    pass
    """def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        b1 = Button(text="A")
        b2 = Button(text="B")
        b3 = Button(text="C")

        self.add_widget(b1)
        self.add_widget(b2)
        self.add_widget(b3)"""


class MainWidget(Widget):
    pass


class TheLabApp(App):
    pass


TheLabApp().run()

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.lang import Builder

# Using Builder to define the layout in a cleaner way (like HTML/CSS)
Builder.load_string('''
<AnqaaLayout>:
    orientation: 'vertical'
        
    # 1. Top Bar
    AnchorLayout(anchor_x='center', anchor_y='top', size_hint_y=None, height=60, padding=[10, 10]):
        BoxLayout:
            size_hint_x: None
            width: self.parent.width - 20
            # Profile Button (Left)
            Button:
                text: '👤' # Profile Icon
                size_hint_x: None
                width: 50
                on_press: app.show_points()
                
            # App Name (Center)
            Label:
                text: 'Anqaa'
                font_size: '24sp'
                bold: True
                
            # Theme Toggle Button (Right)
            Button:
                text: '☀️' # Sun Icon for Light/Dark mode
                size_hint_x: None
                width: 50

    # 2. Conversation Area
    ScrollView:
        BoxLayout:
            id: conversation_area
            orientation: 'vertical'
            spacing: 15
            padding: 10
            size_hint_y: None
            height: self.minimum_height
            # A welcome message
            Label:
                text: "Welcome to Anqaa! How can I help you today?"
                size_hint_y: None
                height: 40

    # 3. Bottom Smart Toolbar
    BoxLayout:
        size_hint_y: None
        height: 60
        padding: 5
        spacing: 5
            
        # Attachment Button
        Button:
            text: '+'
            font_size: '20sp'
            size_hint_x: 0.15

        # Text Input
        TextInput:
            id: text_input
            hint_text: 'Ask Anqaa anything...'
            multiline: False
                
        # Microphone/Video Button
        Button:
            text: '🎤'
            font_size: '20sp'
            size_hint_x: 0.15

        # Advanced Tools Button
        Button:
            text: '🚀'
            font_size: '20sp'
            size_hint_x: 0.15
                
        # Social Integration Button
        Button:
            text: '🔗'
            font_size: '20sp'
            size_hint_x: 0.15

''')

class AnqaaLayout(BoxLayout):
    pass

class AnqaaApp(App):
    def build(self):
        # Set dark theme as default
        Window.clearcolor = (0.1, 0.1, 0.1, 1)
        self.points = 300 # User's daily points
        return AnqaaLayout()

    def show_points(self):
        # This is a placeholder. Later, it will open a profile screen.
        print(f"Button Pressed! Current points: {self.points}")
        # We can add a popup later to show points and invite friends
        pass

if __name__ == '__main__':
    AnqaaApp().run()

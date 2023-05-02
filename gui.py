# This will use kivy and be the frontend gui for the login/register

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition


class Welcome(GridLayout):
    def __init__(self, **kwargs):
        super(Welcome, self).__init__(**kwargs)

        self.cols = 1

        self.top_grid = GridLayout()
        self.top_grid.cols = 2

        self.add_widget(Label(text='Welcome! Please select an option below.'))

        button1 = Button(text="Login")
        button1.bind(on_press=self.login)
        self.top_grid.add_widget(button1)

        button2 = Button(text="Create An Account")
        button2.bind(on_press=self.create)
        self.top_grid.add_widget(button2)

        self.add_widget(self.top_grid)

    def create(self, instance):
        app = App.get_running_app()
        app.root.transition = SlideTransition(direction='left')
        app.root.current = 'create'

    def login(self, instance):
        app = App.get_running_app()
        app.root.transition = SlideTransition(direction='right')
        app.root.current = 'login'


class Template(GridLayout):
    def __init__(self, **kwargs):
        super(Template, self).__init__(**kwargs)
        self.add_widget(Label(text='User Name'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)

        self.add_widget(Label(text='password'))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)

        button1 = Button(text="Clear")
        button1.bind(on_press=self.clear)
        self.add_widget(button1)


    def clear(self, instance):
        self.username.text = ''
        self.password.text = ''
        print("Test")


class LoginScreen(Template):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2

        button = Button(text="Login")
        button.bind(on_press=self.callback)
        self.add_widget(button)
        button2 = Button(text="Go Back")
        button2.bind(on_press=self.back)
        self.add_widget(button2)

    def back(self, instance):
        app = App.get_running_app()
        app.root.transition = SlideTransition(direction='left')
        app.root.current = 'welcome'

    def callback(self, instance):
        print("Username:", self.username.text)
        print("Password:", self.password.text)




class CreateAccount(Template):
    def __init__(self, **kwargs):
        super(CreateAccount, self).__init__(**kwargs)
        self.cols = 2

        button = Button(text="Create An Account")
        button.bind(on_press=self.callback)
        self.add_widget(button)
        button2 = Button(text="Go Back")
        button2.bind(on_press=self.back)
        self.add_widget(button2)

    def back(self, instance):
        app = App.get_running_app()
        app.root.transition = SlideTransition(direction='right')
        app.root.current = 'welcome'



    def callback(self, instance):
        print("Username:", self.username.text)
        print("Password:", self.password.text)


class MyApp(App):
    def build(self):
        # Create the screen manager
        sm = ScreenManager(transition=SlideTransition(direction='right'))

        # Create the screens
        welcome_screen = Screen(name='welcome')
        welcome_screen.add_widget(Welcome())
        login_screen = Screen(name='login')
        login_screen.add_widget(LoginScreen())
        create_screen = Screen(name='create')
        create_screen.add_widget(CreateAccount())

        # Add the screens to the screen manager
        sm.add_widget(welcome_screen)
        sm.add_widget(login_screen)
        sm.add_widget(create_screen)

        # Set the default screen
        sm.current = 'welcome'

        # Return the screen manager as the root widget
        return sm


if __name__ == '__main__':
    MyApp().run()
import kivy  
from kivy.app import App 
kivy.require('1.9.0')

from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.uix.popup import Popup 
from kivy.uix.floatlayout import FloatLayout 
from kivy.uix.widget import Widget

from kivy.network.urlrequest import UrlRequest
import urllib
import json
import os

Builder.load_string("""
<ScreenOne>:
	BoxLayout:
		id: main_win 
        orientation: "vertical"
        spacing: 10
        space_x: self.size[0]/3
					
        canvas.before: 
            Color: 
                rgba: (1, 1, 1, 1) 
            Rectangle: 
                source:'MYc_logo.jpg'
                size: root.width, root.height 
                pos: self.pos 
					
		Button:
			text: "Login"
            pos_hint: {"x":0.333, "top":.3}
            size_hint: .30, 0
            background_color: (0.06, .36, .4, .675) 
            font_size: 40
			on_press:
				# You can define the duration of the change
				# and the direction of the slide
				root.manager.transition.direction = 'left'
				root.manager.transition.duration = 1
				root.manager.current = 'screen_two'

<ScreenTwo>:
	BoxLayout:
		Button:
			text: "Go to Screen 3"
			background_color : 1, 1, 0, 1
			on_press:
				root.manager.transition.direction = 'left'
				root.manager.transition.duration = 1
				root.manager.current = 'screen_three'

<ScreenThree>:
	BoxLayout:
		Button:
			text: "Go to Screen 4"
			background_color : 1, 0, 1, 1
			on_press:
				root.manager.transition.direction = 'left'
				root.manager.transition.duration = 1
				root.manager.current = 'screen_four'

<ScreenFour>:
	BoxLayout:
		Button:
			text: "Go to Screen 5"
			background_color : 0, 1, 1, 1
			on_press:
				root.manager.transition.direction = 'left'
				root.manager.transition.duration = 1
				root.manager.current = 'screen_five'

<ScreenFive>:
	BoxLayout:
		Button:
			text: "Go to Screen 1"
			background_color : 1, 0, 0, 1
			on_press:
				root.manager.transition.direction = 'right'
				root.manager.current = 'screen_one'


""")

# class to call the popup function 
class PopupWindow(Widget): 
    def btn(self): 
        popFun() 
  
# class to build GUI for a popup window 
class P(FloatLayout): 
    pass
  
# function that displays the content 
def popFun(): 
    show = P() 
    window = Popup(title = "popup", content = show, 
                   size_hint = (None, None), size = (300, 300)) 
    window.open() 

class ScreenOne(Screen):
	pass

class ScreenTwo(Screen):
    email = ObjectProperty(None) 
    pwd = ObjectProperty(None) 
    # validating if the email already exists  
    if email != '':
        params = json.dumps({'email': email, 'password': pwd})
        headers = {'Content-type': 'application/json',
                    'Accept': 'application/json'}
        req = UrlRequest(HOST_URL+'api/accounts/login/', method='POST', on_success=self.user_home_welcome, on_failure=self.user_login_error, req_body=params,
                            req_headers=headers)

        # reset TextInput widget 
        email.text = "" 
        pwd.text = "" 

class ScreenThree(Screen):
	pass

class ScreenFour(Screen):
	pass

class ScreenFive(Screen):
	pass


# The ScreenManager controls moving between screens
screen_manager = ScreenManager()

# Add the screens to the manager and then supply a name
# that is used to switch screens
screen_manager.add_widget(ScreenOne(name ="screen_one"))
screen_manager.add_widget(ScreenTwo(name ="screen_two"))
screen_manager.add_widget(ScreenThree(name ="screen_three"))
screen_manager.add_widget(ScreenFour(name ="screen_four"))
screen_manager.add_widget(ScreenFive(name ="screen_five"))

# Create the App class
class ScreenApp(App):
	def build(self):
		return screen_manager

# run the app 
sample_app = ScreenApp()
sample_app.run()

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.button import ButtonBehavior
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput 

#from workoutbanner import WorkoutBanner
import requests
import json

class HomeScreen(Screen):
    pass

class ImageButton(ButtonBehavior, Image):
    pass	

class MustreadScreen(Screen): 
    pass

class PlumbingScreen(Screen):
    pass

class OrderScreen(Screen):
    pass

class CategoryScreen(Screen):
    pass
class SubPlumbingScreen(Screen):
    pass
 

GUI = Builder.load_file("main.kv")
class MainApp(App):
    my_friend_id = 1	
    def build(self):
        return GUI

    def on_start(self):
        #Get database data
        result = requests.get("https://home-service-43c1b.firebaseio.com/" +str(self.my_friend_id) + ".json")
        data = json.loads(result.content.decode())
        #Get and Update Avatar Image
        banner_image = self.root.ids['home_screen'].ids['banner_image']
        banner_image.source = "icons/" + data['avatar']

       # banner_grid = self.root.ids['home_screen'].ids['banner_grid']
        workouts = data['workouts'][1:]
        for workout in workouts:
        	 # populate workout image in home screen
           print(workout['workout_image'])
           print(workout['units'])
          #  W = WorkoutBanner(workout_image = workout['workout_image'], description = workout['description'])
           # banner_grid.add_widget(W)
       	

    def change_screen(self, screen_name):
        #get the screen manager from the kv file
        screen_manager = self.root.ids['screen_manager']
        screen_manager.current = screen_name
        #screen_manager = self.root.ids	


    

if __name__ == '__main__':
 	MainApp().run()





 			

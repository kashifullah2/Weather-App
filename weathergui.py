from tkinter import *
from weather import Weather
class WeatherGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather Forecasting App")
        self.root.geometry("500x600")
        self.root.resizable(False, False)
        self.image_icon = PhotoImage(file="assets/logo.png")
        self.root.iconphoto(False, self.image_icon)
        self.app_background()
        self.search_bar()
        self.show_weather_info()

    #App Main Background
    def app_background(self):
        #Loade Image
        self.bg_image = PhotoImage(file=("assets/background.png"))
        #Passing Image to Lbl
        self.bg_image_lbl = Label(self.root,image=self.bg_image)
        self.bg_image_lbl.place(x=0,y=0)
    
    #Search Bar
    def search_bar(self):
        #search button image
        self.search_button_image = PhotoImage(file=("assets/search.png"))
        self.search_button_lbl = Button(self.root,background="#0075FF",cursor="hand1",image=self.search_button_image,border=0,highlightthickness=0,command=self.get_info)
        self.search_button_lbl.place(x=350,y=32)
        #Search Entry
        
        self.text_field = Entry(self.root,font="arial 14",width=17,border=0,highlightthickness=0)
        self.text_field.place(x=131,y=39)
        self.text_field.focus()

    #Temperature,humidity,pressure,windspeed,description,clock,timezone etc Label it will show using label
    def show_weather_info(self):
        fonts1 = "arial 20 bold"
        fonts2 = "arial 20"
        self.temperature = Label(self.root,font=fonts1,bg="#0B008F",fg="white")
        self.temperature.place(x=76,y=285)
        self.Humidity = Label(self.root,font=fonts2,bg="#0B008F",fg="white")
        self.Humidity.place(x=76,y=372)
        self.Pressure = Label(self.root,font=fonts2,bg="#0B008F",fg="white")
        self.Pressure.place(x=285,y=372)
        self.WindSpeed = Label(self.root,font=fonts2,bg="#0B008F",fg="white")
        self.WindSpeed.place(x=76,y=457)
        self.Description = Label(self.root,font=fonts2,bg="#0B008F",fg="white")
        self.Description.place(x=285,y=458)

        #Clock:
        self.clock = Label(self.root,font="arial 20",bg="#0B008F",fg="white")
        self.clock.place(x=300,y=267)

        #timezone
        self.timezone = Label(self.root,font="arial 10 bold",bg="#0B008F",fg="white")
        self.timezone.place(x=205,y=265)
        self.long_lat = Label(self.root,font="arial 8",bg="#0B008F",fg="white")
        self.long_lat.place(x=205,y=285)

    #Search Button Click Function
    def get_info(self):
        self.city = self.text_field.get()
        #Weather Object created
        weather_obj = Weather(self.city)

        self.temperature.config(text=f"{weather_obj.temperature}°")
        self.Humidity.config(text=f"{weather_obj.humidity}%")
        self.Pressure.config(text=f"{weather_obj.pressure} hPa")
        self.WindSpeed.config(text=f"{weather_obj.pressure} m/s")
        self.Description.config(text=weather_obj.weather_description)
        
        self.clock.config(text=weather_obj.current_time)
        self.timezone.config(text=f"{weather_obj.timezone}")
        self.long_lat.config(text=weather_obj.long_lat)


#it will check the script is being run as the main program
if __name__=="__main__":
    root = Tk()
    app = WeatherGUI(root)
    root.mainloop()
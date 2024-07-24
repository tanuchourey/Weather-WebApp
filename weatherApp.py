from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz
from PIL import Image, ImageTk
import os

root = Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False, False)

# Function to load and place an image
def load_image(path, widget_class=Label, **kwargs):
    try:
        # Load the image using PIL
        image = Image.open(path)
        photo_image = ImageTk.PhotoImage(image)
        
        # Create the widget with the image
        widget = widget_class(root, image=photo_image, **kwargs)
        widget.image = photo_image  # Keep a reference to avoid garbage collection
        return widget
    except Exception as e:
        print(f"Error loading image '{path}': {e}")
        messagebox.showerror("Error", f"Could not load image '{path}': {e}")
        return None

def getWeather():
    city = textfield.get()
    try:
        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")

        # weather
        api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=bf73ad91743cf7827a49356b6c29723e"
        json_data = requests.get(api).json()

        if json_data["cod"] != 200:
            messagebox.showerror("Error", f"City not found: {city}")
            return

        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp'] - 273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']

        t.config(text=f"{temp}°C")
        c.config(text=f"{condition} | FEELS LIKE {temp}°C")
        w.config(text=f"{wind} m/s")
        h.config(text=f"{humidity}%")
        d.config(text=f"{description}")
        p.config(text=f"{pressure} hPa")
    except Exception as e:
        print(f"Error retrieving weather data: {e}")
        messagebox.showerror("Error", f"Could not retrieve weather data: {e}")

# Ensure paths are correct
base_path = "Projects/Tkinter/"
image_paths = {
    "search": os.path.join(base_path, "search.png"),
    "search_icon": os.path.join(base_path, "search_icon.png"),
    "logo": os.path.join(base_path, "logo.png"),
    "box": os.path.join(base_path, "box.png")
}

# Search Box
myimage = load_image(image_paths["search"])
if myimage:
    myimage.place(x=20, y=20)

textfield = tk.Entry(root, justify="center", width=17, font=("poppins", 25, "bold"), bg="#404040", border=0, fg="white")
textfield.place(x=50, y=40)
textfield.focus()

myimage_icon = load_image(image_paths["search_icon"], widget_class=Button, borderwidth=0, cursor='hand2', bg="#404040", command=getWeather)
if myimage_icon:
    myimage_icon.place(x=400, y=34)

# Logo image
logo = load_image(image_paths["logo"])
if logo:
    logo.place(x=150, y=100)

# Bottom box
frame = load_image(image_paths["box"])
if frame:
    frame.pack(padx=5, pady=5, side=BOTTOM)

# Time
name = Label(root, font=("arial", 15, "bold"))
name.place(x=30, y=100)
clock = Label(root, font=("Helvetica", 20))
clock.place(x=30, y=130)

# Labels
label1 = Label(root, text="WIND", font=("Helvetica", 15, 'bold'), fg='white', bg='#1ab5ef')
label1.place(x=120, y=400)
label2 = Label(root, text="HUMIDITY", font=("Helvetica", 15, 'bold'), fg='white', bg='#1ab5ef')
label2.place(x=250, y=400)
label3 = Label(root, text="DESCRIPTION", font=("Helvetica", 15, 'bold'), fg='white', bg='#1ab5ef')
label3.place(x=430, y=400)
label4 = Label(root, text="PRESSURE", font=("Helvetica", 15, 'bold'), fg='white', bg='#1ab5ef')
label4.place(x=650, y=400)

t = Label(font=("arial", 70, "bold"), fg="#ee666d")
t.place(x=400, y=150)
c = Label(font=("arial", 15, "bold"))
c.place(x=400, y=250)

w = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
w.place(x=120, y=430)
h = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
h.place(x=280, y=430)
d = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
d.place(x=450, y=430)
p = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
p.place(x=670, y=430)

root.mainloop()

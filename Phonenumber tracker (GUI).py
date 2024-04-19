import tkinter
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.ttk import *
import phonenumbers
from phonenumbers import carrier, geocoder, timezone
import tkintermapview
import opencage
from opencage.geocoder import OpenCageGeocode

root = tkinter.Tk()
root.geometry("520x600")

lab = Label(text="Phone Number Tracker", font=("calibri", 15, "bold"), justify="center")
lab.configure(background="blue", foreground="white")
lab.pack(fill=BOTH)

def getResult():
    num = number.get("1.0", END)
    try:
        num1 = phonenumbers.parse(num)
    except:
        messagebox.showerror("Error", "Number box is empty or the input is not numeric!!")

    location = geocoder.description_for_number(num1, "en")
    service_provider = carrier.name_for_number(num1, "en")
    time = timezone.time_zones_for_number(num1)

    key = "ba45fcde6e1743c9afddea8ccfa7631a"
    ocr = OpenCageGeocode(key)
    query = str(location)
    results = ocr.geocode(query)

    lat = results[0]['geometry']['lat']
    lng = results[0]['geometry']['lng']

    my_label = LabelFrame(root)
    my_label.pack(pady=10)

    map_widget = tkintermapview.TkinterMapView(my_label, width=520, height=550, corner_radius=0,border=3)
    map_widget.set_position(lat, lng)
    map_widget.set_marker(lat, lng, text="Location")
    map_widget.set_zoom(15)
    map_widget.place(relx=0, rely=0, anchor=tkinter.CENTER)
    map_widget.pack()

    result.insert(END, "Country: " + location)
    result.insert(END, "\nSim Card: " + service_provider)
    result.insert(END, "\nRegistered: "+ str(time))
    result.insert(END, "\nLatitude: " + str(lat))
    result.insert(END, "\nLongitude: " + str(lng))

number = Text(height=1,font="bold",border=2)
number.pack()

button = Button(text='Search', command=getResult)
button.pack(pady=10, padx=100)

button_style = ttk.Style()
button_style.configure('TButton', font=('calibri', 22, 'bold'), borderwidth='5')
button_style.map('TButton', fg=[('active', '!disabled', 'green')], bg=[('active', 'black')])

result = Text(height=5,font="bold",border=2)
result.pack()

root.mainloop()

import tkinter as tk
import requests
import threading

def get_weather():

    city = entry.get()

    def task():
         data = requests.get(f"https://example.com/weather/{city}").text

         label.config(text=data)
    threading.Thread(target=task).start()

root = tk.Tk()
root.title("Weather App")
entry = tk.Entry(root)
button = tk.Button(root, text="Get Weather", command=get_weather)
button.pack()
label = tk.Label(root, text="")
label.pack()
root.mainloop()

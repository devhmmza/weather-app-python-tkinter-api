import tkinter as tk
import requests
from tkinter import messagebox

def get_weather():
    city = city_entry.get()
    if city == "":
        messagebox.showerror("Error", "Please enter a city name")
        return

    api_key = "4e54e600ca6a824a4d7dcfdfd0ef3c3b"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()
        print(data) 

        if data.get("cod") == 200:
            city_name = data["name"]
            country = data["sys"]["country"]
            temp = data["main"]["temp"]
            description = data["weather"][0]["description"]

            result_label.config(
                text=f"Weather in {city_name}, {country}:\nTemperature: {temp}°C\nDescription: {description.capitalize()}"
            )
        else:
            messagebox.showerror("Error", f"City not found: {data.get('message', '')}")

    except requests.exceptions.RequestException:
        messagebox.showerror("Error", "Network error!")

root = tk.Tk()
root.title("Weather App")
root.geometry("400x250")

tk.Label(root, text="Enter city name:", font=("Arial", 12)).pack(pady=10)
city_entry = tk.Entry(root, font=("Arial", 12), width=30)
city_entry.pack()

search_button = tk.Button(root, text="Get Weather", command=get_weather, font=("Arial", 12))
search_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12), justify="left")
result_label.pack(pady=20)

root.mainloop()

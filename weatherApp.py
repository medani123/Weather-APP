import tkinter as tk
import requests

HEIGHT = 500
WIDTH = 600

def test_function(entry):
    print("this is the entry:", entry)

# 928eb1c62725c08ad232cf00447ada05

# api.openweathermap.org/data/2.5/forecast/daily?q={city name},{country code}&cnt={cnt}

def format_Response(weather):
    name = (weather['name'])
    desc = (weather['weather'][0]['description'])
    temp = (weather['main']['temp'])

    return str(name) + ' ' + str(desc) + ' ' + str(temp)

def get_weather(city):
    weather_key = '928eb1c62725c08ad232cf00447ada05'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key,'q': city, 'units':'Metric'}
    response = requests.get(url, params=params)
    weather = response.json()

    label['text'] = format_Response(weather)

    print(weather['name'])
    print(weather['weather'][0]['description'])
    print(weather['main']['temp'])



root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame=tk.Frame(root, bg='blue', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Weather Condition", font=40, command= lambda:get_weather(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame= tk.Frame(root, bg='#80c1ff', bd = 10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label= tk.Label(lower_frame)
label.place(relwidth=1, relheight=1)


root.mainloop()
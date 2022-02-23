import requests
import json

mychoice = ""
sensor = ""

while sensor != "quit".casefold() or mychoice != "quit".casefold():
    print("Choose which sensor do you wanna use")
    sensor = input("")
    if sensor!="sensor".casefold():
        print("No sensor found. Try again")
        pass

    print("Choose:\nTemperature,humidity,all sensor,quit")
    mychoice = input("")
    if mychoice == "temperature".casefold():
            url = "http://127.0.0.1:9090"+"/"+sensor+"/"+mychoice
            x = requests.get(url)
    elif mychoice == "humidity".casefold():
            url = "http://127.0.0.1:9090"+"/"+sensor+"/"+mychoice
            x = requests.get(url)
    elif mychoice == "all sensor".casefold():
            url = "http://127.0.0.1:9090"+"/"+mychoice
            x = requests.get(url)
    else:
            print("Error! there's something wrong")

if sensor == "quit".casefold() or mychoice == "quit".casefold():
    print("Session is stopped")
    pass
else:
    print(x.text)


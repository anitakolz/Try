import random
import cherrypy
import json
import time

class tempsensor():

    exposed = True

    def GET(self,*uri):

        temperature = []
        humidity = []
        newoutput = []
        if len(uri)!=0:
            numsens = list(range(10))
            for i in numsens:
                input = {
                    "bn":"",
                    "e": [
                        {
                            "temperature":0,
                            "humidity":0,
                            "u": "anita",
                            "ID": "1234",
                            "time": round(time.time(),1),
                        }
                    ]
                }
                input["bn"] = "sensor"+str(i)
                print(input)
                newoutput.append(input)
            print(newoutput)

            for sensor in newoutput:
                if uri[0] in sensor["bn"]:
                    for items in sensor["e"]:
                        if uri[1] == "temperature".casefold():
                            temperature.append(round(random.uniform(20.5,40.5),1))
                            items["temperature"] = temperature
                        if uri[1] == "humidity".casefold():
                            humidity.append(round(random.uniform(30,60),1))
                            items["humidity"] = humidity
                elif uri[0] == "all sensor":
                    for items in sensor["e"]:
                        temperature.append(round(random.uniform(20.5,40.5),1))
                        items["temperature"] = temperature
                        humidity.append(round(random.uniform(30,60),1))
                        items["humidity"] = humidity
                else:
                    pass
                
        json.dump(newoutput,open("sensor.json","w"))
        return str(newoutput)

if __name__ == "__main__":
    #Standard configuration to serve the url "localhost:8080"
        conf={
        '/':{
                    'request.dispatch':cherrypy.dispatch.MethodDispatcher(),
                    'tool.session.on':True
            }
        }
        cherrypy.config.update({'server.socket_port': 9090})
        cherrypy.quickstart(tempsensor(),'/',conf)
        cherrypy.engine.start()
        cherrypy.engine.block()
    

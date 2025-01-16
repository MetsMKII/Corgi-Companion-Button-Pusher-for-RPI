#Hello World (Boiler Plate) Start
import json
import RPi.GPIO
print (type("RPI_Button_Pusher Start"))


# Variables
computer_model = None
device_list = []




#Load Config (JSON) Module Start
def load_config():
    with open("config.json","r") as C:
        imported_file = json.load(C)
        return imported_file

config_file = load_config()

"""for item in config_file:
    device_list = {"device_list":None}
    device_list["device_list"] = item["device_list"]
    config_file.append(device_list)
"""


print(config_file["device_list"][0]["device_ID"])
#print(config_file["device_list"][1])

print ("Load Config (Json) Module End")
#Load Config (JSON) Module End


#GPIO Listen Module Start



#print ("GPIO Listen Module End")
#GPIO Listen Module End


#Events Module Start
#print ("Events Module End")
#Events Module End


#Edit Events/Varibles (Json) Module Start

#print ("Edit Events Module End")
#Edit Events/Varible Module End



#Save Events/Varibles  to Config File (JSON) Start
#print ("Events/Varibles to config file End")
#Save Events/Varibles to config file (JSON) End

#GUI





print ("RPI_Button_Pusher End Program")
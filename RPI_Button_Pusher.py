#Hello World (Boiler Plate) Start
import json
import RPi.GPIO as GPIO


GPIO.RPI_INFO

print (type("RPI_Button_Pusher Start"))

# Information
Software_Build = 0001
Software_Version = A.0.0


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

# Setting up GPIPO module

GPIO.setmode(GPIO.BOARD)
mode = GPIO.getmode()
GPIO.setwarnings(False)

chan_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]

GPIO.setup(chan_list, GPIO.in)

#GPIO edge events

if GPIO.event_detected(1):
    print('Button pressed')

GPIO.add_event_detect(chan_list, GPIO.RISING)



#def GPIO_listen():



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


# Program Shut down



GPIO.cleanup()

print ("RPI_Button_Pusher End Program")

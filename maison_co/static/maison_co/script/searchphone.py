# import bluetooth

# target_name = "HUAWEI P20 Pro"
# target_address = None

# nearby_devices = bluetooth.discover_devices()

# for bdaddr in nearby_devices:
#     if target_name == bluetooth.lookup_name( bdaddr ):
#         target_address = bdaddr
#         break

# if target_address is not None:
#     print("found target bluetooth device with address "), target_address
# else:
#     print("could not find target bluetooth device nearby")

# This project requires PyBluez
import tkinter as tk
import bluetooth

#Look for all Bluetooth devices
#the computer knows about.
print("Searching for devices...")
print("")
#Create an array with all the MAC
#addresses of the detected devices
nearby_devices = bluetooth.discover_devices(lookup_names=True)
#Run through all the devices found and list their name
num = 0
print ("Select your device by entering its coresponding number...")

for addr, name in nearby_devices:
	num+=1
	print( num , ": " , name)
	
# #Allow the user to select their Arduino
# #bluetooth module. They must have paired
# #it before hand.
selection = int(input("> ")) - 1


bd_addr = nearby_devices[selection][0]
name = nearby_devices[selection][1]
print ("You have selected", name)
services = bluetooth.find_service(address=str(bd_addr))
for svc in services:
    print("Service Name: %s"    % svc["name"])
    print("    Host:        %s" % svc["host"])
    print("    Description: %s" % svc["description"])
    print("    Provided By: %s" % svc["provider"])
    print("    Protocol:    %s" % svc["protocol"])
    print("    channel/PSM: %s" % svc["port"])
    print("    svc classes: %s "% svc["service-classes"])
    print("    profiles:    %s "% svc["profiles"])
    print("    service id:  %s "% svc["service-id"])
    print("")

# port = 12
# client_sock = bluetooth.BluetoothSocket( bluetooth.RFCOMM )
# client_sock.setblocking(True)
# print(bd_addr, ' : ', port)
# # sock.connect((bd_addr, port))
# timeout = 10
# error=False
# while timeout > 0:
# 	try:
# 		client_sock.connect((bd_addr, port))
# 		timeout = -1
# 	except bluetooth.btcommon.BluetoothError:
# 		time.sleep(1)
# 		timeout -= 1
# 		print("Waiting for connection...")
# 		continue
# 	# except OSError:
# 	# 	print(OSError.message)
# 	# 	error=True
# 	# 	break
# if timeout == 0:
# 	print("Could not connect to server! PLZ try again and hope for better luck")

# elif error==False:
# 	print("Successfully connected to ", addr)

#Create the GUI
# class Application(tk.Frame):

# #Create a connection to the socket for Bluetooth
# #communication
#     sock = bluetooth.BluetoothSocket( bluetooth.RFCOMM )

#     def disconnect(self):
#     	#Close socket connection to device
#         self.sock.close()
        
#     def on(self):
#     	#Send 'H' which the Arduino
#     	#detects as turning the light on
#         data = "H"
#         self.sock.send(data)

#     def off(self):
#     	#Send 'L' to turn off the light
#     	#attached to the Arduino
#         data = "L"
#         self.sock.send(data)

#     def createWidgets(self):
#     	#Form all the buttons.
#     	#Look at a Tkinter reference
#     	#for explanations.
#         self.QUIT = tk.Button(self)
#         self.QUIT["text"] = "QUIT"
#         self.QUIT["fg"]   = "red"
#         self.QUIT["command"] =  self.quit

#         self.QUIT.pack({"side": "left"})

#         self.disconnectFrom = tk.Button(self)
#         self.disconnectFrom["text"] = "Disconnect"
#         self.disconnectFrom["fg"]   = "darkgrey"
#         self.disconnectFrom["command"] =  self.disconnect

#         self.disconnectFrom.pack({"side": "left"})

#         self.turnOn = tk.Button(self)
#         self.turnOn["text"] = "On",
#         self.turnOn["fg"] = "green"
#         self.turnOn["command"] = self.on

#         self.turnOn.pack({"side": "left"})

#         self.turnOff = tk.Button(self)
#         self.turnOff["text"] = "Off"
#         self.turnOff["fg"] = "red"
#         self.turnOff["command"] = self.off

#         self.turnOff.pack({"side": "left"})

#     def __init__(self, master=None):
#     	#Connect to the bluetooth device
#     	#and initialize the GUI
#         self.sock.connect((bd_addr, port))
#         tk.Frame.__init__(self, master)
#         self.pack()
#         self.createWidgets()

# #Begin the GUI processing
# root = tk.Tk()
# app = Application(master=root)
# app.mainloop()
# root.destroy()

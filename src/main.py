import json

with open("data/devices.json") as file:
    devices = json.load(file)

for hostname, device in devices.items():
    
    if device["online"]:
        status = "ONLINE"
    else: 
        status = "OFFLINE"
    print(f"{hostname} - {device["ip"]} - {status}")
    

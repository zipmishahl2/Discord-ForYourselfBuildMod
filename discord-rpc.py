import time
from pypresence import Presence

client_id = "1138490802964791357" 

RPC = Presence(client_id)
RPC.connect()

RPC.update(state="ForYourselfBuildMod", details="Version 3.9", large_image="logomisha", start=int(time.time()))

while True:
    try:
        RPC.update(state="ForYourselfBuildMod", details="Version 3.9", large_image="logomisha", start=int(time.time()))
    except Exception as e:
        print(e)
        RPC.connect()

    time.sleep(15)

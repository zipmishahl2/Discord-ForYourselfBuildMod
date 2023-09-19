import time
from pypresence import Presence

client_id = "YOUR_CLIENT_ID" 

RPC = Presence(client_id)
RPC.connect()

RPC.update(state="Playing Solo", details="In a Match", large_image="large_image", start=int(time.time()))

while True:
    try:
        RPC.update(state="Playing Solo", details="In a Match", large_image="large_image", start=int(time.time()))
    except Exception as e:
        print(e)
        RPC.connect()

    time.sleep(15)

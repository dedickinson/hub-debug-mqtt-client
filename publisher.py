#!/usr/bin/env python3

import signal
import sys
import json
import time
import paho.mqtt.client as mqtt

client = mqtt.Client()

def signal_handler(sig, frame):
        print("Disconnecting")
        client.disconnect()
        sys.exit(0)


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))


def on_publish(client, userdata, mid):
    print(mid)


msg = {
    "message": "hello,world"
}

json_msg: str = json.dumps(msg)

client.on_connect = on_connect
client.on_publish = on_publish

client.connect("mqtt", 1883, 60)

while True:
    msg = client.publish("debug", payload=json_msg)
    msg.wait_for_publish()
    time.sleep(5)

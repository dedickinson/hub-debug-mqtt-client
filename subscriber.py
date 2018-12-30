#!/usr/bin/env python3

import signal
import sys
import json
import paho.mqtt.client as mqtt

client = mqtt.Client()

def signal_handler(sig, frame):
        print("Disconnecting")
        client.disconnect()
        sys.exit(0)


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("debug")


def on_message(client, userdata, msg):
    print(f"{msg.topic} - {str(msg.payload)}")


client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt", 1883, 60)

signal.signal(signal.SIGINT, signal_handler)

client.loop_forever()

import time
import random
import jsons
import pytz
import json

import paho.mqtt.client as mqtt


class Silos:
    id: int
    temp: float
    ph: float
    int_temp: float
    ext_temp: float
    int_humidity: float
    ext_humidity: float
    int_pression: float
    sensor_1: float
    sensor_2: float
    sensor_3: float
    time = None

    def random(self):
        for var, var_type in self.__annotations__.items():
            random_value = None

            if var_type is int:
                random_value = random.randint(1, 10)
            
            elif var_type is float:
                random_value = random.uniform(0.0, 100.0)

            setattr(self, var, random_value)
        
        self.time = time.time_ns()


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("info")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    if msg.topic == 'info':
        print(msg.topic+" "+str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_start()

a = Silos()

try:
    while True:
        a.random()
        client.publish('t/measurement', jsons.dumps(a))
        time.sleep(.5)

except KeyboardInterrupt:
    client.disconnect()
    client.loop_stop()

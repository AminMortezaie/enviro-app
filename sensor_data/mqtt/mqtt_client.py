import paho.mqtt.client as mqtt
from sensor_data.models import SensorData
import os

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker from Client....")
        subscribe()
    else:
        print(f"Failed to connect, return code {rc}")

def on_message(client, userdata, msg):
    try:
        payload = msg.payload.decode()
        data = payload.split(", ")
        temperature = float(data[0].split(": ")[1].replace("C", ""))
        humidity = float(data[1].split(": ")[1].replace("%", ""))
        hub_id = msg.topic.split("/")[-1]

        SensorData.objects.create(
            hub_id=hub_id,
            temperature=temperature,
            humidity=humidity
        )
        print(f"Saved temp: {temperature} and humidity:{humidity} from {hub_id}")
    except Exception as e:
        print(f"Failed to process message: {e}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

def start_mqtt():
    client.connect("mqtt-broker", 1883, 60)
    client.loop_start()


def subscribe():
    hub_id = os.getenv('hub_id')
    client.subscribe(f"sensor/data/{hub_id}")
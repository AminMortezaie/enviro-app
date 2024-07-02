import paho.mqtt.client as mqtt
from sensor_data.models import SensorData

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!\n")
        client.subscribe("sensor/data/#")
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
        print(f"Saved data from {hub_id}")
    except Exception as e:
        print(f"Failed to process message: {e}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

def start_mqtt():
    client.connect("mqtt-broker", 1883, 60)
    client.loop_start()

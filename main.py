import paho.mqtt.client as paho
import random
import base64
from cryptography.fernet import Fernet
import json 

BROKER = 'broker.hivemq.com'  
PORT = 1883  
TOPIC = 'movantchat/python'  
CLIENT_ID = f'movant-mqtt-{random.randint(0, 1000)}'  

CHAT_ROOMS = {
    'python': 'movantchat/python'
}

password = "pippi"  

def generate_key(passphrase: str):
    key = base64.urlsafe_b64encode(bytes(passphrase.ljust(32), 'utf-8'))
    return key

def encrypt(message: dict, fernet: Fernet):
    message_to_json = json.dumps(message)  
    encrypted_message = fernet.encrypt(message_to_json.encode())
    return encrypted_message

#
def decrypt(encrypted_message: bytes, fernet: Fernet):
    """Avkryptera meddelandet och konvertera tillbaka till JSON-objekt"""
    decrypted_message = fernet.decrypt(encrypted_message).decode()
    message = json.loads(decrypted_message)
    return message

class Chat:
    def __init__(self, username, room):
        self.username = username
        self.room = room
        self.topic = CHAT_ROOMS[room]
        self.client = None

        self.key = generate_key(password)  
        self.key_handler = Fernet(self.key)  

        self.connect_mqtt()

    def on_connect(self, client, userdata, flags, rc):
        print(f"Connected to MQTT broker.")
        if rc == 0:
            print("Successfully connected!")
            self.client.subscribe(self.topic)  
        else:
            print(f"Connection failed...")

    def connect_mqtt(self):
        self.client = paho.Client(CLIENT_ID)
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

        print(f"Connecting to MQTT broker {BROKER}...")
        self.client.connect(BROKER, PORT, 60)  
        self.client.loop_start()  

    def on_message(self, client, userdata, msg):
        try:
            decrypted_message = decrypt(msg.payload, self.key_handler)
            print(f"Message received: {decrypted_message}")
        except Exception as e:
            print(f"Error when process the message: {e}")

    def init_client(self):
        pass


    def run(self):
        while True:
            msg_to_send = input(f"{self.username}: ")

            if msg_to_send.lower() == "quit":
                message = {"username": self.username, "message": f"{self.username} has left the chat. Bye bye to u!"}
                encrypted_message = encrypt(message, self.key_handler)
                self.client.publish(self.topic, encrypted_message)
                print(f"{self.username} has left the chat. Goodbye, {self.username}! Take care of u!")
                self.client.disconnect()  
                break
                 
            else:
                message = {"username": self.username, "message": msg_to_send}
                encrypted_message = encrypt(message, self.key_handler)
                self.client.publish(self.topic, encrypted_message)
                print(f"{self.username}: {msg_to_send}")

def main():
    username = input("Enter your username: ")


    print("Pick a room:")
    for room in CHAT_ROOMS:
        print(f"\t{room}")
    room = input("> ")

    try:
        chat = Chat(username, room)
        chat.run()


    except KeyError:
        print("Wrong room!\n")  


if __name__ == '__main__':
    main()
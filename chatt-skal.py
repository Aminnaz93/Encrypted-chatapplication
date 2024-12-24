import paho.mqtt.client as paho
import random
import threading
import queue


CLIENT_ID = f'movant-mqtt-{random.randint(0, 1000)}'
USERNAME = ''
PASSWORD = ''
BROKER = 'broker.hivemq.com'
PORT = 1883

CHAT_ROOMS = {
    'python': 'movantchat/python'
}


class Chat:
    def __init__(self, username, room):
        self.username = username
        self.room = room
        self.topic = CHAT_ROOMS[room]
        self.client = None
        self.connect_mqtt()
        self.input_queue = queue.Queue()
        
        self.running = True

    @staticmethod
    def on_connect(client, userdata, flags, rc):
        pass

    def connect_mqtt(self):
        pass

    def on_message(self, client, userdata, msg):
        pass

    def init_client(self):
        pass

    def run(self):
        self.init_client()
        
        while True:        
            # get input from user.
            
            if msg_to_send.lower() == "quit":
                # Publish a message that this user leaves the chat

                self.client.publish(self.topic, f"{self.username} has left the chat")
                # Indicate to the input thread that it can exit
                self.running = False
                break
        


def main():
    # Init application. Ask for username and chat room
    username = input("Enter your username: ")

    print("Pick a room:")
    for room in CHAT_ROOMS:
        print(f"\t{room}")
    room = input("> ")

    chat = Chat(username, room)
    chat.run()


if __name__ == '__main__':
    main()

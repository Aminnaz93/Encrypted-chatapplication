ENCRYPTED CHAT APPLICATION.

This project is a simple chat application that uses the MQTT-protocol to send and receive messages between users. The data is encrypted with the help of Fernet-encryption so that only the users in the conversation have access to the data.


* To run the the program, you need to install the following Python-paket.

"pip install paho-mqtt cryptography"


* How to use the chat
1. Type in your name when getting asked. 
2. Choice a chatroom to connect(there's only one room - (python))
3. Write messages to the other users. The messages will be encrypted before they are getting sent and decrypt when the messages arrives to the other user.
4. To end the program just type in 'quit' in the chat. 


Programmed by: Amin & Jonathan
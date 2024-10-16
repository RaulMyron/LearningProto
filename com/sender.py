import socket
import messsage_pb2

def main():
    host = '127.0.0.1'
    port = 1660

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        while True:
            message = input("Enter message: ")
            if not message:
                continue

            chat_message = messsage_pb2.ChatMessage()
            chat_message.message = message
            serialized_message = chat_message.SerializeToString()

            s.sendall(serialized_message)

if __name__ == "__main__":
    main()
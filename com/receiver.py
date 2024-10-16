import socket
import messsage_pb2

def main():
    host = '127.0.0.1'
    port = 1660

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print("Waiting for a connection...")
        conn, addr = s.accept()
        print(f"Connected by {addr}")

        with conn:
            while True:
                data = conn.recv(1024)
                if not data:
                    continue

                chat_message = messsage_pb2.ChatMessage()
                chat_message.ParseFromString(data)
                print(f"Received: {chat_message.message}")

if __name__ == "__main__":
    main()
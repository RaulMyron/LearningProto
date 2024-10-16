import hello_pb2

# Create a new message
message = hello_pb2.HelloMessage()
message.greeting = "Hello, world!"
print('m', message)



# Serialize the message to a string
serialized_message = message.SerializeToString()

print(serialized_message)
print('hello_pb2.HelloMessage()', hello_pb2.HelloMessage())

# Deserialize the message from a string
new_message = hello_pb2.HelloMessage()
new_message.ParseFromString(serialized_message)

print(new_message.greeting)
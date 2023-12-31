import grpc

import greeting_service_pb2
import greeting_service_pb2_grpc

def run():
	with grpc.insecure_channel('localhost:8080') as channel:

		stub = greeting_service_pb2_grpc.GreetingServiceStub(channel)

		response =stub.greeting(greeting_service_pb2.HelloRequest(name = 'Vlad Python'))

	print("Greeting from server: " + response.greeting)

run()
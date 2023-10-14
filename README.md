## How to use ##

- Use follow command for generate gRPC code
    ```
    python3 -m grpc_tools.protoc -I./ --python_out=. --grpc_python_out=. greeting_service.proto
    ```
- Run gRPC server
- Run application 
    ```
    python3 grpc_client.py
    ```
import xmlrpc.server

# Define the functions that will be exposed to the clients
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        raise ValueError("Cannot divide by zero")

# Create an RPC server instance
server = xmlrpc.server.SimpleXMLRPCServer(("localhost", 8000))

# Register the functions to be exposed
server.register_function(add, "magicAdd")
server.register_function(subtract, "subtract")
server.register_function(multiply, "multiply")
server.register_function(divide, "divide")

# Start the server
print("Starting RPC server...")
server.serve_forever()
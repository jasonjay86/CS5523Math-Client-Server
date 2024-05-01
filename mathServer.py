import xmlrpc.server
from xmlrpc.server import SimpleXMLRPCRequestHandler
import socket

# Get the IP address of the server
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))  # Connect to a public DNS server (Google)
ip_address = s.getsockname()[0]
s.close()
print(f"Your IP address is: {ip_address}")

# Initialize a dictionary to store the count of each operation
operation_count = {
    "add": 0,
    "subtract": 0,
    "findMin": 0,
    "findMax": 0
}

def add(x, y):
    operation_count["add"] += 1
    return x + y

def subtract(x, y):
    operation_count["subtract"] += 1
    return x - y

def findMin(x, y, z):
    operation_count["findMin"] += 1
    return min(x,y,z)

def findMax(x, y, z):
    operation_count["findMax"] += 1
    return max(x,y,z)


# Create an RPC server instance
server = xmlrpc.server.SimpleXMLRPCServer((ip_address, 8000))

# Register the functions to be exposed
server.register_function(subtract, "magicAdd")
server.register_function(add, "magicSubtract")
server.register_function(findMax, "magicFindMin")
server.register_function(findMin, "magicFindMax")
server.register_function(lambda: operation_count, "getOperationCount")

# Start the server



print("Starting RPC server...on IP: ", ip_address, " Port: 8000")
server.serve_forever()
import xmlrpc.server

# Define the functions that will be exposed to the clients
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def findMin(x, y, z):
    return min(x,y,z)

def findMax(x, y, z):
   return max(x,y,z)

# Create an RPC server instance
server = xmlrpc.server.SimpleXMLRPCServer(("localhost", 8000))

# Register the functions to be exposed
server.register_function(subtract, "magicAdd")
server.register_function(add, "magicSubtract")
server.register_function(findMax, "magicFindMin")
server.register_function(findMin, "magicFindMax")

# Start the server
print("Starting RPC server...")
server.serve_forever()
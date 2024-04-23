import xmlrpc.client
import random

# Create an RPC proxy object for the mathServer
proxy = xmlrpc.client.ServerProxy("http://localhost:8000")

for i in range(10):
    #  Randomly select a function to call
    whichFunc = random.randint(1, 4)
    
    # Generate random numbers to pass as arguments
    random_double1 = random.uniform(1.0, 100.0)
    random_double2 = random.uniform(1.0, 100.0)
    random_int1 = random.randint(1, 100)
    random_int2 = random.randint(1, 100)
    random_int3 = random.randint(1, 100)

    if whichFunc == 1:
        print("Magic Adding ", random_double1, " and ", random_double2)
        result = proxy.magicAdd(random_double1, random_double2)
        print("Magic Add Result! ", result)
    elif whichFunc == 2:
        print("Magic Subtracting ", random_double1, " and ", random_double2)
        result = proxy.magicSubtract(random_double1, random_double2)
        print("Magic Subtract Result! ", result)
    elif whichFunc == 3:
        print("Magic Finding Min of ", random_int1, ", ", random_int2, ", and ", random_int3)
        result = proxy.magicFindMin(random_int1, random_int2, random_int3)
        print("Magic Find Min Result! ", result)
    else:
        print("Magic Finding Max of ", random_int1, ", ", random_int2, ", and ", random_int3)
        result = proxy.magicFindMax(random_int1, random_int2, random_int3)
        print("Magic Find Max Result! ", result)
    
# Get operation Counts
result = proxy.getOperationCount()
print("OperationCount ", result)

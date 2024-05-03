import xmlrpc.client
import random
import argparse
import matplotlib.pyplot as plt

def main(ip, count=10):
    # Create an RPC proxy object for the mathServer
    address = "http://" + ip + ":8000"
    proxy = xmlrpc.client.ServerProxy(address)
    # proxy = xmlrpc.client.ServerProxy("http://localhost:8000")

    for i in range(count):
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
        print("*" * 50)
    # Get operation Counts
    result = proxy.getOperationCount()
    print("OperationCount ", result)

    operations = list(result.keys())
    counts = list(result.values())

    # Create a bar chart
    plt.figure(figsize=(10, 6))
    plt.bar(operations, counts, color='skyblue')
    plt.xlabel('Operation')
    plt.ylabel('Count')
    plt.title('Operation Counts')
    plt.ylim(0, max(counts) + 20)  # Adding a buffer for better visualization
    plt.grid(axis='y', linestyle='--', alpha=0.6)

    # Save the chart as a PNG file
    plt.savefig('operation_counts.png')

    # Display the chart
    plt.show()

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="testClient.py - A simple RPC client to test the mathServer.py RPC server.")
  parser.add_argument("ip", help="The IP address of the RPC server.")
  parser.add_argument("-c", "--count", type=int, default=10,
                      help="Optional argument to specify how many times to call the RPC server. Default is 10.")
  args = parser.parse_args()
  main(args.ip, args.count)
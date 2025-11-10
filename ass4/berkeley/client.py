#!/usr/bin/env python3
import socket
import sys

PORT = 5000

if len(sys.argv) < 3:
    print("Usage: python3 client.py <client_id> <initial_time>")
    print("Example: python3 client.py 1 105")
    sys.exit(1)

client_id = sys.argv[1]
client_time = int(sys.argv[2])

print(f"Client {client_id}")
print(f"Initial Time: {client_time}")
print("Connecting...\n")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', PORT))
print("Connected!\n")

command = client.recv(1024).decode()
if command == "GET_TIME":
    print("Server requested time")
    print(f"Sending: {client_time}")
    client.send(str(client_time).encode())

adjustment = float(client.recv(1024).decode())
print(f"\nAdjustment: {adjustment:+.2f}")

old_time = client_time
client_time += adjustment

print(f"Old Time: {old_time}")
print(f"New Time: {client_time}")

client.close()

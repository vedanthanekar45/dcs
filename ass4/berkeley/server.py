#!/usr/bin/env python3
import socket

PORT = 5000
NUM_CLIENTS = 3
server_time = 100

print("Berkeley Algorithm - Server")
print(f"Server Time: {server_time}")
print(f"Waiting for {NUM_CLIENTS} clients...\n")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', PORT))
server.listen(NUM_CLIENTS)

clients = []
for i in range(NUM_CLIENTS):
    conn, addr = server.accept()
    clients.append(conn)
    print(f"Client {i+1} connected")

print("\n--- Starting Synchronization ---\n")

client_times = []
for i, client in enumerate(clients):
    client.send("GET_TIME".encode())
    time_data = client.recv(1024).decode()
    client_time = int(time_data)
    client_times.append(client_time)
    print(f"Client {i+1} Time: {client_time}")

all_times = [server_time] + client_times
average = sum(all_times) / len(all_times)
print(f"\nAverage Time: {average}")

server_adjustment = average - server_time
print(f"\nServer Adjustment: {server_adjustment:+.2f}")
server_time = average
print(f"New Server Time: {server_time}")

print("\nSending adjustments:")
for i, (client, client_time) in enumerate(zip(clients, client_times)):
    adjustment = average - client_time
    print(f"Client {i+1} Adjustment: {adjustment:+.2f}")
    client.send(f"{adjustment}".encode())

print("\n--- Complete ---")

for client in clients:
    client.close()
server.close()

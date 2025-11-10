import java.io.*;
import java.net.*;
import java.util.*;

public class server {
    public static void main(String[] args) throws IOException {
        ServerSocket serverSocket = new ServerSocket(5000);
        System.out.println("Server started. Waiting for clients...");

        int numClients = 3; // number of clients to connect
        List<Socket> clients = new ArrayList<>();
        List<Long> clientTimes = new ArrayList<>();

        // Wait for all clients
        for (int i = 0; i < numClients; i++) {
            Socket socket = serverSocket.accept();
            clients.add(socket);
            System.out.println("Client " + (i + 1) + " connected: " + socket);
        }

        long serverTime = System.currentTimeMillis();
        System.out.println("Server time (ms): " + serverTime);

        // Send server time to all clients and receive their times
        for (Socket socket : clients) {
            DataOutputStream dos = new DataOutputStream(socket.getOutputStream());
            DataInputStream dis = new DataInputStream(socket.getInputStream());

            dos.writeLong(serverTime); // send server time
            dos.flush();

            long clientTime = dis.readLong(); // receive client time
            clientTimes.add(clientTime);
            System.out.println("Received client time: " + clientTime);
        }

        // Compute time differences
        long totalDiff = 0;
        for (long time : clientTimes) {
            totalDiff += (time - serverTime);
        }

        long averageDiff = totalDiff / (numClients + 1); // +1 includes server
        System.out.println("Average time difference: " + averageDiff + " ms");

        // Adjust server time
        long adjustedServerTime = serverTime + averageDiff;
        System.out.println("Adjusted server time: " + adjustedServerTime);

        // Send offset to each client
        for (Socket socket : clients) {
            DataOutputStream dos = new DataOutputStream(socket.getOutputStream());
            long offset = averageDiff - (System.currentTimeMillis() - serverTime);
            dos.writeLong(offset);
            dos.flush();
        }

        System.out.println("Offsets sent to all clients.");

        // Close connections
        for (Socket socket : clients) socket.close();
        serverSocket.close();
    }
}

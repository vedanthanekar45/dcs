import java.io.*;
import java.net.*;

public class client {
    public static void main(String[] args) throws IOException {
        Socket socket = new Socket("localhost", 5000);
        DataInputStream dis = new DataInputStream(socket.getInputStream());
        DataOutputStream dos = new DataOutputStream(socket.getOutputStream());

        // Receive server time
        long serverTime = dis.readLong();
        System.out.println("Received server time: " + serverTime);

        // Simulate client's local clock (with some drift)
        long localTime = System.currentTimeMillis() + (long)(Math.random() * 5000 - 2500); // ±2.5s drift
        System.out.println("Local client time: " + localTime);

        // Send local time to server
        dos.writeLong(localTime);
        dos.flush();

        // Receive offset and adjust
        long offset = dis.readLong();
        long adjustedTime = localTime + offset;

        System.out.println("Offset received: " + offset + " ms");
        System.out.println("Adjusted client time: " + adjustedTime);

        socket.close();
    }
}

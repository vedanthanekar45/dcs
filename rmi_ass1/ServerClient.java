import java.rmi.Naming;

public class ServerClient {
    
    public static void main (String args[]) {
        String answer, value = "Reflection in Java";

        try {
            Search access = (Search)Naming.lookup("rmi://localhost:1900" + "/andor");
            answer = access.query(value);
            System.out.println("Article on " + value + " " + answer + " at Andor.");
        } catch (Exception ae) {
            System.out.println(ae);
        }
    }

}

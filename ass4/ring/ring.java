import java.util.*;

class Process {
    int id;
    boolean isActive;
    Process next;

    public Process(int id, boolean isActive) {
        this.id = id;
        this.isActive = isActive;
        this.next = null;
    }

    @Override
    public String toString() {
        return "Process(ID: " + id + ", Active: " + isActive + ")";
    }
}

public class ring {

    public static Integer electLeader(List<Process> processes, int initiatorId) {
        if (processes == null || processes.isEmpty())
            return null;

        // Find initiator
        Process initiator = null;
        for (Process p : processes) {
            if (p.id == initiatorId) {
                initiator = p;
                break;
            }
        }

        if (initiator == null || !initiator.isActive) {
            System.out.println("Initiator Process " + initiatorId + " not found or inactive");
            return null;
        }

        // Connect processes in a ring
        int n = processes.size();
        for (int i = 0; i < n; i++) {
            processes.get(i).next = processes.get((i + 1) % n);
        }

        // Start election
        List<Integer> electionMessage = new ArrayList<>();
        electionMessage.add(initiator.id);

        Process current = initiator.next;

        System.out.println("Starting election from Process " + initiator.id);
        while (true) {
            if (current.isActive) {
                System.out.println("Process " + current.id + " receives message: " + electionMessage);
                if (!electionMessage.contains(current.id)) {
                    electionMessage.add(current.id);
                }
                // Sort descending to keep highest ID first
                electionMessage.sort(Collections.reverseOrder());
            } else {
                System.out.println("Process " + current.id + " is inactive, message passed through.");
            }

            current = current.next;

            // If message completes one full circle
            if (current.id == initiator.id) {
                break;
            }
        }

        int leaderId = electionMessage.get(0);
        System.out.println("\nElection complete. Elected Leader: Process " + leaderId);
        return leaderId;
    }

    public static void main(String[] args) {
        // Example processes
        List<Process> processes = new ArrayList<>();
        processes.add(new Process(1, true));
        processes.add(new Process(2, false));
        processes.add(new Process(3, true));
        processes.add(new Process(4, true));
        processes.add(new Process(5, true));

        electLeader(processes, 3);
    }
}

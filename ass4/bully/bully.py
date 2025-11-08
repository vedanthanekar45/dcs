#!/usr/bin/env python3
"""
Bully Algorithm - Simple Implementation
Leader election algorithm where the process with highest ID becomes leader
"""

class Process:
    def __init__(self, process_id):
        self.id = process_id
        self.is_alive = True
        self.is_leader = False
    
    def __str__(self):
        status = "Leader" if self.is_leader else "Alive" if self.is_alive else "Dead"
        return f"Process {self.id} [{status}]"

def print_processes(processes):
    """Display current state of all processes"""
    print("\nCurrent Process Status:")
    for p in processes:
        print(f"  {p}")
    print()

def bully_algorithm(processes, initiator_id):
    """
    Bully Algorithm Implementation
    
    Steps:
    1. Initiator sends ELECTION message to all higher ID processes
    2. If any higher process responds with OK, initiator stops
    3. Higher processes start their own election
    4. Process with highest ID becomes coordinator/leader
    """
    
    print(f"\n{'='*60}")
    print(f"Process {initiator_id} initiating election...")
    print(f"{'='*60}")
    
    initiator = processes[initiator_id]
    
    if not initiator.is_alive:
        print(f"Error: Process {initiator_id} is dead!")
        return
    
    # Step 1: Send ELECTION message to all processes with higher ID
    higher_processes = [p for p in processes if p.id > initiator_id and p.is_alive]
    
    print(f"\n[Process {initiator_id}] Sending ELECTION to higher processes: {[p.id for p in higher_processes]}")
    
    if not higher_processes:
        # No higher process - I become the leader
        print(f"[Process {initiator_id}] No higher processes found!")
        print(f"[Process {initiator_id}] I am the new LEADER!")
        
        # Clear previous leader
        for p in processes:
            p.is_leader = False
        
        initiator.is_leader = True
        
        # Send COORDINATOR message to all lower processes
        lower_processes = [p for p in processes if p.id < initiator_id and p.is_alive]
        print(f"[Process {initiator_id}] Announcing to lower processes: {[p.id for p in lower_processes]}")
        
        return initiator_id
    
    # Step 2: Higher processes respond with OK
    print(f"\n[Higher Processes] Sending OK to Process {initiator_id}")
    for p in higher_processes:
        print(f"  - Process {p.id}: OK")
    
    print(f"[Process {initiator_id}] Received OK, stopping my election")
    
    # Step 3: Highest alive process becomes leader
    highest = max(higher_processes, key=lambda p: p.id)
    print(f"\n[Process {highest.id}] I have the highest ID among alive processes")
    print(f"[Process {highest.id}] I am the new LEADER!")
    
    # Clear previous leader and set new one
    for p in processes:
        p.is_leader = False
    
    highest.is_leader = True
    
    # Step 4: Send COORDINATOR message to all processes
    lower_processes = [p for p in processes if p.id < highest.id and p.is_alive]
    print(f"[Process {highest.id}] Announcing to all lower processes: {[p.id for p in lower_processes]}")
    
    return highest.id

def main():
    # Create 5 processes with IDs 0-4
    num_processes = 5
    processes = [Process(i) for i in range(num_processes)]
    
    print("="*60)
    print("BULLY ALGORITHM - Leader Election")
    print("="*60)
    
    # Initial state - Process 4 is the leader
    processes[4].is_leader = True
    print("\nInitial State: Process 4 is the leader")
    print_processes(processes)
    
    # Scenario 1: Process 4 (leader) crashes
    print("\n" + "="*60)
    print("SCENARIO 1: Leader (Process 4) crashes")
    print("="*60)
    processes[4].is_alive = False
    processes[4].is_leader = False
    print_processes(processes)
    
    # Process 2 detects leader is down and starts election
    input("Press Enter to start election from Process 2...")
    bully_algorithm(processes, 2)
    print_processes(processes)
    
    # Scenario 2: Process 4 comes back online
    print("\n" + "="*60)
    print("SCENARIO 2: Process 4 comes back online")
    print("="*60)
    processes[4].is_alive = True
    print_processes(processes)
    
    input("Press Enter for Process 4 to start election...")
    bully_algorithm(processes, 4)
    print_processes(processes)
    
    # Scenario 3: Process 1 starts election (multiple higher processes)
    print("\n" + "="*60)
    print("SCENARIO 3: Process 1 detects leader down")
    print("="*60)
    
    input("Press Enter for Process 1 to start election...")
    bully_algorithm(processes, 1)
    print_processes(processes)
    
    print("\n" + "="*60)
    print("DEMO COMPLETE")
    print("="*60)

if __name__ == "__main__":
    main()

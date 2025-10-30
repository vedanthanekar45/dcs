class Process:
    def __init__ (self, process_id, is_active=True):
        self.id = process_id
        self.is_active = is_active
        self.next_process = None

    def __repr__ (self):
        return f"Process(ID: {self.id}, Active: {self.is_active})"
    
def elect_leader (processes, initiator_id):

    if not processes:
        return None
    
    initiator_index = -1
    for i, p in enumerate(processes):
        if p.id == initiator_id:
            initiator_index = i
            break

    if initiator_index == -1 or not processes(initiator_index).is_active:
        print(f"Initiator Process {initiator_id} not found or inactive")
        return None

    for i in range(len(processes)):
        processes[i].next_processes = processes[(i+1) % len(processes)]
    
    election_message = [processes[initiator_index].id]
    current_process = processes[initiator_index].next_process

    while current_process.id != initiator_id or len(election_message) < len([p for p in processes if p.is_active]):
        if current_process.is_active:
            print(f"Process {current_process.id} receives message: {election_message}")
            if current_process.id not in election_message:
                election_message.append(current_process.id)
            election_message.sort(reverse=True)
        else:
            print(f"Process {current_process.id} is inactive, message passed through.")

        current_process = current_process.next_process

        if current_process.id == initiator_id and len(election_message) == len([p for p in processes if p.is_active]):
            break

    leader_id = election_message[0]
    print(f"\nElection complete. Elected Leader: Process {leader_id}")
    return leader_id
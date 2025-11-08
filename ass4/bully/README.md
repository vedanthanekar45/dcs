# Bully Algorithm - Leader Election

## Overview

The **Bully Algorithm** is a method for electing a coordinator (leader) in a distributed system. The process with the **highest ID** always becomes the leader.

## How It Works

### Algorithm Steps:

1. **Detection**: A process detects that the leader has failed
2. **Election Message**: Process sends ELECTION message to all processes with higher IDs
3. **Response**: 
   - If a higher process responds with OK → initiator stops
   - If NO response from higher processes → initiator becomes leader
4. **Announcement**: New leader sends COORDINATOR message to all lower processes

### Key Rules:

- **Highest ID wins** - Process with highest ID always becomes coordinator
- **Bully behavior** - Higher processes "bully" lower ones by taking over election
- **Self-election** - If no higher process exists, declare yourself leader

## Files

- `bully.py` - Simple simulation of Bully Algorithm

## How to Run

```bash
cd ass4/bully
python3 bully.py
```

## What You'll See

The simulation demonstrates 3 scenarios:

### Scenario 1: Leader Crashes
```
Process 4 (Leader) crashes
↓
Process 2 detects and starts election
↓
Process 2 sends ELECTION to [3, 4]
↓
Process 3 responds OK
↓
Process 3 becomes new leader
```

### Scenario 2: Previous Leader Returns
```
Process 4 comes back online
↓
Process 4 starts election
↓
No higher processes exist
↓
Process 4 becomes leader again (bullies Process 3)
```

### Scenario 3: Lower Process Starts Election
```
Process 1 starts election
↓
Sends ELECTION to [2, 3, 4]
↓
All respond OK
↓
Process 4 (highest) becomes leader
```

## Example Output

```
BULLY ALGORITHM - Leader Election
============================================================

Initial State: Process 4 is the leader

Current Process Status:
  Process 0 [Alive]
  Process 1 [Alive]
  Process 2 [Alive]
  Process 3 [Alive]
  Process 4 [Leader]

============================================================
SCENARIO 1: Leader (Process 4) crashes
============================================================

Current Process Status:
  Process 0 [Alive]
  Process 1 [Alive]
  Process 2 [Alive]
  Process 3 [Alive]
  Process 4 [Dead]

Press Enter to start election from Process 2...

============================================================
Process 2 initiating election...
============================================================

[Process 2] Sending ELECTION to higher processes: [3]

[Higher Processes] Sending OK to Process 2
  - Process 3: OK
[Process 2] Received OK, stopping my election

[Process 3] I have the highest ID among alive processes
[Process 3] I am the new LEADER!
[Process 3] Announcing to all lower processes: [0, 1, 2]

Current Process Status:
  Process 0 [Alive]
  Process 1 [Alive]
  Process 2 [Alive]
  Process 3 [Leader]
  Process 4 [Dead]
```

## Advantages

✅ **Simple** - Easy to understand and implement  
✅ **Fast** - Leader elected quickly  
✅ **Deterministic** - Highest ID always wins  

## Disadvantages

❌ **High message overhead** - Many messages sent  
❌ **Not fault-tolerant** - Assumes reliable message delivery  
❌ **Unfair** - Lower processes never get to be leader  

## Comparison with Ring Algorithm

| Feature | Bully | Ring |
|---------|-------|------|
| Message complexity | O(n²) | O(n) |
| Leader selection | Highest ID | Highest ID |
| Efficiency | Lower | Higher |
| Implementation | Simpler | More complex |

## Interactive Mode

The program will pause at each scenario and wait for you to press Enter. This lets you:
- See the current state
- Understand what's about to happen
- Follow the election process step-by-step

## Customization

You can modify the code to:
- Change number of processes
- Create custom scenarios
- Simulate different crash patterns
- Add network delays

Example:
```python
# Create 10 processes instead of 5
num_processes = 10
processes = [Process(i) for i in range(num_processes)]
```

## Real-World Applications

- **Database systems** - Selecting primary replica
- **Distributed file systems** - Choosing master node
- **Cluster management** - Electing cluster coordinator
- **Load balancing** - Selecting controller node

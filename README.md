# Distributed Computing Systems (DCS) - Assignment Guide

This repository contains assignments for the Distributed Computing Systems course.

---

## Assignment 1: RMI (Remote Method Invocation)

**Location:** `ass1_rmi/`

**Description:** Java RMI implementation of a simple calculator service with remote method calls.

**How to Run:**

1. **Compile all Java files:**
   ```bash
   cd ass1_rmi
   javac *.java
   ```

2. **Start the RMI Server:**
   ```bash
   java SearchServer
   ```

3. **Run the Client (in a new terminal):**
   ```bash
   java SearchClient
   ```

---

## Assignment 2: CORBA (Common Object Request Broker Architecture)

**Location:** `ass2_corba/`

**Description:** CORBA implementation demonstrating cross-language remote procedure calls.

**Files:**
- `Calculator.idl` - Interface Definition Language file
- `server.cpp` - C++ server implementation
- `client.py` - Python client implementation

**How to Run:**

1. **Generate stubs from IDL:**
   ```bash
   cd ass2_corba
   PYTHONPATH=/usr/lib/omniidl:$PYTHONPATH omniidl -bcxx Calculator.idl
   ```

2. **Compile and run server:**
   ```bash
   # Compilation steps will vary based on your setup
   # Refer to your CORBA installation documentation
   ```

**What it does:** Demonstrates language-independent remote procedure calls using CORBA.

---

## Assignment 3: MPI (Message Passing Interface)

**Location:** `ass3_mpi/`

**Description:** MPI implementation for parallel computing.

**How to Run:**

1. **Compile:**
   ```bash
   cd ass3_mpi
   mpic++ mp.cpp -o mpi
   ```

2. **Run with MPI:**
   ```bash
   mpirun -np 4 ./mpi
   ```
   *(Replace `4` with the number of processes you want)*

**What it does:** Demonstrates parallel processing using Message Passing Interface.

---

## Assignment 4: Clock Synchronization Algorithms

**Location:** `ass4/`

This assignment contains two sub-assignments:

### 4a. Berkeley Algorithm

**Location:** `ass4/berkeley/`

**Description:** Implementation of Berkeley Algorithm for clock synchronization using client-server sockets.

**Files:**
- `server.py` - Master/Coordinator node
- `client.py` - Slave nodes
- `berkeley.py` - Simulation (single program demonstration)

**How to Run:**

Open **4 separate terminals** and run these commands in order:

**Terminal 1 - Start Server:**
```bash
cd ass4/berkeley
python3 server.py
```

**Terminal 2 - Start Client 1:**
```bash
python3 client.py 1 105
```

**Terminal 3 - Start Client 2:**
```bash
python3 client.py 2 95
```

**Terminal 4 - Start Client 3:**
```bash
python3 client.py 3 110
```

**Arguments:**
- First argument: Client ID
- Second argument: Initial clock time

**What it does:**
- Server polls all clients for their time
- Calculates average time across all nodes
- Sends adjustment values to synchronize all clocks

**To run the simulation (no network):**
```bash
python3 berkeley.py
```

### 4b. Ring Algorithm

**Location:** `ass4/ring/`

**Description:** Implementation of Ring Algorithm for leader election.

**How to Run:**
```bash
cd ass4/ring
python3 ring.py
```

---

## Assignment 5: Web Services

**Location:** `ass5_webservice/`

**Description:** Django-based web service implementation.

**How to Run:**

1. **Activate virtual environment:**
   ```bash
   source env/bin/activate
   ```

2. **Navigate to project directory:**
   ```bash
   cd ass5_webservice
   ```

3. **Run Django development server:**
   ```bash
   python manage.py runserver
   ```

4. **Access the service:**
   - Open browser: `http://localhost:8000/greet/?name=YourName`

**What it does:** Provides a RESTful greeting service that returns JSON responses.

---

## General Prerequisites

- **Python 3.x** (for Python-based assignments)
- **Java JDK** (for RMI assignment)
- **MPI libraries** (for MPI assignment)
- **omniORB** (for CORBA assignment)
- **Django** (for web service assignment)

---

## Notes

- Make sure all required dependencies are installed before running assignments
- Some assignments may require additional configuration based on your system
- Port 5000 is used for Berkeley algorithm (change if needed)
- Port 1099 is used for RMI registry

---

## Troubleshooting

**Port already in use:**
```bash
# Find and kill process using the port
lsof -ti:5000 | xargs kill -9
```

**Permission denied:**
```bash
chmod +x script_name.sh
```

**Module not found (Python):**
```bash
pip install <module-name>
```

---

For detailed information about each assignment, refer to the README files in individual assignment directories (if available).

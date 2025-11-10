from datetime import datetime, timedelta

def format_time(dt):
    return dt.strftime("%H:%M:%S.%f")[:-3]

def berkeley_algorithm(master_time, slave_times):
    
    print(f"\n[Master] Starting synchronization...")
    print(f"[Master] My time is {format_time(master_time)}")

    all_times = [master_time] + slave_times
    time_diffs = []
    
    print("[Master] Calculating time differences from slaves:")
    for i, time in enumerate(all_times):
        diff = time - master_time
        time_diffs.append(diff)
        if i == 0:
            print(f"  - Master (self): {diff}")
        else:
            print(f"  - Slave {i}: {diff}")

    sum_of_diffs = sum(time_diffs, timedelta()) 
    
    average_diff = sum_of_diffs / len(all_times)
    print(f"[Master] Average difference: {average_diff}")
    
    adjustments = []
    for diff in time_diffs:
        adjustment = average_diff - diff
        adjustments.append(adjustment)

    print("[Master] Sending adjustments to all nodes:")
    print(f"  - Master adjustment: {adjustments[0]}")
    for i in range(len(slave_times)):
        print(f"  - Slave {i+1} adjustment: {adjustments[i+1]}")
    
    new_master_time = master_time + adjustments[0]
    
    new_slave_times = []
    for i in range(len(slave_times)):
        new_time = slave_times[i] + adjustments[i+1]
        new_slave_times.append(new_time)
        
    return new_master_time, new_slave_times

if __name__ == "__main__":
    base_time = datetime.now()
    master_time = base_time + timedelta(seconds=10)
    slave1_time = base_time - timedelta(seconds=20)
    slave2_time = base_time + timedelta(seconds=5)
    slave_times = [slave1_time, slave2_time]

    print("--- BEFORE SYNCHRONIZATION ---")
    print(f"  Master Clock: {format_time(master_time)}")
    print(f"  Slave 1 Clock: {format_time(slave1_time)}")
    print(f"  Slave 2 Clock: {format_time(slave2_time)}")
    
    synced_master, synced_slaves = berkeley_algorithm(master_time, slave_times)

    print("\n--- AFTER SYNCHRONIZATION ---")
    print(f"  Master Clock: {format_time(synced_master)}")
    print(f"  Slave 1 Clock: {format_time(synced_slaves[0])}")
    print(f"  Slave 2 Clock: {format_time(synced_slaves[1])}")

    print("\nAll clocks are now synchronized.")
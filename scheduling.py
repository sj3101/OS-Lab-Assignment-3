# -------------------------------------------
# OS Lab Assignment 3
# Task 1: CPU Scheduling (Priority & Round Robin)
# -------------------------------------------

def priority_scheduling():
    processes = []
    n = int(input("Enter number of processes: "))

    for i in range(n):
        bt = int(input(f"Enter Burst Time for P{i+1}: "))
        pr = int(input(f"Enter Priority (lower number = higher priority) for P{i+1}: "))
        processes.append([i+1, bt, pr])

    # Sort by priority
    processes.sort(key=lambda x: x[2])

    print("\n--- Priority Scheduling ---")
    print("PID\tBT\tPriority\tWT\tTAT")

    wt = 0
    total_wt = 0
    total_tat = 0

    for pid, bt, pr in processes:
        tat = wt + bt
        print(f"{pid}\t{bt}\t{pr}\t\t{wt}\t{tat}")

        total_wt += wt
        total_tat += tat
        wt += bt

    print("\nAverage Waiting Time:", total_wt / n)
    print("Average Turnaround Time:", total_tat / n)


def round_robin():
    print("\n--- Round Robin Scheduling ---")
    n = int(input("Enter number of processes: "))
    bt = []
    
    for i in range(n):
        bt.append(int(input(f"Enter Burst Time for P{i+1}: ")))

    tq = int(input("Enter Time Quantum: "))

    remaining_bt = bt.copy()
    t = 0

    print("\nGantt Chart:")
    while True:
        done = True

        for i in range(n):
            if remaining_bt[i] > 0:
                done = False
                
                if remaining_bt[i] > tq:
                    print(f"P{i+1}", end=" -> ")
                    t += tq
                    remaining_bt[i] -= tq
                else:
                    print(f"P{i+1}", end=" -> ")
                    t += remaining_bt[i]
                    remaining_bt[i] = 0

        if done:
            break

    print("End\n")


# -------------------------
# MAIN MENU
# -------------------------

print("CPU Scheduling Simulation")
print("1. Priority Scheduling")
print("2. Round Robin Scheduling")

choice = int(input("Enter choice: "))

if choice == 1:
    priority_scheduling()
elif choice == 2:
    round_robin()
else:
    print("Invalid Choice")

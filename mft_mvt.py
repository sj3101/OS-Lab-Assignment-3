class MFT:
    def __init__(self, total_memory, partition_size):
        self.total_memory = total_memory
        self.partition_size = partition_size
        self.num_partitions = total_memory // partition_size
        self.partitions = [-1] * self.num_partitions  # -1 = free

    def allocate(self, pid, process_size):
        print(f"\nAllocating Process {pid} (Size: {process_size}) in MFT...")

        if process_size > self.partition_size:
            print(f"❌ Process {pid} too large for fixed partition size {self.partition_size}.")
            return

        for i in range(self.num_partitions):
            if self.partitions[i] == -1:
                self.partitions[i] = pid
                print(f"✅ Process {pid} allocated in Partition {i}.")
                return

        print(f"❌ No free partitions available for Process {pid}.")

    def display(self):
        print("\n=== MFT Partition Table ===")
        for i, p in enumerate(self.partitions):
            if p == -1:
                print(f"Partition {i}: Free")
            else:
                print(f"Partition {i}: Occupied by Process {p}")


class MVT:
    def __init__(self, total_memory):
        self.total_memory = total_memory
        self.free_memory = total_memory
        self.partitions = []  # (pid, size)

    def allocate(self, pid, size):
        print(f"\nAllocating Process {pid} (Size: {size}) in MVT...")

        if size > self.free_memory:
            print(f"❌ Not enough space. Free memory = {self.free_memory}.")
            return

        self.partitions.append((pid, size))
        self.free_memory -= size
        print(f"✅ Process {pid} allocated. Remaining memory: {self.free_memory}")

    def deallocate(self, pid):
        print(f"\nDeallocating Process {pid} in MVT...")

        for p in self.partitions:
            if p[0] == pid:
                self.partitions.remove(p)
                self.free_memory += p[1]
                print(f"♻ Process {pid} removed. Free memory = {self.free_memory}")
                return

        print("❌ PID not found.")

    def display(self):
        print("\n=== MVT Memory Table ===")
        for pid, size in self.partitions:
            print(f"Process {pid} | Size: {size}")

        print(f"\nFree Memory Remaining: {self.free_memory}")


if __name__ == "__main__":
    print("=== MFT & MVT MEMORY MANAGEMENT ===")

    print("\n1. MFT (Fixed Partitioning)")
    print("2. MVT (Variable Partitioning)")

    ch = int(input("Choose memory management technique: "))

    if ch == 1:
        total = int(input("Enter total memory size: "))
        part = int(input("Enter partition size: "))
        m = MFT(total, part)

        while True:
            print("\n1. Allocate Process\n2. Display Table\n3. Exit")
            c = int(input("Enter choice: "))

            if c == 1:
                pid = input("Enter PID: ")
                size = int(input("Enter process size: "))
                m.allocate(pid, size)

            elif c == 2:
                m.display()

            elif c == 3:
                break

    elif ch == 2:
        total = int(input("Enter total memory size: "))
        m = MVT(total)

        while True:
            print("\n1. Allocate Process\n2. Deallocate Process\n3. Display Table\n4. Exit")
            c = int(input("Enter choice: "))

            if c == 1:
                pid = input("Enter PID: ")
                size = int(input("Enter process size: "))
                m.allocate(pid, size)

            elif c == 2:
                pid = input("Enter PID to deallocate: ")
                m.deallocate(pid)

            elif c == 3:
                m.display()

            elif c == 4:
                break

    else:
        print("Invalid choice!")

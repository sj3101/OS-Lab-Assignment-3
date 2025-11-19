class MemoryAllocation:
    def __init__(self, blocks):
        self.blocks = blocks  # List of block sizes
        self.allocated = [-1] * len(blocks)  # -1 means free

    def first_fit(self, process_sizes):
        print("\n=== FIRST FIT ALLOCATION ===")
        allocation = [-1] * len(process_sizes)

        for p in range(len(process_sizes)):
            for b in range(len(self.blocks)):
                if self.allocated[b] == -1 and self.blocks[b] >= process_sizes[p]:
                    allocation[p] = b
                    self.allocated[b] = p
                    break

        self.display(process_sizes, allocation)

    def best_fit(self, process_sizes):
        print("\n=== BEST FIT ALLOCATION ===")
        allocation = [-1] * len(process_sizes)
        temp_blocks = self.blocks[:]
        temp_alloc = self.allocated[:]

        for p in range(len(process_sizes)):
            best_index = -1
            for b in range(len(temp_blocks)):
                if temp_alloc[b] == -1 and temp_blocks[b] >= process_sizes[p]:
                    if best_index == -1 or temp_blocks[b] < temp_blocks[best_index]:
                        best_index = b

            if best_index != -1:
                allocation[p] = best_index
                temp_alloc[best_index] = p

        self.display(process_sizes, allocation)

    def worst_fit(self, process_sizes):
        print("\n=== WORST FIT ALLOCATION ===")
        allocation = [-1] * len(process_sizes)
        temp_blocks = self.blocks[:]
        temp_alloc = self.allocated[:]

        for p in range(len(process_sizes)):
            worst_index = -1
            for b in range(len(temp_blocks)):
                if temp_alloc[b] == -1 and temp_blocks[b] >= process_sizes[p]:
                    if worst_index == -1 or temp_blocks[b] > temp_blocks[worst_index]:
                        worst_index = b

            if worst_index != -1:
                allocation[p] = worst_index
                temp_alloc[worst_index] = p

        self.display(process_sizes, allocation)

    def display(self, processes, allocation):
        print("\nProcess\tSize\tBlock Allocated")
        for i in range(len(processes)):
            if allocation[i] != -1:
                print(f"P{i}\t{processes[i]}\tBlock {allocation[i]}")
            else:
                print(f"P{i}\t{processes[i]}\tNot Allocated")

        print("\nMemory Blocks:", self.blocks)
        print("Allocation Map:", allocation)


if __name__ == "__main__":
    print("=== MEMORY ALLOCATION SIMULATION ===")

    n_blocks = int(input("Enter number of memory blocks: "))
    blocks = []

    for i in range(n_blocks):
        blocks.append(int(input(f"Enter size of block {i}: ")))

    memory = MemoryAllocation(blocks)

    n_process = int(input("\nEnter number of processes: "))
    processes = []
    for i in range(n_process):
        processes.append(int(input(f"Enter size of process {i}: ")))

    print("\n1. First Fit\n2. Best Fit\n3. Worst Fit")
    ch = int(input("Choose allocation method: "))

    if ch == 1:
        memory.first_fit(processes)
    elif ch == 2:
        memory.best_fit(processes)
    elif ch == 3:
        memory.worst_fit(processes)
    else:
        print("Invalid choice!")

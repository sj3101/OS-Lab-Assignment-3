class SequentialAllocation:
    def __init__(self, total_blocks):
        self.total_blocks = total_blocks
        self.memory = [0] * total_blocks  # 0 = free, 1 = allocated

    def allocate(self, file_name, start, length):
        # Check boundary
        if start + length > self.total_blocks:
            print(f"❌ Allocation failed for {file_name}: Out of memory range.")
            return

        # Check if all blocks are free
        for i in range(start, start + length):
            if self.memory[i] == 1:
                print(f"❌ Allocation failed for {file_name}: Block {i} already allocated.")
                return

        # Allocate
        for i in range(start, start + length):
            self.memory[i] = 1

        print(f"✅ File '{file_name}' allocated from block {start} to {start + length - 1}.")

    def display(self):
        print("\n📌 Memory Status (0 = Free, 1 = Allocated):")
        print(self.memory)


if __name__ == "__main__":
    print("=== Sequential File Allocation Simulation ===")
    total = int(input("Enter total number of memory blocks: "))
    sa = SequentialAllocation(total)

    while True:
        print("\n1. Allocate File")
        print("2. Display Memory")
        print("3. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            fname = input("File name: ")
            start = int(input("Enter start block: "))
            length = int(input("Enter file size (in blocks): "))
            sa.allocate(fname, start, length)

        elif choice == 2:
            sa.display()

        elif choice == 3:
            print("Exiting...")
            break

        else:
            print("❌ Invalid choice. Try again.")

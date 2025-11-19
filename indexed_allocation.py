class IndexedAllocation:
    def __init__(self, total_blocks):
        self.total_blocks = total_blocks
        self.memory = [0] * total_blocks  # 0 = free, 1 = allocated
        self.index_table = {}  # file_name -> (index_block, data_blocks list)

    def find_free_blocks(self, count):
        free = []
        for i in range(self.total_blocks):
            if self.memory[i] == 0:
                free.append(i)
                if len(free) == count:
                    return free
        return None  # Not enough space

    def allocate(self, file_name, file_size):
        needed_blocks = file_size + 1  # 1 index block + size data blocks

        free_blocks = self.find_free_blocks(needed_blocks)
        if free_blocks is None:
            print(f"❌ Allocation failed for {file_name}: Not enough free blocks.")
            return

        index_block = free_blocks[0]
        data_blocks = free_blocks[1:]

        # Allocate in memory
        for b in free_blocks:
            self.memory[b] = 1

        # Store in index table
        self.index_table[file_name] = (index_block, data_blocks)

        print(f"✅ File '{file_name}' allocated.")
        print(f"📌 Index Block: {index_block}")
        print(f"📦 Data Blocks: {data_blocks}")

    def display(self):
        print("\n📌 Memory Status (0 = Free, 1 = Allocated):")
        print(self.memory)

        print("\n📂 Indexed Allocation Table:")
        for file, (index_block, data_blocks) in self.index_table.items():
            print(f"File: {file} | Index Block: {index_block} | Data Blocks: {data_blocks}")


if __name__ == "__main__":
    print("=== Indexed File Allocation Simulation ===")
    total = int(input("Enter total number of memory blocks: "))
    ia = IndexedAllocation(total)

    while True:
        print("\n1. Allocate File")
        print("2. Display Memory State")
        print("3. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            fname = input("Enter file name: ")
            size = int(input("Enter file size (data blocks): "))
            ia.allocate(fname, size)

        elif choice == 2:
            ia.display()

        elif choice == 3:
            print("Exiting...")
            break

        else:
            print("❌ Invalid choice. Try again.")

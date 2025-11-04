class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)] 
    def hash_function(self, key):
        """Division method hash function"""
        return key % self.size

    def insert(self, key, value):
        """Insert a key-value pair"""
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                print(f"Updated key {key} with value {value}.")
                return
       
        self.table[index].append([key, value])
        print(f"Inserted ({key}, {value}) at index {index}.")

    def search(self, key):
        """Search for a value by key"""
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                print(f"Found key {key} with value {pair[1]} at index {index}.")
                return pair[1]
        print(f"Key {key} not found.")
        return None

    def delete(self, key):
        """Delete a key-value pair"""
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                self.table[index].remove(pair)
                print(f"Deleted key {key} from index {index}.")
                return
        print(f"Key {key} not found. Cannot delete.")

    def display(self):
        """Display the hash table"""
        print("\nHash Table:")
        for i, chain in enumerate(self.table):
            print(f"Index {i}: {chain}")
        print()

if __name__ == "__main__":
    ht = HashTable()

    ht.insert(10, "Apple")
    ht.insert( 5, "Cherry")
    ht.insert(20, "Avocado")
    ht.insert(25, "Mango")  
    ht.display()

    ht.search(15)
    ht.search(99)

    ht.delete(20)
    ht.delete(99)
    ht.display()

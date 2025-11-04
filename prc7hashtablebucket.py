class Bucket:
    def __init__(self, local_depth):
        self.local_depth = local_depth
        self.items = {}  # key-value pairs

    def is_full(self, threshold):
        return len(self.items) >= threshold

class ExtendibleHashTable:
    def __init__(self, bucket_size=2):
        self.global_depth = 1
        self.bucket_size = bucket_size
        self.directory = [Bucket(local_depth=1) for _ in range(2)]  # 2^1 entries

    def _hash(self, key):
        """Hash function returning integer."""
        return hash(key) & 0xFFFFFFFF  # keep positive

    def _get_bucket_index(self, key):
        """Return directory index using lower bits of hash."""
        hash_value = self._hash(key)
        return hash_value & ((1 << self.global_depth) - 1)

    def insert(self, key, value):
        index = self._get_bucket_index(key)
        bucket = self.directory[index]

        # If key already exists, update value
        if key in bucket.items:
            bucket.items[key] = value
            return

        # If bucket not full, insert
        if not bucket.is_full(self.bucket_size):
            bucket.items[key] = value
        else:
            # Bucket full → split
            self._split_bucket(index)
            # Reinsert the key after split
            self.insert(key, value)

    def _split_bucket(self, index):
        bucket = self.directory[index]
        print(f"Splitting bucket with local depth {bucket.local_depth}...")

        if bucket.local_depth == self.global_depth:
            # Double the directory
            print("Doubling directory...")
            self.directory += self.directory
            self.global_depth += 1

        # Create new bucket
        new_bucket = Bucket(local_depth=bucket.local_depth + 1)
        old_items = list(bucket.items.items())
        bucket.items.clear()
        bucket.local_depth += 1

        # Update directory pointers
        pattern_bit = 1 << (bucket.local_depth - 1)
        for i in range(len(self.directory)):
            if self.directory[i] is bucket and (i & pattern_bit):
                self.directory[i] = new_bucket

        # Redistribute items
        for k, v in old_items:
            self.insert(k, v)

    def search(self, key):
        index = self._get_bucket_index(key)
        bucket = self.directory[index]
        return bucket.items.get(key, None)

    def delete(self, key):
        index = self._get_bucket_index(key)
        bucket = self.directory[index]
        if key in bucket.items:
            del bucket.items[key]
            print(f"Deleted key {key}")
        else:
            print("Key not found!")

    def display(self):
        print("\n--- Hash Table ---")
        print(f"Global Depth: {self.global_depth}")
        seen = set()
        for i, bucket in enumerate(self.directory):
            if id(bucket) not in seen:
                seen.add(id(bucket))
                print(f"Index {i:0{self.global_depth}b}: {bucket.items}, LD={bucket.local_depth}")
        print("------------------\n")

# Example Usage
if __name__ == "__main__":
    ht = ExtendibleHashTable(bucket_size=2)
    ht.insert(5, "A")
    ht.insert(7, "B")
    ht.insert(13, "C")
    ht.insert(9, "D")
    ht.display()

    print("Search(7):", ht.search(7))
    ht.delete(13)
    ht.display()


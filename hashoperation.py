class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]  # list of lists for chaining

    def _hash(self, key):
        # Simple hash function (modulus of key's hash)
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        # Check if key already exists, update value if found
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                print(f"Updated key '{key}' with value '{value}'.")
                return
        # Otherwise, insert new key-value pair
        self.table[index].append((key, value))
        print(f"Inserted key '{key}' with value '{value}'.")

    def delete(self, key):
        index = self._hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                print(f"Deleted key '{key}'.")
                return
        print(f"Key '{key}' not found.")

    def search(self, key):
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                print(f"Found key '{key}' with value '{v}'.")
                return v
        print(f"Key '{key}' not found.")
        return None

    def display(self):
        print("Hash Table Contents:")
        for i, bucket in enumerate(self.table):
            print(f"Bucket {i}: {bucket}")

# Example usage
ht = HashTable()

ht.insert("apple", 10)
ht.insert("banana", 20)
ht.insert("orange", 30)

ht.display()

ht.search("banana")
ht.delete("banana")
ht.search("banana")

ht.display()

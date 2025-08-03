#!/usr/bin/python3
class HashMap:
    def __init__(self, size):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def _hash(self, value):
        return hash(value) % self.size

    def set(self, key, value):
        index = self._hash(key)
        bucket = self.buckets[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        
        bucket.append((key, value))

    def get(self, key):
        index = self._hash(key)
        bucket = self.buckets[index]

        for k, v in bucket:
            if k == key:
                return v
            
        raise KeyError(f"Key {key} not found!")
    
    def delete(self, key):
        index = self._hash(key)
        bucket = self.buckets[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return
            
        raise KeyError(f"Key {key} not found!")

    def __str__(self):
        return str(self.buckets)

if __name__ == "__main__":
    h = HashMap(10)
    h.set("apple", 2)
    h.set("mango", 5)
    h.set("melon", 10)
    h.set("kiwi", 3)
    print(h.get("apple"))
    h.delete("apple")
    #print(h.get("apple"))
    print(h.__str__())
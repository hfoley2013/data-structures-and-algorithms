class Hashtable:
    def __init__(self, size=1024):
        self.size = size
        self._buckets = [[] for _ in range(self.size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def set(self, key, value):
        index = self.hash_function(key)
        for i, kv in enumerate(self._buckets[index]):
            if kv[0] == key:
                self._buckets[index][i] = (key, value)
                return
        self._buckets[index].append((key, value))

    def get(self, key):
        index = self.hash_function(key)
        for k, v in self._buckets[index]:
            if k == key:
                return v
        return None

    def has(self, key):
        index = self.hash_function(key)
        for k, _ in self._buckets[index]:
            if k == key:
                return True
        return False

    def keys(self):
        keys = []
        for bucket in self._buckets:
            for k, _ in bucket:
                keys.append(k)
        return keys

    def hash(self, key):
        return self.hash_function(key)


if __name__ == '__main__':
    pass

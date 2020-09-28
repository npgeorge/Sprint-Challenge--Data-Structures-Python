class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.ring = []
        self.cur = 0


    def append(self, item):
        if len(self.ring) < self.capacity:
            self.ring.append(item)

        else:
            self.ring[self.cur] = item

        self.cur += 1
        self.cur = self.cur % (self.capacity)

    def get(self):
        return self.ring
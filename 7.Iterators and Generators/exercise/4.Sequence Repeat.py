class sequence_repeat:
    def __init__(self, seq, count):
        self.seq = seq
        self.count = count
        self.current_idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_idx < self.count:
            idx = self.current_idx
            self.current_idx += 1
            return self.seq[idx % len(self.seq)]
        else:
            raise StopIteration
# EASY

# first submission
# runtime: 65 ms O(n log n)
# memory: 23.31 MB
class Solution:
    def countBits(self, n: int) -> List[int]:
        counts = []
        for num in range(0, n + 1):
            counts.append(str(bin(num)).count('1'))

        return counts
    

# second submission
# runtime: 228 ms O(n log n)
# memory: 23.17 MB
class Solution:
    BITS = "01"
    def countBits(self, n: int) -> List[int]:
        counts = []
        for num in range(0, n + 1):
            counts.append(self.convert(num).count('1'))

        return counts

    def encode(self, n: int) -> str:
        try:
            return self.BITS[n]
        except IndexError:
            raise Exception("\ncannot encode: %s" % n)

    def convert(self, decimal: int) -> str:
        if decimal < 2:
            return self.encode(decimal)
        else:
            return self.convert(decimal // 2) + self.encode(decimal % 2)
            
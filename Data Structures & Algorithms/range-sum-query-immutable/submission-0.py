class NumArray:

    def __init__(self, nums: List[int]):

        self.nums = nums
        self.prefix= []

        tot = 0

        for n in self.nums:
            tot+=n
            self.prefix.append(tot)
        

    def sumRange(self, left: int, right: int) -> int:
        

        left -=1

        if left == -1:
            return self.prefix[right]
        
        return self.prefix[right] -self.prefix[left]


        # [-2, 0, 3, -5, 2, -1]
        # [-2,-2, 1, -4,-2, -3]


        
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
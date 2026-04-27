class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        d = Counter(nums)
        ans = []

        arr = [[] for _ in range(len(nums)+1)]

        for num,freq in d.items():

            arr[freq].append(num)


        for array in arr[-1::-1]:
            print(array)
            for num in array:
                ans.append(num)
                k-=1
                if k == 0: return ans



        return ans
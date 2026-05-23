class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        if len(nums1) > len(nums2):
            A = nums2
            B = nums1

        else:
            A = nums1
            B = nums2


        l,r = 0, len(A)-1
        half = (len(A)+len(B))//2

        while True:

            midA = l + (r-l)//2
            midB = half - (midA+1) -1

            leftA = A[midA] if midA >= 0 else -float('inf')
            rightA = A[midA +1] if midA +1 < len(A) else float('inf')
            leftB = B[midB] if midB >= 0 else -float('inf')
            rightB = B[midB +1] if midB +1 < len(B) else float('inf')

            if leftA <= rightB and leftB <= rightA:

                if (len(A) + len(B))%2 == 1:
                    return min(rightA,rightB)

                return (max(leftA,leftB) + min(rightA, rightB))/2


            if leftA > rightB:
                r = midA-1
            
            else:
                l =midA+1




            
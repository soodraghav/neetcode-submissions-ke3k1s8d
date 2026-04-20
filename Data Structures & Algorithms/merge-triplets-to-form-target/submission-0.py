class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        a,b,c =0,0,0


        for row in triplets:

                x,y,z = row[0], row[1], row[2]

                if x > target[0] or y > target[1] or z > target[2]:
                    continue
                
                a = max(a,x)
                b = max(b,y)
                c = max(c,z)

        
        return target == [a,b,c]
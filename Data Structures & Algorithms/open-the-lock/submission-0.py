class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        
        
        visited = set()
        steps = 0

        d = {"0": ("9","1"),"1": ("0","2"), "2": ("1","3"), "3": ("2","4"),
            "4": ("3","5"), "5": ("4","6"), "6": ("5","7"), "7": ("6","8"),
            "8": ("7","9"), "9": ("8","0")}

        q = ["0000"]
        deadends = set(deadends)

        if "0000" in deadends: return -1

        visited.add("0000")
        while q:

            tq = []

            for combination in q:

                if combination == target: return steps
                

                for i in range(4):

                    for digit in d[combination[i]]:

                        new_comb = combination[:i] + digit + combination[i+1:]
                        # print(new_comb)

                        if  new_comb not in visited and new_comb not in deadends:

                            tq.append(new_comb)
                            visited.add(new_comb)
            q = tq
            steps+=1

        return -1
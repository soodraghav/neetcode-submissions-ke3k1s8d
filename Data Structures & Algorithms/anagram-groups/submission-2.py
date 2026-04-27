from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        d = defaultdict(list)

        for word in strs:

            val = [0] * 26

            for letter in word:
                val[ord(letter) - ord('a')]+=1

            join_key = '#'.join(str(val))

            d[join_key].append(word)

        return list(d.values())




            


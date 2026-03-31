class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        d = {}

        for word in strs:
            wordlist = [0] * 26

            for letter in word:
                wordlist[ord(letter) - ord('a')]+=1
            
            wordtuple = tuple(wordlist)

            if wordtuple not in d:
                d[wordtuple] = []
            d[wordtuple].append(word)


        return list(d.values())
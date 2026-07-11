class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        pos = 0
        d = {}
        length = 0

        for letter in order:
            d[letter] = pos
            pos+=1

        
        for i in range(1,len(words)):

            word1 = words[i-1]
            word2 =  words[i]
            

            for j in range(len(word1)):
                # same prefix words also need to be taken care of 
                if j >= len(word2) or d[word1[j]] > d[word2[j]]: return False

                elif d[word1[j]] < d[word2[j]]: break

        return True



        

        
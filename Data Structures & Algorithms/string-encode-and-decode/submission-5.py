class Solution:

    def encode(self, strs: List[str]) -> str:

        new = []

        for word in strs:

            new_word = str(len(word)) + "#" + word
            new.append(new_word)

        
        return "".join(new)

    def decode(self, s: str) -> List[str]:

        l = r = 0
        ans = []

        while r < len(s):

            while s[r]!="#":
                r+=1

            # #r #

            # 2#is4#
            #   l
            #     r

            length = int(s[l:r])
            r+=1
            l =r
            r+=length
            ans.append(s[l:r])

            l = r

        
        return ans




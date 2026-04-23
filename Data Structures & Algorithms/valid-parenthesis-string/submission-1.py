class Solution:
    def checkValidString(self, s: str) -> bool:

        open = []
        star = []

        for i,n in enumerate(s):

            if n == "(":
                open.append(i)

            elif n == ")":

                if open: open.pop()

                elif star: star.pop()

                else: return False

            else:
                star.append(i)

    

        while open and star:
                if open.pop() > star.pop(): return False

        if open: return False
        return True




        
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

    

        while open and len(open) <= len(star):

            if open[-1] > star[-1]: star.pop()
            else:
                open.pop()
                star.pop()

        if open: return False
        return True




        
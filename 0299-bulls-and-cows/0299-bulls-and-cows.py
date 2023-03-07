class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0

        counted = ""

        for i in range(len(secret)):
            if guess[i] in secret:
                if guess[i] == secret[i]:
                    bulls += 1
                    counted += guess[i]
                    if counted.count(guess[i]) > secret.count(guess[i]):
                        cows -= 1
                elif counted.count(guess[i]) < secret.count(guess[i]):
                    cows += 1
                    counted += guess[i]

        return "%iA%iB" % (bulls, cows)
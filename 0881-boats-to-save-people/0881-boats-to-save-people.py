class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)[::-1]

        p1 = 0
        p2 = len(people) - 1
        count = 0
        while p1 < p2:
            if people[p1] == limit:
                count += 1
                p1 += 1
            elif people[p1] + people[p2] <= limit:
                count += 1
                p1 += 1
                p2 -= 1
            else:
                p1+=1
                count += 1
        if p1==p2:
            count += 1

        return count
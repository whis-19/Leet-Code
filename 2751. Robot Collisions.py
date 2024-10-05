class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        indices = list(range(len(positions)))
        indices.sort(key=lambda i: positions[i])
        robots = []
        for i in indices:
            if directions[i] == 'R':
                robots.append(i)
            else:
                while robots and healths[i] > 0:
                    n = robots[-1]
                    if healths[n] > healths[i]:
                        healths[n] -= 1
                        healths[i] = 0
                    else:
                        robots.pop()
                        healths[i] -= (1 if healths[n] < healths[i] else healths[i])
                        healths[n] = 0
        return [health for health in healths if health > 0]
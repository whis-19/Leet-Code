class Solution:
    def maximumPoints(self, enemyEnergies: List[int], currentEnergy: int) -> int:
        # take the minimum possible value from the enemy energy array
        minEnergy = min(enemyEnergies)
        minEnergyIdx = enemyEnergies.index(minEnergy)
        # calculate the most points we can earn of it
        points = currentEnergy // minEnergy
        currentEnergy = currentEnergy % minEnergy # remaining HP (remainder) after the above division
        if points > 0:
            # at least one point, so we can take all the other energies now
            # (Except the min energy)
            for x in range(len(enemyEnergies)):
                if x != minEnergyIdx:
                    currentEnergy += enemyEnergies[x]
        # now we have our "team" built up, with as much HP as we can, we can grind
        # the weakest enemy for a point every time we defeat it
        points += currentEnergy // minEnergy # same as at the start
        return points

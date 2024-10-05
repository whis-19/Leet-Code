class Solution(object):
    def findTheWinner(self, n, k):
        friends = list(range(1, n + 1))  # List of friends numbered from 1 to n
        start = 0  # Starting index
        
        while len(friends) > 1:
            start = (start + k - 1) % len(friends)  # Find the friend who loses
            friends.pop(start)  # Remove the friend who loses
        
        return friends[0]
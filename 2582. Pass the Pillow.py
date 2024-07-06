class Solution(object):
    def passThePillow(self, n, time):
        # Calculate the period of one full round trip
        period = 2 * (n - 1)
        
        # Reduce the time to a single cycle
        effective_time = time % period
        
        # Determine the position within the period
        if effective_time <= n - 1:
            # Pillow is moving forward
            return effective_time + 1
        else:
            # Pillow is moving backward
            return n - (effective_time - (n - 1))
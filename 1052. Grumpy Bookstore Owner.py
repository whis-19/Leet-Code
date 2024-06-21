class Solution(object):
    def maxSatisfied(self, customers, grumpy, minutes):
        
        # Calculate the baseline satisfaction
        total_satisfied = sum(customers[i] for i in range(len(customers)) if grumpy[i] == 0)
        
        # Calculate the initial window sum for the first 'minutes' window
        extra_satisfied = 0
        for i in range(minutes):
            if grumpy[i] == 1:
                extra_satisfied += customers[i]
        
        max_extra_satisfied = extra_satisfied
        
        # Slide the window across the rest of the array
        for i in range(minutes, len(customers)):
            if grumpy[i] == 1:
                extra_satisfied += customers[i]
            if grumpy[i - minutes] == 1:
                extra_satisfied -= customers[i - minutes]
            
            max_extra_satisfied = max(max_extra_satisfied, extra_satisfied)
        
        return total_satisfied + max_extra_satisfied
            
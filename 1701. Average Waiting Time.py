class Solution:
    def averageWaitingTime(self, customers):
        n = len(customers)
        # Initialize total waiting time with the first customer's time
        time_waiting = customers[0][1]
        # Initialize the finish time of the first customer
        finished_prev = customers[0][0] + customers[0][1]

        for customer_ind in range(1, n):
            times = customers[customer_ind]
            arrive = times[0]

            # Chef starts cooking this as soon as he finished the last dish or customer arrived
            start_cook = max(arrive, finished_prev)
            end_time = start_cook + times[1]
            finished_prev = end_time
            time_waiting += end_time - arrive

        return float(time_waiting) / n


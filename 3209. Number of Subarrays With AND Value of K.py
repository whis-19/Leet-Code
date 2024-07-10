class Solution:
    def countSubarrays(self, nums, k):
        cnt, res = Counter(), 0
        for n in nums:
            cnt1 = Counter()
            if k & n == k:
                cnt[n] += 1
                for v, count in cnt.items():
                    cnt1[v & n] += count
                res += cnt1[k]
            cnt = cnt1
        return res    
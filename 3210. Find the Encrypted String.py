class Solution(object):
    def getEncryptedString(self, s, k):
        n = len(s)
        encrypted = []

        for i in range(n):
            new_index = (i + k) % n
            encrypted.append(s[new_index])

        return ''.join(encrypted)

    
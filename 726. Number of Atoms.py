import collections

class Solution(object):
    def countOfAtoms(self, formula):
        stack = [collections.defaultdict(int)]
        i = 0
        n = len(formula)
        
        while i < n:
            if formula[i] == '(':
                stack.append(collections.defaultdict(int))
                i += 1
            elif formula[i] == ')':
                i += 1
                start = i
                while i < n and formula[i].isdigit():
                    i += 1
                multiplicity = int(formula[start:i] or 1)
                top = stack.pop()
                for element in top:
                    stack[-1][element] += top[element] * multiplicity
            else:
                start = i
                i += 1
                while i < n and formula[i].islower():
                    i += 1
                name = formula[start:i]
                start = i
                while i < n and formula[i].isdigit():
                    i += 1
                multiplicity = int(formula[start:i] or 1)
                stack[-1][name] += multiplicity
        
        result = []
        for name in sorted(stack[-1]):
            result.append(name)
            count = stack[-1][name]
            if count > 1:
                result.append(str(count))
        
        return ''.join(result)


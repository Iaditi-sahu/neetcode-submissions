class Solution:
    def countOfAtoms(self, formula: str) -> str:
        counts = defaultdict(int)
        stack = []
        multi = 1
        freq = 0

        i = len(formula) - 1
        while i>= 0: 
            char = formula[i]

            if char.isdigit():
                freq = 0
                place_val = 1
                while i>= 0 and formula[i].isdigit():
                    freq += int(formula[i]) * place_val
                    place_val *= 10
                    i-=1
                continue
            if char.isalpha():
                end = i
                while formula[i].islower():
                    i-=1
                element = formula[i:end + 1]
                counts[element] += max(freq, 1) * multi
                freq = 0 
            elif char == ')':
                stack.append(multi)
                multi *= max(freq, 1)
                freq = 0
            else:
                multi = stack.pop()
            i-=1

        result = []
        for element in sorted(counts):
            result.append(element)
            if counts[element] > 1:
                result.append(str(counts[element]))
        return ''.join(result)


#given int n, generate all the valid combinations of n pairs of parentheses
# use backtracking!

# n = 0
# n = 1 ()
# n = 2 ()(), (())
# n = 3 ()()(),(())(),((()))
# n = 9

# def is_valid(combination):
#     stack = []
#     for par in combination:
#         if par == '(':
#             stack.append(par)
#         else:
#             if len(stack) == 0:
#                 return False
#             else:
#                 stack.pop()
#     return len(stack) == 0


def generate(n):
    def rec(n, diff, comb, combs):
        if diff < 0 or diff > n:
            return
        elif n == 0:
            if diff == 0:
                combs.append(''.join(comb))
        else:
            comb.append('(')
            rec(n-1, diff+1, comb, combs)
            comb.pop()
            comb.append(')')
            rec(n-1, diff-1, comb, combs)
    combs =[]
    rec(2*n, 0, [], combs)
    return combs

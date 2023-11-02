from math import log
def triangle(row):
    rules = {'RR': 'R', 'GG': 'G', 'BB': 'B',
         'BG': 'R', 'RB': 'G', 'RG': 'B',
         'GB': 'R', 'BR': 'G', 'GR': 'B'}
    n = len(row)
    if n == 1:
        return row
    d = n - 3**int(log(n-1, 3))
    return rules[triangle(row[:d]) + triangle(row[-d:])]
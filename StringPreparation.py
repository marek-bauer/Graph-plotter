# Replaces |exp| to abs(exp)
def abs_replace(s):
    res = s
    i = 1
    if s[0] == "|":
        res = res.replace("|", "abs(", 1)
        i = 4
    while i < len(res):
        if res[i] == "|":
            if '0' <= res[i-1] <= '9' or res[i-1] == 'x' or res[i-1] == ')':
                res = res.replace("|", ")", 1)
            else:
                res = res.replace("|", "abs(", 1)
                i += 3
        i += 1
    return res


def assumed_multiply(s):
    res = s
    i = 1
    while i < len(res):
        if ((res[i-1] == ")" or res[i-1] == "x") and (res[i] == "(" or res[i] == "x")) or ((res[i-1] == ")" or res[i-1] == "x") and '0' <= res[i] <= '9') or ('0' <= res[i-1] <= '9' and (res[i] == "(" or res[i] == "x")):
            res = res[:i] + '*' + res[i:]
            i += 2
        else:
            i += 1
    return res


def prepare(s):
    prev = s
    curr = prev.replace("  ", " ")
    while prev != curr:
        curr, prev = curr.replace("  ", " "), curr
    curr = abs_replace(curr)
    curr = assumed_multiply(curr)
    return curr
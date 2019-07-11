# Replaces |exp| to abs(exp)
def abs_replace(s):
    res = s
    i = 1
    if s[0] == "|":
        res = res.replace("|", "abs(", 1)
        i = 4
    while i < len(res):
        if res[i] == "|":
            if res[i-1] in ")0123456789xei":
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
        if (res[i-1] in ")xei" and res[i] in "(xep") or (res[i-1] in ")xei" and '0' <= res[i] <= '9') or ('0' <= res[i-1] <= '9' and res[i] in "(xep"):
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
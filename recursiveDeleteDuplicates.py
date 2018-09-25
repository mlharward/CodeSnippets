

def superReducedString(s):
    """This function takes in any string and removes successive letters such
    as "aa" "bb". What makes this code interesting is the recursive nature.
    """
    if len(s) == 0:
        return "Empty String"
    elif len(s) == 1:
        return s
    for n in range(len(s)-1):
        if s[n] == s[n+1]:
            s = s[:n] + s[n+2:]
            return superReducedString(s)
    return s

def ispalindrome(valstring):
    import re
    forwards = ''.join(re.findall(r'[a-z]',valstring.lower()))
    backwards = forwards[::-1]
    return forwards ==  backwards

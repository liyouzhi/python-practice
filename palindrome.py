#构造回数数列

def is_palindrome(n):
    s = str(n)
    l = len(s)
    for i in range(l//2):
        if s[i] != s[-i-1]:
            return False
    return True

output = filter(is_palindrome,range(1,1000))

print(list(output))

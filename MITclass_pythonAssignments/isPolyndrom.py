def ispolindrome(s):
    
    def toChars(s):
        s=s.lower()
        ans=''
        for c in s:
            if c in 'abcdefghi':
                ans=ans+c
        return ans
    
    def isPal(s):
        if len(s)==1:
            return True
        else:
            return s[0]==s[-1] and isPal[1:-1]
    return isPal(toChar(s))
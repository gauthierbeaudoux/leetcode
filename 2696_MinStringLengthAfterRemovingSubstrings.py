s = "CCCCDDDD"

def minLength(s: str) -> int:
    while "AB" in s or "CD" in s:
        # print(s)
        if "AB" in s:
            s = s.replace("AB","")
        if "CD" in s:
            s = s.replace("CD","")
    
    return len(s)


print(minLength(s))
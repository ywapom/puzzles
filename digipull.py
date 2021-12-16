# extract digits from a string

s = "sd23lks9"

def extract(s):
    nums = ""
    for c in s:
        if(c.isdigit()):
            nums += c
    return nums

print(extract(s))

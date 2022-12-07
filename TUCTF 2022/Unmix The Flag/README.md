# Hyper Maze

## Challenge description:


## Solution description:
My script:

```python
import string

upperFlag = string.ascii_uppercase[:26]
lowerFlag = string.ascii_lowercase[:26]
MIN_LETTER = 97
MIN_CAPLETTER = 65

def re_mix(oneLetter,num):
    if(oneLetter.isupper()):
        w_s26 = upperFlag.index(oneLetter)
        for i in range(65, 90):
            if (i-65+ord(num)-65)%26 == w_s26:
                return chr(i)

    if oneLetter.islower():
        w_s26 = lowerFlag.index(oneLetter)
        for i in range(97, 122):
            if (i-97+ord(num)-97)%26 == w_s26:
                return chr(i)

def puzzled(puzzle):
    toSolveOne = ""
    for letter in puzzle:
    
        if (letter.isupper()):
            binary ="{0:015b}".format(ord(letter))

            toSolveOne += upperFlag[int(binary[:5],2)]
            toSolveOne += upperFlag[int(binary[5:10],2)]
            toSolveOne += upperFlag[int(binary[10:],2)]

        elif(letter.islower()):
            six = "{0:02x}".format(ord(letter))
            toSolveOne += lowerFlag[int(six[:1],16)]
            toSolveOne += lowerFlag[int(six[1:],16)]
        elif(letter == "_"):
            toSolveOne += "CTF"  
    return toSolveOne   

dct = {"CTF": '_'}

for i in lowerFlag:
    dct[puzzled(i)] = i
for j in 'ABCDEFGHIJKLMNOPQRSTUVWXY':
    dct[puzzled(j)] = j

re_mixed = []
mixed = 'ZBTZBHZBIZBSBSEzcawBSEzyzuawac'
for i in lowerFlag:
    a = ''
    for j in mixed:
        a += str(re_mix(j,i))
    re_mixed.append(a)

mixed_flag =''
for i in re_mixed:
    if 'CTF'  in i:
        mixed_flag = i
# ACUACIACJACTCTFgjhdCTFgfgbhdhj

for key, value in dct.items():
    if key in mixed_flag:
        mixed_flag = mixed_flag.replace(key, value)

print(mixed_flag)
```
Run the script we get `THIS_is_easy`  
So the flag is:
```
TUCTF{THIS_is_easy}
```
# Hyper Maze

## Challenge description:


## Solution description:

Source file contains:
```python
import string

upperFlag = string.ascii_uppercase[:26]
lowerFlag = string.ascii_lowercase[:26]
MIN_LETTER = ord("a")
MIN_CAPLETTER = ord("A")

def mix(oneLetter,num):

    if(oneLetter.isupper()):
        word = ord(oneLetter)-MIN_CAPLETTER
        shift = ord(num)-MIN_CAPLETTER
        return upperFlag[(word + shift)%len(upperFlag)]
    if(oneLetter.islower()):
        word = ord(oneLetter)-MIN_LETTER
        shift = ord(num)-MIN_LETTER
        return lowerFlag[(word + shift)%len(upperFlag)]

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

    
flag = "Figure it Out! :)"
numShift = "??"
mixed = ""

assert all([x in lowerFlag for x in numShift])
assert len(numShift) == 1

encoding = puzzled(flag)
print(encoding)
for count, alpha in enumerate(encoding):
    mixed += mix(alpha, numShift)

print(mixed)
```

After decode the cipher in the description, we got the output of the above script.  
The 'mix' function can easily be reverse:
```python
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
```

And the 'puzzled' function just change a character to 3 character if the letter is upper or 2 character if the letter is lower. So that we can easily know all the case and add to a dictionary like this:
```python
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
```
We got:  
```
dct = {'CTF': '_', 'gb': 'a', 'gc': 'b', 'gd': 'c', 'ge': 'd', 'gf': 'e', 'gg': 'f', 'gh': 'g', 'gi': 'h', 'gj': 'i', 'gk': 'j', 'gl': 'k', 'gm': 'l', 'gn': 'm', 'go': 'n', 'gp': 'o', 'ha': 'p', 'hb': 'q', 'hc': 'r', 'hd': 's', 'he': 't', 'hf': 'u', 'hg': 'v', 'hh': 'w', 'hi': 'x', 'hj': 'y', 'hk': 'z', 'ACB': 'A', 'ACC': 'B', 'ACD': 'C', 'ACE': 'D', 'ACF': 'E', 'ACG': 'F', 'ACH': 'G', 'ACI': 'H', 'ACJ': 'I', 'ACK': 'J', 'ACL': 'K', 'ACM': 'L', 'ACN': 'M', 'ACO': 'N', 'ACP': 'O', 'ACQ': 'P', 'ACR': 'Q', 'ACS': 'R', 'ACT': 'S', 'ACU': 'T', 'ACV': 'U', 'ACW': 'V', 'ACX': 'W', 'ACY': 'X', 'ACZ': 'Y'}
```
Now we can easily `unmix the flag` with this script:

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
            if (i-MIN_CAPLETTER+ord(num)-MIN_CAPLETTER)%26 == w_s26:
                return chr(i)

    if oneLetter.islower():
        w_s26 = lowerFlag.index(oneLetter)
        for i in range(97, 122):
            if (i-MIN_LETTER+ord(num)-MIN_LETTER)%26 == w_s26:
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
# Rapid Arithmetic
## Challenge description:


## Solution description:
Our task is to calculate some arithmetic.
My script using pwntool:

```python
from pwn import *
import time

from word2number import w2n

def sol(a):
    xyz = a.replace(',', '')

    b = xyz.replace('minus', '').replace('plus', '').split('  ')
    c = xyz.replace('minus', '').replace('plus', '').split('  ')
    d = {'minus': '-', 'plus': '+'}
    for i in range(len(b)):
        if 'negative' in b[i]:
            b[i] = w2n.word_to_num(b[i]) -2*w2n.word_to_num(b[i])
        else:
            b[i] = w2n.word_to_num(b[i])
        d[c[i]] = b[i]
    d_2 = sorted(list(d.items()), key = lambda key : len(key[0]), reverse=True)
    res = {ele[0] : ele[1]  for ele in d_2}
    for key, value in res.items():
        if key in xyz:
            xyz = xyz.replace(key, str(value))
    print(xyz)
    return round(eval(xyz))    

def roman_int(s):
      roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900, '0':0}
      i = 0
      num = 0
      while i < len(s):
         if i+1<len(s) and s[i:i+2] in roman:
            num+=roman[s[i:i+2]]
            i+=2
         else:
            #print(i)
            num+=roman[s[i]]
            i+=1
      return num

def cal_roman(a):

    b = a.replace('(', '').replace(')', '').replace('+', '').replace('-', '')
    c = b.split()
    d = b.split()
    e = {}
    for i in range(len(c)):
        c[i] = roman_int(c[i])
        e[d[i]] = c[i]
    d_2 = sorted(list(e.items()), key = lambda key : len(key[0]), reverse=True)
    res = {ele[0] : ele[1]  for ele in d_2}

    for key, value in res.items():
        if key in a:
            a = a.replace(key, str(value))
    print(a)
    return(round(eval(a)))

def from_morse(s):
    CODE = {'A': '.-',     'B': '-...',   'C': '-.-.', 
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',

        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.' 
        }

    CODE_REVERSED = {value:key for key,value in CODE.items()}
    return ''.join(CODE_REVERSED.get(i) for i in s.split())

def cal_morese(a):
    b = a.replace('(', '').replace(')', '').replace(' - ', '').replace(' + ', '').replace(' / ', '')
    c = b.split()
    d = b.split()
    e = {}
    for i in range(len(c)):
        c[i] = from_morse(c[i])
        e[d[i]] = c[i]
    d_2 = sorted(list(e.items()), key = lambda key : len(key[0]), reverse=True)
    res = {ele[0] : ele[1]  for ele in d_2}

    for key, value in res.items():
        if key in a:
            a = a.replace(key, str(value))

    a = a.replace(' ', '')
    print(a)
    return(round(eval(a)))
def cal_art(a):
    c = {'====': '-', '++++++': '+', '00  00': '0','11':'1' , '22':'2' , '333':'3','444444':'4', '55555': '5', '66666': '6','77':'7' , '8888': '8', '99999':'9'}
    for key, value in c.items():
        if key in a:
            a = a.replace(key, str(value))
    a = a.replace(' ', '').replace('  ', '')
    print(a)
    return(round(eval(a)))




r = remote('chals.tuctf.com', 30200)

while True:
    
    console = r.recv().decode()
    a = console.split("\n")
    print(console+'\n')
    for j in a:
        if j.startswith('('):
            if '-.' in j or '.-' in j or '---' in j or '...' in j:
                b=cal_morese(j)
                c = str(b) + '\n'
                print(f'Solution: {c}')
                if 'UC' not in a:
                    r.send(str(c).encode())
                else:
                    print(console)
                    break
                break 
            elif 'X' in j or 'I' in j or 'V' in j or 'L' in j:
                b=cal_roman(j)
                c = str(b) + '\n'
                print(f'Solution: {c}')
                if 'UC' not in a:
                    r.send(str(c).encode())
                else:
                    print(console)
                    break
                break 
            else:
                b = round(eval(j))      
                c = str(b) + '\n'
                print(f'Solution: {c}')
                if 'UC' not in a:
                    r.send(str(c).encode())
                else:
                    print(console)
                    break
                break 
        elif 'plus' in j or 'minus' in j:
            b = sol(j)
            c = str(b) + '\n'
            print(f'Solution: {c}')
            if 'UC' not in a:
                r.send(str(c).encode())
            else:
                print(console)
                break
            break 
        elif '====' in j or '++++++' in j:
            b=cal_art(j)
            c = str(b) + '\n'
            print(f'Solution: {c}')
            if 'UC' not in a:
                r.send(str(c).encode())
            else:
                print(console)
                break
            break 
        else:
            time.sleep(0.5)
```

After running the script for a while. Here's the flag:

```
TUCTF{7h4nk5_f0r_74k1n6_7h1n65_4_l177l3_5l0w_4268285}
```
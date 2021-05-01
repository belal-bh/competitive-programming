import re

regex_num = re.compile('\d+')
regex_str = re.compile('[A-Z]+')

def solve(cell):
    global regex_num
    global regex_str

    ms_num = regex_num.findall(cell)
    if len(ms_num) == 2:
        r = int(ms_num[0])
        c = int(ms_num[1])
        c_str = ''
        while c > 0:
            c -= 1
            c_str = chr((c%26)+65) + c_str
            c //= 26
        return f'{c_str}{r}'

    else:
        ms_str = regex_str.findall(cell)
        r = int(ms_num[0])
        c_str = ms_str[0]
        
        c_num = 0
        for letter, i in zip(c_str[::-1], range(len(c_str))):
            c_num += (ord(letter)-64)* 26**i
        return f'R{r}C{c_num}'

for _ in range(int(input())):
    print(solve(input()))
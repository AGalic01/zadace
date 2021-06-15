def obrnuto(s):
    if len(s)==1:
        return s[0]
    else:
        return obrnuto(s[1:])+s[0]


print(obrnuto("kaktus"))

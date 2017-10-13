string = "HUKUUEUUYREUYYKGRRGNZZKXNGNOLKXTSAQNZYEGNZTRGTOYALSSEHSYGRVSOOLEGIKVKNZOEJYXT"


def char_frequency(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict


s = str(char_frequency(string))
print(s)

f = open('wow.txt', 'w')
f.write(s)
f.close()
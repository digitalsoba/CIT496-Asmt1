candidate = "BOEOOYOOSLYOSSEALLAHTTERHAHIFERNMUKHTSYAHTNLANISUFMMYBMSALPMIIFYACEPEHTIYDSR"
words = file('/usr/share/dict/words').read()
#This generator calls find twice, it should be rewritten as a normal loop
generate_matches = ((candidate.find(word),word) for word in words.split('\n')
                     if candidate.find(word) != -1 and word != '')

for match in generate_matches:
    print ("Found %s at (%d,%d)" % (match[1],match[0],match[0] + len(match[1])))
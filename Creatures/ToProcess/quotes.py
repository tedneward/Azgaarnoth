teststr = "Over time, “Granny” convinces the child that it’s okay to have bad thoughts"
print(teststr)
if teststr.find(u"“") > 0:
    print("SMART QUOTES!!!!")
    print(teststr.replace(u"“", '"'))
if teststr.find(u"’") > 0:
    print("SMART QUOTES!!!!")
    print(teststr.replace(u"’", "'"))

with open('Hags.txt', 'r', errors='ignore', encoding='utf-8') as argfile:
    lines = argfile.readlines()
    linect = 0
    while linect < len(lines):
        if lines[linect].find(u"“") > 0:
            line = lines[linect].replace(u"“", '"')
            lines[linect] = line
        if lines[linect].find(u"”") > 0:
            line = lines[linect].replace(u"”", '"')
            lines[linect] = line
        if lines[linect].find(u"’") > 0:
            line = lines[linect].replace(u"’", "'")
            print("SMART QUOTES!!!!")
            lines[linect] = line
        linect += 1
    
    print(lines)

def ProcPosition(position, index, src):
    src = src.decode("utf-8")
    s1 = src.index(':')
    s1 += 1
    e1 = src.index(',')
    p1 = src[s1:e1]
    p1 = p1.replace(' ','')#delet the spacing
    position[index].append(int(p1))
    src = src[e1+1:]
    s2 = src.index(':')
    s2 += 1
    e2 = src.index('}')
    p2 = src[s2:e2]
    p2 = p2.replace(' ', '')  # delet the spacing
    position[index].append(int(p2))
    print(position)

def ParseCost (src):
    #print(src)
    table = []
    s1 = src.index(':')
    s1 += 1
    e1 = src.index(',')
    p1 = src[s1:e1]
    p1 = p1.replace(' ','')#delet the spacing
    table.append(int(p1))
    src = src[e1+1:]
    s2 = src.index(':')
    s2 += 1
    e2 = src.index(',')
    p2 = src[s2:e2]
    p2 = p2.replace(' ', '')  # delet the spacing
    table.append(int(p2))
    src = src[e2 + 1:]
    s3 = src.index(':')
    s3 += 1
    e3 = src.index('}')
    p3 = src[s3:e3]
    #print(table)
    #print(p3)
    table.append(float(p3))
    return table


def ProcCost(src):
    src = src.decode("utf-8")
    cost = []
    bp = 0 #break point
    while(len(src) > 20):
        bp = src.index('\n')
        #print("remain length" + str(len(src)))
        #print(bp)
        subString = src[:bp]
        src = src[bp+1:]
        cost.append(ParseCost(subString))
    print(cost)
    return cost
#mic Programming Python implementation of Min Cost Path 
# problem 
#def searchIndex(i,j,base):

def Initialize(cost, Si, Sj, Gi, Gj,obstacle):
    #Si,Sj are the coordinates of startswith
    #Gi,Gj are the coordinates of Goal
    R = len(cost)
    C = len(cost[0])
    path = []
    #parameter check
    if (Si >= R) or (Gi >= R) or \
       (Sj >= C) or (Gj >= C):
            print("parametet error")
            exit()
    #initialize tc ： total cost table
    tc = [[obstacle for x in range(C)] for x in range(R)]#set the cost of unreachable point equal to obstacle
    tc[Si][Sj] = cost[Si][Sj]
    #initialize path: path in line with total cost
    path = [[[] for x in range(C)] for x in range(R)]
    #path[0][0] = [0,0]
    return R,C, tc, path
    
def LookAround(cost, tc, path, x,y,R,C,obstacle):
    #return a batter next hop if exist
    #return None if can not find better one
    if cost[x][y] == obstacle: #we dont care the path to obstacle
        return None 
    advise = None
    #look up
    if (x-1) >= 0: 
        #print("look up")
        if tc[x][y] > tc[x-1][y] + cost[x][y]:
            #prevent from loop
            if [x,y] not in path[x-1][y]:
                path[x][y] = path[x-1][y].copy()
                path[x][y].append([x-1,y])
                tc[x][y] = tc[x-1][y] + cost[x][y]
                advise = [x-1,y]
    #look down
    if (x+1) < R: 
        #print("look down")
        if tc[x][y] > tc[x+1][y] + cost[x][y]:
            #prevent from loop
            if [x,y] not in path[x+1][y]:
                path[x][y] = path[x+1][y].copy()
                path[x][y].append([x+1,y])
                tc[x][y] = tc[x+1][y] + cost[x][y]
                advise = [x+1,y]
    #look left
    if (y-1) >= 0:
        #print("look left")    
        if tc[x][y] > tc[x][y-1] + cost[x][y]:
            #prevent from loop
            if [x,y] not in path[x][y-1]:
                path[x][y] = path[x][y-1].copy()
                path[x][y].append([x,y-1])
                tc[x][y] = tc[x][y-1] + cost[x][y]
                advise = [x,y-1]
                
    #look right
    if (y+1) < C: 
        #print("look right")  
        if tc[x][y] > tc[x][y+1] + cost[x][y]:
            #prevent from loop
            if [x,y] not in path[x][y+1]:
                path[x][y] = path[x][y+1].copy()
                path[x][y].append([x,y+1])
                tc[x][y] = tc[x][y+1] + cost[x][y]
                advise = [x,y+1]
    
    return advise
    
def search(cost, Si, Sj, Gi, Gj,obstacle):
    R,C, tc, path = Initialize(cost, Si, Sj, Gi, Gj,obstacle)
    #searching util no update
    update = True
    advise = None
    cnt = 0
    while(update == True):
        update = False
        i = 0
        j = 0
        while(i < R):
            j = 0
            while(j < C):
                advise = LookAround(cost, tc, path, i,j,R,C,obstacle)
                if advise != None:
                    update = True
                j += 1
            i += 1
        cnt += 1
        #print(cnt)
    print("After " + str(cnt)+" times loop")
    #print(path)
    path[Gi][Gj].append([Gi,Gj])
    print(tc)
    print(path[Gi][Gj])
    return path[Gi][Gj]


def run(position, Tcost):
    print("start searching path")
    R = position[0][0]
    C = position[0][1]
    si = position[1][0]
    sj = position[1][1]
    gi = position[2][0]
    gj = position[2][1]
    #print(Tcost[0])
    ob = Tcost[0][2]
    maze = [[1 for x in range(C)] for x in range(R)]
    maze[si][sj] = 0
    for item in Tcost:
        maze[item[0]][item[1]] = ob
    path = search(maze, si, sj, gi, gj, ob)
    path = path[::-1]
    resp = str(path)
    step = len(path)
    resp = "200 ok {'steps': " + str(step) + ", 'path': [" + resp + "]}"
    print(resp)
    return resp
#inspired by:
#https://www.geeksforgeeks.org/min-cost-path-dp-6/

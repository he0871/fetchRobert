#mic Programming Python implementation of Min Cost Path 
# problem 
#def searchIndex(i,j,base):
import copy    
def minCost(cost, m, n,R,C): 
  
    # Instead of following line, we can use int tc[m+1][n+1] or 
    # dynamically allocate memoery to save space. The following 
    # line is used to keep te program simple and make it working 
    # on all compilers. 
    tc = [[0 for x in range(C)] for x in range(R)] 
    path = [[[] for x in range(C)] for x in range(R)]
    tc[0][0] = cost[0][0] 
    path[0][0] = []
    #print(path)
    # Initialize first column of total cost(tc) array 
    for i in range(1, m+1): 
        tc[i][0] = tc[i-1][0] + cost[i][0] 
        #print(i)
        #print(path[i-1][0])
        path[i][0]= copy.copy( path[i-1][0])
        path[i][0].append([i-1,0])
        #print(path[i][0]) 
    # Initialize first row of tc array 
    for j in range(1, n+1): 
        tc[0][j] = tc[0][j-1] + cost[0][j]
        path[0][j] = copy.copy( path[0][j-1])
        path[0][j].append([0,j-1]) 
    #path = []
    #temp = []  
    # Construct rest of the tc array 
    for i in range(1, m+1): 
        for j in range(1, n+1): 
            if (tc[i-1][j]>tc[i][j-1]):
                tc[i][j] = tc[i][j-1] + cost[i][j]
                path[i][j] = copy.copy( path[i][j-1])
                path[i][j].append([i,j-1])
            else:
                tc[i][j] = tc[i-1][j] +  cost[i][j]
                path[i][j] = copy.copy( path[i-1][j])
                path[i][j].append([i-1,j])

            #tc[i][j] = min(tc[i-1][j], tc[i][j-1]) + cost[i][j] 
            #temp = []
    path[m][n].append([m,n])
    return path[m][n] 
#reference:
#https://www.geeksforgeeks.org/min-cost-path-dp-6/

#dfs
import sys
import copy


def dfs(map,num,nRow):
    maxNum=num
    for i in range(nRow):
        for j in range(nRow):
            if map[i][j]=='.':
                
                tempMap=copy.deepcopy(map)
                tempMap[i][j]='o';
                
                tempI=i
                tempJ=j
                while (tempI-1>=0)and(tempMap[tempI-1][j]!='X'): 
                    tempMap[tempI-1][j]='o'
                    tempI-=1
                tempI=i
                tempJ=j
                while (tempI+1<nRow)and(tempMap[tempI+1][j]!='X'):
                    tempMap[tempI+1][j]='o'
                    tempI+=1
                tempI=i
                tempJ=j
                while (tempJ-1>=0)and(tempMap[i][tempJ-1]!='X'):
                    tempMap[i][tempJ-1]='o'
                    tempJ-=1
                tempI=i
                tempJ=j
                while (tempJ+1<nRow)and(tempMap[i][tempJ+1]!='X'):
                    tempMap[i][tempJ+1]='o'
                    tempJ+=1
                if dfs(tempMap,num+1,nRow)>maxNum:
                    maxNum=dfs(tempMap,num+1,nRow)
    return maxNum


data=sys.stdin.readlines()
row=0
nRow=int(data[row][0])
#print data[1][1]
while nRow!=0:
    map=[['' for i in range(nRow)] for j in range(nRow)]
    
    for i in range(nRow):
        for j in range(nRow):
            map[i][j]=data[row+1+i][j]
            #print map[i][j],data[row+1+i][j],i,j

    #print map
    print dfs(map,0,nRow)
    row+=nRow+1
    nRow=int(data[row][0])


                  
                   
    
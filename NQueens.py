#BackTracking

import sys
def NQueens(board,row,col,tq,qpsf,ans):
    if(qpsf==tq):
        print(ans)
        for i in board:
            print(i)
        #sys.exit()
        return
    if(col==len(board[0])):
        col=0
        row+=1
    if(row==len(board)):
        return
    if(isSafe(board,row,col)):
        board[row][col]=True
        NQueens(board,row,col+1,tq,qpsf+1,ans+"["+ str(row) + "," + str(col)+"]" )
        board[row][col]=False
    NQueens(board,row,col+1,tq,qpsf,ans )
def isSafe(board,row,col):
    #vertically up
    r=row-1
    c=col
    while(r>=0):
        if board[r][c]==1:
            return False
        r-=1
    #horizontally Left
    r=row
    c=col-1
    while(c>=0):
        if board[r][c]==1:
            return False
        c-=1

    #diagonally left
    r=row-1
    c=col-1
    while(c>=0 and r>=0):
        if board[r][c]==1:
            return False
        c-=1
        r-=1
    #diagonally right
    r=row-1
    c=col+1
    while(c<len(board[0]) and r>=0):
        if board[r][c]==1:
            return False
        c+=1
        r-=1
    return True
def backtrack(n):
    board=[[False for i in range(n)]for j in range(n)]
    NQueens(board,0,0,n,0,'')

backtrack(4)










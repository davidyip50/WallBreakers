from collections import defaultdict
class Solution(object):
    def find(self,parent,node):
        if(parent[node] == -1):
            return node
        else:
            return self.find(parent,parent[node])
        
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        //check borders for O
        //if there is a O put it into a list 
        //check all other Os if connected 
        //if connected add to sub set
        """
        if(len(board) <= 0):
            return
        parents = [-1] * (len(board[0]) * len(board))
        hit = []
        checks = defaultdict(int)
        for row in range(len(board)):
            for col in range(len(board[row])):
                if(board[row][col] == "O"):
                    #print(row,col,parents)
                    if(row == 0):
                        hit.append(row * len(board[row]) + col)
                    if(row == len(board) - 1):
                        hit.append(row * len(board[row]) + col)
                    if(col == 0):
                        hit.append(row * len(board[row]) + col)
                    if(col == len(board[row]) - 1):
                        hit.append(row * len(board[row]) + col)
                        
                    rParent = self.find(parents,row * len(board[row]) + col)
                    if(row - 1 >= 0 and board[row - 1][col] == "O"):
                        #add to subset
                        sParent = self.find(parents, (row - 1) * len(board[row]) + col)
                        #print(sParent)
                        if(sParent != rParent):
                            parents[sParent] = rParent
                        #if(rParent == row * len(board[row]) + col and sParent == -1):
                        #    parents[rParent] = (row - 1) * len(board[row]) + col
                        #if(and rParent != sParent):
                        #    parents[rParent] = (row - 1) * len(board[row]) + col  
                            
                    if(row + 1 < len(board) and board[row + 1][col] == "O"):
                        #add to subset
                        sParent = self.find(parents, (row + 1) * len(board[row]) + col)
                        #print(sParent)
                        if(sParent != rParent):
                            parents[sParent] = rParent
                        #if(rParent != self.find(parents, (row + 1) * len(board[row]) + col)):
                         #   parents[rParent] = (row + 1) * len(board[row]) + col 
                    if(col - 1 >= 0 and board[row][col - 1] == "O"):
                        #add to subset
                        sParent = self.find(parents, (row) * len(board[row]) + col - 1)
                        #print(sParent)

                        if(sParent != rParent):
                            parents[sParent] = rParent
                        #if(rParent != self.find(parents, (row) * len(board[row]) + col + 1)):
                        #    parents[rParent] = (row) * len(board[row]) + col + 1
                    if(col + 1 < len(board[row]) and board[row][col + 1] == "O"):
                        #add to subset
                        sParent = self.find(parents, (row) * len(board[row]) + col + 1)
                        #print(sParent)

                        if(sParent != rParent):
                            parents[sParent] = rParent
                        #if(rParent != self.find(parents, (row - 1) * len(board[row]) + col - 1)):
                        #    parents[rParent] = (row) * len(board[row]) + col - 1
        
        for i in hit:
            rParent = self.find(parents,i)
            checks[rParent] += 1
        #print(parents)
        for row in range(len(board)):
            for col in range(len(board[row])):
                if(board[row][col] == "O"):
                    rParent = self.find(parents,row * len(board[row]) + col)
                    if(rParent not in checks):
                        board[row][col] = "X"
        
                
        

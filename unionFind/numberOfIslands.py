class Solution(object):    
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        if it is a one check all four neighbors
            and if it is a one then put in subset
        
        """
        if(grid == []):
            return 0
        if(len(grid) > 0):
            parent = [-1] * (len(grid) * len(grid[0]))
        checks = {}
        
        
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if(grid[row][col] == 1):
                    if(row - 1 >= 0 and grid[row-1][col] == 1):
                        rParent = self.find(parent,(row - 1) * len(grid[row]) + col)
                        parent[(row - 1) * len(grid[row]) + col] = rParent
                    
                    if(row + 1 >= len(grid) and grid[row+1][col] == 1):
                        rParent = self.find(parent,(row + 1) * len(grid[row]) + col)
                        parent[(row + 1) * len(grid[row]) + col] = rParent
                        
                    if(col - 1 >= 0 and grid[row][col-1] == 1):
                        rParent = self.find(parent,row * len(grid[row]) + col - 1)
                        parent[row * len(grid[row]) + col - 1] = rParent
                    
                    if(col - 1 >= 0 and grid[row][col+1] == 1):
                        rParent = self.find(parent,row * len(grid[row]) + col + 1)
                        parent[row * len(grid[row]) + col + 1] = rParent

        for i in range(len(parent)):
            if(i != -1 and parent[i] not in checks):
                checks[parent[i]] = i
            if(i != -1 and parent[i] in checks):
                checks[parent[i]] += i
        
        counter = 0
        for i in checks:
            counter += 1
        return counter
    
    def find(self,parent,node):
        """
        :type parent: List[]
        :rtype: int
        """
        if(parent[node] == -1):
            return node
        else:
            return self.find(parent,parent[node])
        

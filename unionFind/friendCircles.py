class Solution(object):
    def find(self,parent,node):
        """
        :type parent: List[]
        :rtype: int
        """
        if(parent[node] == -1):
            return node
        else:
            return self.find(parent,parent[node])
        
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        directFriends = []
        parent = []
        counter = 0
        
        for i in range(len(M)):
            parent.append(-1)
        
        for row in range(len(M)):
            for col in range(len(M)):
                if(M[row][col] == 1):
                    directFriends.append([row,col])
        
        for connects in directFriends:
            #if(connects[0] != connects[1]):
             #   print(str(self.find(parent,connects[0])) + " " + str(self.find(parent,connects[1])))
            if(connects[0] != connects[1] and self.find(parent,connects[0]) != self.find(parent,connects[1])):
                if(parent[connects[0]] == -1):
                    parent[connects[0]] = connects[1]
                else:
                    parent[self.find(parent,connects[0])] = connects[1]

                #for i in range(len(parent)):
                 #   print(i,parent[i])
                
        for i in parent:
            if( i == -1):
                counter += 1
        return counter
                

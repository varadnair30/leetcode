class DisjointSet:
    def __init__(self, n):
        self.parent=[i for i in range(n)]
        self.size=[1]*n

    def find(self,node):
        if node==self.parent[node]:
            return node

        self.parent[node]=self.find(self.parent[node])

        return self.parent[node]

    def union(self,u,v):

        pu,pv = self.find(u), self.find(v)

        if pu==pv:
            return False

        if self.size[pu]<self.size[pv]:
            self.parent[pu]=pv

            self.size[pv] += self.size[pu]

        else:

            self.parent[pv]=pu

            self.size[pu] += self.size[pv]

        return True



class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:

        '''
        n nodes (0 to n-1 )

        connections[i]= [ai,bi] (edges)
        make adjLst using connections array
        the nodes from 0 to n-1 not present in adjLst are unreachable

        
        '''
        

        ds=DisjointSet(n)

        extraEdges=0

        for u,v in connections:
            if not ds.union(u,v):
                extraEdges+=1

        components= sum(1 for i in range(n) if ds.parent[i]==i)

        operations_needed = components-1

        return operations_needed if extraEdges >= operations_needed else -1


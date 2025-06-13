class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if  n==0: return True# empty graph is a tree
        # Generate adjLs for the edges
        # if already in visit retrn false else put the nodes in the visit set 
        # maintain the previous node but make sure the immediate parent is not detected as cycle
        # run a recursive dfs algorithm where I can return false if found in visit (cycle detected)
        # return dfs func and len vis == n

        adjLs=[[] for _ in range(n)]

        for u,v in edges:
            adjLs[u].append(v)
            adjLs[v].append(u) 

        visit=set()

        def dfs(node,prev):
            

            if node in visit: return False

            visit.add(node)

            for neighbor in adjLs[node]:
                if neighbor==prev:
                    continue

                if not dfs(neighbor,node):
                    return False

            return True

        return dfs(0,-1) and len(visit)==n


        
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:


        graph = defaultdict(list)
        for src, dst in edges:
            graph[src].append(dst)  
            graph[dst].append(src)   
        
        queue = deque([source]) 
        visited = {source}
        while queue:
            node = queue.popleft() 
            if node == destination:
                return True  
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor) 
        return False 


        
        
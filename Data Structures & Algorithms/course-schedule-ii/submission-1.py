class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        premap = {i: [] for i in range(numCourses)}
        indeg = [0] * numCourses
        for course, pre in prerequisites:
            premap[pre].append(course)
            indeg[course] += 1
        
        q = deque()
        for course, deg in enumerate(indeg):
            if deg == 0:
                q.append(course)
        processed = 0
        valid = []
        while q:
            cur = q.popleft()
            processed += 1
            valid.append(cur)

            for c in premap[cur]:
                indeg[c] -= 1
                if indeg[c] == 0:
                    q.append(c)
            
        if processed == numCourses:
            return valid
        else:
            return []
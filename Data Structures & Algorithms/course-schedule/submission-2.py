class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap = {i:[] for i in range(numCourses)}
        indeg = [0] * numCourses

        for course, pre in prerequisites:
            premap[pre].append(course)
            indeg[course] += 1
        
        queue = deque()

        for c, ideg in enumerate(indeg):
            if ideg == 0:
                queue.append(c)

        processed = 0
        while queue:
            cur = queue.popleft()
            processed += 1
            for course in premap[cur]:
                indeg[course] -= 1
                if indeg[course] == 0:
                    queue.append(course)
        if processed == numCourses:
            return True
        else:
            return False
            

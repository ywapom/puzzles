# can you finish the courses:
# n courses and array of prereqs[i] = [a,b] meaning you have to have b to take a...

from collections import deque


test = {
    'input':{
        'prereqs':[[3,0],[1,3],[2,1],[4,1],[4,2],[5,3],[5,4]],
        'n':6
    },
    'output' : "True"
}

#DFS after topological sort?

def dfs(graph, vertex, path, order, visited):
    path.add(vertex)
    for neighbor in graph[vertex]:
        visited.add(neighbor)
        dfs(graph, neighbor, path, order, visited)
    path.remove(vertex)
    order.append(path.pop())
    return True

def top_sort(graph):
    visited = set()
    path = []
    order = []
    for vertex in graph:
        if vertex not in visited:
            visited.add(vertex)
            dfs(graph, vertex, path, order, visited)
    return order[::-1]

def course_schedule(n, prerequisites):
    # T(V,E) = O(|V| + |E|)
    # O(n+m)
    
    # build adjacency list
    graph = [[] for i in range(n)]
    for pre in prerequisites:
        graph[pre[1]].append(pre[0])

    visited = set()
    path = set()
    order = []
    for course in range(n):
        if course not in visited:
            visited.add(course)
            if not dfs(graph, course, path, order, visited):
                return False
    return True

#----------------------
# alternate: BFS
def course_schedule_bfs(n, prerequisites):
    graph = [[] for i in range(n)]
    indegree = [0 for i in range(n)]
    for pre in prerequisites:
        graph[pre[1]].append(pre[0])
        indegree[pre[0]] += 1
    order = []
    queue = deque([i for i in range(n) if indegree[i] == 0])
    while queue:
        vertex = queue.popleft()
        order.append(vertex)
        for neighbor in graph[vertex]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    return len(order) == n

print(course_schedule_bfs(test['input']['n'], test['input']['prereqs']))


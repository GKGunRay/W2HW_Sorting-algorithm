#20201230
graph = {
    '1':['2', '4', '5'],
    '2':['1', '3'],
    '3':['3'],
    '4':['1', '3', '5'],
    '5':['2', '3']
    }
def BFS(graph, start):
    queue = []
    queue.append(start)
    seen = set()
    seen.add(start)
    while(len(queue)>0):
        vertex = queue.pop(0)
        nodes = graph[vertex]
        for path in nodes:
            if path not in seen:
                queue.append(path)
                seen.add(path)
        if len(queue)!=0:
            print(vertex, end="->")
        else:
            print(vertex)

def DFS(graph, start):
    stack = []
    stack.append(start)
    seen = set()
    seen.add(start)
    while(len(stack)>0):
        vertex = stack.pop()
        nodes = graph[vertex]
        for path in nodes:
            if path not in seen:
                stack.append(path)
                seen.add(path)
        if len(stack)!=0:
            print(vertex, end="->")
        else:
            print(vertex)

        
print("BFS:", end="")
BFS(graph,'1')

print("DFS:", end="")
DFS(graph,'1')

"""
RECURSIVE ALGORIGHM OF DFS

marked = [False] ** len(G)
def dfs(G, v):
    visit(v)
    marked[v] = True
    for w in G.neighbors(v):
        if not marked[v]:
            dfs(G, w)




ITERATIVE IMPLEMENTATION

marked = [False] * len(G)

def dfs(G, v):
    stack = [v]

    while len(stack) > 0:
        v = stack.pop()
        if not marked[v]:
            visit(v)
            marked[v] = True
            for w in G.neighbors(v):
                if not marked[w]:
                    stack.append(w)
"""
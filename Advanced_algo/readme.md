### Graph 20222.11.01
1. Graph data structure:
    |        | space    | traversal | recommended | restriction |
    | -      |   -      |  -        | -           | - |
    | Matrix | O(v^2)   | O(v^2)    |             |   |
    | Dict   | O(v^2\*H)| O(v)      | v           | nested dict, aka out-D, compute parents_dict in advance for some situations |
    | Node   | O(v+e)   | O(v+e)    |             | complex and rarely seen in disconnected graph |
    + data structure transformation can use dict as media e.g. clone graph (node->dict->node)

2. General graph traversal:
    + **Graph** (general) vs **Binary tree** (connected+directed+acyclic): **acyclic doesn't need to record "visit"**
    + Connection:
        + **Connected** (One entry point can go to everywhere) -> visit e.g. Maze, Word search
        + **Disconnected** (Every entry points are needed) -> unvisit e.g. Number of provinces
    + **DFS** is easier and enough:
        + (Recommended) bottom-up recursion 1 or 2 arguments: node, visit/unvisit 
        + stack iteration arguments: while stack, node, visit/unvisit
        + [Note] Revoke traversal need to pop the node after traversal if use recursive-bu-2 so recursive-bu-1 is better e.g. Word Search
    + Traversal not consider unweighted/weighted

3. Topological sort (directed):
    + **Kahn's algorithm (Iteration)**: Remove in-degree=0 nodes gradually (In-D is needed).
    + Applications: Scheduling, Cycle determination e.g. Course scheduling
    
4. Shortest path problem (directed/undirected):
    |            | Dijkstra | Bellman-Ford by Matrix |
    | -          | -        | -                      |
    | situation  | positive edge and no step restriction | can have either left |
    | concept    | Explored distance dict -> get unvisited min dist node (v times)<br>-> triangular update (neighbor times) | copy distance dict (v times) -> triangular update (all edges times) |
    | time       | Naive:O(v^2)<br>Heap:O(elog(v)) | O(ve) |
    | example    | Network delay time | Cheapest flights within k steps |
    + Dijkstra in naive is recommended since its easier and efficient in general case (dense graph)
    
5. Minimum spanning tree (directed): Prim's algorithm
    + Pick min adjacent weight of each nodes

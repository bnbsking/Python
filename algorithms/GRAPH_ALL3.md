### Version3:
1. Graph data structure:
    |        | space    | traversal | recommended | restriction |
    | -      |   -      |  -        | - | - |
    | Matrix | O(v^2)   | O(v^2)    |   |   |
    | Dict   | O(v^2\*H)| O(v)      | v | nested dict, compute parents_dict in advance for some situations |
    | Node   | O(v+e)   | O(v+e)    |   | complex and rarely seen in disconnected graph |

2. General graph traversal:
    + Graph (cyclic) vs binary tree (directed acyclic): **acyclic doesn't need to record "visit"**
    + Basic paremeters: **DFS recursion is the best (more precise) in most cases**
        |   | DFS | BFS |
        | - | - | - |
        | recursion input | f(i), iterate once | f(i), iterate twice |
        | iteration condition | len(stack) | len(queue) |
    
    + Strategy:
        | | connected (Given 1 node only) | disconnected (Given all nodes, while unvisit at out loop) |
        | - | - | - |
        | undirected | recursion: global visit + f(i) <br> iteration: while stack/queue | recursion: while global unvisit + f(i) <br> iteration: while unvisit while stack/queue |
        | directed   | --- | recursion: while global unvisit + f(i) <br> iteration: while unvisit while stack/queue |

    + Examples:
        + connected undirected: Maze, Word Search, Clone Graph, Minimum of Tree Heights, Evaluate Division
        + connected directed: most of the tree problems.
        + disconnected undirected: Surrounded Regions, Number of Islands
        + disconnected directed: Course Schedule
        
    + Traversal not consider unweighted/weighted

3. Repeat path problem for recursion: **delete i from visit/parent/parents at the end of the function !!!**
    + e.g. Course schedule (directed cycle check) e.g. [[0,1],[0,2],[1,2]] will has cycle if forget to delete
    + e.g. Word Search

4. Cycle determination:
    + undirected: must add parent (int) argument to f. Has node if a node visit twice excludes parent.
    + directed: must add parents (list) argument to f. Has node if visiting a node is already in parents.
    + directed(best): **topological sort - Kahn's algorithm (Iteration)** - remove in degree==0 nodes gradually
    
5. Shortest path problem:
    |            | Dijkstra | Bellman-Ford |
    | -          | - | - |
    | situation  | No "Negative cycle" or "step restriction" | has either left |
    | parameters | iteration,visit | iteration |
    | concept    | update neighbors from 1 current | update all current from neighbors |
    | time       | O(va) | O(kva) |
    
    + a: average number of in-degree nodes
    + k: step restrictions (at most n)

6. Minimum spanning tree: Prim's algorithm
    + Pick min adjacent weight of each nodes

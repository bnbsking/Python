### Version3:
1. Graph data structure:
    |        | space  | traversal | recommended | restriction |
    | -      |   -    |  -        | - | - |
    | Matrix | O(v^2) | O(v^2)    |   |   |
    | Dict   | O(v\*H)| O(v)      | v | compute getEdge(a,b), parents_dict in advance for some situations |
    | Node   | O(v+e) | O(v)      |   | complex and rarely seen in disconnected graph |

2. General graph traversal:
    + Graph (cyclic) vs binary tree (directed acyclic): acyclic doesn't need to record "visit"
    + Basic paremeters: DFS recursion is the best (more precise) in most cases
        |   | DFS | BFS |
        | - | - | - |
        | recursion input | f(i) | f(i), iterate twice |
        | iteration condition | len(stack) | len(queue) |
    
    + Strategy:
        | | connected (Given 1 node only) | disconnected (Given all nodes, while unvisit at out loop) |
        | - | - | - |
        | undirected | recursion: f(i,visit) <br> iteration: while stack/queue | recursion: while unvisit + f(i) <br> iteration: while unvisit while stack/queue |
        | directed   | --- | recursion: while unvisit + f(i) <br> iteration: while unvisit while stack/queue |

    + Examples:
        + connected undirected: Maze, Word Search, Clone Graph, Minimum of Tree Heights
        + connected directed: most of the tree problems.
        + disconnected undirected: Surrounded Regions, Number of Islands
        + disconnected directed: Course Schedule
        
    + Traversal not consider unweighted/weighted

3. Cycle determination:
    + undirected: must add parent (int) argument to f. Has node if a node visit twice excludes parent.
    + directed: must add parents (list) argument to f. Has node if visiting a node is already in parents.
    + directed(best): **topological sort - Kahn's algorithm (Iteration)** - remove in degree==0 nodes gradually

4. Repeat path problem for recursion: **delete i from visit/parent/parents at the end of the function !!!**
    + e.g. Course schedule (directed cycle check) e.g. [[0,1],[0,2],[1,2]] will has cycle if forget to delete
    + e.g. Word Search

5. Minimum spanning tree: Prim's algorithm
    + Pick min adjacent weight of each nodes
    
6. Shortest path problem: Dijkstra algorithm
    + Initialize start to each node distance, and visit
    + Initialize "getWeights(a,b)" and "parents"
    + Iterate until all nodes are visited: Find unvisited shortest path node
    + update the nodes neighbbor distance

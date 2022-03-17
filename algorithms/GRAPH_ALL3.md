### Version3:
1. Graph data structure:
    |        | space  | traversal | recommended | restriction |
    | -      |   -    |  -        | - | - |
    | Matrix | O(v^2) | O(v^2)    |   |   |
    | Dict   | O(v\*H)| O(v)      | v | compute getEdge(a,b), parents_dict in advance for some situations |
    | Node   | O(v+e) | O(v)      |   | complex and rarely seen in disconnected graph |


2. General graph traversal:
    + Graph (cyclic) vs binary tree (directed acyclic): acyclic doesn't need to record "visit"
    + Basic paremeters:
        |   | DFS | BFS |
        | - | - | - |
        | recursion input | f(i) | f(i), iterate twice |
        | iteration condition | len(stack) | len(queue) |
    
    + Strategy:
        | | connected (Given 1 node only) | disconnected (Given all nodes, while unvisit at out loop) |
        | - | - | - |
        | undirected | f(i,visit) simple recursion \n while stack/queue | while unvisit + f(i) simple recursion // while unvisit while stack/queue |
        | directed   | --- |  while unvisit + f(i) recursion // while unvisit while stack/queue |

    + Examples:
        + connected undirected: Maze, Word Search, Clone Graph, Minimum of Tree Heights
        + connected directed: most of the tree problems.
        + disconnected undirected: Surrounded Regions, Number of Islands
        + disconnected directed: Course Schedule
        
    + Traversal not consider unweighted/weighted
    
3. Repeat traversal problem: Start from a node and different path pass through same node. e.g. Word Search, Course Schedule
    + delete node from parent/parents at the end of the function !!! e.g. [[0,1],[0,2],[1,2]] will has cycle if forget to delete

4. Determine has cycle:
    + undirected: must add parent (int) argument to f. Has node if a node visit twice excludes parent.
    + directed: must add parents (list) argument to f. Has node if visiting a node is already in parents. e.g. Course Schedule

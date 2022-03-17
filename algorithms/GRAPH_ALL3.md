### Version3:
1. Graph data structure:
    |        | space  | traversal | recommended | restriction |
    | -      |   -    |  -        | - | - |
    | Matrix | O(v^2) | O(v^2)    |   |   |
    | Dict   | O(v\*H)| O(v)      | v | compute getEdge(a,b), parents_dict in advance for some situations |
    | Node   | O(v+e) | O(v)      |   | complex and rarely seen in disconnected graph |


2. General graph traversal (DFS):
    + Iteration use stack support, but Reucrsion don't.
    + For Recursion is recommended: (unweighted/weighted are not necessary to be considered)

    | | connected | disconnected |
    | - | - | - |
    | undirected | f(node,visit) and start from 1 node | f(node) and start until unvisit (global) is empty |
    | directed   | Tree /  | f(node) and start until unvisit (global) is empty |
    
    + Examples:
        + connected undirected: Maze, Word Search, Clone Graph
        + disconnected undirected: Surrounded Regions, Number of Islands
        + disconnected directed: Course Schedule
    + Repeat traversal problem: Start from a node and different path pass through same node. e.g. Word Search, Course Schedule
        + delete node from parent/parents at the end of the function !!! e.g. [[0,1],[0,2],[1,2]] will has cycle if forget to delete 


3. Determine has cycle:
    + undirected: must add parent (int) argument to f. Has node if a node visit twice excludes parent.
    + directed: must add parents (list) argument to f. Has node if visiting a node is already in parents. e.g. Course Schedule

# DFS

python pacman.py -l tinyMaze -p SearchAgent

python pacman.py -l mediumMaze -p SearchAgent

python pacman.py -l bigMaze -z .5 -p SearchAgent

# BFS

python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs

python pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5

# Uniform Cost Function

python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs

# A* Search

python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic

# Corners Problem

python pacman.py -l tinyCorners -p SearchAgent -a fn=bfs,prob=CornersProblem

python pacman.py -l mediumCorners -p SearchAgent -a fn=bfs,prob=CornersProblem

# A* int Corners Problem

python pacman.py -l mediumCorners -p AStarCornersAgent

# Stay west and Stay east

python pacman.py -l mediumDottedMaze -p StayEastSearchAgent

python pacman.py -l mediumDottedMaze -p StayWestSearchAgent
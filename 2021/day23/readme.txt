lessons:

1 using string as a state, computing distance based on the state
2 using heapq to maintain a priority queue, whose member should implement a method __lt__
3 using keywords to flag the visited state or unvisited state, so avoid duplicate state computation
4 using a dictionary to store the state(string) and its relevant cost
5 using a list to store all legal moves and its cost for a given state, and using base cost and predictive cost
to indicate the importance of the move
6 base cost computation is simple, just check whether the move is legal and correponding distance
7 predictive cost computation is based on manhattan distance
8 Overall, we need to achieve it step by step, using the right data structure and right algorithm.
9 Make it simple, give yourself one hour to find a solution, if you can't, search the internet for help.

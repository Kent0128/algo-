import numpy
from queue import PriorityQueue 
maze = numpy.array(
    [
        [0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
        [1, 1, 1, 0, 1, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 1, 1, 1, 1, 1, 0],
        [0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
        [0, 1, 1, 1, 1, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 1, 0, 1, 1],
        [0, 1, 1, 1, 1, 0, 1, 0, 0, 0]
    ]
)
def heuristic(a,b):
    (x1,y1)=a
    (x2,y2)=b
    return abs(x1-x2)+abs(y1-y2)
def neighbors(graph,current):
    Nei=[]
    if 9>=current[0]+1>=0:
        if graph[current[0]+1][current[1]]==0:
            new1=(current[0]+1,current[1])
            Nei.append(new1)
    if 9>=current[1]+1>=0:
        if graph[current[0]][current[1]+1]==0:
            new2=(current[0],current[1]+1)
            Nei.append(new2)
    if 9>=current[0]-1>=0:
        if graph[current[0]-1][current[1]]==0:
            new3=(current[0]-1,current[1])
            Nei.append(new3)
    if 9>=current[1]-1>=0:
        if graph[current[0]][current[1]-1]==0:
            new4=(current[0],current[1]-1)
            Nei.append(new4)
    return Nei
def a_star(graph,start,goal):
    frontier=PriorityQueue()
    frontier.put(start,0)
    came_from={}
    cost_so_far={}
    came_from[start]=None
    cost_so_far[start]=0
    while not frontier.empty():
        current=frontier.get()
        if current==goal:
            break
        for next in neighbors(graph,current):
            new_cost=cost_so_far[current]+1
            if next not in cost_so_far or new_cost<cost_so_far[next]:
                cost_so_far[next]=new_cost
                prioity=new_cost+heuristic(goal,next)
                frontier.put(next,prioity)
                came_from[next]=current
    def trace(current):
        if current!=(0,0):
            print(came_from[current])
            return trace(came_from[current])
    return trace(goal)

a_star(maze,(0,0),(9,9))


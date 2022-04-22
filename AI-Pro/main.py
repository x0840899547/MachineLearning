import utils
import ucs
import inputfunc
import balls_finder as problem

inputfunc.inputfuction()

goal_node, n_visits = ucs.uniform_cost_graph_search(problem)
print(" ")

print("Path Cost= %d" % goal_node[2])
utils.print_solution(goal_node)


#if goal_node is not None:
    #print("Step ")
    #print("========")
    #utils.print_solution(goal_node)
    #print("========")
    #print("Path cost = %d" % goal_node[3])
    #print("Number of Visited States = %d" % n_visits)
#else:
    #print("No solutions found")
'''def print_solution(n):
  r = deque()
  while n is not True:
    r.appendleft(n[0])
    n = n[1]
  for s in r:
    print("\nStep")
    for i in s:
      print(i)'''
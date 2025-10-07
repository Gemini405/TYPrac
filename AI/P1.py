import queue as Q
from RMP import dict_gn

start = 'Arad'
goal = 'Bucharest'
result = ''

def BFS(city, cityQ, visitedQ):
  global result
  if city == start: result = city
  for eachCity in dict_gn[city].keys():
    if eachCity == goal:
      result = result + ', ' + eachCity
      return
    if eachCity not in cityQ.queue and eachCity not in visitedQ.queue:
      cityQ.put(eachCity)
      result = result + ', ' + eachCity
  
  visitedQ.put(city)
  BFS(cityQ.get(), cityQ, visitedQ)

def main():
  cityQ = Q.Queue()
  visitedQ = Q.Queue()
  BFS(start, cityQ, visitedQ)
  print(f"BFS Traversal from {start} to {goal} is {result}")

main()

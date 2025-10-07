import queue as Q
from RMP import dict_gn

start = 'Arad'
goal = 'Bucharest'
result = ''

def DLS (city, visitedStack, startLimit, endLimit):
  global result
  found = 0
  result = result + ' ' + city
  visitedStack.append(city)
  if (city == goal): return 1 
  if (startLimit == endLimit): return 0
  for eachCity in dict_gn[city].keys(): 
    if eachCity not in visitedStack:
      found = DLS(eachCity, visitedStack, startLimit + 1, endLimit)
      if found: return found

def IDDFS (city, visitedStack, endLimit):
  global result
  for i in range(0, endLimit):
    print(f"Searching at Limit {i}")
    found = DLS(city, visitedStack, 0, i)
    if found:
      print("Found")
      break
    else:
      print("Not Found! ")
      print(result)
      print("-----")
      result = ''
      visitedStack = []

def main():
  visitedStack = []
  IDDFS(start, visitedStack, 9)
  print(f"IDDFS Traversal from {start} to {goal} is:{result}")

main()

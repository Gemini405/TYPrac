import queue as Q
from RMP import dict_gn
from RMP import dict_hn

start = 'Arad'
goal = 'Bucharest'
result = ''

def get_fn(cityStr):
  cities = cityStr.split(', ')
  hn = gn = 0
  for ctr in range(0, len(cities) - 1):
    gn = gn + dict_gn[cities[ctr]][cities[ctr + 1]]
  hn = dict_hn[cities[len(cities) - 1]]
  return(hn + gn)

def expand(cityQ):
  global result
  tot, cityStr, thisCity = cityQ.get()
  if thisCity == goal:
    result = cityStr + "\nTotal travel cost: " + str(tot)
    return 
  for city in dict_gn[thisCity]:
    cityQ.put((get_fn(cityStr + ", " + city), cityStr + ", " + city, city))
  expand(cityQ)

def main():
  cityQ = Q.PriorityQueue()
  thisCity = start
  cityQ.put((get_fn(start), start, thisCity))
  expand(cityQ)
  print(f"Optimal path from {start} to {goal} using A* Search: {result}")

main()

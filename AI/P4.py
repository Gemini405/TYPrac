import queue as Q
from RMP import dict_gn
from RMP import dict_hn

start = 'Arad'
goal = 'Bucharest'
result = ''

def get_fn(cityStr):
  cities = cityStr.split(", ")
  hn = gn = 0
  
  for ctr in range(0, len(cities) - 1):
    gn += dict_gn[cities[ctr]][cities[ctr + 1]]
  hn = dict_hn[cities[len(cities) - 1]]
  return(hn + gn)

def printOut(cityQ):
  for i in range(0, cityQ.qsize()):
    print(cityQ.queue[i])

def expand(cityQ):
  global result
  tot, cityStr, thisCity = cityQ.get()
  nextTot = 999
  
  if not cityQ.empty():
    nextTot = cityQ.queue[0][0]  
  
  if thisCity == goal and tot < nextTot:
    result = cityStr + '\nTotal path cost: ' + str(tot)
    return
  
  print(f"Expanded city — {thisCity}")
  print(f"Second best f(n) — {nextTot}\n")
  tempQ = Q.PriorityQueue()
  
  for city in dict_gn[thisCity]:
    tempQ.put((get_fn(cityStr + ", " + city), cityStr + ", " + city, city))
  
  for ctr in range(1, 3):
    ctrTot, ctrCityStr, ctrThisCity = tempQ.get()
    if ctrTot < nextTot:
      cityQ.put((ctrTot, ctrCityStr, ctrThisCity))
    else:
      cityQ.put((ctrTot, cityStr, thisCity))
      break

  printOut(cityQ)
  expand(cityQ)

def main():
  cityQ = Q.PriorityQueue()
  thisCity = start
  cityQ.put((999, "NA", "NA"))
  cityQ.put((get_fn(start), start, thisCity))
  expand(cityQ)
  print(result)

main()

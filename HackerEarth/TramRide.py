# A city has N Tram stations numbered from 1 to N  that are connected to one another and form a circle.
# You are given an array ticket_cost  where ticket_cost[i] is the cost of a ticket between the stops number i and (i+1)%N.
# The Tram can travel in both directions i.e. clockwise and anti-clockwise.
# Return the minimum cost to travel between the given start and finish station.
# You are given an integer N where N represents the total number of the tram stations,
# an integer start which represents the start station, and an integer finish which represents the finish station.
# You are given an array of positive integers  ticket_cost where ticket_cost[i] represents
# the ticket cost between the station number i and (i + 1) % N.


#given: list-> ticket_cost, N = total number of stations,start=Starting Station,finish=Finish Station,ticket_cost

def tram_ride(ticket_cost,n,start,finish):
 start -=1
 finish -=1
 if start > finish:
  start, finish=finish, start
 clockwise=sum(ticket_cost[start:finish])
 anit=sum(ticket_cost)-clockwise
 return min(clockwise,anit)


t_c=[3,1,4,2]
n=4
start=1
fin=3
print(tram_ride(t_c,n,start,fin))
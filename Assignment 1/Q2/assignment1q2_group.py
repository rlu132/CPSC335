# Ryan Lu, Anthony Thornton, Carla Madriz
# Group 9
# Dr. Sampson Akwafuo
# CPSC 335-04
# 02/25/2024

# Emails: rlu132@csu.fullerton.edu, anthonythornton140@csu.fullerton.edu, cmadriz@csu.fullerton.edu	 

def preferred_city(distances,fuel,mpg) -> int:
    graph = {}
    n = len(distances)
    # create a graph with adjacency list with v1 = v2
    for i in range(n-1):
        graph[i] = i+1
    graph[n-1] = 0

    # iterate through every possible starting vertex (city)
    for curr in graph:
        mileage = 0
        visited = []
        # run while not all nodes are visited
        while len(visited) < n:
            mileage += fuel[curr]*mpg
            # don't bother visiting more nodes if you cannot make it to the next city
            if mileage < distances[curr]:
                break
            mileage -= distances[curr]
            visited.append(curr)
            curr = graph[curr]
        # if the it is a spanning tree, aka visited all vertices, than the current city is a preferred starting city
        if len(visited) == n:
            return curr
    return -1


# Sample 1
city_distances = [5,25,15,10,15]
fuel = [1,2,1,0,3]
mpg = 10
print("Input for sample 1:\nCity distances:",city_distances,"\nFuel:",fuel,"\nMPG:",mpg)
print("The preferred city is city", preferred_city(city_distances, fuel, mpg))

# Example 1
city_distances = [5,25,15,10,15,20,40,10,5,15,60,5,10,20,40]
fuel = [1,2,1,0,1,3,2,6,5,4,1,3,5,7,4]
mpg = 10
print("Input for sample 1:\nCity distances:",city_distances,"\nFuel:",fuel,"\nMPG:",mpg)
print("The preferred city is city", preferred_city(city_distances, fuel, mpg))

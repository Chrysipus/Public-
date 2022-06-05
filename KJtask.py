"""
Flatland is a country with a number of cities, some of which have train stations. Cities are 
numbered consecutively and each has a road of 1km length connecting it to the next city. 
It is not a circular route, so the first city doesn't connect with the last city. Determine 
the maximum distance from any city to its nearest train station.

Notes:
- Cities are indexed from 0.
- Number of cities is between 1 and 10000.
- Number of cities with train station is between 1 and number of cities.
- No city has more than one train station.

Example:

number_of_cities == 3
cities_with_train_station == [1]

There are 3 cities and city #1 has a train station. They occur consecutively along a route. 
City #0 is 1km away, city #1 is 0km away and city #2 is 1km away from its nearest train station.
The maximum distance is 1.

"""

from typing import List
import math

def find_maximum_distance(
    number_of_cities: int, cities_with_train_station: List[int]
) -> int:
    # TODO: Replace this with real implementation:
    number_of_cities-=1
    maximum_distance = cities_with_train_station[0] #Distance to the first station.
    if maximum_distance < number_of_cities - cities_with_train_station[-1]: maximum_distance = number_of_cities - cities_with_train_station[-1] #Distance from the last station.
    next_station=0
    for current_station in cities_with_train_station:
        if next_station<len(cities_with_train_station)-1:
            next_station+=1
            if (cities_with_train_station[next_station] - current_station)/2 > maximum_distance: #Radius between stations.
                maximum_distance = (cities_with_train_station[next_station] - current_station)/2
    print(math.floor(maximum_distance))
    return math.floor(maximum_distance)

if __name__ == "__main__":
    # These are some of test cases. When evaluating the task, more will be added:
    assert find_maximum_distance(number_of_cities=3, cities_with_train_station=[1]) == 1
    assert find_maximum_distance(number_of_cities=4, cities_with_train_station=[3]) == 3
    assert find_maximum_distance(number_of_cities=5, cities_with_train_station=[0, 4]) == 2
    assert find_maximum_distance(number_of_cities=10000, cities_with_train_station=[1, 10, 11, 111, 112, 999, 1645, 2999, 4999, 8722]) == 1861
    assert find_maximum_distance(number_of_cities=100, cities_with_train_station=[50, 99]) == 50
    assert find_maximum_distance(number_of_cities=1000, cities_with_train_station=[0, 400]) == 599 #Train station 400 is in city 401! 1000-401=599. 
    assert find_maximum_distance(number_of_cities=9876, cities_with_train_station=[14, 17, 53, 86, 98, 296, 456, 637, 958, 1985, 3546, 5464, 7648, 8346, 8845, 9134, 9645, 9764]) == 1092
    assert find_maximum_distance(number_of_cities=9, cities_with_train_station=[0]) == 8
    assert find_maximum_distance(number_of_cities=7, cities_with_train_station=[0, 6]) == 3
    assert find_maximum_distance(number_of_cities=11, cities_with_train_station=[10]) == 10
    print("ALL TESTS PASSED")

# -*- coding: utf-8 -*-
import hashmap

# create a mapping of state to avvreviatuion
states = hashmap.new()
hashmap.set(states, 'Orengon', 'OR')
hashmap.set(states, 'Florida', 'FL')
hashmap.set(states, 'California', 'CA')
hashmap.set(states, 'New York', 'NY')
hashmap.set(states, 'Michigan', 'MI')

#create a mapping of states and some cities in them
cities = hashmap.new()
hashmap.set(cities, 'CA', 'San Francisco')
hashmap.set(cities, 'MI', 'Detroit')
hashmap.set(cities, 'FL', 'Jacksonvillo')

# add some more cities
hashmap.set(cities, 'NY', 'New York')
hashmap.set(cities, 'OR', 'Portland')

# print out some cities
print '_' * 10
print "NY State has: %" % hashmap.get(cities, 'NY')
print "NY State has: %" % hashmap.get(cities, 'OR')

# print some state
print '_' * 10
print "Michigan's abbreviation is: %s" % hashmap.get(states, 'Michigan')
print "Michigan's abbreviation is: %s" % hashmap.get(states, 'Florida')

# do itby using the state then cities dict
print '_' * 10
print "Michigan has: %s" % hasmap.get(cities, hasmap.get(states, 'Michigan'))
print "Florida has: %s" % hasmap.get(cities, hasmap.get(states, 'Florida'))

#print every state abbreviation
print '_' *10
hashmap.list(states)

# print every city in state
print '_' * 10
hashmap.list(cities)

print '_' * 10
tate = hashmap.get(states,'Texas')

if not state:
    print "Sorry,no Texas."

# default values using ||= with the nil result
# can you do this on one line?
city = hashmap.get(cities, 'TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city

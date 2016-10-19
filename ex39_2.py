#-*- coding:utf-8 -*-

import hashmap

#创建一个映射
states = hashmap.new();
hashmap.set(states,'Oregon','OR')
hashmap.set(states,'Florida','FL')
hashmap.set(states,'California','CA')
hashmap.set(states,'New York','NY')
hashmap.set(states,'Michigan','MI')


cities = hashmap.new()
hashmap.set(cities,'CA','San Francisco')
hashmap.set(cities,'MI','Detroit')
hashmap.set(cities,'FL','Jacksonville')
hashmap.set(cities,'NY','New York')
hashmap.set(cities,'OR','Portland')

print "1",'-' * 10
print "NY State has:",hashmap.get(cities,'NY')
print "OR State has:",hashmap.get(cities,'OR')

print "2",'-' * 10
print "Michigan's abbreviation is:",hashmap.get(states,'Michigan')
print "Florida's abbreviation is:",hashmap.get(states,'Florida')

print "3",'-' * 10
print "Michigan has:",hashmap.get(cities,hashmap.get(states,'Michigan'))
print "Florida has:",hashmap.get(cities,hashmap.get(states,'Florida'))

print "4",'-' * 10
print hashmap.list(states)

print "5",'-' * 10
print hashmap.list(cities)

print "6",'-' * 10
state = hashmap.get(states,'Texas')
if not state:
    print "Sorry,no Texas"

city = hashmap.get(cities,'TX',"Does Not Exit")
print "The city for the state 'TX' is:%s" % city

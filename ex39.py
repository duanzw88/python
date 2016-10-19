#-*- coding:utf-8 -*-

#创建一个映射
states = {
    'Oregon':'OR',
    'Florida':'FL',
    'California':'CA',
    'New York':'NY',
    'Michigan':'MI'
}

cities = {
    'CA':'San Francisco',
    'MI':'Detroit',
    'FL':'Jacksonville'
}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print "1",'-' * 10
print "NY State has:",cities['NY']
print "OR State has:",cities['OR']

print "2",'-' * 10
print "Michigan's abbreviation is:",states['Michigan']
print "Florida's abbreviation is:",states['Florida']

print "3",'-' * 10
print "Michigan has:",cities[states['Michigan']]
print "Florida has:",cities[states['Florida']]

print "4",'-' * 10
for state,abbrev in states.items():
    print "%s is abbrev:%s" %(state,abbrev)

print "5",'-' * 10
for abbrev,city in cities.items():
    print "%s has the city %s" %(abbrev,city)

print "6",'-' * 10
for state,abbrev in states.items():
    print "%s has state is abbreviated %s and has city %s" % (state,abbrev,cities[abbrev])

print "7",'-' * 10
state = states.get('Texas')

if not state:
    print "Sorry,no Texas"

city = cities.get('TX',"Does Not Exit")
print "The city for the state 'TX' is:%s" % city

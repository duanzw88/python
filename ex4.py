#-*- coding:utf-8 -*-
#汽车数量
cars = 100;
#每个汽车的座位
space_in_a_car = 4.0;
# 驾驶员数量
drivers = 30;
# 乘客数量
passengers = 90;
# 没人开的汽车数量
cars_not_driven = cars - drivers
# 可以开的汽车数量
cars_driven = drivers;
# 汽车的人数容量
carpool_capacity = cars_driven * space_in_a_car;
# 平均每个车的乘客
average_passengers_per_car = passengers / cars_driven

print "There are",cars,"cars available"
print "There are only",drivers,"drivers available"
print "There will be",cars_not_driven,"empty cars today"
print "We can transport",carpool_capacity,"people today"
print "We have",passengers,"to carpool today"
print "We need to put about",average_passengers_per_car,"in each car."

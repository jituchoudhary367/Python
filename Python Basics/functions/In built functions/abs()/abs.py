from django.utils.dateparse import postgres_interval_re

v= -454
print("The absolute value of v is",abs(v))

complex_number = (3-4j)
print("the absolute value is :",abs(complex_number))

def Distance(speed,time):
    print("Distance in km:",speed)
    print("time in seconds:",time)
    print(abs(speed*time))

Distance(21,5)

def Time(distance,speed):
    print("the distance is :" , distance)
    print("the speed is :",abs(speed))
    print(abs(distance/speed))

Time(21.5,-25)
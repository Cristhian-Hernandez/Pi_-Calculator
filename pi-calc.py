import math
pie = 0
drange1 = list(range(1,22000,2)) # The bigger the max number, the more accurate this is
drange2 = drange1[1::2]

for i in drange2:  # We don't want repeated digits
    if i in drange1:
        drange1.remove(i)

for i1, i2 in zip(drange1, drange2):  # This is the Pi formula
    pie += (4/i1)-(4/i2)

print("Calculated Pi: ", round(pie,4))  # Only 1st 4 digits are accurate
print("Python's math.pi: ", math.pi)

#20201007
import time

#More time, less space. 
start = time.time()
for i in range(41):
    if ((time.localtime().tm_year + i) % 4 == 0):
        print("Current year: " + str(time.localtime().tm_year + i) + ", a leap year.")
    else:
        print("Current year: " + str(time.localtime().tm_year + i) + ", not a leap year.")
end = time.time()
print("Processing time: " + str(end - start) + "s")
print("---" * 10)

#More space, less time. 
def checkWhetherLeapYear(currentyear):
    if (currentyear % 4 == 0):
        return " ";
    else:
        return " not ";

start = time.time()
for i in  range(time.localtime().tm_year, time.localtime().tm_year + 41):
    print("Current year: " + str(i) + "," + checkWhetherLeapYear(i) +"a leap year.") 
end = time.time()
print("Processing time: " + str(end - start) + "s")

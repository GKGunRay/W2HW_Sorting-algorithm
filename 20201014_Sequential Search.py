#20201014
data = [20, 31 ,50, 17, 16, 36, 19, 8]

def sequentoal_search(data, key):
    for i in data:
        if i == key:
            return str(key)+" is founded.";
    return str(key)+" is not founded."
    

print(sequentoal_search(data, 17))
print(sequentoal_search(data, 6))


names = ['Ramen', 'Rahul', 'Nithin', 'Raghav', 'Rakesh', 'Rahul', 'Ramen']
data = dict()
for name in names:
    data[name] = data.get(name, 0)+1

print("data are ", data)

print("pints the list of keys: ", data.keys())
print("pints the list of keys: ", data.values())

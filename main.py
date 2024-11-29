#declare a list
numBox = []

print(f"The length of an empty list is {len(numBox)}")

numBox.append(56) 
numBox.append(78)
numBox.append(33)
numBox.append(100)
numBox.append(-3)

print(numBox)

for iNum in range(len(numBox)):
    print(f"numBox[{iNum}] = {numBox[iNum]}")

print("Printing the list in rever order")
for iNum in range(len(numBox) - 1, -1, -1):
    print(f"numBox[{iNum}] = {numBox[iNum]}")

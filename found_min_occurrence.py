import operator
input = "aabbccdeeeff"
valueHolder = {}
for c in input:
  if c in valueHolder:
    valueHolder[c] = valueHolder[c] + 1
  else:
    valueHolder[c] = 1
print(min(valueHolder.items(), key=operator.itemgetter(1))[0])


def evenly_divisible():
  index = 1;
  for i in range(1, 20):
    if index % i != 0:
      for j in range(1,20):
        if (index * j) % i == 0:
          index *= j
          break
  return index


print evenly_divisible()


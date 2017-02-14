def multiples_three_five(num):
  multiples = [];
  sum_of_nums = 0;
  for i in range(num):
    if i % 3 == 0 or i % 5 == 0:
      multiples.append(i)
  for x in multiples:
    sum_of_nums += x
  return sum_of_nums

print multiples_three_five(10)
print multiples_three_five(1000)

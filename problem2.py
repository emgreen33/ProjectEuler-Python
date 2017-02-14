def sum_even_fibs(max):
  sum_evens = 0;
  fib_array = [1, 2];
  index = 2;
  while fib_array[-1] < max:
    new_num = fib_array[index-1] + fib_array[index-2]
    fib_array.append(new_num)
    index += 1
  for i in fib_array:
    if i % 2 == 0:
      sum_evens += i
  return sum_evens


print sum_even_fibs(4000000)
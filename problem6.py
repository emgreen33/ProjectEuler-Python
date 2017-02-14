def sum_of_squares(num):
  sum = 0;
  for i in range(1, num+1):
    sum += i * i
  return sum

def square_of_sum(num):
  sum = 0;
  for i in range(1, num+1):
    sum += i
  return sum * sum


def difference(num):
  difference = square_of_sum(num) - sum_of_squares(num)
  return difference

print difference(10)
print difference(100)
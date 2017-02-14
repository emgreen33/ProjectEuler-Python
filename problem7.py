def is_prime(num):
  for i in range(3, num):
    if num % i == 0:
      return False
  return True


def nth_prime(num):
  prime_array = [2];
  i = 3;
  while len(prime_array) <= num:
    if is_prime(i):
      prime_array.append(i)
    i += 1
  return prime_array[-1]

print nth_prime(6)
print nth_prime(10001)
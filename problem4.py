def is_palindrome(x, y):
  if str(x * y)[::-1] == str(x * y):
    return True

def largest_pal(max, min):
  largest = 0;
  for i in range(min, max):
    for j in range(min, max):
      if i * j > largest and is_palindrome(i, j):
        largest = i * j
  return largest

print largest_pal(999, 100)
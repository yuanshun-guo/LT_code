def all_equal(lst):
  print(lst[::2])
  print(lst[:])
  print(lst[1:] == lst[:-1])

all_equal([1, 2, 3, 4, 5, 6]) # False
all_equal([1, 1, 1, 1]) # True
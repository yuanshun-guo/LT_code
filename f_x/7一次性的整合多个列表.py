def flatten(lst):
  return [x for y in lst for x in y]

print(flatten([[1,2,3,4],[5,6,7,8],[5,8,6,11,88,25]])) # [1, 2, 3, 4, 5, 6, 7, 8, 5, 8, 6, 11, 88, 25]
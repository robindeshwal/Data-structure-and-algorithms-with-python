import sys


def test():
  arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
  print(f'arr -> id: {id(arr)}, hex : {hex(id(arr))}')
  for x in arr:
    print(f'number: {x}, id: {id(x)}, hex: {hex(id(x))}', end=" ")
    print(id(0), hex(id(0)))


def maximum_number():
  min_int = -sys.maxsize - 1

  print(min_int)
  print(-2**31)

def extreme_print():
  arr = [1,2,3,4,5,6,7,8]

  start = 0
  end = len(arr)-1

class BitwiseOperator:

  def __init__(self) -> None:
    pass

  def operators(self, a, b):
    print(f"a = {a}, b = {b}")
    print(f"a & b = {a & b}")
    print(f"a | b = {a | b}")
    print(f"a ^ b = {a ^ b}")
    print(f"a << b = {a << b}")
    print(f"a >> b = {a >> b}")

    print(f"a << 1 = {a << 1}")
    print(f"a >> 1 = {a >> 1}")
    print(f"a << 2 = {a << 2}")
    print(f"a >> 2 = {a >> 2}")

  def break_and_continue(self, n):
    for _ in range(n):
      if _ == 2:
        break
      print(_)

    print("Loop ended")

    for _ in range(n):
      if _ == 2:
        continue
        print(f'n: {n}')
      print(_)

  # count no of set bits in a number.
  def count_set_bits(self, n):
    ans = 0
    while n:
      if n & 1:
        ans += 1
      n >>= 1
    print(f'ans : {ans}')


  # Set the kth bit.
  def set_kth_bit(self, n, k):
    value = 1<<k
    result = n | value
    print(result, end="")

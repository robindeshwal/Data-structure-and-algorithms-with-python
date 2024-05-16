class PrimeNumber:

  def __init__(self) -> None:
    pass

  # check number is prime or not.
  def is_prime(self, n):
    result = True
    for i in range(2, n):
      if n % i == 0:
        result = False
    return result

  # prime number from 1 to N.
  def all_prime_numbers(self, n):
    temp = "All prime numbers from 1 to N: "
    for i in range(1, n + 1):
      if self.is_prime(i):
        temp += str(i) + ", "
    print(temp, end="")

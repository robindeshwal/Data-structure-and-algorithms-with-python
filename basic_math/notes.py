import math


class Practice:

  def __init__(self):
    pass

  def prime_numbers(self):
    """
    0 not a prime
    1 not a prime
    smallest prime = 2
    from 2 to n-1 can be prime.
    can be divide by itself only or 1.

    Approches:    
    1. Naive approach
    2. Sqrt approach
    3. sieve of eratosthenes
    4. segmented sieve
    """

    # Naive approach
    def isPrime_naive(number):
      if number <= 1:
        return False
      for i in range(2, number):
        if number % i == 0:
          return 0
      return 1

    def naive(n):
      count = 0
      for i in range(n):
        if isPrime_naive(i):
          count += 1
      return count

    # Sqrt approach.
    def isPrime(self, number):
      if number <= 1:
        return False
      sqrtN = int(math.sqrt(number))
      for i in range(2, sqrtN + 1):
        if number % i == 0:
          return 0
      return 1

    def countPrime_using_sqrt(self, n):

      count = 0
      for i in range(n):
        if self.isPrime(i):
          count += 1
      return count

    # sieve of eratosthenes approach
    def countPrimes(self, n):
      if n <= 1:
        return 0
      isPrime = list(1 for _ in range(n))
      isPrime[0] = isPrime[1] = 0

      for i in range(2, int(n**0.5) + 1):
        if isPrime[i]:
          j = i * i
          while (j < n):
            isPrime[j] = 0
            j += i
      return sum(isPrime)

  def segmented_sieve(self):
    """
    """

    def sieve(n):
      sieve = ""

  def GCDandHCF(self):
    """
    Greasted common divisor
    1. Euclid's algorithm to find GCD.
      gcd(a,b) = gcd(a-b, b) or gcd(a%b, b)

    Higest common factor
    2. LCM(a,b)* gcd(a,b) = a*b
    """
    a = 72
    b = 24

    def gcd_two_number(a, b):

      if a == 0: return b
      if b == 0: return a

      while a > 0 and b > 0:
        if a > b:
          a = a - b
        else:
          b = b - a

      return a if b == 0 else b

    print(gcd_two_number(a, b))

    def lcm_two_number(a, b):
      lcm = (a * b) // gcd_two_number(a, b)
      return lcm

    print(f"LCM : {lcm_two_number(a, b)}")

  def modulo_arthmetic(self):
    """
    1. (a%n) -> [0,...., n-1]
    2. Generally, to avoid overflow while storing interger we do modulo with a large number.
      1. (a+b)%M = a%M + b%M
      2. a%M - b%M = (a-b)%M
      3. ((a%M) %M) %M = a%M
      4. a%M * b%M = (a*b)%M
    """

  def fast_exponentiation(self):
    """
    1. Normal solution to find a^b -> O(b).
    2. Better solution a^b -> O(log b).
    """
    a = 2
    b = 50

    def simple(a, b):
      ans = 1
      for i in range(b):
        ans *= a
      return ans

    # print(simple(a, b))

    def fast(a, b):
      ans = 1
      while b > 0:
        if b & 1:
          ans = ans * a
        a = a * a
        b >>= 1
      return ans

    print(fast(a, b))

  def modulo_exponentiation(self, a, b, M):
    ans = 1
    while b > 0:
      if b & 1:
        ans = (ans * a) % M
      a = (a * a) % M
      b >>= 1
    return ans % M

  def Advance_topics(self):
    """
    1. Pigeon Hole
    2. Catalan number (BST)
    3. Inclusion - Exclusion Principles
    4. Chinese reminder Theorem.
    5. Lucas' theorem
    6. fermat's theoram
    7. probability concepts.
    """

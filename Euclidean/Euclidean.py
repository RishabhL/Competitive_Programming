# RishabhL, Made as part of Competitive Programming
# Functions to work out the GCD and LCM of two numbers, a and b, using the Euclidean Algorithm

def gcd(a, b):
  while b > 0:
    a, b = b, a % b
  return a

def lcm(a, b):
  return (a * b) / gcd(a, b)

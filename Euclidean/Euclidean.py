# Rishabh Luthra, Made as part of Competitive Programming
# Code to work out the GCD and LCM of two numbers, a and b, using Euclidean Algorithm

def gcd(a, b):
  while b > 0:
    r = a % b
    a = b
    b = r
  return a

print(gcd(513, 324))
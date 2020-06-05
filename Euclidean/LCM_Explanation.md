# How can one find the LCM using the Euclidean Algorithm?
In order to find the LCM of two integers, <code>A</code> and <code>B</code>, we will need to use the algorithm that we formulated in the previous explanation of finding the [GCD using the Euclidean Algorithm](GCD_Explanation.md). 
```python
def gcd(a, b):
  while b > 0:
    a, b = b, a % b
  return a
```

There is one property that allows us to find the LCM of a two numbers <code>A</code> and <code>B</code> knowing their product and their gcd. This property / equation to calculate lcm from the gcd and product of two numbers goes as follows:

```
lcm(a, b) = (a * b) / gcd(a, b)
```
# Formulating the Algorithm.
In the previous explanation on finding the [GCD using the Euclidean Algorithm](GCD_Explanation.md), we already formed a function that we can use to find the gcd of two numbers, <code>A</code> and <code>B</code>. Therefore we can use that function, along with one more arithmetic operation to find the product of those two numbers and then divide one by the other to find the lcm.

We start off by the declaring the following function:
```python
def lcm(a, b):
```
All we have to do is add a few lines of code to complete the operations detailed above:
```python
def lcm(a, b):
  product = a * b
  gcd = gcd(a, b)
  lcm = product / gcd
  return lcm
```

Although, again this code will perfectly fine, we are able to condense the code and save a few lines by transforming the code into the following:
```python
def lcm(a, b):
  return (a * b) / gcd(a, b)
```
And here we have finished the code. Do keep in mind that this is dependent on the algorithm we made in the last explanation of finding the [GCD using the Euclidean Algorithm](GCD_Explanation.md).

# Completed Code
```python
def gcd(a, b):
  while b > 0:
    a, b = b, a % b
  return a

def lcm(a, b):
  return (a * b) / gcd(a, b)
```


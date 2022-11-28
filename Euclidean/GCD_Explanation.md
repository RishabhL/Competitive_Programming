# What is the Euclidean Algorithm used for?

The Euclidean Algorithm is an efficient method used to work out the GCD and LCM of 2 integers. The GCD(Greatest Common Divisor) of two or more numbers is the largest number that divides into each of the numbers with no remainder. The LCM(Lowest Common Multiple) of two or more numbers is the smallest positive integer that is evenly divisible by both numbers.

# How does the Euclidean Algorithm work? 
In the examples shown below we are assuming that we are trying to find the Greatest Common Divisor of two numbers, <code>A</code> and <code>B</code>.
There are a few properties that the Euclidean Algorithm is dependent on. The first one being that:
```
gcd(A, 0) = A
```
and
```
gcd(0, B) = B
```
The second one, and perhaps the most important property being:
```
gcd(A, B) = gcd(B, R)
```
Where <code>R</code> is equal to the remainder of <code>A / B</code>. This is also known as <code>A MOD B</code>, and can be found in Python like this, <code>A % B</code>

Knowing this, we can already start to formulate an algorithm. We have an end point; when either <code>A</code> or <code>B</code> becomes <code>0</code>. We know how to reach that end point; By finding <code>A MOD B</code> to get <code>R</code>, and then plugging in <code>B</code> and <code>R</code> back into the function and repeating until we reach the end point described.

# Worked Example
Before diving in and writing an algorithm, it may be worth to have a look at a worked example done by hand, so one can better understand how the algorithm should work.

Finding the GCD of <code>513</code> and <code>324</code>.
```
A = 513
B = 324

513 % 324 = 189

A = 324
B = 189

324 % 189 = 135

A = 189
B = 135

189 % 135 = 54

A = 135
B = 54

135 % 54 = 27

A = 54
B = 27

54 % 27 = 0

A = 27
B = 0.
```
As the end point was either <code>A</code> or <code>B</code> being <code>0</code>, this is where we finish as here <code>B = 0</code>. As a result, the GCD of <code>513</code> and <code>324</code> is <code>27</code>.

# Formulating the Algorithm in Python.
We start of declaring a function which takes in two arguments, <code>A</code> and <code>B</code>, and returns the GCD of these two numbers. As a result, we begin with the following code:
```Python
def gcd(a, b):
  pass
```
We have to then set the end point, i.e. when this function returns the final value. From what we discussed above, it can be seen that the endpoint is when <code>A</code> or <code>B</code> is <code>0</code>. To condense this down further, we can say that the endpoint is when only <code>B</code> = 0. When we reach this endpoint, we want to return <code>A</code>. This develops the algorithm into the following:
```Python
def gcd(a, b):
  while b > 0:
    pass
  return a
```
For now, we have left part where we implement the modulating part as <code>pass</code>. Time to now implement that part of that code. What we want to do is as follows: Get <code>A MOD B</code> and assign it to <code>R</code>, Assign <code>A</code> as <code>B</code> and <code>B</code> as <code>R</code> and repeat. With this in place, the code looks as follows:
```Python
def gcd(a, b):
  while b > 0:
    r = a % b
    a = b
    b = r
  return a
```
Although this code will work absolutely fine, there is one way in which we can save a couple of lines and this is by doing the following:
```Python
def gcd(a, b):
  while b > 0:
    a, b = b, a % b
  return a
```
And here is the completed code. This will return the GCD of <code>A</code> and <code>B</code> using Euclidean's algorithm.
# Completed Code
```Python
def gcd(a, b):
  while b > 0:
    a, b = b, a % b
  return a
```

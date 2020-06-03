# What is the Euclidean Algorithm used for?

The Euclidean Algorithm is and efficient method used to work out the GCD and LCM of 2 integers. The GCD(Greatest Common Divisor) of two or more numbers is the largest number that divides into each of the numbers with no remainder. The LCM(Lowest Common Multiple) of two or more numbers is the smallest positive integer that is evenly divisible by both numbers.

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

Finding the GCD of <code>324</code> and <code>513</code>.
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

As the end point was either A or B being 0, this is where we finish as here B = 0. As a result, the GCD of 513 and 324 is 27.


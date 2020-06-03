# What is the Euclidean Algorithm used for?

The Euclidean Algorithm is and efficient method used to work out the GCD and LCM of 2 integers. The GCD(Greatest Common Divisor) of two or more numbers is the largest number that divides into each of the numbers with no remainder. The LCM(Lowest Common Multiple) of two or more numbers is the smallest positive integer that is evenly divisible by both numbers.

# How does the Euclidean Algorithm work? 
In the examples shown below we are assuming that we are trying to find the Greatest Common Divisor of two numbers, **A** and **B**.
There are a few properties that the Euclidean Algorithm is dependent on. The first one being that:
```
gcd(A, 0) = A
```
and
```
gcd(0, B) = B
```
The second one, and perhaps the most important one being:
```
gcd(A, B) = gcd(B, R)
```
Where <code>R</code> is equal to the remainder of <code>A / B</code>. This is also known as <code>A MOD B</code>, and can be found in Python like this, <code>A % B</code>

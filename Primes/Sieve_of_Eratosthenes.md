# What is the Sieve of Eratosthenes and how does it work?
The Sieve of Eratosthenes is an ancient, yet efficient algorithm to find all primes up to a given limit, <code>N</code>.

It does this by an iterative process of starting with the first prime number, 2, and marking it's multiples as composite - i.e. not prime. It then moves onto the next number that hasn't been marked as composite, marks the number itself as prime and marks all its multipes as composite. This process repeats until the current number we are checking the multiples for, <code>P</code>, does not exceed <code>√N</code>. After this we can return all the values that haven't been marked as composite. 

# Formulating the Algorithm in Python

We begin by initiating a function that will take in <code>N</code> as an argument and perhaps return a list of all integers up to <code>N</code> that are prime. Let's start of by first initiating the function itself:

```python
def sieve_of_erathosthenes(n):
```

We want to begin by assigning a list that will contain the current state of all the numbers from <code>2 to N</code>. We can do this by either first initiating a list of integers from <code>2 to N</code> and removing integers that are composite, keeping only the ones with are prime. We can also do this by creating a list of Booleans that represent the numbers from <code>2 to N</code>. The state of these Booleans will first be all set to <code>True</code>, and we then mark all composites as <code>False</code>.

# What is the Sieve of Eratosthenes and how does it work?
The Sieve of Eratosthenes is an ancient, yet efficient algorithm to find all primes up to a given limit, <code>N</code>.

It does this by an iterative process of starting with the first prime number, 2, and marking it's multiples as composite - i.e. not prime. It then moves onto the next number that hasn't been marked as composite, marks the number itself as prime and marks all its multipes as composite. This process repeats until the current number we are checking the multiples for, <code>P</code>, does not exceed <code>√N</code>

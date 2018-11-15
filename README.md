# Prime Stuff
Generating prime numbers, factoring, and recording them.

## Motication
I want to make my own encrypion function. Since prime numbers are the basis of most modern encryption first I'll need to generate a few and save them for later usage.

## Notes Learned Along the Way
* When factoring primes you need to test i=2 and then from 3 onwards can increment by 2 because testing i=2 already checks all even numbers
* a//b seems to be a bit faster than a/b when doing calculations and in most cases here they can be used interchngeably
* You could generate a number to test to be prime by using a random number generator and say set it to find integers between 100 and 999 if you are looking for 3 digit primes. However, I used random number generators to produce digits 0-9, with constraints that the first digit cannot be 0 and the last cannot be even. Not sure if this is faster/more "random" but I prefer it.


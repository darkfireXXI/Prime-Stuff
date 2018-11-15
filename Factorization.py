import json
import os
import time
import csv
import sys
import math
import numpy as np
import pandas as pd
import random

np.set_printoptions(suppress=True)

maxNumber = 9223372036854775807
# print('{:,}'.format(maxNumber))
# print(len(str(maxNumber))) # 19 digits

def primeFactors(number):
	x = number
	i = 2
	factors = []
	while(x%i == 0):
		x //= i
		factors.append(i)
	i += 1
	while(i*i <= x):
		if(x%i != 0):
			i += 2
		else:
			x //= i
			factors.append(i)
	if(x > 1):
		factors.append(x)

	primes = []
	exponents = []
	for i in range(0, len(factors)):
		if(factors[i] not in primes):
			primes.append(factors[i])
			exponents.append(factors.count(factors[i]))	
	if(sum(exponents) == 1):
		return False
	else:
		primes, exponents = np.array(primes), np.array(exponents)
		check = 1
		for i in range(0, len(primes)):
			check *= (primes[i]**exponents[i])
		if(check != number):
			print('There\'s a problem')
		else:
			factors = np.vstack((primes, exponents))

	return factors

def allFactors(number):
	all_factors = []
	for i in range(2, int(np.sqrt(number))):
		if(number%i == 0):
			all_factors.append(i)
	if(sum(all_factors) == 0):
		return False
	elif(len(all_factors) == 1):
		all_factors.append(int(number/all_factors[0]))
	return all_factors

def randomXdigitGenerator(digits):
	number = ''
	i = 0
	while(i < digits):
		x = random.randint(0, 9)
		# print(x)
		if(i == 0 and x == 0):
			continue
		elif((i == (digits - 1)) and (x%2 == 0 or x == 5)):
			continue
		else:
			number += str(x)
			i += 1
	return int(number)

def findXdigitPrime(digits):
	i = 0
	while True:
		number = randomXdigitGenerator(digits)
		print('{} Trying {} ...'.format(i, number))
		factors = primeFactors(number)
		if(type(factors) == bool):
			return number
		else:
			i += 1

def sortNewPrime(digitsX, primeNumber):
	NOT = ''
	for i in range(0, len(digitsX)):
		if(primeNumber < digitsX[i]):
			digitsX.insert(i, primeNumber)
			break
		elif(primeNumber == digitsX[i]):
			print('This number {} has already been found'.format(primeNumber))
			NOT = 'NOT '
			break
		elif(i == len(digitsX) - 1):
					digitsX.append(primeNumber)
	return digitsX, NOT

def recordPrimes(primeNumber):
	with  open('/Users/XXI/Desktop/0/Stuff/Prime Stuff/Higher_Digit_Primes.txt', 'r', encoding = 'utf16') as primesRecorded:
		lowDigits, highDigits = 16, 19 +1
		XdigitPrime = [[], [], [], []]

		line = primesRecorded.readline()
		for i in range(lowDigits, highDigits):
			if(line == '{} digits\n'.format(i)):
				line = primesRecorded.readline()
				while line:
					if(line != '\n'):
						XdigitPrime[i - lowDigits].append(int(line))
						line = primesRecorded.readline()
					else:
						line = primesRecorded.readline()
						break

		for i in range(lowDigits, highDigits):
			if(len(str(primeNumber)) == i):
				XdigitPrime[i - lowDigits], NOT = sortNewPrime(XdigitPrime[i - lowDigits], primeNumber)

	with open('/Users/XXI/Desktop/0/Stuff/Prime Stuff/Higher_Digit_Primes.txt', 'w', encoding = 'utf16') as newRecorded:
		for i in range(lowDigits, highDigits):
			newRecorded.write('{} digits\n'.format(i))
			for j in range(0, len(XdigitPrime[i - lowDigits])):
				newRecorded.write('{}\n'.format(XdigitPrime[i - lowDigits][j]))
			newRecorded.write('\n')

	print('\n{} - ({} digits) has {}been recorded'.format(primeNumber, len(str(primeNumber)), NOT))



number = 936291500716862867123
# number = randomXdigitGenerator(18)
print('{} - {} digits - {:,}'.format(number, len(str(number)), number))

if(number >= maxNumber):
	print('\nThis number will cause an overflow: calculations not guaranteed to hold accuracy\n')

start_time = time.time()

factors = primeFactors(number)
# all_factors = allFactors(number)

# for i in range(19, 16 - 1, -1):
# 	prime = findXdigitPrime(i)
# 	recordPrimes(prime)

end_time = time.time()

if('factors' in locals()):
	if(type(factors) == bool):
		print('\n{:,} ({} digits) is Prime\n'.format(number, len(str(number))))
	else:
		print('\nFactored {:,} ({} digits) into base primes:\n{}\n'.format(number, len(str(number)), factors))
elif('all_factors' in locals()):
	if(type(all_factors) == bool):
		print('\n{:,} ({} digits) is Prime\n'.format(number, len(str(number))))
	else:
		print('\nAll factors of {:,} ({} digits) up to the square root:\n{}\n'.format(number, len(str(number)), all_factors))
else:
	print('\n{} ({} digits) is Prime - {:,}\n'.format(prime, len(str(prime)), prime))

time = end_time - start_time 
print(time, 'seconds')
print('or')
print(time/60, 'minutes')




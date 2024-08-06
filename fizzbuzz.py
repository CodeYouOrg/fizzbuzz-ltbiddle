import time

start_time = time.time()


numbers = 1

while numbers <= 100:
	if numbers % 3 == 0 and numbers % 5 == 0:
		print('FizzBuzz')
	elif numbers % 3 == 0:
			print('Fizz')
	elif numbers % 5 == 0:
			print('Buzz')
	else:
		print(numbers)
	numbers += 1
end_time = time.time()
		
elapsed_time = end_time - start_time
print('Execution time:', elapsed_time, 'seconds')# add your code here


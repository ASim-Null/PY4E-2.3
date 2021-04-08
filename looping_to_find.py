print('Before')
for thing in [9,41,12,3,74,15]:
    print(thing)
print('After')

#How to find the largest number 

largest_so_far = -1
print('Before', largest_so_far)
for the_num in [9,41,12,3,74,15]:
  if the_num > largest_so_far:
    largest_so_far = the_num
  print(largest_so_far, the_num)
  
  print('After', largest_so_far)
  
  #goes through each of the numbers in turn and compares them.
  
  # finding the smallest number in a loop
  
  smallest = None
  print('Before')
  for value in [9,41,12,3,74,15]:
    if smallest is None:
      smallest = value
    elif value < smallest:
      smallest = value
    print(smallest, value)
  print('After', smallest)
  
  
  #summing in a loop
  
  n = 0 
  print('Before', n)
  for num in [9.41,12,3,74,15]:
    n = n + num
    print(n, num)
 print('After', n)

#goes through and adds them all together. INSTEAD you should use the .sum() function ! so much easier

#finding the average in a loop

count = 0 
sum = 0 

print('Before', count, sum) 
for value in [9,41,12,3,74,15]:
  count = count + 1
  sum = sum + value
  print(count, sum, value) 
print('After', count, sum, sum / count) 


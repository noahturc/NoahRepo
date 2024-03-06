def find_highest(lst):
  highest = lst[0]
  for num in lst:
    if num > highest:
      highest = num
  return highest


def fizz_buzz(num):
  if num is not None:
    if (num%3 == 0) and (num%5 == 0):
      print('FizzBuzz')

    elif num%3 == 0:
      print('Fizz')
    elif num%5 == 0:
      print('Buzz')
    else:
      print(str(num))
  else:
    print('None')

#fizz_buzz(3)

def snakefill(n):

  x = n*n
  snake = 1
  i = 0
  while snake <= x:
    snake *= 2
    i += 1
  return i - 1

#print(snakefill(24))

# converts normal time to 24 hour clock time
def convertTime(time):
  x = time[-2]
  firstTwoDigits = time[:2]
  lastDigits = time[2:]
  if x.upper() == 'A':
    if firstTwoDigits == '12':
      result = '00' + lastDigits 
    else:
      result = time
  
  elif x.upper() == 'P':
    if firstTwoDigits == '12':
      result = time
    else:
      converted = int(firstTwoDigits) + 12
      result = str(converted) + lastDigits 

  else:
    result = 'You supposed to specify PM or AM bruhhh'
   
  return result[:-2]

#print(convertTime('07:05:45PM'))
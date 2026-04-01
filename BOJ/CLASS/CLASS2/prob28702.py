first = input()
second = input()
third = input()

curNum = 0

if first.isdigit():
    curNum = int(first)+3
elif second.isdigit():
    curNum = int(second)+2
elif third.isdigit():
    curNum = int(third)+1
    
if curNum % 3 == 0 and curNum % 5 == 0:
    print('FizzBuzz')
elif curNum % 3 == 0:
    print('Fizz')
elif curNum % 5 == 0:
    print('Buzz')
else:
    print(curNum)
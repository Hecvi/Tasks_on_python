# В математике функция sign(x) (знак числа) определена так:
# sign(x)=1, если x>0,
# sign(x)=-1, если x<0,
# sign(x)=0, если x=0.
# Для данного числа x выведите значение sign(x)

num = int(input())

if num > 0:
    print(1)
elif num < 0:
    print(-1)
else:
    print(0)

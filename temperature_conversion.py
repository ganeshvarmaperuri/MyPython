'''

def tempConversion():
    if n==1:
        f=int(input("Enter Fahrenheit Temperature"))
        print(f)
        c = (f-32)*1.8
        print("Celsius Temperature is ", c)
        return
    elif n==2:
        c = int(input('Enter Celsius Temperature'))
        print(c)
        f = (c*1.8)-32
        print('Fahrenheit Temparature is ', f)
        return
    else:
        print('please select the choice 1 or 2')

print('choice your Temperature conversion')
print('1-> Celsius to Fahrenheit')
print('2-> Fahrenheit to Celsuis')
n = int(input('Enter your choice'))
tempConversion()


'''


class TempConversion:
    print('choice your Temperature conversion')
    print('1-> Celsius to Fahrenheit')
    print('2-> Fahrenheit to Celsuis')
    n = int(input('Enter your choice'))

    @staticmethod
    def main():
        if TempConversion.n == 1:
            f = int(input("Enter Fahrenheit Temperature"))
            print(f)
            c = (f - 32) * 1.8
            print("Celsius Temperature is ", c)
            return
        elif TempConversion.n == 2:
            c = int(input('Enter Celsius Temperature'))
            print(c)
            f = (c * 1.8) - 32
            print('Fahrenheit Temparature is ', f)
            return
        else:
            print('please select the choice 1 or 2')


TempConversion.main()


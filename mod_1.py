print('This is mod_1s name',__name__)

def amazing_sum(number1, number2):
    return(int(number1 + int(number2)))

def demo_amazing_sum():
    print('Welcome to the amazing sum demo!')
    number1 = int(input('What is your first number?'))
    number2 = int(input('What is your second number?'))
    print(amazing_sum(number1, number2))

if __name__ == '__main__':
    print('We are running this file directly')
    demo_amazing_sum()
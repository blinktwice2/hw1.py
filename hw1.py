from math import sqrt
def greeting():
    capture = input("What's your name? ")
    print("Hello %s " % capture)

def number():
    number = input("enter any real number ")
    numberint = int(number)
    print("Your number is", numberint )

def average():
    first = input("enter your first number ")
    firstint = float(first)
    second = input("enter your second number ")
    secondint = float(second)
    third = input("enter your third number ")
    thirdint = float(third)
    average = ((firstint+secondint+thirdint)/3)
    print("the average is", average)
    
def graduate():
    gradyear = input("What's your class year? ")
    gradyearint = int(gradyear)
    yearstogo = gradyearint - 2019
    print("You will graduate from USNA in", yearstogo, "years" )

def sphere( radius ):
    A = (4*3.14)*(radius**2)
    V = (4/3)*(3.14)*(radius**3)
    print( "Surface area is", A," and volume is", V)

def division(divisor, dividend):
    divisor = float(divisor)
    dividend = float(dividend)
    quotient = 0
    while dividend >= divisor: 
        dividend -= divisor
        quotient += 1 
        remainder = dividend 
    print("Quotient is" ,quotient, "and remainder is" ,remainder)

def division_alt(divisor, dividend):
    divisor = int(divisor)
    dividend = int(dividend)
    quotient = 0
    while dividend >= divisor: 
        dividend -= divisor
        quotient += 1 
        remainder = dividend 
    print("Quotient is" ,quotient, "and remainder is" ,remainder)

def feet( inches ):
    feet = inches // 12
    rem = inches % 12 
    print( feet, "feet", rem, "inches" )

def triangle():
    length = input("length of one leg of an isocleles right triangle: ")
    length = float(length)
    hypotenuse = sqrt(2 * (length ** 2))
    print("The length of the hypotenuse is",hypotenuse)

def register(number_Burgers, number_Drinks, number_Fries):
    Burgers = 4 * number_Burgers
    Drinks = 2 * number_Drinks
    Fries = 3 * number_Fries
    Tax = ((Burgers + Drinks + Fries) * (.05)) 
    print(Tax + (Burgers + Drinks + Fries))

def change(dinner_cost):
    cost = float(dinner_cost) * 100
    rem = cost % 5
    rem = int(rem)
    print("You will need to pay", rem, "pennies")

def volume( dim1, dim2, dim3 ):
    volume = dim1 * dim2 * dim3
    print("The volume of your rectangular prism is", volume)
    
def packets ( bits_in_file, bits_in_packet ):
    num_full_packets = bits_in_file // bits_in_packet
    rem_bits = bits_in_file % bits_in_packet
    print( num_full_packets, " packets and ", rem_bits, " bits" )

def exchange( dollars, conversion, target_currency ):
    dollars = float(dollars)
    conversion = float(conversion)
    target_currency = str(target_currency)
    calculated_value = dollars * conversion
    print(dollars, "is equivalent to", calculated_value, "in", target_currency)

def rect_base( length, width ):
    area = length * width
    print(area)
    return area

def pyramid ( length, width, height ):
    volume = rect_base ( length, width ) * ( height )
    print(volume)
    return volume


greeting()
number()
average()
graduate()
sphere(32)
feet(72)
division(3,10)
division_alt(3.5,10)
triangle()
register(1,1,1)
change(3.59)
volume(5,5,5)
exchange(5,1.5,"pounds")
rect_base( 5, 5 )
pyramid(5, 5, 5)


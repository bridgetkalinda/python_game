def my_name():
    print "Bridget"
    print 2 + 2
my_name()

def addtition(x, y):
    print x+ y
addtition(5, 7)
addtition(x=5, y=7)
addtition("Bree ", "Flav")

def add_two_numbers(number1, number2):
    answer = number1 + number2
    print "{} plus {} is equal to {}".format(number1, number2, answer)
add_two_numbers(1, 2)
add_two_numbers(67, 87)

def add_two_numbers_and_return_value(x, y):
    answer = x + y
    return answer 
return_value = add_two_numbers_and_return_value(4, 5)

print return_value

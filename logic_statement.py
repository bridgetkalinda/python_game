is_red = True
is_blue = True
print "Dress is red and blue: {}".format(is_red and is_blue)
print "Dress is red or blue: {}".format(is_red and is_blue)
print "Dress is red and blue: {}".format(not is_red and is_blue)

thing_1 = "book"
thing_2 = "bike"
print "Are a book and bike the same things? {}".format(thing_1 == thing_2)

print "What's your age?"
age = int(raw_input())

if age >= 18 and age < 25:
    print "You get charged extra"
elif age >= 25:
    print "You can rent car"
else:
    print "You cannot rent a car"

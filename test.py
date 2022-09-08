from StringCalculator import *


#-----------------------------TEST CASE 1------------------
def calc_for_empty_string():
    s=StringCalculator()
    ans=s.add("")
    print("Passing empty string for calculation-",ans)


def calc_for_one_char_string():
    s=StringCalculator()
    ans=s.add("6")
    print("Passing one char string for calculation-",ans)


#----------------------------- TEST CASE 2 -------------------------
def calc_for_multiple_char_string():
    s=StringCalculator()
    ans=s.add("1,1,1,1,5")
    print("Passing multiple char string for calculation-",ans)



#----------------------------- TEST CASE 3 -------------------------
def calc_for_string_with_lowercase_alphabates():
    s=StringCalculator()
    ans=s.add("1,1,1,1,b")
    print("Passing multiple char string for calculation-",ans)    


#----------------------------- TEST CASE 4 -------------------------
def calc_for_single_negative_number_string():
    s=StringCalculator()
    ans=s.add("6,-1")
    print("Passing string with single negative number for calculation-",ans)


#----------------------------- TEST CASE 5 -------------------------
def calc_for_multiple_negative_number_string():
    s=StringCalculator()
    ans=s.add("6,-2,-3,-4")
    print("Passing string with multiple negative number for calculation-",ans)  


#----------------------------- TEST CASE 6 -------------------------
def calc_for_number_bigger_than_1000():
    s=StringCalculator()
    ans=s.add("6,10000,1")
    print("Passing string with number bigger than 1000 for calculation-",ans)  


#----------------------------- TEST CASE 7 -------------------------
def calc_for_newline_char_string():
    s=StringCalculator()
    ans=s.add("1,1\n1,1\n5")
    print("Passing string with newkine character for calculation-",ans)



#-------------------------------------------------------------------------------
#Cases for testing

calc_for_empty_string()
print("\n")

calc_for_one_char_string()
print("\n")

calc_for_multiple_char_string()
print("\n")

calc_for_string_with_lowercase_alphabates()
print("\n")

calc_for_number_bigger_than_1000()
print("\n")

calc_for_newline_char_string()
print("\n")

calc_for_single_negative_number_string()
print("\n")

calc_for_multiple_negative_number_string()
print("\n")


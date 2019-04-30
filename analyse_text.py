# count Alpha chars
# count char "e"
# percent of chars are "e" to two decimals

def count_alpha_char(string):
    alpha_count = 0
    for char in string:
        if char.isalpha():
            alpha_count += 1
    return alpha_count

def count_e_char(string):
    e_count = 0
    e = "e"
    cap_e = "E"
    for char in string:
        if char == e or char == cap_e:
            e_count +=1
    return e_count
    
def percent_of_char_is_e(e_count, alpha_count):
    percent = e_count / alpha_count
    percent = percent * 100
    percent = "{:.2f}".format(percent)
    return percent

def analyze_text(text):
    # Your code here
    alpha_count = count_alpha_char(text)

    e_count = count_e_char(text)

    percent = percent_of_char_is_e(e_count, alpha_count)
 
    return (f"The text contains {alpha_count} alphabetic characters, of which {e_count} ({percent}%) are 'e'.")


# Note that depending on whether you use str.format or string concatenation
# your code will pass different tests. As long as your code passes either
# tests 1-3 OR tests 4-6, yo'll be okay. See below for more details.
from test import testEqual

# Tests 1-3: solutions using string concatenation should pass these
text1 = "Eeeee"
answer1 = "The text contains 5 alphabetic characters, of which 5 (100.0%) are 'e'."
testEqual(analyze_text(text1), answer1)

text2 = "Blueberries are tasteee!"
answer2 = "The text contains 21 alphabetic characters, of which 7 (33.3333333333%) are 'e'."
testEqual(analyze_text(text2), answer2)

text3 = "Wright's book, Gadsby, contains a total of 0 of that most common symbol ;)"
answer3 = "The text contains 55 alphabetic characters, of which 0 (0.0%) are 'e'."
testEqual(analyze_text(text3), answer3)

# Tests 4-6: solutions using str.format should pass these
text4 = "Eeeee"
answer4 = "The text contains 5 alphabetic characters, of which 5 (100%) are 'e'."
testEqual(analyze_text(text4), answer4)

text5 = "Blueberries are tasteee!"
answer5 = "The text contains 21 alphabetic characters, of which 7 (33.33333333333333%) are 'e'."
testEqual(analyze_text(text5), answer5)

text6 = "Wright's book, Gadsby, contains a total of 0 of that most common symbol ;)"
answer6 = "The text contains 55 alphabetic characters, of which 0 (0%) are 'e'."
testEqual(analyze_text(text6), answer6)

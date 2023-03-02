
# solving HackerRank problems (python textWrapping)
# Sahed Ahmed Palash
# December 2022, Dhaka

# problem:
# You are given a string S and width W.
# Your task is to wrap the string into a paragraph of width W.
# Function Description: Complete the wrap function in the editor below.
# wrap has the following parameters:
# string: a long string.
# int max_width: the width to wrap to.
# Returns:
# string: a single string with newline characters ('\n') where the breaks should be.
# solution:

# defining the function which will wrap the string
def textWrapper(string, max_width):
    import textwrap
    wrapper = textwrap.TextWrapper(width=max_width)
    word_list = wrapper.wrap(text=string)
    for element in word_list:
        print(element)

# calling the input variable and function
if __name__ == "__main__":
    string = input("write your string here: ")
    max_width = int(input("write line width: "))
    textWrapper(string, max_width)


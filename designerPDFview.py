
# solving HackerRank problems
# Sahed Ahmed Palash
# February 2023, Dhaka

# problem:
# When a contiguous block of text is selected in a PDF viewer,
# the selection is highlighted with a blue rectangle. In this PDF viewer,
# each word is highlighted independently. For example:
# There is a list of  character heights aligned by index to their letters.
# For example, 'a' is at index  and 'z' is at index . There will also be a string.
# Using the letter heights given, determine the area of the rectangle highlight
# in  assuming all letters are  wide.
# solution:

# defining the function which will find the measurement of highlighted text
def designerPDFViewer():
    import string
    word_value = []
    for i in word:
        word_index = string.ascii_lowercase.index(i)
        word_value.append(h[word_index])
    measurement = max(word_value)*1*len(word_value)
    print(measurement)


# calling the designerPDFViewer function as the main
if __name__ == "__main__":
    h = list(map(int, input().rstrip().split()))
    word = input()
    designerPDFViewer()


# solving HackerRank problems
# Sahed Ahmed Palash
# October 2022, Dhaka

# problem:
# In a book, page 1 starts on the right side of the book and then page 2 and 3 to the next page. and
# it follows the same till the last page. last page end on the left side of the book.
# given total page number (n) of a book and a target page (p) in that book.
# find the minimum number of page to be turned to get the target page.
# turn can be done from the first page or even from the last page of the book.
# solution:

# defining the function which will count the page
def page_count(n, p):
    page_in_book = p // 2
    total_pages = n // 2

    from_front = page_in_book
    from_back = total_pages - page_in_book
    print(min(from_front, from_back))


# calling the input variable and function as __main__
if __name__ == '__main__':
    n = int(input().strip())
    p = int(input().strip())
    page_count(n, p)

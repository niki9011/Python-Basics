fav_book = input()
books_count = 0
is_found = False

current_book = input()
while current_book != 'No More Books':
    if current_book == fav_book:
        is_found = True
        break

    books_count += 1
    current_book = input()

if is_found :
    print(f'You checked {books_count} books and found it.')
else:
    print(f'The book you search is not here!')
    print(f'You checked {books_count} books.')



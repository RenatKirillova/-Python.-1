# TODO Найдите количество книг, которое можно разместить на дискете
a = 1.44 #Объем дискеты
b  = 100 #Количество страниц в книге
c = 50 #Число строк на странице
d = 25 #Количество символов в строке
e = 4 #Для хранения кода одного символа нужно

book_size = b * c * d
book_size_bytes = book_size * e
a_byetes  = a * 1024 * 1024
books_on_disk = a_byetes // book_size_bytes
print("Количество книг, помещающихся на дискету:", int(books_on_disk))

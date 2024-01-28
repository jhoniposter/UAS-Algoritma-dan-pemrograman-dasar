""" Program python - Algoritma pencari bilangan biner
----------------------------------------
"""
# implementasi pencarian bilangan biner secara iteratif pada Python
def binary_search(a_list, item):
    # """Melakukan bilangan biner secara iteratif untuk menemukan posisi dari integer pada list yg terurut
    # a_list -- list dari integer yang terurut
    # item -- integer yang anda cari pada posisi tertentu integer 
    first = 0
    last = len(a_list) - 1
    while first <= last:
        i = (first + last) / 2
        if a_list[i] == item:
            return ' ditemukan pada posisi '.format(item=item, i=i)
        elif a_list[i] > item:
            last = i - 1
        elif a_list[i] < item:
            first = i + 1
        else:
            return ' tidak di temukan di dalam list'.format(item=item)
# Implementasi pencarian bilangan biner secara recursive pada Python
def binary_search_recursive(a_list, item):
    # """Melakukan pencarian bilangan biner secara recursive dari integer pada list yang berurutan.
    # a_list -- list dari integer yang terurut
    # item -- integer yang anda cari pada posisi tertentu integer 
    first = 0
    last = len(a_list) - 1
    if len(a_list) == 0:
        return ' tidak di temukan di dalam list'.format(item=item)
    else:
        i = (first + last) // 2
        if item == a_list[i]:
            return ' ditemukan'.format(item=item)
        else:
            if a_list[i] < item:
                return binary_search_recursive(a_list[i+1:], item)
            else:
                return binary_search_recursive(a_list[:i], item)

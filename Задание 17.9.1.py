array = list(map(int, input('Введите числа через пробел:').split()))

def merge_sort(L):
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L) // 2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        return merge(left, right)


def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result

print(merge_sort(array))

while True:
    try:
        element = int(input("Введите число от 1 до 999: "))
        if element < 0 or element > 999:
            raise Exception
        break
    except ValueError:
        print("Нужно ввести число")
    except Exception:
        print("Введите число в рамках диапазона")

sorted_array = merge_sort(array)

def binary_search(sorted_array, element, left, right):
    if left > right:
        return False
    middle = (right + left) // 2
    if sorted_array[middle] < element and sorted_array[middle+1] >= element:
        return middle
    elif element <= sorted_array[middle]:
        return binary_search(sorted_array, element, left, middle - 1)
    else:
        return binary_search(sorted_array, element, middle + 1, right)

if element <= min(sorted_array) or element > max(sorted_array):
    print("Условие задачи не выполняется")
else:
    print(binary_search(sorted_array, element, 0, len(array)))

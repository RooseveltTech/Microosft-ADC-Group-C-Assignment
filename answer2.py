# To Sort this array from middle
def sortArray(arr):
      if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        sortArray(left)
        sortArray(right)
        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
  
        # Checking if any element was left
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
  
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
  
def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    sortArray(arr)
    printList(arr)
sortArray([1,5,3])

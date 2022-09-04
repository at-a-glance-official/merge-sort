# At A Glance! (Yash Ajit Paddalwar)

def merge_sort(arr):
    if len(arr) > 1:
        left_arr = arr[0:len(arr)//2]
        right_arr = arr[len(arr)//2:]

        merge_sort(left_arr)
        merge_sort(right_arr)

        i,j,k = 0,0,0

        while len(left_arr) > i and len(right_arr) > j:
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1
        
        while len(left_arr) > i:
            arr[k] = left_arr[i]
            i += 1
            k += 1
        
        while len(right_arr) > j:
            arr[k] = right_arr[j]
            j += 1
            k += 1

        return arr

arr = [10,32,-1223,838,0,100,1,77,4389,9488,439]
print(merge_sort(arr))

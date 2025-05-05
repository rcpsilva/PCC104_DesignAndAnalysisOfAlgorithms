def find_peak(arr,b,e):

    middle = (b+e) // 2

    if arr[middle] > arr[middle-1]:
        if arr[middle] > arr[middle+1]:
            print(middle)
        else:
            find_peak(arr,middle,e)

    if arr[middle] < arr[middle+1]:
        find_peak(arr,middle-1,e)

    if arr[middle] < arr[middle-1]:
        find_peak(arr,b,middle+1)


if __name__ == '__main__':
    arr = [0,0,1,0,0,0,0,0,0]
    find_peak(arr,0,len(arr))
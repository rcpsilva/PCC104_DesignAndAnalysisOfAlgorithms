def quick_sort(a):
    if len(a) <= 1:
        return a
    pivot = a[-1]
    left = [a[i] for i in range(len(a)) if ((a[i] <= pivot) and (i != len(a)-1))]
    right = [a[i] for i in range(len(a)) if ((a[i] > pivot) and (i != len(a)-1))]

    return quick_sort(left) + [pivot] + quick_sort(right)

if __name__ == "__main__":
    a = [9,1,8,2,7,3,7,4,6,5]

    print(a)
    print(quick_sort(a))
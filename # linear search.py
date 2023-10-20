def linearsearch(arr,x):
    for i in range(len(arr)):
        if arr[i]==x:
            return i
        return -1
    arr=['t','u','t','o','r','i','a','l']
    x='a'
    m=linearsearch(arr,x)
    if(m==-1):
        print("Element is not found in list")
    else:
                print("")
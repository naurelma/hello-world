def lajittelu(arr):
    yht = 0
    for i in range(len(arr)):
        j = i
        #print("="*10)
        while(arr[j] < arr[j-1] and j > 0):
            #print(arr)
            yht +=1
            arr[j],arr[j-1] = arr[j-1], arr[j]
            j -= 1
            #print(arr)
    return arr,yht, (len(arr)**2)/2
            

def right_greater(a):
    for i in range(len(a)):
        large = -1
        for j in range(i+1,len(a),1):
            if a[i]<a[j]:
                large = a[j]
                break  #only if loop breaks with incremenrs of j 
            # print(large)
        print(large)

abc = [1,20,3,10,5]       
right_greater(abc)

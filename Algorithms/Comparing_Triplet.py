def compareTriplets(a, b):
    a_rating_0=0 # initialize to 0
    a_rating_1=0
    a_rating_2=0
    b_rating_0=0
    b_rating_1=0
    b_rating_2=0
    a_rating_all=0
    b_rating_all=0
    if int(a[0]) > int(b[0]):
        a_rating_0+=1
        b_rating_0+=0
    elif int(a[0]) == int(b[0]):
        a_rating_0+=0
        b_rating_0+=0
    else:
        a_rating_0+=0
        b_rating_0+=1
    if int(a[1]) > int(b[1]):
        a_rating_1+=1
        b_rating_1+=0
    elif int(a[1]) == int(b[1]):
        a_rating_1+=0
        b_rating_1+=0
    else:
        a_rating_1+=0
        b_rating_1+=1
    if int(a[2]) > int(b[2]):
        a_rating_2+=1
        b_rating_2+=0
    elif int(a[2]) == int(b[2]):
        a_rating_2+=0
        b_rating_2+=0
    else:
        a_rating_2+=0
        b_rating_2+=1
    a_rating_all=a_rating_0+a_rating_1+a_rating_2
    b_rating_all=b_rating_0+b_rating_1+b_rating_2
    return a_rating_all, b_rating_all

a=[int(i) for i in str(input().strip()).split(' ')]
b=[int(i) for i in str(input().strip()).split(' ')]
result=compareTriplets(a, b)
print(str(result[0])+' '+str(result[1]))
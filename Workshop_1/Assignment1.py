import numpy as np
def square(x):
    """
    This is a demo function
    Where in you just return square of the number
    args:
        x (int)
    returns:
        y (int)
    ex:
        x = 5
        ## then
        y = 25
    """

    # Code Here
    return x**2


def word_is_palindrome(string):
    """
    This function returns True if the given string is
    a Palindrome
    args:
        string (str)
    returns:
        flag (bool)
    ex:
        string = 'abcba'
        ## then
        flag = True
    """

    # Code Here
    s=""
    flag=False
    for i in string:
        s=i+s
    if s==string:
        flag=True
    return flag


def sqrt_of_numbers(num):
    """
    This function returns the magnitude of the square root of the number
    args:
        num (int) Need not be positive
    returns:
        sqroot (float) rounded off upto 2 decimal places.
    ex:
        num = 27
        ## then
        sqroot = 5.20
    """
    if num < 0:
        raise ValueError('Number must be positive')

    # Code Here
    r=np.sqrt(num)
    return round(r,2)


def Maximum(arr):
    """
    This function returns first maximum and the second maximum
    number in the array
    args:
        arr (list)
    returns:
        Max1, Max2 (int, int)
    ex:
        arr = [1, 2, 3, 4, 5]
        ## then
        Max1, Max2 = 5, 4
    """

    # Code Here
    arr.sort()
    return arr[-1], arr[-2]


def even_sort(arr):
    """
    This function sorts the array giving higher preference to even numbers
    args:
        arr (list)
    returns:
        sort_arr (list)
    ex:
        arr = [15, 2, 6, 88, 7]
        ## then
        sort_arr = [2, 6, 88 ,7 ,15]
        ## This is any even number is smaller than any odd number
    """

    # Code Here
    e=[]
    o=[]
    for i in arr:
        if i%2==0:
            e.append(i)
        else :
            o.append(i)
    e.sort()
    o.sort()        
    arr=[]
    for i in e:
        arr.append(i)
    for i in o:
        arr.append(i)
    return arr


def eqn_solver(A, B, C):
    """
    This function solves a two variable system
    i.e.,
        A = [ 1, 2 ]
        B = [ 3, 4 ]
        C = [ 5, 6 ]
        then it means
        1x + 3y = 5
        2x + 4y = 6
        Hence you are required to find x, y for such a linear system
    args:
        A, B, C (list, list, list) representing coefficients in the equation
    returns:
        x, y (float, float)
    """

    # Code Here
    y=float((C[1]-(float(A[1]/A[0])*C[0]))/(B[1]-(float(A[1]/A[0])*B[0])))
    x=float((C[1]-(float(B[1])*y))/A[1])
    return x, y


def swap_case(string):
    """
    This function swaps the case of the string.
    args:
        string (str)
    returns:
        string (str)
    ex:
        string = 'Hello World'
        ## then
        string = 'hELLO wORLD'
    """

    # Code Here
    s=""
    for i in string :
        a=ord(i)
        if (a>64) and (a<91):
            a+=32
            i=chr(a)
        elif (a>96) and (a<123):
            a-=32
            i=chr(a)
        s=s+i
    return s


def is_prime(num):
    """
    This function returns True if the number is prime
    args:
        num (int)
    returns:
        flag (bool)
    """

    # Code Here
    flag=True
    for i in range(2,num):
        if num%i==0:
            flag=False
    return flag


def is_leap_year(year):
    """
    This function returns True if the year is leap year
    args:
        year (int)
    returns:
        flag (bool)
    """

    # Code Here
    flag=False
    if (year%100==0 and year%400==0) or (year%4==0 and year%100!=0):
        flag=True
    return flag


def is_perfect_square(num):
    """
    This function returns True if the number is perfect square i.e. it is a square of some integer.
    args:
        num (int)
    returns:
        flag (bool)
    """

    # Code Here
    x=np.sqrt(num)
    y=round(np.sqrt(num))
    return x==y


def is_perfect_number(num):
    """
    This function returns True if the number is perfect number.
    A perfect number is a positive integer that is equal to the sum of its proper positive divisors.
    For example 6 is a perfect number because 1+2+3 = 6
    args:
        num (int)
    returns:
        flag (bool)
    ex:
        num = 6
        ## then
        flag = True

        num = 7
        ## then
        flag = False
    """

    # Code Here
    s=0
    for i in range(1,num):
        if num%i==0:
            s=s+i
    return s==num


def resize_array(a):
    """
    This function resizes a 1D array to 2D array of size 2x3
    args:
        a (np.array) of size 1x6
    returns:
        b (np.array) of size 2x3
    ex:
        a = np.array([1, 2, 3, 4, 5, 6])
        ## then
        b = np.array([[1, 2, 3], [4, 5, 6]])
    """

    # Code Here
    return np.resize(a,(2,3))


def reverse_step_array(a):
    """
    This function returns the reversed array with step size of 3.
    args:
        a (np.array)
    returns:
        b (np.array)
    ex:
        a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
        ## then
        b = np.array([9, 6, 3])
    """

    # Code Here
    b=np.flip(a)
    a=[]
    for i in range(0,len(b),3):
        a.append(b[i])
    return a


def reverse_words(string):
    """
    This function reverses the words in the string.
    args:
        string (str)
    returns:
        string (str)
    ex:
        string = 'Hello Again World'
        ## then
        string = 'World Again Hello'
    """

    # Code Here
    s=""
    ss=""
    for i in string:
        if i!=' ':
            ss=ss+i
        else:
            s=' '+ss+s
            ss=""
    s=ss+s
    return s


def count_characters(string):
    """
    This function counts the frequency of characters(ignore spaces as characters) in the input string.
    args:
        string (str)
    returns:
        dict (dict)
    ex:
        string = 'Hello World'
        ## then
        dict = {'H': 1, 'e': 1, 'l': 3, 'o': 2, 'W': 1, 'r': 1, 'd': 1}
    """

    # Code Here
    dict={}
    for i in string:
        if (ord(i)>64 and ord(i)<91) or (ord(i)>96 and ord(i)<123) or (ord(i)>47 and ord(i)<58):
            if i in dict.keys():
                dict[i]+=1
            else:
                dict[i]=1

    return dict


def remove_special_characters(string):
    """
    This function removes the special characters from the input string. Special characters are those which are not letters or numbers.
    args:
        string (str)
    returns:
        string (str)
    ex:
        str = 'Hello, World! 123$ th15 1s 4 t35t str1ng'
        ## then
        str = 'Hello World 123 th15 1s 4 t35t str1ng'
    """

    # Code Here
    s=""
    for i in string:
        if (ord(i)>64 and ord(i)<91) or (ord(i)>96 and ord(i)<123) or (ord(i)>47 and ord(i)<58) or i==' ':
            s=s+i
    return s


def sort_tuple_of_tuples(input_tuple):
    """
    This function sorts the input tuple of tuples by the second item.
    args:
        input_tuple (tuple)
    returns:
        input_tuple (tuple)
    ex:
        input_tuple: (('a', 55), ('z', 1), ('f', 37), ('w', 19))
        ## then
        input_tuple: (('z', 1), ('w', 19), ('f', 37), ('a', 55))
    """

    # Code Here
    tup=list(input_tuple)
    l=len(tup)
    for i in range(0,l):
        for j in range(0,l-i-1):
            if tup[i]:
                if tup[j][1]>tup[j+1][1]:
                    temp = tup[j]
                    tup[j] = tup[j + 1]
                    tup[j + 1] = temp
    return tuple(tup)


def alpha_numeric_words(string):
    """
    This function finds words with both alphabets and numbers from an input string.
    args:
        string (str)
    returns:
        string (str)
    ex:
        string: "Hey there33 how11 are you1"
        ## then
        string: "there33 how11 you1"
    """

    # Code Here
    s=""
    ss=""
    a=0
    n=0
    for i in string:
        if i!=' ':
            ss=ss+i
            if (ord(i)>64 and ord(i)<91) or (ord(i)>96 and ord(i)<123):
                a+=1
            elif ord(i)>47 and ord(i)<58:
                n+=1
        else:
            if a>0 and n>0:
                s=s+ss+' '
            a=0
            n=0
            ss=""
    if a>0 and n>0:
        s=s+ss
    return s


def count_them_all(string):
    """
    This function counts all letters, digits, and special symbols from an input string.
    args:
        string (str)
    returns:
        dict (dict)
    ex:
        string: "IdDk3837#$fsd%%"
        ## then
        dict: {'Characters': 7, 'Numbers': 4, 'Symbols': 4}
    """

    # Code Here
    a=0
    n=0
    s=0
    for i in string:
        if (ord(i)>64 and ord(i)<91) or (ord(i)>96 and ord(i)<123):
            a+=1
        elif ord(i)>47 and ord(i)<58:
            n+=1
        elif i!=' ':
            s+=1
    dict={'Characters': a, 'Numbers': n, 'Symbols': s}      
    return dict


def hash_supremacy(string):
    """
    This function replaces each special symbol with '#' in the input string.
    args:
        string (str)
    returns:
        string (str)
    ex:
        string: "&He was a^%$ great @guy"
        ## then
        string: "#He was a### great #guy"
    """

    # Code Here
    s=""
    for i in string:
        if (ord(i)>64 and ord(i)<91) or (ord(i)>96 and ord(i)<123) or (ord(i)>47 and ord(i)<58) or i==' ':
            s=s+i
        else:
            s=s+'#'
    return s

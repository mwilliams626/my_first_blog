MAX = 6
'''
Author: Maya Shende
Date: 6/28/2017
Girls Who Code SIP
'''
# input: two numbers
# output: subtracts if num1 > num2, adds otherwise
def numbers(num1, num2): #num1 = 1, num2 = 1
    if (num1 > num2): # false
        print(num1 > num2)
        print(str(num1)+'>'+str(num2)+' is true')
        return_val = num1 - num2
    else:
        print(num1 > num2)
        print(str(num1)+'<='+str(num2)+' is true')
        return_val = num1 + num2
    return return_val # return 2

if __name__ == '__main__':
    # test case 1
    # expected output: 7
    first = 3
    second = 4
    value = numbers(first, second) # 7
    print (value)
    # test case 2
    # expected output: 2
    first = 7
    second = 5
    value = numbers(first, second) # 2
    print (value)
    # test case 3
    #expected output: 2
    first = 1
    second = 1
    value = numbers (first, second) # 2
    print(value)

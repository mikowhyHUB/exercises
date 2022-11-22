#Write a program in Python that asks the user to enter an integer n and display the value of the sum 1 + 2 + ... + n =

def value_of_sum():
    num = int(input())
    sum_of_num = 0
    for i in range(0, num+1):
        sum_of_num+=i
    print(sum_of_num)
    
value_of_sum()
def square_of_number(num):
    return num**2

numbers=[4,5,2,9]
squares=list(map(square_of_number,numbers))
print('Square the elements of the list:',squares)


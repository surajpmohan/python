#Program explains function declaration and usage.
def day_difference(day1, day2):
    '''Accept two days between 1 and 365 and returns the difference between\
    them.'''
    return day2 - day1
print("Enter two days")
day1 = int(input())
day2 = int(input())
print("Difference is: ",day_difference(day1,day2))


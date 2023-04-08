#  If the number is positive, increase it to 1, else decrease it to 2.
def task_1(x):
    """
    If the number is positive, increase it to 1, else decrease it to 2.

    args:
        x: int
    return:
        int
    """
    if x>=0:
        x = x+1
    if x<0:
        x = x-2
    return x
print(task_1(1))
 


    

    
    

# Example:
# task_1(1) -> 1
# task_1(-4) -> -2  

def task_2(x):
    """
    If the number is positive, increase it to 1, 
    if the number is negative, decrease it to 2,
    if the number is 0, leave it unchanged.
    Args:
        x: int

    Returns:
        int
    """
    if x>0:
        x=x+1
    if x<0:
        x=x-2
    if x==0:
        x=0
    return x
print(task_2(0))

# Example:
# task_2(1) -> 2
# task_2(-4) -> -6
# task_2(0) -> 0

def task_3(x):
    """
    If the number is positive, increase it to 1,
    if the number is negative, decrease it to 2,
    if the number is 0, return 10.
    Args:
        x: int
    return:
        int
    """
    if x>0:
        x=x+1
    if x<0:
        x=-2
    if x==0:
        x=10
    return x
print(task_3(1))


# Example:
# task_3(1) -> 1
# task_3(-4) -> -2
# task_3(0) -> 10

def task_4(a,b,c):
    """
    Find the sum of the positive numbers.
    Args:
        a: int
        b: int
        c: int
    return:
        int
    """
    if a>=0:
        a=a
    if b>=0:
        a=a+b
    if c>=0:
        a=a+c

        
    return a
print(task_4(1,2,3))

# Example:
# task_4(1,2,3) -> 6
# task_4(-1,2,3) -> 5
# task_4(-1,-2,3) -> 3

def task_5(a,b,c):
    """
    Find how many positive numbers are there.
    Args:
        a: int
        b: int
        c: int
    return:
        int


    """
    if a>=0:
        a=1
    if b>=0:
        a=a+1
    if c>=0:
        a=a+1

    return a
print(task_5(1,2,3))

# Example:
# task_5(1,2,3) -> 3
# task_5(-1,2,3) -> 2
# task_5(-1,-2,3) -> 1


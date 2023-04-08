def find_max(a,b,c):
    """
    Find the maximum number.
    Args:

        a: int
        b: int
        c: int
    return:
        int
    """
    # import math
    # if a==a:
    #     a=math,max(a,b,c)
    if a<c>b:
        a=c
    if a<b>c:
        a=b
    if b<a>c:
        a=a

    return a
print(find_max(1,12,3))

# Example:
# find_max(1,2,3) -> 3
# find_max(-1,12,3) -> 12

def find_max_idx(a,b,c):
    """
    Find the index of the maximum number.
    Args:
        a: int
        b: int
        c: int
    return:
        int
    """
    if b<a>c:
        a=0
    if a<b>c:
        a=1
    if a<c>b:
        a=2

    return a
print(find_max_idx(1,4,3))

# Example:
# find_max_idx(10,2,13) -> 3
# find_max_idx(-1,12,3) -> 2
# finding prime numberas
def eratosfen(number):
    nums = []
    for i in range(2,number+1):
        nums.append(i)
    for i in range(2,number+1):
        for j in range(2*i,number+1,i):
            if j in nums:
                nums.remove(j)
    return nums



if __name__ == '__main__':
    print(f'Please enter the number')
    n = int(input())
    print(f'Prime numbers to {n}: {eratosfen(n)}')
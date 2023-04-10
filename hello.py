print("Hello Python ! \n")

def sum(n) :
    max = n
    total = 0
    for i in range(max):
        total += i
    return total

num = 10
ret = 0
if __name__ == "__main__" :
   ret = sum (num)

print("sum = ", ret)
print("The end of custom branch testing")

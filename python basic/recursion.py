# n = 4
# product = 1
# for i in range(n) :
#     product = product *(i+1)
# print(product)

# def factorial_inter(n):
#     product = 1
#     for i in range(n) :
#         product = product *(i+1)
#     return product

# print(factorial_inter(5))

# def factorial_inter(n):
#     product = 1
#     for i in range(n) :
#         product = product *(i+1)
#     return product

def factorial_recursive(n):
    if n == 1 or n == 0:
        return 1
    return n*factorial_recursive(n - 1)

f = factorial_recursive(0)
print(f)
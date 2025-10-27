#
# def devolver_distintos(*args):
#
#     total = sum(args)
#
#     if total > 15:
#         return max(args)
#     elif total < 10:
#         return min(args)
#     elif 10<= total <= 15:
#         return sorted(args)[1]
#
#
#
# res = devolver_distintos(1,4,6)
# print(res)

#EJERCICIO 2

# def mi_funcion(palabra):
#
#     lista = list(palabra)
#     lista.sort()
#     return lista
#
# print(mi_funcion('tres'))


#EJERCICIO 3
#
# def validate_func(*args):
#
#  nums = list(args)
#  for a,b in zip(nums, nums[1:]):
#     vali_flag = True
#      if a == b:
#          vali_flag = False
#          return vali_flag
#     return vali_flag

# def validate_func(*args):
#     #nums = list(args)
#     #vali_flag = False
#     for a,b in zip(args, args[1:]):
#         if a==0 and a==b:
#             #vali_flag=True
#             return True
#     return  False
#
#
# print(validate_func(1,0,0,2,2,3))

def contar_primos(num):

    if num == 1:
        return 'El numero 1 no se considera primo'

    nums = list(range(2,num+1))

    for n in nums:
        if :




print(contar_primos(1))
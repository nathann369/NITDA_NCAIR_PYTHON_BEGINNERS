#                                  ERRORS

# UNCOMMENT TO ACCESS CODE
# UNCOMMENT TO ACCESS CODE
# UNCOMMENT TO ACCESS CODE
# UNCOMMENT TO ACCESS CODE  one section at a time  if possible 
# ------------------------------------------------------------------------------

# AttributeError: occors when you try to use a . notation on something that doesnt exiA
#
# class car:
#     def __init__(self, brand: str, year: int) -> None:
#         self.barnd = brand
#         self.year = year

# bmw: car = car(brand="BMW", year=2025)
# print(bmw.brand)
# print(bmw.year)
# print(bmw.color) : this is an attribute error


# ------------------------------------------------------------------------------

# ImportError: occors what you try to import a module that doesnt exist in that module
#
# import os
# from os import bob : this is known as a module or import error


# ------------------------------------------------------------------------------

# IndexError: when you try to access a non-existing index
#
# def test2():
#     names: list[str] = ['bob', 'lob']
#     nums: tuple[int, ...] = (1,2,3,4)

#     print(names[2]) this is an index error
#     print(nums[5])

# test2()

# ------------------------------------------------------------------------------


# KeyError: when trying to access a key that does not exist
#
# def test3():
#     data: dict[str, str] = {
#         'name': 'BIG YAO',
#         'nationality': 'Libarian',
#         'location': 'Abuja',
#         'job': 'Gammer'
#     }

#     print(data['name'])
#     print(data.get['satary', '$10k'])
#     print(data['salalry']) this is a key error

# test3()

# ------------------------------------------------------------------------------


# NameError: when you try accessing an attribute that was never defined

# print(score) this was never defined



# ------------------------------------------------------------------------------


# NotImplementedError: this error is a user made where that user or dev might want to remind themself of something using this error
# def scarap_website(url: str) -> dict:
#     raise NotImplementedError("I havent made this function yet")

# scarap_website('www.linkedin.com')


# ------------------------------------------------------------------------------


# StopIterationError:

# from typing import Generator

# def num_genarator()-> Generator[int, None, None]:
#     for i in range(2):
#         yield i
# my_gen: Generator[int, None, None] = num_genarator()
# print(next(my_gen))
# print(next(my_gen))
# print(next(my_gen))


# ------------------------------------------------------------------------------


# SyntaxError: mostly due to typo and might be user caused

# print('hello'  not putting the closing braces will casue this kind of error 


# ------------------------------------------------------------------------------


# IndentationError: caused due to non python style indentation 

# for i in range(2):
# print(i)


# ------------------------------------------------------------------------------


# ValueError: when user trys to insert a value that does not correspond with the datatype iiish

# print(int('one'))
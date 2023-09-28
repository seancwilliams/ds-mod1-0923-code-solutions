#1. bool_to_int


bool_to_int = lambda value: 1 if value == True else (0 if isinstance(value, bool) else "not c/bool!")
print(bool_to_int("False"))

#2. get_smaller

get_smaller = lambda a,b: a if a < b else b
print(get_smaller(13, 22))

#3. cube

def cube(base):
  return base ** 3

print(cube(3))

#4. absolute_difference

def absolute_difference(a,b):
  return abs(a - b)
print(absolute_difference(14,11))

#5. squared_difference

def squared_difference(a,b):
  return ((a - b) ** 2)
print(squared_difference(14,11))

#6. hours_to_minutes
def hours_to_minutes(hours):
  return hours * 60
print(hours_to_minutes(hours = 3.5))

#7. get_circumference
def get_circumference(radius):
  return 6.283185307179586 * radius
print(get_circumference(radius = 9.2))

#8. linear_transform
def linear_transform(x, slope, intercept):
  return ((x * slope) + (intercept))
print((linear_transform(x = 5, slope = 3, intercept = -8.5)))

#9 standardize
def standardize(x, x_center, scale_size):
  return ((x - x_center) / abs(scale_size))
print(standardize(x=8.2, x_center=13.8, scale_size=4.83))

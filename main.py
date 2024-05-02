if __name__ == "__main__":
  # Tuple unpacking

  x, y = 10, 20

  print(x)
  print(y)

  def add(x, y):
    return x + y

  print(add(10, 20))

  x, y, *z = 10, 20, 30, 40
  print(x)
  print(y)
  print(z)

  def add(x, y, *args):
    total = x + y

    for arg in args:
      total += arg

    return total

  print(add(10, 20, 30, 40))

  # Introduction to the Python *args parameter

  def add(*args):
    total = 0
    for number in args:
      total += number
    return total

  print(add(1, 2, 3))

  # Python *args argument exhausts positional arguments

  def add(x, y, *args, z):
    return x + y + sum(args) + z

  # add(10, 20, 30, 40, 50))
  # TypeError

  print(add(10, 20, 30, 40, z = 50))

  # Unpacking arguments

  def point(x, y):
    return f"({x}, {y})"

  a = (0, 0)
  # point(a)
  # TypeError

  print(point(*a))

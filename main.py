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

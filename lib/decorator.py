
def print_before(func):
  def wrapper(*args, **kwargs):
    print()
    print(f'{func.__name__}: ')
    return func(*args, **kwargs)
  return wrapper
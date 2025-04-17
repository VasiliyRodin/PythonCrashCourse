def count_fits(number, divisor):
  """
  Calculates how many times the divisor fits into the number.

  Args:
    number: The number to be divided.
    divisor: The number to divide by.

  Returns:
    The number of times the divisor fits into the number.
  """
  if divisor == 0:
    raise ZeroDivisionError("Divisor cannot be zero.")
  return number // divisor

# Example usage:
number = 17
divisor = 3.1
result = count_fits(number, divisor)
print(f"{divisor} fits into {number} {result} times.")

number = 10
divisor = 2
result = count_fits(number, divisor)
print(f"{divisor} fits into {number} {result} times.")

number = 5
divisor = 7
result = count_fits(number, divisor)
print(f"{divisor} fits into {number} {result} times.")
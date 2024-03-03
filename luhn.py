def luhn10(string_of_numbers):
  string_of_numbers_reversed = string_of_numbers[::-1]

  odd_digits = string_of_numbers_reversed[::2]
  sum_of_odd_digits = 0
  for digit in odd_digits:
    sum_of_odd_digits += int(digit)
  
  even_digits = string_of_numbers_reversed[1::2]
  sum_of_even_digits = 0
  for digit in even_digits:
    number = int(digit) * 2
    if number >= 10:
      number = (number // 10) + (number % 10)
    sum_of_even_digits += number
  
  total_sum = sum_of_odd_digits + sum_of_even_digits

  return total_sum % 10 == 0
    
def luhn10_compute_check_digit(string_of_numbers):
  string_of_numbers_reversed = string_of_numbers[::-1]

  odd_digits = string_of_numbers_reversed[::2]
  sum_of_odd_digits = 0
  for digit in odd_digits:
    number = int(digit) * 2
    if number >= 10:
      number = number // 10 + number % 10
    sum_of_odd_digits += number

  even_digits = string_of_numbers_reversed[1::2]
  sum_of_even_digits = 0
  for digit in even_digits:
    sum_of_even_digits += int(digit)

  total_sum = sum_of_odd_digits + sum_of_even_digits

  return (10 - (total_sum % 10)) % 10

def luhn10_validate_check_digit(string_of_numbers):
  payload = string_of_numbers[:-1]
  check_digit = string_of_numbers[-1:-2:-1]
  return luhn10_compute_check_digit(payload) == int(check_digit)

def main():
  print(luhn10('17893729974'))
  print(luhn10_compute_check_digit('1789372997'))
  print(luhn10_validate_check_digit('17893729974'))

  card_number = '4211-1111-4555-1141'
  card_translation = str.maketrans({'-': '', ' ': ''})
  translated_card_number = card_number.translate(card_translation)

  if luhn10(translated_card_number):
    print('VALID!')
  else:
     print('INVALID!')
    
main()

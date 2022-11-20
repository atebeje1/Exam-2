from collections import Counter

# Count lexemes of file
def countLexemes(file):
  out = 1 # Accounts for next line character
  for line in file:
    line = line.split(' ')
    for lexum in line:
      out += 1
  return '# of lexums: {}'.format(out)

# Counts lines of file
def countLines(file):
  return '# of lines: {}'.format(len(file))

# Gets id of token
def getID(token):
  try:
    int(token)
    return 1
  except:
    if token == '(':
      return 2
    if token == ')':
      return 3
    if token == '*':
      return 4
    if token == '/':
      return 5
    if token == '%':
      return 6
    if token == '+':
      return 7
    if token == '-':
      return 8

# Solves any given expression
def solve(expression):
  arr = expression.split()
  while len(arr) > 0:
    # Handler for parentheses
    assert Counter(expression).get('(') == Counter(expression).get(')'), 'Too many or missing parentheses.'
    if getID(arr[0]) == 2:
      expression2 = ''
      while True:
        print(True)
        expression2 += x
        if getID(expression2[-1]) == 3:
          break
      arr[0] = solve(expression2)
    
    num1 = arr.pop(0)
        
    #Handler for multiplication
    print(arr[0])
    if getID(arr[0]) == 4:
      print(arr.pop(0), 'removed,', arr)
      arr[0] = eval(num1) * eval(arr[0])
  return arr[0]

print(solve('3 * 2'))
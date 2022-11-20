import os
import re

# char type 1 byte
# short type 2 bytes
# num type is 4 bytes
# lnum is 8 byte

def solve(expression):
  expression = expression.replace('(', '( ')
  expression = expression.replace(')', ' )')
  arr = expression.split(' ')
  terms = []
  operators = []
  while len(arr) > 1:
    try:
      int(arr[0])
      terms.append(arr.pop())
      print(terms)
    except:
      operators.append(arr.pop())
    if operators[-1] == '*' or operators[-1] == '/' or operators[-1] == '%':
      operation = operators.pop()
      if operation == '*':
        arr[0] = terms.pop() * terms.pop()
      elif operation =='/':
        arr[0] = terms.pop() / terms.pop()
      elif operation == '%':
        arr[0] = terms.pop() % terms.pop()
  print(arr)
  if len(arr) == 1:
    return arr[0]
  else:
    assert len(arr) % 2 == 1, 'Unable to evaluate expression.'
  

def analyze(line, file):
  variables = {}

  
  
  # Variable initialization / assignment operators
  
  # Handler for char type
  if line.startswith('letter'):
    # Verifies semicolon at end of line then removes for parsing
    assert line.endswith(';\n'), 'Missing semicolon.'
    line = line[:line.index(';')]

    arr = line.split(' ')

    # Verifies variable name is valid
    assert re.match('[A-Za-z_]{6,8}', arr[1]).string == re.match('[A-Za-z_]{6,8}', arr[1]).group(), 'Invalid variable name.'

    if len(arr) > 2:
      # Verifies presence of assignment operator
      assert arr[2] == '=', 'Missing or out of place assignment operator.'

      # Verifies string formatting
      assert arr[3][0] == '\'' and arr[3][2] == '\'', 'String format error.'
      
      variables[arr[1]] = str(arr[3])[1]
    else:
      variables[arr[1]] = NotImplemented
  
  # Handler for int type
  elif line.startswith('num'):
    # Verifies semicolon at end of line then removes for parsing
    assert line.endswith(';\n'), 'Missing semicolon.'
    line = line[:line.index(';')]

    arr = line.split(' ')

    # Verifies variable name is valid
    assert re.match('[A-Za-z_]{6,8}', arr[1]).string == re.match('[A-Za-z_]{6,8}', arr[1]).group(), 'Invalid variable name.'

    # Checks if variable initialized with a value
    if len(arr) > 2:
      assert line[2] == '=', 'Missing or out of place assignment operator'
      variables[arr[1]] = int(arr[3])
    else:
      variables[arr[1]] = NotImplemented

  elif line.startswith('lnum'):
    # Verifies semicolon at end of line then removes for parsing
    assert line.endswith(';\n'), 'Missing semicolon.'
    line = line[:line.index(';')]

    arr = line.split(' ')

    # Verifies variable name is valid
    assert re.match('[A-Za-z_]{6,8}', arr[1]).string == re.match('[A-Za-z_]{6,8}', arr[1]).group(), 'Invalid variable name.'

    # Checks if variable initialized with a value
    if len(arr) > 2:
      assert arr[2] == '=', 'Missing or out of place assignment operator'
      variables[arr[1]] = float(arr[3])
    else:
      variables[arr[1]] = NotImplemented

  # Handler for if statements
  elif line.startswith('met'):
    condition = True
    assert line.endswith(':'), 'Missing code block.'
    line = line[:line.index(':')]

    arr = line.split(' ')
    arr.pop(0)

    index = 0
    while True:
      termParsed = re.match('[<>!=]', arr[1]).group() != ''
      if termParsed:
        arr[index] = solve(arr[index])
        if index == 0:
          index = 2
        else:
          break
      else:
        arr[index] += arr.pop(index + 1)
        continue
    if arr[1] == '<=':
      condition = (arr[0] <= arr[2])
    elif arr[1] == '>=':
      condition = (arr[0] >= arr[2])
    elif arr[1] == '==':
      condition = (arr[0] == arr[2])
    elif arr[1] == '!=':
      condition = (arr[0] != arr[2])
    print(condition)
    # while re.match('[<>!=]', arr[1]).group()

  print(variables)

# Looks through current directory for .abel files
dir = os.listdir()
src = []
for x in dir:
  if x.endswith('.abel'):
    src.append(x)

for x in src:
  file = open(x, 'r')
  for y in file.readlines():
    analyze(y, file)
from itertools import product
def add(a,b):
    return a+b
def mul(a,b):
        return a*b
def con(a,b):
        return str(a) + str(b)
operators = {'+':add, '*': mul, '||': con}

def combinations(numberofspaces, part=1):
    operators_list = ['+', '*'] if part == 1 else ['+', '*', '||']
    return list(product(operators_list, repeat=numberofspaces))
     
def part(input_text, part=1):
     ans = 0
     for i in input_text.splitlines():
          total, numbers = i.split(':')
          numbers = numbers.strip().split() 
          spaces = len(numbers) - 1 
          for ops in combinations(spaces, part):
              result = numbers[0]
              for i, op in enumerate(ops):
                  next_num = numbers[i + 1]
                  if op == '||':
                      result = operators[op](result, next_num) 
                  else:
                      result = operators[op](int(result), int(next_num))
              if(int(result)==int(total)):
                  ans = ans + int(total)
                  break
     return ans

with open('/Users/.../Advent-Of-Code/2024/input.txt') as f:
    input_text = f.read()

print(part(input_text, 1))
print(part(input_text, 2))
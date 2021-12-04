# part 2
def compute(input):
  aim = 0
  dep = 0
  hor = 0
  for line in input:
    i = line.split(" ")
    unit = int(i[1])
    if i[0] == "up":
      aim -= unit
    if i[0] == "down":
      aim += unit
    if i[0] == "forward":
      hor += unit
      dep += aim * unit
  return dep * hor

with open('input.txt', 'r') as file:
    data = file.read().split('\n')

print(compute(data))
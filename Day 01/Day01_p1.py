import re

file = "./"+ __file__.split('\\')[-1].split('.')[0]+"/input.txt"
finalTotal = 0
input = []

def parse():
    with open(file) as f:
        for line in f:
            if False:
                input.extend(re.split("",line.strip()))
            elif False:
                input.append(int(line.strip()))
            else:
                input.append(line.strip())

def part1():
    
    print(0)

def part2():
    
    print(0)

if __name__ == '__main__':
    try:
        parse()
    except:
        pass
    part1()
    part2()
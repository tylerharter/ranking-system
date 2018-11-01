
list = []

candidates = input("Please input all the candidates' names: ")
candidates = candidates.split(" ")
candidates.sort()

with open("votes.txt") as f:
    for line in f:
        line = line.strip()
        line = line.split(">")
        for i in range(len(line)):
            line[i] = line[i].split("=")
        list.append(line)

dict = {}

def compare(x, y):
    count = 0
    for vote in list:
        for ix in range(len(vote)):
            if x in vote[ix]:
                break
        for iy in range(len(vote)):
            if y in vote[iy]:
                break
        if ix < iy:
            count += 1
        elif ix > iy:
            count -= 1
    if x not in dict:
        dict[x] = [count]
    else:
        dict[x].append(count)
    if y not in dict:
        dict[y] = [-count]
    else:
        dict[y].append(-count)

for cand1 in candidates:
    for cand2 in candidates:
        if cand2 > cand1:
            compare(cand1, cand2)

for cand in dict:
    lose = 0
    for item in dict[cand]:
        if item < 0 or item == 0:
            lose -= 1
            break
    if lose == 0:
        print("Condorcet Winner is " + cand)
        exit()

print("There is no Condorcet winner.")
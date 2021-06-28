def preCreatePAttern(pattern):
    i = 0
    position = [1]*len(pattern)
    for val in pattern:
        if val == "_":
            position[i]= 0
        i = i+1
    return position

def hash(pattern,position):
    i=0
    strength=0
    for val in pattern:
        if position[i] == 1:
            strength = strength + ord(val)*i
        else:
            strength = strength +1
        i=i+1
    return strength

def search(text,pattern):

    position = preCreatePAttern(pattern)

    strengthpat = hash(pattern,position)
    m = len(text)
    n = len(pattern)
    position1=0
    for x in position:
        if x == 0:
            position1 = position1+1
        else:

            break
    i=0
    while i < m :
        if (i == m-n):
            break
        elif (pattern[position1] == text[i+position1]):
            temparray = text[i:i+n]
            strength1 = hash(temparray,position)
            if strength1 == strengthpat:
                f = open("output.output","a")
                f.write("pattern found index ")
                f.write(str(i+1))
                f.write(" ")
                tex = text[i:i+n]
                f.write(tex)
                f.write("\n")
                f.close()
                
        i=i+1

file1 = open('text1.txt', 'r',encoding="utf-8")
lines = file1.readlines()
k =0

file2 = open("pattern1.txt","r",encoding="utf-8")
pattern = file2.readline()
f = open("output.output", "w")
f.truncate()
f.close()
for line in lines:
    k=k+1
    f = open("output.output","a")
    f.write("\n\n\tRow ")
    f.write(str(k))
    f.write("\n")
    f.write(line)
    f.close()
    search(line,pattern)

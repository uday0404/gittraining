f = open('poems.txt')
t = f.read()
if 'mahesh' in t:
    print("mahesh is present")
else:
    print("mahesh is not present")
f.close()
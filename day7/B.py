f=open("input.txt","r")
limit=70000000
req=30000000
stack=[]
score={}
it=0

# dfs with stack
for line in f:
	line=line[0:len(line)-1].split(' ')
	if line[0]=='$' and line[1]=='cd':
		if line[2]!='..':
			stack.append(it)
			score[it]=0
			it+=1
		else:
			cur=score[stack.pop()]
			score[stack[-1]]+=cur
		continue
	if line[1]=='ls' or line[0]=='dir':
		continue
	score[stack[-1]]+=int(line[0])

while len(stack)>1:
	cur=score[stack.pop()]
	score[stack[-1]]+=cur
	
dirs=sorted([score[key] for key in score])
delete=req-(limit-dirs[-1])

for size in dirs:
	if size>=delete:
		print(size)
		break
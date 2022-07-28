id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2
report = list(set(report))
user_list = {}
answer = [0]*len(id_list)


for id in id_list:
    user_list[id] = 0
for id in report:
    user_list[id.split()[1]] += 1
print(user_list)

for id in report:
    if user_list[id.split()[1]] >=k:
        answer[id_list.index(id.split()[0])] +=1



print(answer)

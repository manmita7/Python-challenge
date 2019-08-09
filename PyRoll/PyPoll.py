#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os


# In[3]:


import csv


# In[4]:


csvpath = os.path.join('election_data.csv')
print(csvpath)


# In[13]:


with open (csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    my_list = list(csvreader)
    print("Election Results")
    print("--------------------")
    candidates = [pl[2] for pl in my_list]
#print (candidates)

total_votes = len(candidates)
print(f"Total votes: {total_votes}")

unique_candidates =[]

for x in candidates:
    if x not in unique_candidates:
        unique_candidates.append(x)

can1 = str(unique_candidates[0])
can2 = str(unique_candidates[1])
can3 = str(unique_candidates[2])
can4 = str(unique_candidates[3])
can1list = []
can2list = []
can3list = []
can4list = []
        
for y in candidates:
    if y == can1:
        can1list.append(y)
    elif y == can2:
        can2list.append(y)
    elif y == can3:
        can3list.append(y)
    elif y == can4:       
        can4list.append(y)
       
#print(f"{can1list[0]}: votes {len(can1list)}")
#print(f"{can2list[0]}: votes {len(can2list)}")
#print(f"{can3list[0]}: votes {len(can3list)}")
#print(f"{can4list[0]}: votes {len(can4list)}")

p_1 = round(len(can1list) /total_votes *100,2)
p_2 = round(len(can2list) /total_votes *100,2)
p_3 = round(len(can3list) /total_votes *100,2)
p_4 = round(len(can4list) /total_votes *100,2)

#print(p_1)
#print(p_2)
#print(p_3)
#print(p_4)

results =[p_1,p_2,p_3,p_4]
max_results = max(results)
ind = results.index(max_results)
winner = unique_candidates[ind]
#print(f"Winner:{winner}")

print(f"{can1}: {p_1}% ({len(can1list)})")
print(f"{can2}: {p_2}% ({len(can2list)})")
print(f"{can3}: {p_3}% ({len(can3list)})")
print(f"{can4}: {p_4}% ({len(can4list)})")
print(f"Winner:{winner}")

csvpath2 = os.path.join('PyPoll.csv')
with open (csvpath2, "w" , newline = '') as csvfile2:
    csvwriter = csv.writer(csvfile2, delimiter =",")
    csvwriter.writerow ([f"Total votes: {total_votes}",""])
    csvwriter.writerow ([f"{can1}: {p_1}% ({len(can1list)})",""])
    csvwriter.writerow ([f"{can2}: {p_2}% ({len(can2list)})",""])
    csvwriter.writerow ([f"{can3}: {p_3}% ({len(can3list)})",""])
    csvwriter.writerow ([f"{can4}: {p_4}% ({len(can4list)})",""])
    csvwriter.writerow ([f"Winner:{winner}",""])
    
           
    
    


# In[ ]:





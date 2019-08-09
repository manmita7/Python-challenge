#!/usr/bin/env python
# coding: utf-8

# In[3]:


import os
import csv


# In[4]:


csvpath = os.path.join('budget_data.csv')
print(csvpath)


# In[7]:


with open (csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    my_list = list(csvreader) 

pnl = [int(pl[1]) for pl in my_list]
months = [mo[0] for mo in my_list]
#print(months)
total_months = len(months) 
rolling_change = [pnl[i + 1] - pnl[i] for i in range(len(pnl) - 1)]
#print(rolling_change)
avg_pnl = round(sum(rolling_change)/ len(rolling_change),2)
sum_rc = sum(pnl)
g_increase = max(rolling_change)
#print(g_increase)

ind1 = rolling_change.index(g_increase)
#print(ind)
max_month = months[ind1 + 1]
#print(max_month)

g_decrease = min(rolling_change)
ind2 = rolling_change.index(g_decrease)
min_month = months[ind2 + 1]
print("Financial Analysis")
print("---------------------")
print(f"Total Months:{total_months}")
print(f"Total:$ {sum_rc}")
print(f"Average Change: {avg_pnl}")
print(f"Greatest increase in profits:{max_month} ({g_increase})")
print(f"Greatest increase in profits:{min_month} ({g_decrease})")

csvpath2 = os.path.join('PyBank.csv')
with open (csvpath2, "w" , newline = '') as csvfile2:
    csvwriter = csv.writer(csvfile2, delimiter =",")
    csvwriter.writerow (["Financial analysis",""])
    csvwriter.writerow ([f"Total Months:{str(total_months)}",""])
    csvwriter.writerow ([f"Total:$ {sum_rc}",""])
    csvwriter.writerow ([f"Average Change: {avg_pnl}",""])
    csvwriter.writerow ([f"Greatest increase in profits:{max_month} ({g_increase})",""])
    csvwriter.writerow ([f"Greatest increase in profits:{min_month} ({g_decrease})",""])
    
  
    


# In[ ]:





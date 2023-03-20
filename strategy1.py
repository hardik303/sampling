import json
import random


# Load input file
with open('input.json', encoding='utf-8-sig') as f:
    data = json.load(f)


# Process file to nested array
input_data = []
for i in data:
    for key in i:
        input_data.append(i[key])

print(input_data)
N = len(input_data)
S = len(input_data[0])

# Total comparisions = 15*20*20 = 6000
# Target = 30 comparisions of 15 pairs = 450 comparisions
# Goal = 30 comparisions in 15 surveys which are uniformly distributed in each survey as well as globally

# PARAMS
num_survey = 15
num_ques = 30

surveys = []

for i in range(0,num_survey):
    
    survey = []
    while len(survey)<num_ques:
        
        # pick two classes and then sentences from classes
        n1 = random.randint(0,N-1)
        n2 = random.randint(0,N-2)
        if n2>=n1:
            n2+=1
        s1 = random.choice(input_data[n1])
        s2 = random.choice(input_data[n2])
        if (s1,s2) not in survey and (s2,s1) not in survey: survey.append((s1,s2))
    surveys.append(survey)

print(surveys)


# Printing stats
stats = {} # - per survey
global_stats = {} # - global

# STATS PER SURVEY
for i,s in enumerate(surveys):
    for p,q in s:
        try:
            stats[i][p[0]+q[0]]+=1
            stats[i][q[0]+p[0]]+=1
        except:
            try:
                stats[i][p[0]+q[0]]=1
                stats[i][q[0]+p[0]]=1
            except:
                stats[i]={}
                stats[i][p[0]+q[0]]=1
                stats[i][q[0]+p[0]]=1

# GLOBAL STATS
for i,s in enumerate(surveys):
    for p,q in s:
        try:
            global_stats[p[0]+q[0]]+=1
            global_stats[q[0]+p[0]]+=1
        except:
            global_stats[p[0]+q[0]]=1
            global_stats[q[0]+p[0]]=1

# PRINT GLOBAL STATS
for n1 in ['A','B','C','D','E','F']:
    for n2 in ['A','B','C','D','E','F']:
        if n1>=n2:continue
        print(n1+n2,global_stats[n1+n2])   

# PRINT STATS PER SURVEY
for i in range(0,num_survey):
    print("SURVEY :",i," \n\n")
    for n1 in ['A','B','C','D','E','F']:
        for n2 in ['A','B','C','D','E','F']:
            if n1>=n2:continue
            try:
                print(n1+n2,stats[i][n1+n2])
            except:
                print(n1+n2,0)

#EXPORT TO JSON

out_data = {}

for survey_num in range(0,num_survey):
    out_data[survey_num] = surveys[i]

with open("output.json", "w") as f:
    json.dump(out_data, f)
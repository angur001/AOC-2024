from functools import cmp_to_key


f = open("input.txt", "r")
lines = f.readlines()
f.close()

rules = lines[:1176]
reports = lines[1177:]
reports = [report.strip().split(",") for report in reports]



def get_element_in_middle(arr):
    return int(arr[len(arr) // 2])

def create_dict(arr):
    # Create a dictionary with the key as report and value of array of reports that come after it
    dict = {}
    for i in range(len(arr)):
        a,b = arr[i].strip().split("|")
        if a not in dict:
            dict[a] = [b]
        else:
            dict[a].append(b)

    return dict

def validate_report(report, dict):
    for i in range(len(report)):
        for j in range(i+1, len(report)):
            if report[j] not in dict[report[i]]:
                return False
            
    return True

reference = create_dict(rules)

def compare(a, b):
    if b in reference[a]:
        return 1 
    else:
        return -1 

sum = 0
for report in reports:
    if not(validate_report(report, reference)):
        sorted_report = sorted(report, key=cmp_to_key(compare))
        sum += get_element_in_middle(sorted_report)
print(sum)
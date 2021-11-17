import csv

def countOcc(list, target):
    count = 0
    for i in list:
        if i == target:
            count += 1
    return count


# parse data
f = open('data')

data = f.readlines()

for i in range(len(data) - 1):
  data[i] = data[i][:-1]

for i in range(len(data)):
  data[i] = data[i].split(' ')


# translate data into map
d = {}

for i in range(len(data)):
  for j in range(len(data[i])):
    if data[i][j] not in d:
      d[data[i][j]] = []

      for k in range(len(data)):
        if data[i][j] in data[k]:
          for l in range(len(data[k])):
            if data[k][l] != data[i][j]:
              d[data[i][j]].append(data[k][l])


# convert map into integer frequency table
d2 = {}

for key in d:
  d2[key] = {}

  for i in d[key]:
    d2[key][i] = countOcc(d[key], i)




# format data for csv
fields = ['Source', 'Target', 'Weight']

rows = []

for key in d2:
  for i in d2[key]:
    temp = []
    temp.append(key)
    temp.append(i)
    temp.append(d2[key][i])
    rows.append(temp)


# write csv
with open("emoji_data.csv", 'w') as csvfile:
  csvwriter = csv.writer(csvfile)
  csvwriter.writerow(fields)
  csvwriter.writerows(rows)


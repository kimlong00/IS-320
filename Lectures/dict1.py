taxpayers = {} #key: name  value: [income, married, tax]
#income = value[0]
#married = value[1]
#tax = value[2]

#Dictionaries
countries = {}
countries['USA'] = 'DC' #key, value pair. USA is key, DC is the value
countries['France'] = 'Paris'
# print(countries)

# print(countries.keys())
# print(countries.values())
# print(countries.items())

for key in countries.keys(): #use this only if you need keys. Remeber: with keys, values can be found
    print(key, countries[key])

for value in countries.values(): #use this if you only need values
    print(value)

countries['USA'] = 'Washington DC'

# print(countries)
#the key is unique

students = {} #key: name    value: score
students['Alex'] = [85,'A']
students['Ben'] = [70,'B']

for name in students.keys():
    valuelist = students[name]
    score = valuelist[0]
    grade = valuelist[1]
    print(name, score, grade)
    #print(key, valuelist[0], valuelist[1])

for value in students.values():
    score = value[0]
    grade = value[1]
    print(score, grade)



#lists
# inlist = ['Joe', '10000', '1']
# name = inlist[0]
# income = float(inlist[1])
# married = int(inlist[2])

# print(name, income, married)
# for index, value in enumerate(inlist):
#     print(index, value, type(value))
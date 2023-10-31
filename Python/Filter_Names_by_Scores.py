# Use a list comprehension to create a list of names passed
# that only include those that scored at least 65.

scores = {
             "Rick Sanchez": 70,
             "Morty Smith": 35,
             "Summer Smith": 82,
             "Jerry Smith": 23,
             "Beth Smith": 98
          }

# write your list comprehension here

passed = [i for i in scores if scores[i] >= 65]
print(passed)
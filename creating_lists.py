#lists

colors = ['red', 'yellow', 'blue', 'green']
print (colors)

#first on list is 0, second is 2...
print (colors[0])

print (colors[1])

print (colors[2].title())

#-1 prints last on list
print (colors[-1])

#-2 prints the 2nd to last on the list, -3 is 3rd to last...
print (colors[-3])

#uses f string
message = f"The bear from the Jungle Book is {colors[2].title()}."
print(message)


names = ['brooks', 'rae', 'jay', 'micah', 'logan', 'paul']
print(names)

message = f"Greetings, {names[4].title()}!"
print(message)

#replace name 1 w/ 'paul' instead of 'brooks'
names[0] = 'paul'
print(names)

# replace last item on list w/ 'brooks'
names[-1] = 'brooks'
print(names)

#append = add it to the end
names.append('rango')
print(names)

last_names1 = ['errigo', 'fauver', 'haney', 'baird', 'ryle', 'munns']
print(last_names1)

#insert = asign to location
last_names = []
print(last_names)
last_names.append('errigo')
last_names.append('fauver')
last_names.insert(2, 'haney')
last_names.append('baird')
last_names.insert(4, 'ryle')
last_names.append('munns')
last_names.append('munns but lizard')
print(last_names)

#del deletes from list according to location
#use del if you want to delete it and not use it again
del last_names[-1]
print(last_names)

# pop =  deletes last item (or other specified specified) from the list and isolate it
#use pop if you want to delete it and use it again
animals = ['bird', 'dog', 'cat', 'rabbit', 'horse']
print(animals)
popped_animals = animals.pop()
print(animals)
print(popped_animals)

sizes = ['large', 'medium', 'small', 'tiny']
print(sizes)
smallest = sizes.pop()
print(sizes)
print(smallest)

print(f"the smallest size available is {smallest.title()}")

print(sizes)


#you can use pop to isolate any item in a list
biggest = sizes.pop(0)
print(f"the biggest size available is {biggest.title()}")

#use remove method to delete based on value
body_parts = ['head', 'shoulders', 'knees', 'toes', 'brain cell']
print(body_parts)

body_parts.remove('brain cell')
print(body_parts)

body_parts.append('brain cell')

#provide reason for remove
print(body_parts)

consumed_by_brainrot = 'brain cell'
body_parts.remove(consumed_by_brainrot)
print(body_parts)

#\n = new line, \t = tab/indent
print(f"\n\tA {consumed_by_brainrot.title()} was consumed by brainrot\n")



tasks = ["laundry", "dishes", "sweep", "homework", "shower", "workout"]
print(tasks)

#sorting lists alphabetically permanently
tasks.sort()
print(tasks)

#sorting lists reverse alphabetically permanently
tasks.sort(reverse=True)
#True must be uppercase T
print(tasks)

#sorting lists temporarily w/ sorted() function
#sorted function = dislpay list in specific order, but doesn't change permanently
print("Here is the original list:")
print(tasks)

print("Here is the sorted list")
print(sorted(tasks))

print("here is the original list again")
print(tasks)

#reverse the order of a list (print list in reverse order)
MCR_albums = ["welcome to the black parade", "three cheers for sweet revenge", "danger days"]
print(MCR_albums)
MCR_albums.reverse()
print(MCR_albums)

#len() function = find length of list
#do this in python interpretor
pets = ["cat", "dog", "fish", "lizard", "horse", "bird", "rodent"]
len(pets)

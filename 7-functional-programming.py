'''
Functional Programming

Functional programming is all about separation of concerns; OOP does this as well. 

It's all about packaging our code into separate chunks so that everything's well organized in each part of our code. And each part is organized in a way that makes sense based on functionality. 

So when we say separation of concerns, we mean each part concerned with self with one thing that it's good at. 

Functional programming uses the idea of separating concerns but it also separates data and functions. That's how a functional programmer views the world. Instead of combining methods and attributes, we separate them up because they're two separate things. 

There's data - it gets interacted with and acted upon. But we're not going to combine both data and functions as one piece in an object like we see with OOP. 

There is no correct definition for what is and isn't functional. But generally, functional languages have an emphasis on simplicity where data and functions are concerned. This is because in most functional programming paradigms, we don't have this idea of classes and objects. Instead, functions operate on well-defined data structures like lists and dictionaries rather than 'belonging' that data structure to an object. 

Goals of Both OOP & Functional Programming
1. Clear + Understandable
2. Easy to Extend
3. Easy to Maintain
4. Memory Efficient
5. DRY

When it comes to Functional Programming, we have a very important pillar. In OOP, we had those 4 pillars (encapsulation, abstraction, inheritance, and polymorphism). 

If you want to break things down in FP, it all comes down to this concept of pure functions. The idea here is that there is a separation between data of a program and the behavior of a program. 

In OOP, we kind of had a box that held all those objects with its functionalities. With Pure Functions, it's just a simple function. Whatever input we put into the PF, we expect that the output results in the same thing every time. 

Two Rules of a Pure Function:
1. Given the same input, it will always return the same output. That is, every time we give x,y,z in a list and give it to the function that we create, it returns a,b,c every single time. So if we run the function millions of times with the same input, it should result in the same output always.
2. A function should NOT produce any side effects. Side effects are things that a function does that affects the outside world of that function. For example, if the function prints something, it affects the outside world. We're printing something onto a screen, and the screen is the outside world to the function. 

'''


# This passes both tests because the print is NOT inside the function
def multiply_by2(li):
	new_list = []
	for item in li:
		new_list.append(item*2)
	return new_list

print(multiply_by2([1,2,3]))

# Does NOT pass both tests because the print inside the function affects the outside world. If you place new_list outside of the function, it will have side effects from other functions as well. 
def subtract_by2(li):
	new_list = []
	for item in li:
		new_list.append(item-2)
	return print(new_list)

subtract_by2([3,4,5])


wizard = {
    'name': 'Merlin',
    'power': 50
}

def attack(character):
    new_list = []
    for item in character:
        new_list.append(item * 2)
    return new_list

# At the end of the day, it's all about trying to keep our code clean and avoiding bugs in our code. 



### map(), filter(), zip(), and reduce()

#### MAP ####

# Map actually allows us to simplify the code we have of multiply_by2. With Map, we have it available as a built-in function and we see that the first parameter a function. Then the second parameter is an iterable. A good way to think about it is we want to take some sort of action here (the function) and the data that we want to take action upon. 


def multiply_by3(li):
	new_list = []
	for item in li:
		new_list.append(item * 3)
	return new_list

print(map(multiply_by3, [4,5,6]))

# In the terminal, it will print out the exact memory location ( <map object at 0x000001F81CCD5C70> ) and map automatically gives us this object that it has created in this memory. So in order for us to actually view it, we have to turn it into a list!

#print(list(map(multiply_by3, [4,5,6]))) ### RETURNS ERROR

# Just adding a list around map, gives us an error that the Int is not iterable. That's because we no longer need to create a list inside our function. So instead of having all that previous code, we just return the item by 3. Don't forget to change the li param to item

def multiply_by3_again(item):
	return item * 3

print(list(map(multiply_by3_again, [4,5,6])))

# With the map function, we're saying "hey, run this function multiply_by3_again." Notice we don't use parens after the function name. It's because we don't need to call it. Map does it for us. We're not calling the function, Map is. 

# We're just saying "Hey, when I call Map like this, I want you to use this function at this memory address and then use this data from the 2nd param." 

# Remember our functional programming paradigm. We have data that gets acted upon (multiply_by3_again), so we separate those 2 out. Now, the function is going to take each one of the items in our iterables (2nd param), In our case, the first time around 'item' will be 4, then 5, then 6. And then all we need to do is return what effect we want to have on that item. In our case, it's 5. 

# So by doing this, Map automatically runs this function for us and loops through all the items in the iterable and returns for us a new Map Object that we're going to convert into a list. If I run this, I get 12,15,18. 

# Now here's the neat part. If I do a named list and then make it the 2nd param, and also print my_list, you'll see that my_list hasn't changed when you run the program. Remember, a pure function is a function that doesn't affect the outside world.  

# And this way, Map allows us to create a whole new list that doesn't modify my_list so my_list is immutable. We don't change it and all it does is the Map function takes care of it and returns a new list for us but we don't affect the outside world. There are no side effects in this function. We're simply just multiplying item to item by 3 but creating a new list out of this. And everytime we give it the same input, it's going to result in the same output. 

# Map is extremely useful because anytime we have something that we can iterate over and we want to change - let's say we have emails or usernames and we need to update the usernames to be all caps. In that case, we can iterate and using the map function, change all the usernames in our list to capital letters. 


my_list = [4,5,6]
def multiply_by3_again_again(item):
    return item * 3

print(list(map(multiply_by3_again_again, my_list)))
print(my_list)



#### FILTER ####
# Filter returns a Boolean value

# If we want to check if a number is odd, we can say item modulo 2. Modulo 2 is going to divide the number by 2 and if it equals zero, then it's determined to be even. To make sure you're checking that it is NOT even, add the not operator into it

# Notice that we're not calling a function because filter accepts a function or what we call a 'function signature' that looks for the memory space to go to and make an action. 


filter_list = [1,2,3,4,5,6,7,8,9]
#this is a pure function since it doesn't modify the original list
def only_odd(item):
	return item % 2 != 0 

print(list(filter(only_odd, my_list))) #returns only the odd numbers
print(list(filter(only_odd, filter_list))) #returns only the odd numbers

# Filter is going to read the data from 'filter_list' and then run the only_odd function on each item in the list. Basically, the 1 in the filter_list becomes 'item' that is passed into the only_odd function. Since 1 is odd, it gets added to the new list that we create. When we get to 2 though, it's going to return false and it will NOT join 1 in the list again. The process repeats until all the Odds are in this filtered list. 


#### ZIP ####
# The zip() kind of works like a zipper (lol). We need 2 lists (or, 2 iterables) and we can zip them together. We can git zip as many iterables as we want, but for our purposes, we'll just use 2.

zip_list = [1,2,3]
zip_list2 = [10,20,30]
zip_list3_tuple = (100, 200, 300)

print(list(zip(zip_list, zip_list2))) # Returns [(1, 10), (2, 20), (3, 30)]

# Zip takes the 2 iterables, grabs the first item from each and "zips" them together to make a Tuple. Then it goes to the next item from each and zips those. So forth and so on. 

print(list(zip(zip_list, zip_list3_tuple))) # Returns [(1, 100), (2, 200), (3, 300)]
# If you have a list in one and a tuple in the other, it does NOT matter. They will still get zipped. 

# Zip is actually a VERY IMPORTANT FUNCTION. Because it's so generic, zip() can be used in so many different things. For example, in a database, if we collected all the usernames from one column in the database & then from another part of the DB we collect all the phone numbers and they were all in the same order, we can combine these into a Tuple using zip() that has the username and phone numbers attached to them & create a whole new data structure. 

username = ['amber', 'francesca', 'nick']
phone = [8009912421, 8006842598, 8009916543]
location = ['atlanta', 'venice', 'seattle']

print(list(zip(username, location, phone)))
# Returns [('amber', 'atlanta', 8009912421), ('francesca', 'venice', 8006842598), ('nick', 'seattle', 8009916543)]

# AGAIN, zip iterates over each one of these lists or data structures and zips them together. And once again, notice that we are not modifying any of our current data. Instead, we create a whole, new one. Zip is a pure function.


#### REDUCE ####

# Reduce does NOT come as part of the Python built-in functions. In order to use reduce, we have to import it from functools. Essentially, what's happening here is when we downloaded the Python Interpreter (PIP) and the Python package, we can import something from these functools.

# Functools are what we call a tool belt that we can use for functional tools that comes with the python installation. From there, there is a specific function that we can import. 

# We're saying, 'hey, from functools - from this toolbelt - I want you to import the reduce function so that I can use it in my code.'

# With reduce, we're going to need a few things first. First, we need the function and then we need the sequence (the data). 

from functools import reduce

my_list2 = [9,8,7]

# Once I've added my_list2, the reduce function lets us do something interesting. I can give it a function, accumulator, that will take 2 params. 

# Remember, the accumulator is going to get called by reduce. Reduce is going to be in charge of giving these 2 params from the data that we give it (my_list2). The first param is going to be what we call the accumulator (or in our case, the 'acc') and the 2nd is the current 'item' from my_list2. 

# When we first pass my_list2 from the reduce, we'll get the first 'item'. This first 'item' will be the 'item' in the parameter. However, what is the 'acc' initially? In reduce, we have the function, the sequence (in our case is our list), and then the initial. An initial is what the accumulator is going to be. We're giving it an initial value of 0. 

# accumulator defaults to zero if we DON'T give it an initial. The item starts with the first item in the list we supplied.

# We need to remove the list function, because the reduce will produce an 'int' error otherwise. 

def accumulator(acc, item):
	print(acc, item)
	return acc + item


print(reduce(accumulator, my_list2, 0))

# Returns: 
# 0 9 (a + b = c)
# 9 8 (c + d = e)
# 17 7 (e + f = g)
# 24 (g)

### VIDEO 4:40 ###
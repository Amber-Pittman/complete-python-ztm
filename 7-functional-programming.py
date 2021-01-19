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
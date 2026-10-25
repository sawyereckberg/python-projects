import re

test_settings = {
    'key1': 'value1',
    'key2': 'value2',
    'key3': 'value3'
}

'''
'key1': 'value1',
    'key2': 'value2',
    'key3': 'value3'

'''



"""
add_setting function:
what does the function do?
accepts two parameters: a dictionary of settings and a tuple containing a key_value pair.
the tuple containing a key-value pair is the settings that are being added.
The dictionary is where the settings are being added to.
So you're using this function to define where the settings are going and what settings are being added. 
We need to validate these parameters first to make sure the first is a dictionary and the second is a tuple with a key-value pair.
Lets call the first paramater test_settings and the second added_settings for now. 
This validation will work for every function.
Maybe you don't actually need this validation. We'll keep it commented out for now. 
So the add_setting function takes a place to store the settings, and a key value pair of the settings we want to add. 
The first thing we want to do is convert both key and value to lowercase. 
The .lower() method should be good
First we need to full the key from this tuple.
The parameter will be like this (<key>, <value>)
How can we access the key from a tuple? Furthermore we'll have to change the data type likely since tuples are immutable. 
How can we access the tuple and change each value at index 0 and 1, then change to lowercase?
There we go, now key and value are both lowercase strings so they are mutable.

Now, we want to check if the key settings exists. If it does, we want to print the statement 
"Setting '[key]' already exists! Cannot add a new setting with this name."
In order to do this, we're going to have to access the current dictionary and use the in operator. 
How can we access the current dictionary? We use the in operator with the first parameter. 
Then, for the else clause, we access the dictionary using the access syntax: dictionary[key] = value.
We define the given print statement as well to satisfy those requirements.
This function is looking pretty good, let's move on to the next. 

"""
def add_setting(test_settings, added_settings):
    added_settings_list = list(added_settings)
    key = added_settings_list[0].lower()
    value = added_settings_list[1].lower()

    if key in test_settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        test_settings[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!"
#print(add_setting(dictionary, ('SETTING1', 'SETTING2')))

'''
update_setting function:
The parameters of this function will be the same as the add_setting function.
The function accepts where the settings are being updated (test_settings) and the settings that are being updated (updated_settings).
updated_settings will be a tuple with a key-value pair.
We can borrow our logic from the add settings function to convert the key and value to lowercase.
Next, we have to check if the key exists in the settings dictionary. 
We can do this, again, by using the in operator combined with the first parameter.
If the key is in the test_settings parameter, we need to update its value to the provided value in the second parameter.
That function looks good, lets move to the next.
'''

def update_setting(test_settings, updated_settings):
    updated_settings_list = list(updated_settings)
    key= updated_settings_list[0].lower()
    value = updated_settings_list[1].lower()

    if key in test_settings:
        test_settings[key] = value
        return f"Setting '{key}' updated to '{value} successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."
        

#print(update_setting(test_settings, ('SETTING1', '67')))
#print(test_settings)
'''
Now we need a delete_setting function. This function accepts the same two parameters as the first two.
For this function, we can also borrow the lowercase logic.
There we go, now we have mutable list to work with. 
If the key setting does exist in the dictionary, we want to remove the key and value from the dictionary and return the given message. 
So, how are we going to delete these settings? It doesn't look like the pop method is working, but don't count it out yet. 
Let's back it up. 
We're turning the second parameter into a mutable list, and defining key and value variables as the first and second values of the tuple.
So in the if statement, the first thing we're doing is checking if the key that needs to be deleted exists in the settings dictionary. This should be fine.
When we want to remove the key and value, it has to be a list. 

'''

def delete_setting(test_settings, deleted_settings):
    deleted_settings_list = list(deleted_settings)
    key = deleted_settings_list[0].lower()
    value = deleted_settings_list[1].lower()

    if key in test_settings:
        del test_settings[key]
        return f"Setting '{key}' deleted successfully!"
    else:
        return f"Setting not found!"

#print(delete_setting(test_settings, ('setting1', 'setting2')))

'''
The parameter of this function is an actual written dictionary.
if no settings are in the dictionary (if not test_settings), print 'No settings available.'
if there are settings in the dictionary:
print a string that starts with 'Current User Settings:'
followed by key1: value1,
key2: value2,
key3: value3
Start with an empty list called settings_list = []
We could loop through each element in the dictionary:
for key, value in test_settings
Then we can append the key and value to the list.
Once the list is created, we can use a print statement starting with the string
Then use the join function but instead of ' '.join() it would be ': '.join()
get more specific
We want to create a list of key value pairs. Then print it in a very specific way. 
The way we want to print it is to concatenate a sentence.
Now, we need to make the first letter of each key uppercase. We can use the .capitalize() method to do this.
'''

def view_settings(test_settings):
    if not test_settings:
        print('No settings available.')
    else:
        settings_list = []
        for key, value in test_settings.items():
            settings_list.append(f"{key.capitalize()}: {value}")
        return f"Current User Settings:\n" + "\n".join(settings_list)
        
        
        
        


print(view_settings(test_settings))

#{'theme': 'dark', 'notifications': 'enabled', 'volume': 'high'}

'''
def validate(test_settings, added_settings):

    is_dictionary = isinstance(test_settings, dict)
    is_tuple = (added_settings, tuple)
    if not is_dictionary:
        print('The first paramater must be a dictionary.')
        is_invalid = True
    elif not is_tuple:
        print('The second parameter must be a tuple with a key value pair.')
        is_invalid = True
    else
        is_invalid = False
'''
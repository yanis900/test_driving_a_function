# Function Design Recipe

## 1. Describe the Problem
As a user
So that I can find my tasks among all my notes
I want to check if a line from my notes includes the string `#TODO`.

## 2. Design the Function Signature

```python
#Fucntion name/structure 
def task_list(notes): 
"""

    Parameters: (list all parameters and their types)
        notes: a list of all the lines in the note book 

    Returns: (state the return value and its type)
        If True: return a string that inclues the lines that include todo 
        If False: return 'No items currently to do'

    Side effects: (state any side effects)
        No notes/empty list throws error 
    """
```
## 3. Create Examples as Tests

```python
"""
~Test if it picks it up one todos 
task_list(['#TODO Go Shopping , '#DONE Eat food']) == Here is your TODO list, you have 1 task: #TODO Go Shopping'

~Test if multiple todos are outputted 
task_list(['#TODO Go Shopping' , '#DONE Eat food' '#TODO Put the bins out', '#DONE Go for a walk' , ' #TODO Go to the gym']) == 'Here is your TODO list, you have 3 tasks TODO: #TODO Go Shopping', #TODO Put the bins out, #TODO Go to the gym'.

~Test if input was input initially 
task_list(['#DONE Go Shopping , '#DONE Eat food']) == 'You have nothing TODO. Enjoy your free time!'

~Test if input contains an empty list:
task_list([]) == 'You have not entered any notes'

"""
```
def task_list(notes):
    to_do = "#TODO"
    to_do_items = [i for i in notes if to_do in i]

    to_do_items_length = len(to_do_items)
    
    if notes == []: 
        raise Exception("You have not entered any notes.")
    if to_do_items_length == 1: 
        return f"Here is your TODO list, you have {to_do_items_length} task: {', '.join(to_do_items)}."
    elif to_do_items_length > 1: 
        return f"Here is your TODO list, you have {to_do_items_length} tasks: {', '.join(to_do_items)}."
    elif to_do_items_length == 0: 
        return f"You have nothing TODO. Enjoy your free time!"


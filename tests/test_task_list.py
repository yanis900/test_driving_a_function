import pytest
from lib.task_list import *

def test_task_list_includes_one_todo():
    result = task_list(['#TODO Go Shopping' , '#DONE Eat food'])
    assert result == 'Here is your TODO list, you have 1 task: #TODO Go Shopping.'
    
def test_task_list_includes_multiple_todos():
    result = task_list(['#TODO Go Shopping' , '#DONE Eat food','#TODO Put the bins out', '#DONE Go for a walk' , '#TODO Go to the gym'])
    assert result == 'Here is your TODO list, you have 3 tasks: #TODO Go Shopping, #TODO Put the bins out, #TODO Go to the gym.'
    
def test_task_list_no_todos():
    result = task_list(['#DONE Go Shopping' , '#DONE Eat food'])
    assert result == 'You have nothing TODO. Enjoy your free time!'
    
def test_task_list_empty_input():
    with pytest.raises(Exception) as e:
        task_list([])
    error_message = str(e.value)
    assert error_message == 'You have not entered any notes.'
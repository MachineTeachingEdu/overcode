# Prompt for ChatGPT

'''
So now I want to create the master script of my system:

Create a function, runnable as a script, so that user should input only the problem id (lets call <id>).

Then the function checks the '../problems_data/problem_<id>' directory (note that it doesnt always exist, neither the problems_data directory)

if the problem_<id> dir has a subdir called 'output', then the script should call replace_output_data function (from replace_output_data.py) with the <id> and '../ui' as arguments.
Then it should run the run_interface function from run_interface.py with '../ui' as argument.

if the problem_<id> dir doesnt have a subdir called 'output', but has a subdir called 'data', then the script should:
    - get the function name and save it in a variable (lets call it funcname)
        * it will do that by calling the get_function_name function (from get_function_name.py) with '../problems_data/problem_<id>/data/answer.py' as argument
    - call run_pipeline function (from run_pipeline.py) with base_dir='../problems_data/problem_<id>' and funcname=funcname.
    - then it should call replace_output_data function (from replace_output_data.py) with the <id> and '../ui' as arguments.
    - Then it should run the run_interface function from run_interface.py with '../ui' as argument.

if the problem_<id> dir doesnt have a subdir called 'output' nor 'data', then the script should:
    - call the get_problem_data function (from get_problem_data.py) with the <id> as argument.
    - get the function name and save it in a variable (lets call it funcname)
         * it will do that by calling the get_function_name function (from get_function_name.py) with '../problems_data/problem_<id>/data/answer.py' as argument
    - call run_pipeline function (from run_pipeline.py) with base_dir=../problems_data/problem_<id> and funcname=funcname.
    - then it should call replace_output_data function (from replace_output_data.py) with the <id> and '../ui' as arguments.
    - Then it should run the run_interface function from run_interface.py with '../ui' as argument.
'''

import os
import sys

# Add the root directory to the Python path
root_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(root_dir, 'src'))
sys.path.append(os.path.join(root_dir, 'scripts'))

from scripts.get_function_name import get_function_name
from src.run_pipeline import run_pipeline
from scripts.replace_output_data import replace_output_data
from scripts.run_interface import run_interface
from scripts.get_problem_data import get_problem_data

def run_master_script(problem_id):
    """
    Master script to run Overcode on an existing problem whose ID is given as argument.

    Args:
        problem_id (int): The ID of the problem.

    Returns:
        None
    """

    problems_dir = "problems_data"
    problem_dir = os.path.join(problems_dir, f"problem_{problem_id}")
    data_dir = os.path.join(problem_dir, "data")
    output_dir = os.path.join(problem_dir, "output")
    interface_dir = "ui"

    if not os.path.exists(output_dir):
        if not os.path.exists(data_dir):
            get_problem_data(problem_id, problem_dir)

        funcname = get_function_name(os.path.join(data_dir, "answer.py"))

        run_pipeline(problem_dir, funcname)

    replace_output_data(problem_id, output_dir, os.path.join(interface_dir, "output"))
    run_interface(interface_dir)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        problem_id = int(sys.argv[1])
        run_master_script(problem_id)
    else:
        print("Usage: python master_script.py <problem_id>")



    

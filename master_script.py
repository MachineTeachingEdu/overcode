import os
import sys
import time
import json

# Add the root directory to the Python path
root_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(root_dir, 'src'))
sys.path.append(os.path.join(root_dir, 'scripts'))

from scripts.get_function_name import get_function_name
from src.run_pipeline import run_pipeline
from scripts.replace_output_data import replace_output_data
from scripts.run_interface import run_interface
from scripts.get_problem_data import get_problem_data

def run_master_script(problem_id, interface=True):
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
        master_script_start = time.time()

        if not os.path.exists(data_dir):
            get_problem_data(problem_id, problem_dir)

        funcname = get_function_name(os.path.join(data_dir, "answer.py"))

        overcode_start = time.process_time()
        run_pipeline(problem_dir, funcname)
        overcode_end = time.process_time()

        master_script_end = time.time()

        overcode_time = overcode_end - overcode_start
        master_script_time = master_script_end - master_script_start

        with open(os.path.join(output_dir, "execution_times.json"), "w") as f:
            json.dump({"overcode_time": overcode_time, "master_script_time": master_script_time}, f)

        print(f"Overcode took {overcode_time} seconds to run. (only CPU time)")
        print(f"Master Script took {master_script_time} seconds to run. (CPU + I/O time)")

    if interface:
        replace_output_data(problem_id, output_dir, os.path.join(interface_dir, "output"))
        run_interface(interface_dir)
    
    print(f"Master Script finished running for problem {problem_id}.")

    

if __name__ == "__main__":
    if len(sys.argv) > 1:
        problem_id = int(sys.argv[1])
        run_master_script(problem_id)
    else:
        print("Usage: python master_script.py <problem_id>")



    

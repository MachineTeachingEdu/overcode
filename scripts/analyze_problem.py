# Prompt for ChatGPT

'''
So now I want to create the master script of my system:

The user should input only the problem id (lets call <id>).

Then the script checks the '../problems_data/problem_<id>' directory (note that it doesnt always exist, neither the problems_data directory)

if the problem_<id> dir has a subdir called 'output', then the script should run replace_output_data.py with the <id> as argument.
Then it should run the runServer.sh script(or run_interface.py).

if the problem_<id> dir doesnt have a subdir called 'output', but has a subdir called 'data', then the script should:
    - get the function name and save it in a variable (lets call it funcname)
    - call run_pipeline function (from run_pipeline.py) with base_dir=../problems_data/problem_<id> and funcname=funcname.
    - then it should call replace_output_data function (from replace_output_data.py) with the <id> as argument.
    - Then it should run the runServer.sh script(or run_interface.py).

if the problem_<id> dir doesnt have a subdir called 'output' nor 'data', then the script should:
    - call the get_problem_data function (from get_problem_data.py) with the <id> as argument.
    - get the function name and save it in a variable (lets call it funcname)
    - call run_pipeline function (from run_pipeline.py) with base_dir=../problems_data/problem_<id> and funcname=funcname.
    - then it should call replace_output_data function (from replace_output_data.py) with the <id> as argument.
    - Then it should run the runServer.sh script (or run_interface.py).
'''


    

import sys
import os
from get_answer import get_answer
from get_solutions import get_solutions
from get_testcase import get_testcase

def get_problem_data(problem_id, problem_dir):
    """
    Retrieve data for a given problem ID from the database and store it in a directory.

    Args:
        problem_id (int): The ID of the problem for which data is requested.
        problem_dir (str): The directory where problem data will be stored.

    Returns:
        None

    Raises:
        psycopg2.Error: If an error occurs during the database connection or query execution.

    Notes:
        - The 'db_params.json' file should contain the necessary parameters for the PostgreSQL connection.
        - The 'get_answer', 'get_solutions', and 'get_testcase' functions should be imported and available.
        - The function creates a directory structure under 'problems_dir' to store the retrieved data.
        - If the directory for the given problem ID already exists, the function will exit early without re-fetching data.

    Example:
        >>> get_problem_data(123, "../problems_data/problem_123")
        Problem 123 data already exists.
    """

    # Verify if problem data already exists. Create problem directory if it does not exist.
    if os.path.exists(problem_dir):
        print(f"Problem {problem_id} data already exists.")
        return
    else:
        os.makedirs(problem_dir)

    # Get problem solutions
    get_solutions(problem_id, problem_dir)

    # Get problem correct answer and save alongside the students solutions
    get_answer(problem_id, os.path.join(problem_dir, "data"))

    # Get problem test case
    get_testcase(problem_id, problem_dir)

if __name__ == "__main__":
    # Check if command line arguments exist
    if len(sys.argv) > 1:
        # Retrieve the problem ID and problems directory from the command line
        problem_id = int(sys.argv[1])
        problem_dir = f"../problems_data/problem_{problem_id}"
        get_problem_data(problem_id, problem_dir)
    else:
        print("Usage: python get_problem_data.py <problem_id>")



    

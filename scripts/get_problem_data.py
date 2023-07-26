import sys
import os
import psycopg2
from get_answer import get_answer
from get_problems_with_m_correct_solutions import get_problems_with_at_least_n_and_m_solutions
from get_solutions import get_solutions
from get_testcase import get_testcase

def get_problem_data(problem_id):
    """
    Retrieve data for a given problem ID from the database and store it in a directory.

    This function retrieves the correct answer, user-submitted solutions, and test cases for a given problem ID from
    the database and saves them in a structured directory.

    Args:
        problem_id (int): The ID of the problem for which data is requested.

    Returns:
        None

    Raises:
        psycopg2.Error: If an error occurs during the database connection or query execution.

    Notes:
        - The 'db_params.json' file should contain the necessary parameters for the PostgreSQL connection.
        - The 'get_answer', 'get_solutions', and 'get_testcase' functions should be imported and available.
        - The function creates a directory structure under '../problems_data' to store the retrieved data.
        - If the directory for the given problem ID already exists, the function will exit early without re-fetching data.

    Example:
        >>> get_problem_data(123)
        Problem 123 data already exists.
    """

    # Create problems directory if it does not exist
    problems_dir = "../problems_data"
    os.makedirs(problems_dir, exist_ok=True)

    # Verify if problem data already exists. Create problem directory if it does not exist.
    problem_dir = f"{problems_dir}/problem_{problem_id}"
    if os.path.exists(problem_dir):
        print(f"Problem {problem_id} data already exists.")
        return
    else:
        os.makedirs(problem_dir)

    # Get problem correct answer
    get_answer(problem_id, problem_dir)

    # Get problem solutions
    get_solutions(problem_id, problem_dir)

    # Get problem test case
    get_testcase(problem_id, problem_dir)

if __name__ == "__main__":
  # Check if command line arguments exist
  if len(sys.argv) > 1:
      # Retrieve the problem ID from the command line
      problem_id = int(sys.argv[1])
      get_problem_data(problem_id)
  else:
      print("No command line arguments provided.")


    

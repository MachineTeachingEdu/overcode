import sys
import os
import psycopg2
from get_answer import get_answer
from get_problems_with_m_correct_solutions import get_problems_with_at_least_n_and_m_solutions
from get_solutions import get_solutions
from get_testcase import get_testcase

def get_problem_data(problem_id):
    """

    Args:

    Returns:

    Raises:
        psycopg2.Error: If an error occurs during the database connection or query execution.
    """

    # Create problems directory if it does not exist
    problems_dir = "../problems_data"
    os.makedirs(problems_dir, exist_ok=True)

    # Create problem directory if it does not exist
    problem_dir = f"{problems_dir}/problem_{problem_id}/"
    os.makedirs(problem_dir, exist_ok=True)

    # Get problem correct answer
    get_answer(problem_id, problem_dir)

if __name__ == "__main__":
  # Check if command line arguments exist
  if len(sys.argv) > 1:
      # Retrieve the problem ID from the command line
      problem_id = int(sys.argv[1])
      get_problem_data(problem_id)
  else:
      print("No command line arguments provided.")

    

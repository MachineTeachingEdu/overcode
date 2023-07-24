import sys
import psycopg2
import json

def get_answer(problem_id, dst_dir=""):
    """
    Connects to a PostgreSQL database, executes a query to retrieve the answer for a given problem ID,
    and saves the answer to a file named 'answer.py'.

    Args:
        problem_id (int): The ID of the problem for which the answer is requested.

    Returns:
        None

    Raises:
        psycopg2.Error: If an error occurs during the database connection or query execution.
    """

    # Load Database parameters
    with open("db_params.json", "r") as f:
        params = json.load(f)

    with psycopg2.connect(**params) as connection:
        with connection.cursor() as cursor:

            # execute query with cursor
            query = f""" SELECT content
                      FROM questions_solution qs
                      WHERE problem_id = {problem_id};"""
            cursor.execute(query)

            # retrieve results of query
            answer = cursor.fetchall()

            # verify data
            if answer is None:
                print("Error! No answer found!")
            elif len(answer) > 1:
                print("Error! More than one answer found!")
            else:
                filepath = dst_dir + "answer.py"
                with open(filepath, "w") as f:
                    f.write(answer[0][0])
                    print(f"Answer saved to '{filepath}'")

if __name__ == "__main__":
  # Check if command line arguments exist
  if len(sys.argv) > 1:
      # Retrieve the problem ID from the command line
      problem_id = int(sys.argv[1])
      get_answer(problem_id)
  else:
      print("No command line arguments provided.")

    

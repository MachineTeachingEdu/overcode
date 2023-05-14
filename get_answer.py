import sys
import psycopg2

def get_answer(problem_id):
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

    # database parameters
    params = {
        "host": "localhost",  # host on which the database is running
        "database": "db_test",  # name of the database to connect to
        "user": "newuser",  # username to connect with
        "password": "",
    }  # password associated with your username

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
                with open("answer.py", "w") as f:
                    f.write(answer[0][0])
                    print("Answer saved to answer.py")

if __name__ == "__main__":
  # Check if command line arguments exist
  if len(sys.argv) > 1:
      # Retrieve the problem ID from the command line
      problem_id = int(sys.argv[1])
      get_answer(problem_id)
  else:
      print("No command line arguments provided.")

    

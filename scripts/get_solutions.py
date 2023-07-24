import sys
import os
import shutil
import json
import psycopg2


def create_solutions(data):
    """
    Generate Python files for each solution in the given data.

    Args:
        data (list): A list of tuples containing the solution code and user ID.

    Returns:
        None
    """
    # Remove 'data' folder if it exists
    if os.path.exists("data"):
        shutil.rmtree("data")

    # Create 'data' folder
    os.makedirs("data")

    for code, user_id in data:
        with open(f"data/{user_id}.py", "w") as f:
            f.write(code)
    print("Python files for each solution generated!")


def get_solutions(problem_id):
    """
    Retrieve the most recent solutions for a given problem ID from the database and generate Python files.

    Args:
        problem_id (int): The ID of the problem.

    Returns:
        None
    """
    # Load Database parameters
    with open("db_params.json", "r") as f:
        params = json.load(f)

    with psycopg2.connect(**params) as connection:
        with connection.cursor() as cursor:
            # Query solutions and user IDs, getting only the most recent solution for each user
            query = f"""SELECT solution, user_id
                        FROM (
                            SELECT solution, user_id,
                                ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY timestamp DESC) AS rn
                            FROM questions_userlog
                            WHERE problem_id = {problem_id}
                        ) AS submissions
                        WHERE rn = 1;"""
            cursor.execute(query)
            solutions = cursor.fetchall()

            # Verify data
            if solutions is None:
                print("Error! No solutions found!")
            else:
                create_solutions(solutions)


if __name__ == "__main__":
    # Check if command line arguments exist
    if len(sys.argv) > 1:
        # Retrieve the problem ID from the command line
        problem_id = int(sys.argv[1])
        get_solutions(problem_id)
    else:
        print("No command line arguments provided.")

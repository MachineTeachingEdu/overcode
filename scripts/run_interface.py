import sys
import os
from http.server import HTTPServer, SimpleHTTPRequestHandler

def run_interface(dir):
    """
    Run an HTTP server serving files from the specified directory.

    Args:
        dir (str): The directory from which to serve files.

    Returns:
        None
    """

    # Get the absolute path of the specified directory
    abs_dir = os.path.abspath(dir)

    PORT = 8000

    class Handler(SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=abs_dir, **kwargs)

    httpd = HTTPServer(('localhost', PORT), Handler)
    print(f"Serving files from '{abs_dir}' on http://localhost:{PORT}")
    httpd.serve_forever()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        directory = sys.argv[1]
        run_interface(directory)
    else:
        print("Usage: python run_interface.py <directory>")

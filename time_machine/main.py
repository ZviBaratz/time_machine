from pathlib import Path

from time_machine.analyze_data import analyze
from time_machine.data_reader import read_data

DEFAULT_PATH = Path("/my_data/dir/")

def execute_workflow(directory=DEFAULT_PATH):
    data = read_data(directory)
    return analyze(data)


if __name__ == "__main__":
    execute_workflow()

import os
import pytest
from logic import read_input, filter_lines, write_output, filter_file

@pytest.fixture
def input_file(tmp_path):
    input_file = tmp_path / "test_input.txt"
    with open(input_file, "w") as f:
        f.write("apple\nbanana\ncherry\ngrape\n")
    return input_file

@pytest.fixture
def output_file(tmp_path):
    return tmp_path / "test_output.txt"

@pytest.mark.parametrize("lines, keyword, expected_filtered", [
    (["apple", "banana", "cherry", "grape"], "a", ["apple", "banana", "grape"]),
    (["apple", "banana", "cherry", "grape"], "b", ["banana"]),
    (["apple", "banana", "cherry", "grape"], "z", []),
])
def test_filter_lines(lines, keyword, expected_filtered):
    filtered = filter_lines(lines, keyword)
    assert filtered == expected_filtered

def test_read_input(input_file):
    lines = read_input(input_file)
    assert lines == ["apple\n", "banana\n", "cherry\n", "grape\n"]

def test_write_output(output_file):
    lines = ["Line 1", "Line 2", "Line 3"]
    write_output(lines, output_file)


    assert os.path.exists(output_file)
    with open(output_file, "r") as f:
        content = f.read()
        assert content == "Line 1\nLine 2\nLine 3\n"

def test_filter_file(input_file, output_file):
    filter_file(input_file, output_file, "a")

    assert os.path.exists(output_file)
    with open(output_file, "r") as f:
        content = f.read()
        assert content == "apple\nbanana\ngrape\n"


def test_filter_file_nonexistent_input(tmp_path, output_file):
    input_file = tmp_path / "nonexistent_input.txt"
    with pytest.raises(FileNotFoundError):
        filter_file(input_file, output_file, "keyword")


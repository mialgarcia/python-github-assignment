import sys
import subprocess


def run_input(user_input: str) -> str:
    """Run app.py with given input and return combined stdout/stderr."""
    p = subprocess.Popen([sys.executable, "app.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    out, _ = p.communicate(user_input + "\n")
    return out


def test_valid_input():
    out = run_input("2")
    assert "You are on track to study 14.0 hours this week." in out


def test_invalid_input():
    out = run_input("abc")
    assert "Error: Please enter a valid number." in out

import sys
from io import StringIO
from app.calculator import calculator

def run_calculator_with_input(monkeypatch, inputs):
    iterator = iter(inputs)
    monkeypatch.setattr('builtins.input', lambda _: next(iterator))
    captured_output = StringIO()
    sys.stdout = captured_output
    calculator()
    sys.stdout = sys.__stdout__
    return captured_output.getvalue()

def test_addition(monkeypatch):
    inputs = ['add 1 2', 'exit']
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Result: 3.0" in output

def test_subtraction(monkeypatch):
    inputs = ['subtract 1 2', 'exit']
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Result: -1.0" in output

def test_multiplication(monkeypatch):
    inputs = ['multiply 2 3', 'exit']
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Result: 6.0" in output

def test_division(monkeypatch):
    inputs = ['divide 10 2', 'exit']
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Result: 5.0" in output

def test_division_by_zero(monkeypatch):
    inputs = ['divide 10 0', 'exit']
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Cannot divide by zero" in output

def test_invalid_operation(monkeypatch):
    inputs = ['factorial 1 2', 'exit']
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Unknown operation" in output

def test_invalid_input(monkeypatch):
    inputs = ['add two 3', 'exit']
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Invalid input" in output

def test_exit(monkeypatch):
    inputs = ['exit']
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Exiting calculator..." in output
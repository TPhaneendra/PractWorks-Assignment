# Assignment of PractWorks Mentors Private Limited

## Overview

This Python program generates a unique set of math questions and their corresponding step-by-step solutions each time it is executed. The questions and answers are outputted in JSON format, with the mathematical expressions formatted using MathJax.

The goal is to maximize the variations in the generated math problems while ensuring correctness and efficiency. The coefficients, numerators, and denominators of the equations are randomized, and the answers are derived step-by-step following standard algebraic rules.

## Features

- **Randomized Questions:** The program generates random values for the equation's coefficients and fractions.
- **MathJax Support:** The output is formatted for MathJax, making it suitable for rendering in any environment that supports LaTeX or MathJax.
- **Efficient Execution:** The program avoids unnecessary loops or inefficiencies and ensures that there are no zero denominators in the generated questions.
- **Step-by-step Answers:** The answers are generated in a structured manner, demonstrating each step taken to solve the equation.

## How It Works

1. **Equation Generation:**
   - A linear equation of the form `a*x - (1/b) = (1/d) - c*x` is generated, where `a`, `b`, `c`, and `d` are randomly selected integers.
   - Denominators are ensured to be non-zero to avoid invalid equations.

2. **Solution Generation:**
   - The program solves the generated equation step-by-step, transposing terms and solving for `x`.
   - Each step of the solution is formatted in MathJax and stored in the `a_tex` field of the output JSON.

3. **Output:**
   - The program outputs a JSON structure that contains:
     - `q_tex`: The question formatted in MathJax.
     - `a_tex`: The detailed answer formatted in MathJax, showing all the steps.

## Usage

### Requirements

This program does not require any additional packages beyond the standard Python installation.

### Running the Program

To generate a new question and answer pair, simply run the Python script:

```bash```
python generate_mathjax_question.py

Each time you run the script, it will output a new variation of the question and its solution in JSON format.

```JSON```
```
{
    "q_tex": "\\( 2x - \\frac{1}{3} = \\frac{1}{5} - x \\)",
    "a_tex": "\\( 2x - \\frac{1}{3} = \\frac{1}{5} - x \\)\\newline\\( 2x + x = \\frac{1}{5} + \\frac{1}{3} \\)\\newline\\( 3x = \\frac{3 + 5}{15} \\)\\newline\\( 3x = \\frac{8}{15} \\)\\newline\\( 3x \\times 15 = 8 \\)\\newline\\( 45x = 8 \\)\\( x = \\frac{8}{45} \\)"
}
```

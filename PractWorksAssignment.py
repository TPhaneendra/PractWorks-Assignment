import random
import json
import fractions



#Tummala Nikhil Phaneendra

def fun():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(1, 10)
    d = random.randint(1, 10)
    e = random.randint(1, 10)
    f = random.randint(1, 10)

    q_tex = f"\\( {a}x - \\frac{{1}}{{{b}}} = \\frac{{1}}{{{d}}} - {c}x \\)"

    sum_coeff = a + c
    left_side = fractions.Fraction(1, d) + fractions.Fraction(1, b)
    simplified_left = f"{left_side.numerator} / {left_side.denominator}"

    answer_steps = [
        f"\\( {a}x - \\frac{{1}}{{{b}}} = \\frac{{1}}{{{d}}} - {c}x \\)\\newline",
        f"\\( {a}x + {c}x = \\frac{{1}}{{{d}}} + \\frac{{1}}{{{b}}} \\)",
        "\\text{ (Transposing) }\\newline",
        f"\\( {sum_coeff}x = \\frac{{{left_side.numerator}}}{{{left_side.denominator}}} \\)",
        f"\\( {sum_coeff}x \\times {left_side.denominator} = {left_side.numerator} \\)",
        f"\\( {sum_coeff * left_side.denominator}x = {left_side.numerator} \\)",
        f"\\( x = \\frac{{{left_side.numerator}}}{{{sum_coeff * left_side.denominator}}} \\)"
    ]
    
    a_tex = "\\newline".join(answer_steps)

    return json.dumps({
        "q_tex": q_tex,
        "a_tex": a_tex
    }, indent=4)

if __name__ == "__main__":
    print(fun())

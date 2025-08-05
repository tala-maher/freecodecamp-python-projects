def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

   
    first_line = []
    second_line = []
    dashes_line = []
    results_line = []

    for problem in problems:
        
        parts = problem.split()
        if len(parts) != 3:
            return "Error: Each problem must consist of two operands and one operator."

        num1, operator, num2 = parts

       
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        
        if not num1.isdigit() or not num2.isdigit():
            return "Error: Numbers must only contain digits."

       
        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Calculate the width needed (longest number + 2)
        width = max(len(num1), len(num2)) + 2

        # Add formatted lines
        first_line.append(num1.rjust(width))
        second_line.append(operator + ' ' + num2.rjust(width - 2))
        dashes_line.append('-' * width)

        # Calculate result if needed
        if show_answers:
            if operator == '+':
                result = int(num1) + int(num2)
            else:
                result = int(num1) - int(num2)
            results_line.append(str(result).rjust(width))

    # Join the individual pieces with 4 spaces in between
    arranged_problems = (
        '    '.join(first_line) + '\n' +
        '    '.join(second_line) + '\n' +
        '    '.join(dashes_line)
    )

    if show_answers:
        arranged_problems += '\n' + '    '.join(results_line)

    return arranged_problems

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')

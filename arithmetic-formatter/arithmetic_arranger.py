def arithmetic_arranger(problems, show_solutions=False):
  # Check if the number of problems exceeds the limit
  if len(problems) > 5:
      return "Error: Too many problems."

  # Initialize lists to store various parts of the arranged problems
  arranged_problems = []  # The final arranged problems
  top_row = []            # The top row of numbers in each problem
  bottom_row = []         # The bottom row of numbers in each problem
  dashes = []             # The dashed line separating the problem from the solution
  solutions = []          # The solutions to the arithmetic problems

  # Iterate through each problem in the list of problems
  for problem in problems:
      # Split the problem into its components: number1, operator, and number2
      num1, operator, num2 = problem.split()

      # Validate the numbers and operator
      if not (num1.isdigit() and num2.isdigit()):
          return "Error: Numbers must only contain digits."
      if len(num1) > 4 or len(num2) > 4:
          return "Error: Numbers cannot be more than four digits."
      if operator not in ['+', '-']:
          return "Error: Operator must be '+' or '-'."

      # Calculate the width needed for the columns based on the length of the numbers
      width = max(len(num1), len(num2)) + 2

      # Right justify and append the top and bottom rows for the current problem
      top_row.append(num1.rjust(width))
      bottom_row.append(operator + num2.rjust(width - 1))

      # Create and append the dashed line for the current problem
      dashes.append('-' * width)

      # Calculate and append the solution for the current problem
      solution = int(num1) + int(num2) if operator == '+' else int(num1) - int(num2)
      solutions.append(str(solution).rjust(width))

  # Join each row with spaces and add them to the arranged problems list
  arranged_problems.append("    ".join(top_row))
  arranged_problems.append("    ".join(bottom_row))
  arranged_problems.append("    ".join(dashes))

  # If the show_solutions flag is True, add the solutions to the arranged problems list
  if show_solutions:
      arranged_problems.append("    ".join(solutions))

  # Join all rows with newlines to get the final arranged problems
  return "\n".join(arranged_problems)

import random


def generate_random_number(min_value, max_value):
    """
    Generates a random integer between min_value and max_value (inclusive).
    
    Args:
        min_value (int): The minimum possible value.
        max_value (int): The maximum possible value.
    
    Returns:
        int: A random integer between min_value and max_value.
    """
    return random.randint(min_value, max_value)


def select_random_operator():
    """
    Selects a random mathematical operator from '+', '-', or '*'.
    
    Returns:
        str: A random operator.
    """
    return random.choice(['+', '-', '*'])


def create_math_problem(num1, num2, operator):
    """
    Generates a math problem and its correct answer.
    
    Args:
        num1 (int): The first operand.
        num2 (int): The second operand.
        operator (str): The operator to apply ('+', '-', '*').
    
    Returns:
        tuple: A tuple containing the problem as a string and the correct answer as an integer.
    """
    problem_str = f"{num1} {operator} {num2}"
    
    # Calculate the answer based on the operator
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    elif operator == '*':
        answer = num1 * num2
    else:
        raise ValueError("Invalid operator")
    
    return problem_str, answer


def math_quiz_game():
    """
    Main function to run the Math Quiz Game.
    Presents random math problems to the user and tracks their score.
    """
    score = 0
    total_questions = 3  # Number of questions in the quiz

    print("Welcome to the Math Quiz Game!")
    print("Try to solve the following math problems:")

    for _ in range(total_questions):
        # Generate random numbers and operator
        number1 = generate_random_number(1, 10)
        number2 = generate_random_number(1, 5)
        operator = select_random_operator()

        # Create a math problem and get the correct answer
        problem, correct_answer = create_math_problem(number1, number2, operator)
        print(f"\nQuestion: {problem}")

        # Get user input and handle possible errors
        try:
            user_answer = int(input("Your answer: "))
            
            if user_answer == correct_answer:
                print("Correct! You earned a point.")
                score += 1
            else:
                print(f"Wrong answer. The correct answer is {correct_answer}.")
        
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    # Display the final score
    print(f"\nGame over! Your final score is: {score}/{total_questions}")


# Run the math quiz game if this script is executed
if __name__ == "__main__":
    math_quiz_game()

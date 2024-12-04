def divide_numbers():
    try:
        # Get input from the user
        numerator = float(input("Enter the numerator: "))
        denominator = float(input("Enter the denominator: "))
        
        # Perform division
        result = numerator / denominator
        print("Result:", result)
    
    except ZeroDivisionError:
        error_message = "Error Type: ZeroDivisionError | Message: Division by zero is not allowed"
        print(error_message)
        log_error(error_message)
    
    except ValueError as e:
        error_message = f"Error Type: ValueError | Message: Invalid numeric input ({e})"
        print(error_message)
        log_error(error_message)
    
    except Exception as e:
        error_message = f"Error Type: {type(e).__name__} | Message: {e}"
        print(error_message)
        log_error(error_message)

def log_error(message):
    """Logs the error message to a file."""
    with open("error_log.txt", "a") as log_file:
        log_file.write(message + "\n")

if __name__ == "__main__":
    divide_numbers()



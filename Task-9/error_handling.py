
import logging

# Step 5 & 6: Configure logging and save logs to a file
logging.basicConfig(
    filename="error.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def divide_numbers(a, b):
    try:
        print("Trying to divide numbers...")
        
        result = a / b   # may cause ZeroDivisionError
        number = int("abc")  # may cause ValueError (simulated runtime error)
        
    except ZeroDivisionError as e:
        logging.error("Division by zero error occurred", exc_info=True)
        print("❌ Error: You cannot divide by zero.")
        
    except ValueError as e:
        logging.error("Invalid value conversion", exc_info=True)
        print("❌ Error: Invalid value provided.")
        
    except Exception as e:
        logging.error("Unexpected error occurred", exc_info=True)
        print("❌ Error: Something went wrong.")
        
    else:
        # Step 4: else runs if no exception occurs
        print("✅ Division successful:", result)
        
    finally:
        # Step 4: finally always runs
        print("✔ Execution completed (finally block).")

# Step 8: Simulate runtime error
divide_numbers(10, 0)

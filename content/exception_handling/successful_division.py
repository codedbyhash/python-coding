try:
    n=200
    res=100/n

except ZeroDivisionError:
    print("Division by zero is not allowed.")

except ValueError:
    print("enter a valid number")

else:
    print("Result is:", res)

finally:
    print("Execution Completed.")
    
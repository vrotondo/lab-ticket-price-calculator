# Ticket Price Calculator

# Display welcome message
print("Welcome to the Movie Theater Ticket Price Calculator!")

# Get user input for age
age = int(input("Please enter your age: "))
if age < 0:
    print("Error: Age cannot be negative.")
    exit()

# Get user input for movie type
movie_type = input("Please enter the movie type (regular/premium): ").lower().strip()

# Validate movie type input
if movie_type not in ["regular", "premium"]:
    print("Error: Invalid movie type. Please enter 'regular' or 'premium'.")
    exit()

# Calculate ticket price based on age and movie type
if age <= 12: # Children
    if movie_type == 'regular':
        ticket_price = 8
    else: # premium
        ticket_price = 10
elif age >= 60: # Seniors
    if movie_type == 'regular':
        ticket_price = 10
    else:
        ticket_price = 12
else: # Adults
    if movie_type == 'regular':
        ticket_price = 12
    else:
        ticket_price = 14

# Display the calculated ticket price
print(f"\nTicket Details:")
print(f"Age: {age}")
print(f"Movie Type: {movie_type.capitalize()}")
print(f"Ticket Price: ${ticket_price:.2f}")
print("\nEnjoy your movie!")
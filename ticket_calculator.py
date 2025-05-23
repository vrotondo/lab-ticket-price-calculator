'''FUNCTION TicketPriceCalculator
    // Display welcome message
    DISPLAY "Welcome to the Movie Theater Ticket Price Calculator!"
    
    // Get and validate age
    INPUT age as integer
    IF age < 0 THEN
        DISPLAY "Error: Age cannot be negative."
        EXIT program
    END IF
    
    // Get and validate movie type
    INPUT movie_type as string (prompt for regular/premium)
    CONVERT movie_type to lowercase and remove whitespace
    
    IF movie_type is not "regular" AND movie_type is not "premium" THEN
        DISPLAY "Error: Invalid movie type. Please enter 'regular' or 'premium'."
        EXIT program
    END IF
    
    // Calculate ticket price based on age and movie type
    IF age <= 12 THEN // Children
        IF movie_type equals "regular" THEN
            SET ticket_price to 8
        ELSE // premium
            SET ticket_price to 10
        END IF
    ELSE IF age >= 60 THEN // Seniors
        IF movie_type equals "regular" THEN
            SET ticket_price to 10
        ELSE // premium
            SET ticket_price to 12
        END IF
    ELSE // Adults (13-59)
        IF movie_type equals "regular" THEN
            SET ticket_price to 12
        ELSE // premium
            SET ticket_price to 14
        END IF
    END IF
    
    // Display ticket details
    DISPLAY "Ticket Details:"
    DISPLAY "Age: " + age
    DISPLAY "Movie Type: " + capitalize(movie_type)
    DISPLAY "Ticket Price: $" + format_decimal(ticket_price, 2)
    DISPLAY "Enjoy your movie!"
END FUNCTION

CALL TicketPriceCalculator'''

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

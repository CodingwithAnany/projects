import pyjokes  # Correct module name

while True:  # Create an infinite loop
    joke = pyjokes.get_joke()  # Get a random joke
    print(joke)  # Print the joke
    
    # Add a pause to avoid overwhelming the output (optional)
    input("Press Enter to get another joke or Ctrl+C to exit.")
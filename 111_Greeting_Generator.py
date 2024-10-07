# 109. Greeting Generator: Write a Python function called greeting_generator that takes a name as input and returns a greeting message using nested functions. The greeting message should be customizable (e.g., “Hello, {name}! How are you today?”).

def greeting_generator(name):
    """
    Function to generate a customizable greeting message.

    Parameters:
    name (str): The name of the person to greet.

    Returns:
    str: A greeting message.
    """
    
    def create_greeting(person_name):
        return f"Hello, {person_name}! How are you today?"
    
    def personalize_greeting(greeting):
        return f"{greeting} Have a great day!"

    # Generate the initial greeting
    initial_greeting = create_greeting(name)
    
    # Personalize the greeting
    final_greeting = personalize_greeting(initial_greeting)
    
    return final_greeting

# Test the function with different names
print(greeting_generator("Alice"))  # Output: Hello, Alice! How are you today? Have a great day!
print(greeting_generator("Bob"))    # Output: Hello, Bob! How are you today? Have a great day!

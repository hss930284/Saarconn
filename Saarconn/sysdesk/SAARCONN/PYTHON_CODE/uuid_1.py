import uuid

def generate_random_uuid():
    """Generate a random UUID."""
    return str(uuid.uuid4())

def main():
    # Generate a random UUID
    random_uuid = generate_random_uuid()
    
    # Print the generated UUID
    print("Generated UUID:", random_uuid)

    # You can use the UUID in your application as needed
    # For example, you might want to store it in a database or use it as a unique identifier
    # Here, we'll just demonstrate using it in a simple message
    print(f"Your unique identifier is: {random_uuid}")

if __name__ == "__main__":
    main()
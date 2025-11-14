import random
import string

# File path for storing passwords
FILE_PATH = "passwords.txt"
# Length of generated passwords
PASSWORD_LENGTH = 16


def make_pass():
    """Generate a random 16-character password."""
    # Combine letters, digits, and special characters for password generation
    chars = string.ascii_letters + string.digits + "!#$%^&*()<>,./?\;:{}[]-_+=~`"
    # Select random characters from the pool
    password = [random.choice(chars) for _ in range(PASSWORD_LENGTH)]
    # Return as a single string
    return "".join(password)


def read(line_number):
    """Read a specific line from the password file."""
    try:
        # Open and read all lines from the file
        with open(FILE_PATH, "r") as file:
            lines = file.readlines()
            # Return the line if it exists, remove trailing newline
            if line_number < len(lines):
                return lines[line_number].rstrip("\n")
            # Return None if line number is out of range
            return None
    except FileNotFoundError:
        # Return None if file doesn't exist
        return None



def append(string):
    """Append a string to the password file."""
    try:
        # Open file in append mode and write the string
        with open(FILE_PATH, "a") as file:
            file.write(str(string))
    except FileExistsError:
        # Handle case where file operations fail
        pass




def main():
    """Main program loop."""
    # Ask user if they want to create a new password or retrieve one
    new_password = input("Would you like to make a new password? (y/n): ")
    
    if new_password.lower() == "y":
        # Path for creating a new password
        user = input("What's your email/username: ").lower()
        service = input("What service is this for: ").lower()
        
        # Generate and display the new password
        temp_pass = make_pass()
        print("Your password is:")
        print(temp_pass)
        
        # Append data to file in format: service | username | password
        append(service)
        append(" | ")
        append(user)
        append(" | ")
        append(temp_pass)
        append("\n")
    else:
        # Path for retrieving an existing password
        service = input("What service is this for: ").lower()
        x = 0
        
        # Search through file line by line
        while True:
            line = read(x)
            # Stop if end of file is reached
            if line is None:
                print(f"Service '{service}' not found.")
                break
            
            # Parse line with '|' separators into service, username, and password
            parts = [p.strip() for p in line.split("|")]
            # Ensure the line has the correct format (3 parts)
            if len(parts) == 3:
                service_name, username, password = parts
                
                # Check if service name matches user's search
                if service in service_name.lower():
                    print("Service | Username | Password")
                    print(f"{service_name} | {username} | {password}")
                    break
            
            # Move to next line
            x += 1


if __name__ == "__main__":
    main()
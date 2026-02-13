import json


def load_users_data(file_path="users.json"):
    """
    Loads user data from a JSON file with error handling for empty or invalid files.

    Args:
        file_path (str): The path to the JSON data.

    Returns:
        list: A list of user dictionaries or an empty list if an error occurs.
    """
    try:
        with open(file_path, "r") as file:
            content = file.read().strip()
            if not content:
                print(f"Error: The file '{file_path}' is empty.")
                return []

            return json.loads(content)

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return []
    except json.JSONDecodeError:
        # feedback fix: Gracefully handles malformed JSON or empty files
        print(f"Error: '{file_path}' contains invalid JSON formatting.")
        return []


def filter_users_by_name(users, name):
    """
    Filters users by name using partial matching (case-insensitive).
    Search 'Smith' will return 'Alice Smith'.
    """
    filtered = [u for u in users if name.lower() in u.get("name", "").lower()]
    display_results(filtered, f"names containing '{name}'")


def filter_users_by_age(users, min_age_input):
    """
    Filters users by minimum age.
    """
    try:
        age_val = int(min_age_input)
        filtered = [u for u in users if u.get("age", 0) >= age_val]
        display_results(filtered, f"age >= {age_val}")
    except ValueError:
        print("Invalid age input. Please enter a whole number.")


def filter_users_by_email(users, email):
    """
    Filters users by partial email match.
    """
    filtered = [u for u in users if email.lower() in u.get("email", "").lower()]
    display_results(filtered, f"email containing '{email}'")


def display_results(filtered_users, criteria):
    """
    Prints the results and includes a count of how many users were found.
    """
    if not filtered_users:
        print(f"\nNo users found matching {criteria}.")
    else:
        print(f"\nFound {len(filtered_users)} user(s) matching {criteria}:")
        for user in filtered_users:
            print(user)


def main():
    """
    Main entry point for the user filtering script.
    """
    users = load_users_data("users.json")

    if not users:
        return

    filter_option = input("Filter by? (name/age/email): ").strip().lower()

    if filter_option == "name":
        search = input("Enter name: ").strip()
        filter_users_by_name(users, search)
    elif filter_option == "age":
        search = input("Enter min age: ").strip()
        filter_users_by_age(users, search)
    elif filter_option == "email":
        search = input("Enter email: ").strip()
        filter_users_by_email(users, search)
    else:
        print(f"Option '{filter_option}' not supported.")


if __name__ == "__main__":
    main()
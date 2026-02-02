import json


def filter_users_by_name(name):
    """Filters users by their exact name (case-insensitive)."""
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [
        user for user in users if user["name"].lower() == name.lower()
    ]

    for user in filtered_users:
        print(user)


def filter_users_by_age(min_age):
    """Filters users who meet or exceed a minimum age."""
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["age"] >= int(min_age)]

    for user in filtered_users:
        print(user)


def filter_users_by_email(email):
    """Filters users by their email address (partial match)."""
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [
        user for user in users if email.lower() in user["email"].lower()
    ]

    if not filtered_users:
        print(f"No users found with email containing: {email}")
    else:
        for user in filtered_users:
            print(user)


if __name__ == "__main__":
    prompt = "Filter by? (name/age/email): "
    filter_option = input(prompt).strip().lower()

    if filter_option == "name":
        name_to_search = input("Enter name: ").strip()
        filter_users_by_name(name_to_search)

    elif filter_option == "age":
        age_to_search = input("Enter min age: ").strip()
        filter_users_by_age(age_to_search)

    elif filter_option == "email":
        email_to_search = input("Enter email to search: ").strip()
        filter_users_by_email(email_to_search)

    else:
        print(f"Option '{filter_option}' not supported.")
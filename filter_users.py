import json


def filter_users_by_name(name):
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["name"].lower() == name.lower()]

    for user in filtered_users:
        print(user)


def filter_users_by_age(min_age):
    """Filters users who are equal to or older than the specified age."""
    with open("users.json", "r") as file:
        users = json.load(file)
    # Conversion
    # Convert age to int to ensure comparison works
    filtered_users = [user for user in users if user["age"] >= int(min_age)]

    if not filtered_users:
        print(f"No users found age {min_age} or older.")
    else:
        for user in filtered_users:
            print(user)


if __name__ == "__main__":
    # Updated the prompt to reflect the new feature
    filter_option = input("What would you like to filter by? (name/age): ").strip().lower()

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(name_to_search)

    elif filter_option == "age":
        try:
            age_to_search = input("Enter minimum age to filter users: ").strip()
            filter_users_by_age(age_to_search)
        except ValueError:
            print("Please enter a valid number for the age.")

    else:
        print(f"Filtering by '{filter_option}' is not yet supported.")
# import json
#
#
# def filter_users_by_name(name):
#     with open("users.json", "r") as file:
#         users = json.load(file)
#
#     filtered_users = [user for user in users if user["name"].lower() == name.lower()]
#
#     for user in filtered_users:
#         print(user)
#
#
# if __name__ == "__main__":
#     filter_option = input("What would you like to filter by? (Currently, only 'name' is supported): ").strip().lower()
#
#     if filter_option == "name":
#         name_to_search = input("Enter a name to filter users: ").strip()
#         filter_users_by_name(name_to_search)
#     else:
#         print("Filtering by that option is not yet supported.")

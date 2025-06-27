
List_of_US_states_by_date_of_admission_to_the_Union = [
    "Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland",
    "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky",
    "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas",
    "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia",
    "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming",
    "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"
]
print(List_of_US_states_by_date_of_admission_to_the_Union)
user_input = input("Please enter the number of the order in which a state entered the Union (max 50), or type 'all' to see all states with their order: ")

if user_input == "all":
    for index, value in enumerate(List_of_US_states_by_date_of_admission_to_the_Union, start=1):
        print(f"{index}: {value}")
elif user_input.isdigit():
    user_index = int(user_input) - 1
    if 0 <= user_index < len(List_of_US_states_by_date_of_admission_to_the_Union):
        print(List_of_US_states_by_date_of_admission_to_the_Union[user_index])
    else:
        print("Please enter a number between 1 and 50.")
else:
    print("Invalid input. Please enter a number or 'all'.")
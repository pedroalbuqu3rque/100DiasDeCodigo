def register_user():
    name = input("Enter the user's name: ")
    age = input("Enter the user's age: ")
    while not age.isdigit():   # age is a valid number
        print("Age must be a number.")
        age = input("Enter the user's age: ")
    email = input("Enter the user's email: ")
    with open('dia20_users.txt', 'a') as file:
        file.write(f'{name},{age},{email}\n')
    print('User registered successfully!')
def list_users():
    try:
        with open('dia20_users.txt', 'r') as file:
            for line in file:
                name, age, email = line.strip().split(',')
                print(f"Name: {name}, Age: {age}, Email: {email}")
    except FileNotFoundError:
        print('No users registered yet.')
    except Exception as e:
        print(f"An error occurred: {str(e)}")
def menu():
    while True:
        print('\nMenu:')
        print('1. Register user')
        print('2. List users')
        print('3. Exit')
        option = input('Choose an option: ')
        if option == '1':
            register_user()
        elif option == '2':
            list_users()
        elif option == '3':
            print('Exiting the program...')
            break
        else:
            print('Invalid option. Please try again.')
if __name__ == '__main__':
    menu()
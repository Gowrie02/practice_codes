def main():
    user_input = ""
    while user_input.lower() != 'stop':
        user_input = input('enter something,if you wanna stop enter stop: ')
        if user_input.lower() == 'stop':
            print('The End')
            break
        else:
            print(f'{user_input};')

if __name__ == "__main__":
    main()

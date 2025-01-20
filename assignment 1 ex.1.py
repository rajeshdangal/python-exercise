def tester(string="The length of string is too short."):
    if string == "Too short" or len(string) < 20:
        print(string)
    else:
        print(string)

def main():
    while True:
        user_input = input("Write something whatever you want: ")
        if user_input.lower() == "quit":
            break
        if len(user_input) < 20:
            tester()
        else:
            tester(user_input)

if __name__ == "__main__":
    main()
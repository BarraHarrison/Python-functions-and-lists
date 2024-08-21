def first_function():
    print("Hello World")

def second_function(string_input, number_input):
    print("The String you entered is: ", string_input)
    print("The Number you entered is: ", number_input)

user_string = input("Enter a string: ")
user_number = int(input("Enter a number: "))

second_function(number_input = user_number, string_input = user_string)

def writing_many_things(args):
    for things in args:
        print(things)

writing_many_things("bar", "bam", "zoo", "cat", "dog", "cup", "bat", "jet", 
"hat", "sun", "fan", "mat", "pen", "log", "net", "kit", 
"bin", "rod", "rug", "pit")
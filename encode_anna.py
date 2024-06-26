def encode(password):       # I wrote this part

    empty_password = ''
    count = 0

    for item in password:   # used a for loop and check for each number and incr by 3. At first I wanted to use enumerate but that did not work so I did it the long way

        if item == '0':
            count = '3'
            empty_password += count     # added each number into an empty string

        elif item == '1':
            count = '4'
            empty_password += count

        elif item == '2':
            count = '5'
            empty_password += count

        elif item == '3':
            count = '6'
            empty_password += count

        elif item == '4':
            count = '7'
            empty_password += count

        elif item == '5':
            count = '8'
            empty_password += count

        elif item == '6':
            count = '9'
            empty_password += count

        elif item == '7':
            count = '0'
            empty_password += count

        elif item == '8':
            count = '1'
            empty_password += count

        elif item == '9':
            count = '2'
            empty_password += count

    return empty_password


def decode(encode_password):  # you will be finishing this function!
    joined_string_decoded = ""
    """ Abby is making changes to Anna's code in the encode function"""
    encoded_password2 = encode(encode_password)
    for char in encoded_password2:
        """converts each individual string character in the encoded password to an integer 
            value and assigns it to the variable int_pass"""
        int_pass = int(char)
        """subtracts three from the value of the individual string character in the encoded password"""
        subtracted_word = int_pass - 3
        print(subtracted_word)
        subtractedword_as_string = str(subtracted_word)
        """converts the endcoded individual integers into individual strings"""
        joined_string_decoded = joined_string_decoded + subtractedword_as_string
    print(joined_string_decoded)

    return joined_string_decoded

    """print statement that tells the user what the encoded password is and what the original 
           password is"""



def main():     # my main menu function

    while True:

        print("Menu")       # the menu itself
        print('-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')

        user_option = int(input("Please enter an option: "))

        if user_option == 1:
            encode_password = str(input("Please enter your password to encode:"))
            encode(encode_password)
            print("Your password has been encoded and stored!")
            print()

        elif user_option == 2:
            decode(encode_password)
            print(f"The encoded password is {encode(encode_password)} and the original password is {decode(encode_password)}")
            # f string where I inserted encode/decode functions.

        elif user_option == 3:
            break
            # ends the code

if __name__ == '__main__':
    main()
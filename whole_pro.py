print("1.Do you want to make hand gesture?")
print("2.Do you want to speak?")
print("\nPlease enter your choice:")
choice = int(input())
match choice:
    case 1:
        print("a.Do you want to recognize digits?")
        print("b.Do you want to recognize alphabets?")
        print("c.Do you want to recognize daily life actions?")

        print("\nPlease enter your choice:")
        ch=input()
        match ch:
            case 'a':
                import data_test_digit
            case 'b':
                import data_test_alpha
            case 'c':
                import data_test_actions
    case 2:
        import speech_txt




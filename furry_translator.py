

def break_text(text):
    text_list = []
    word = ""
    for character in text:
        if character.isalpha() or character.isnumeric() or character == "'":
            word += character  
        else:
            text_list.append(word)
            text_list.append(character)
            word = ""
    
    if word != "":
        text_list.append(word)
    
    return text_list
            


def furify_text(text_list):
    
    new_word = ""
    for i in range(len(text_list)):
        for character in text_list[i]:
            if character in "rl":
                new_word += "w"
            else:
                new_word += character
        
        text_list[i] = new_word
        new_word = ""


def list_to_string(list_):
    string = ""
    for element in list_:
        string += element
    
    return string

#test = break_text("This is a test to see how well the function is working. I'll list a few things: chicken, apple, banana :3 \n")
#furify_text(test)
#print(list_to_string(test))


if __name__ == "__main__":
    while True:
        print("Copy and paste your text and hit enter to translate: ")
        lines = []
        while True:
            line = input()
            if line:
                lines.append(line)
            else:
                break
        text = '\n'.join(lines)
        text = list_to_string(text)
        text_list = break_text(text)
        furify_text(text_list)
        print(list_to_string(text_list))
        
        if input("Would you like to continue [Y/N]").upper() == "N":
            break
        
    
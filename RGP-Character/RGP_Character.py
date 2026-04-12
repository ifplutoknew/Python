full_dot = '●'
empty_dot = '○'

def create_character(name, strength, intelligence, charisma):
    #Check if name is a string
    if not isinstance(name,str):
        return "The character name should be a string"
    
    #Check if empty
    if name=="":
        return "The character should have a name"
    
    #Check length
    if len(name)>10:
        return "The character name is too long"
    
    #Check spaces
    if " " in name:
        return "The character name should not contain spaces"
   
    #Check all stats are integers
    if not isinstance(strength,int) or not isinstance(intelligence,int) or not isinstance(charisma,int):
        return "All stats should be integers"
    if strength<1 or intelligence<1 or charisma<1:
        return "All stats should be no less than 1"
    if strength>4 or intelligence>4 or charisma>4:
        return "All stats should be no more than 4"
    if strength+intelligence+charisma !=7:
        return "The character should start with 7 points"
    
    #Create stat bars
    str_bar= full_dot*strength + empty_dot*(10-strength)
    int_bar= full_dot*intelligence + empty_dot*(10-intelligence)
    cha_bar= full_dot*charisma + empty_dot*(10-charisma)

    #return string
    return f"{name}\nSTR {str_bar}\nINT {int_bar}\nCHA {cha_bar}"

character_name=input("Enter a character name: ")
char_strength=int(input("Enter the character health: "))
char_intelligence=int(input("Enter the character intelligence: "))
char_charisma = int(input("Enter the character charisma: "))
character=create_character(character_name,char_strength,char_intelligence,char_charisma)
print(character)

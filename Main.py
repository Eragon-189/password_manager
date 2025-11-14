import random
file_path = "passwords.txt"
#add encription
separator1 = ""
separator2 = "\n"
def make_pass():
    password = []
    char_list=["1","2","3","4","5","6","7","8","9","0","!","#","$","%","^","&","*","(",")","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","<",">",",",".","/","?",";",":","{","}","[","]","-","_","+","=","~","`"]
    for i in range(16):
        random_char = char_list[random.randint(0, 71)]
        password.append(random_char)
    return make_string(password)



def read(line_number):
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()          # read all lines at once
            if line_number < len(lines):
                return lines[line_number].rstrip("\n")
            return None
    except FileNotFoundError:
        return None




def append(string):
    try:
        with open(file_path, "a") as file:
            file.write(str(string))
    except FileExistsError:
        pass


def make_string(list):
    string_list = [str(i) for i in list]
    return separator1.join(string_list)

def main():
    new_password = input("would you like to make a new password. y/n")
    #checks if you whant a new password
    if new_password == "y":
    #asks for email or username to be assosiated with the password
        user = input("Whats your email/username:")
    #sets user to lowercase
        user = user.lower()
    #asks for service
        service = input("whats service is this for:")
    #sets to lowercase
        service = service.lower()
        #make password
        temp_pass = make_pass()
        #print password 
        print("your password is:")
        print(temp_pass)
        #append data to file separated by " | "
        append(service)
        append(" | ")
        append(user)
        append(" | ")
        append(temp_pass)
    else:
        service = input("whats service is this for:")
        service = service.lower()
        x = 0
        while True:
            line = read(x)
              # ensure the line has the correct structure using '|' separators
            parts = [p.strip() for p in line.split("|")]
            if len(parts) == 3:              # must be: Service | Username | Password
                service_name, username, password = parts

                # compare only service names
                if service in service_name.lower():
                    print("Service | Username | Password")
                    print(service_name, " | ", username, " | ", password)
                    break
            x += 1





main()
import random
file_path = "passwords.txt"
#add encription
sepparator1 = ""
sepparator2 = "\n"
def make_pass():
    password = []
    char_list=["1","2","3","4","5","6","7","8","9","0","!","#","$","%","^","&","*","(",")","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","<",">",",",".","/","?",";",":","{","}","[","]","-","_","+","=","~","`"]
    for i in range(16):
        random_char = char_list[random.randint(0, 71)]
        password.append(random_char)
    return password



def read(line):

    try:
        with open(file_path, "r") as file:
            return file.readline(str(line))
    except FileExistsError:
        pass


def append(string):
    try:
        with open(file_path, "r") as file:
            file.write(sepparator1.join(str(string)))
    except FileExistsError:
        pass

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
        print(temp_pass)
        #append data to file separated by " | "
        append(service)
        append(" | ")
        append(user)
        append(" | ")
        append(temp_pass)
    else:
        #ask what sirvise thay whnt to fid password and uername for
        #find service by looping thu the file reading the line by calling read() function
        #print output


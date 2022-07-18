#Fiz de duas maneiras pois a primeira utilizei uma função já do python, a segunda maneira seria a mais "tradicional"

string = "teste"

#Primeira maneira 
print(string[::-1])

#Segunda maneira utilizando um loop
def inverte_string(string):
    nova_string = ""
    for i in string:
        nova_string = i + nova_string
    return(nova_string)

print(inverte_string(string))


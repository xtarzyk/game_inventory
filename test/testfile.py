def read_file():
    with open('E:/Dev/Python/second weekend/Homework2/game_inventory/file.txt') as fp:
         for line in fp.readlines():
             print(line)

read_file()


lista = ['jeden\n', 'dwa\n', 'trzy\n', 'cztery\n']

def write_to_file(towrite):
    with open("E:/Dev/Python/second weekend/Homework2/game_inventory/file.txt", "a") as fp:
        for var in towrite:
            fp.write(var)

write_to_file(lista)
print('Nowa zawartość pliku: ')
read_file()

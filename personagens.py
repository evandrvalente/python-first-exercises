characters_file = open("favorite-characters.txt", mode='w')

characters_file.write("Monkey D. Luffy\n")
characters_file.write("Uchiha Madara\n")
characters_file.write("Logan\n")
characters_file.write("Charizard\n")
characters_file.write("Takeshi Kovacs\n")

print('Goku', file=characters_file)

characters_list = ['John Snow\n', 'Jean Grey\n', 'Wanda Maximorf\n']
characters_file.writelines(characters_list)

characters_file.close()

file_name = 'dzest.txt'
add_1 = 'Man garšo mandarīni'
add_2 = 'Piparkūkas danco'

try:
    with open(file_name,'a', encoding='UFT=8') as fails:
        fails.write('\n',add_1)
    print(f'jauna informācija ir veiksmīgi pievienota failam"{file_name}".')

except FileExistsError:
    print(f'Kļūda: data "{file_name}" nav atrasta .')
except Exception as e:
    print(f'Kļūda: neparedzēta kļūda-{e}')
izdevumi = input('vai tev ir laikā nenodots izdevums?(j/n):')
if izdevumi == ('n'):
    saraksts = input('vai jūs esat skolēns?(j/n):')
    if saraksts == ('j'):
        publikacijas = input('vai jums ir nepieciešamas grāmatas?(j/n):')
        if publikacijas == ('j'):
            pieprasitie = input('vai jums ir nepieciešams izdevms, kas ir izdevumu sarakstā?(j/n)')
            if pieprasitie == ('j'):
                print('visas publikācijas izsniesdz uz 2 dienām.')
            elif pieprasitie == ('n'):
                print('skoleniem izsniedz uz 14 dienām.')
        elif publikacijas == ('n'):
            print('žurnālus isniedz ikvienam uz 7 dienām.')
    elif saraksts == ('n'):
        print('personālam izniedz uz 28 dienām.')
else:
    print('izdevumus aizliegts iegādāties.')



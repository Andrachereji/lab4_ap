def show_menu():
    print('1.Citire lista')
    print('2.Afisare partii intregi a tuturor numerelor din lista')
    print('3.Afisarea numerelor care apartin unui interval inchis cititi de la tastatura')
    print('4.Afisarea tuturor numerelor a caror parte intreaga este divizor al partii fractionare')
    print('x.Iesire')
def read_list():
    float_as_str = input('Dati o lista de float-uri separate prin spatiu')
    float_as_list_of_str = float_as_str.split(' ')
    floats = []
    for float_str in float_as_list_of_str:
        floats.append(float(float_str))
    return floats
def afisare_parte_intreaga(lst):
    '''
    Returneaza o lista doar cu partea intreaga a numerelor
    :param lst:o lista de float-uri
    :return: o lista cu prorpietatea ceruta
    '''
    result = []
    for elem in lst:
        str_elem = str(elem)
        if '.' in str(elem):
            parte_intreaga= str_elem.split('.')[0]
            result.append(int(parte_intreaga))
        else:
            result.append(elem)
    return result
def test_afisare_parte_intreaga():
    assert afisare_parte_intreaga([1.2, 4.5, 3]) == [1, 4, 3]
    assert afisare_parte_intreaga([]) == []
    assert afisare_parte_intreaga([1.3, 2.6, 4]) == [1, 2, 4]
def numere_din_interval(lst,capat1,capat2):
    '''
    Returneaza o lista cu toate numerele din intervalul [capat1,capat2]
    :param lst:o lista de float-uri
    :param capat1: capatul din stanga al intervalului
    :param capat2: capatul din dreapta a intervalului
    :return: o lista cu proprietatea ceruta
    '''
    result=[]
    for i in range(len(lst)):
        if lst[i]>=capat1 and lst[i]<=capat2:
            result.append(lst[i])
    return result
def test_numere_din_interval():
    assert numere_din_interval([1.2, 5, 4, -3],-4,4)==[1.2, 4, -3]
    assert numere_din_interval([], -4, 4) == []
    assert numere_din_interval([2.4, 5, 4, -3, 1.4, -2], -4, 4) == [2.4, 4, -3, 1.4, -2]
def intreg_divizor_fractionar(lst):
    '''
    Returneaza o lista cu toate numerele a caror parte intreaga este divizor a partii fractionare
    :param lst: o lista de float-uri
    :return: o lista cu proprietatile cerute
    '''
    result=[]
    for elem in lst:
        str_elem = str(elem)
        if '.' in str(elem):
            parte_intreaga= str_elem.split('.')[0]
            partea_fractionara=str_elem.split('.')[1]
            if int(partea_fractionara) % int(parte_intreaga) ==0:
                result.append(elem)
    return result
def test_intreg_divizor_fractionar():
    assert intreg_divizor_fractionar([1.5, -3.3, 8, 9.8, 3.2])==[1.5, -3.3]
    assert intreg_divizor_fractionar([]) == []
    assert intreg_divizor_fractionar([1.5, -3.3, 8.16, 9.8, 3.2]) == [1.5, -3.3, 8.16]

def main():
    lst = []
    while True:
        show_menu()
        optiune = input('Alegeti optiunea:')
        if optiune == '1':
            lst = read_list()
        elif optiune == '2':
            print(f'Lista cu partea intreaga a numerelor este {afisare_parte_intreaga(lst)}')
        elif optiune=='3':
            capat1=int(input('Dati capatul din stanga a intervalului:'))
            capat2=int(input('Dati capatul din dreapta a intervalului'))
            print(f'Numerele din interval sunt {numere_din_interval(lst,capat1,capat2)}')
        elif optiune=='4':
            print(f'numerele a caror parte intreaga este divizor al partii fractionare sunt: {intreg_divizor_fractionar(lst)}')
        elif optiune=='x':
            break
        else:
            print('Optiuneinvalida.Mai incearca!')


if __name__ == '__main__':
    test_afisare_parte_intreaga()
    test_numere_din_interval()
    test_intreg_divizor_fractionar()
    main()

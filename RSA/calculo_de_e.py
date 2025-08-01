from eh_primo import eh_primo
def calculo_de_e(tot):
    primo = 3
    if tot%2 != 0:
        return 2
    else:
        while True:
            if eh_primo(primo) and tot%primo != 0:
                return primo
            primo += 2

from menu_structure import CTG_COMMAND
from menu_structure import CTG_SUBMENU
from menu_structure import menu

OPT_MENU_BACK = '0'


def show_menu(item, can_go_back):
    """Visualizza su console un menu.

    Mostra il titolo e l'elenco degli elementi del menu con i rispettivi
    shortcut. Viene usato un progressivo numerico per gli elementi che non 
    hanno lo shortcut.

    Args:
        item (MenuItem): il menu da visualizzare
        can_go_back ([type]): flag che indica se da questo menu si può tornare 
        indietro

    Returns:
        dict: mappatura tra shortcut e elementi del menu
    """
    title = '\n\n<> MENU : %s <>' % item.item_name
    print(title)
    print('='*len(title))
    choices = dict()
    num = 1
    for option in item.items:
        key = option.shortcut
        if key is None:
            key = str(num)
            num += 1
        choices[key] = option
        print('%3s. %s' % (key, option.item_name))
    if can_go_back:
        print('%3s. %s' % (OPT_MENU_BACK, 'Previous menu'))
    print('-'*len(title))
    return choices


def process_menu_item(item, previous):
    """Elabora un elemento di menu.

    Se l'elemento passato è terminale (ha un comando) esegue il comando e
    restituisce il menu che lo contiene.

    Se l'elemento passato è un menu a sua volta, viene visualizzato il menu
    e l'utente deve scegliere un elemento.

    Args:
        item (namedtuple MenuItem): l'elemento da elaborare
        previous (namedtuple MenuItem): il menu precedente, passare `None` se
            si sta elaborando il menu principale (sopra quello non c'è nulla)

    Returns:
        MenuItem: se si elabora un menu è l'elemento selezionato, oppure il 
        menu precedente se l'utente decide di tornare indietro.
    """
    if item.category == CTG_COMMAND:
        # se ho passato un comando esegue il comando
        item.command()
        # e restituisce il menu che lo contiene
        return previous
    elif item.category == CTG_SUBMENU:
        # se è un menu, lo mostra, e ottiene la mappatura tra shortcut ed
        # elemento di menu
        choices = show_menu(item, previous is not None)
        choice = None
        valid_choice = False
        # loop di input
        while not valid_choice:
            choice = input('Your choice: _')
            choice = choice.upper()
            # la scelta dell'utente è valida se e solo se lo shortcut è
            # mappato (è nelle chiavi del dict) oppure se ho chiesto di
            # tornare indietro da un menu che non è quello principale
            valid_choice = choice in choices or \
                (choice == OPT_MENU_BACK and previous is not None)
            if not valid_choice:
                print('\tInvalid choice, please try again.')
            else:
                print()
        if choice == OPT_MENU_BACK:
            return previous
        else:
            return choices[choice]
    else:
        raise Exception('unknown item type')


def menu_main():
    # l'elemento corrente, all'inizio è in cima al menu
    current_item = menu
    # lo uso come stack, ci tengo l'ultimo menu che ho visitato
    history = [None]
    # loop continuo ==> il menu DEVE avere un comando di uscita per
    # chiudere il processo
    while True:
        # elabora l'elemento corrente del menu e ottiene il prossimo
        # elemento di menu da elaborare
        selected_item = process_menu_item(current_item, history[-1])
        if selected_item not in history:
            # se l'elemento selezionato non è nello stack vuol dire che sono
            # ad una "profondità" di menu più alta, quindi metto il menu
            # corrente sullo stack
            history.append(current_item)
            # e vado giù nel menu successivo
            current_item = selected_item
        else:
            # l'elemento richiesto è nello stack: questo accade solo quando
            # l'utente chiede di tornare indietro di un livello.
            current_item = history[-1]
            history.pop(-1)


if __name__ == "__main__":
    menu_main()

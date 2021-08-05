"""
Struttura del menu.
"""

from collections import namedtuple
import functions


CTG_COMMAND = 'MENU_CATEGORY_COMMAND'
CTG_SUBMENU = 'MENU_CATEGORY_SUBMENU'

"""
Il menu è un composito, ogni elemento può essere un comando o un menu a sua 
volta, contenendo altri elementi di menu.
NamedTuple è la svolta.

Category indica se si tratta di un comando (elemento terminale) o di un menu.
Shortcut è opzionale.
Items contiene ulteriori MenuItem nel caso di elementi non terminali.
Command è tipicamente un puntatore e funzione con il comando vero e proprio
da eseguire, nel caso di elementi terminali.
"""
MenuItem = namedtuple('MenuItem', 'item_name category shortcut items command')

menu = MenuItem('Main Menu', CTG_SUBMENU, None, [
    MenuItem('Greetings', CTG_SUBMENU, None, [
        MenuItem('Hello', CTG_COMMAND, None, [], functions.saluto_semplice),
        MenuItem('GoodbyTe', CTG_COMMAND, None, [], functions.commiato_semplice),
        MenuItem('Italian slurs', CTG_SUBMENU, None, [
            MenuItem('Fagiano', CTG_COMMAND, None, [], functions.saluto_insulto_fagiano),
            MenuItem('Maiale', CTG_COMMAND, 'M', [], functions.saluto_insulto_maiale),
            MenuItem('Tacchino', CTG_COMMAND, 'T', [], functions.saluto_insulto_tacchino)
        ], None),
    ], None),
    MenuItem('Maths', CTG_SUBMENU, None, [
        MenuItem('Square root of 2', CTG_COMMAND,
                 None, [], functions.root_of_2),
    ], None),
    MenuItem('Exit program', CTG_COMMAND, None, [], exit),
], None)

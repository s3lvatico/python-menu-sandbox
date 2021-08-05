"""menu.py

Definition of Armageddon menu building blocks.

"""

from collections import namedtuple

MENUITEM_TYPE_MENU = 'menu'
MENUITEM_TYPE_ITEM = 'item'

MenuItem = namedtuple('MenuItem', 'label item_type shortcut command items')

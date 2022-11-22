from enum import Enum


class SignalNames(Enum):
    PLACEHOLDER = 'placeholder'
    NEW_CATEGORY = 'new_category'
    REMOVE_CATEGORY = 'remove_category'
    LOCAL_UPDATE = 'local_update'
    GLOBAL_UPDATE = 'global_update'
    ITEM_UPDATE = 'item_update'
    ITEM_DELETE = 'item_delete'

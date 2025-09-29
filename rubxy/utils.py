from rubxy import types, enums

def anies(*args):
    return any(args)

def keypad_parse(chat_keypad, inline_keypad, chat_keypad_type=None):
    if anies(chat_keypad, inline_keypad):
        if isinstance(chat_keypad, types.Keypad):
            chat_keypad = chat_keypad._to_dict()
            chat_keypad_type = enums.ChatKeypadType.NEW if chat_keypad_type is enums.ChatKeypadType.NONE else chat_keypad_type

        elif isinstance(inline_keypad, types.Keypad):
            inline_keypad = inline_keypad._to_dict()
        else:
            raise TypeError("`chat_keypad` or `inline_keypad` must be of type types.Keypad")
    
        return chat_keypad, inline_keypad
    return None, None
import keyboard
import re



# Define the mapping for straight quotes to curly quotes
quote_mapping = {
    '"': ('“', '”'),    # Double straight quotes to opening and closing curly quotes
    "'": ('‘', '’')     # Single straight quotes to opening and closing curly quotes
}

# Define the state variable to track the quote key presses
quote_key_presses = {}
is_alphabet_char = False
set_space = False
alphabet_correct_char = True
# Callback function to replace the text input
def replace_quotes(event):
    global is_alphabet_char
    global set_space
    global alphabet_correct_char
    

    if event.event_type == keyboard.KEY_DOWN:
        typed_char = event.name
        if re.match(r'^[a-zA-Z]$', typed_char):
            is_alphabet_char = True
            
            if typed_char == 'i':
                alphabet_correct_char = False
            else:
                alphabet_correct_char = True

                
        if event.name == 'space':
                set_space = True
        else:
            if event.name != 'i' and event.name != 'space':
                set_space = False
        if event.name == 'i' and set_space == True:
                keyboard.send('backspace')
                keyboard.write('I')
        
                
            

        
        elif event.name in quote_mapping:
            

            if event.name not in quote_key_presses:
                quote_key_presses[event.name] = False

            if quote_key_presses[event.name]:
                opening_quote, closing_quote = quote_mapping[event.name]

                # Replace the previous quote with curly quotes
                keyboard.send('backspace')
                keyboard.send('backspace')
                
                if is_alphabet_char == True:
                    keyboard.write(closing_quote)
                    is_alphabet_char = False
                    quote_key_presses[event.name] = False
                else:
                    keyboard.write(opening_quote)
                    keyboard.write(closing_quote)
                    is_alphabet_char = False
                    quote_key_presses[event.name] = False

                # Reset the state
                
            else:
                quote_key_presses[event.name] = True
        else:
            for key in quote_key_presses:
                quote_key_presses[key] = False



# Hook the keypress event and replace the quotes
keyboard.hook(replace_quotes)
keyboard.wait()  # Wait for the script to be interrupted

# Cleanup: Unhook the keypress event
keyboard.unhook(replace_quotes)








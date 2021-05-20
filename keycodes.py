""" keycodes.py

holds definitions for the different keycodes we need 
for the editor window
"""

KEY_RETURN  = b'\r'

# special character keycodes
KEY_SPEC    = b'\xe0'
KEY_SPEC_1  = b'\000'

# these require that the special character was read / caught first
KEY_UP      = b'H'
KEY_DOWN    = b'P'
KEY_LEFT    = b'K'
KEY_RIGHT   = b'M'
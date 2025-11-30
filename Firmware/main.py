import board
import digitalio
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.keys import KC
from kmk.modules.macros import Macros
from kmk.modules.mouse_keys import MouseKeys
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys

# Create the keyboard object
keyboard = KMKKeyboard()

# Add modules
macros = Macros()
keyboard.modules.append(macros)

mouse = MouseKeys()
keyboard.modules.append(mouse)

media_keys = MediaKeys()
keyboard.extensions.append(media_keys)

encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)

# Define the row and column pins
keyboard.row_pins = (
    board.GP0,  # R1
    board.GP1,
    board.GP2,
    board.GP3,
    board.GP4,  # R5
    board.GP5,
)

keyboard.col_pins = (
    board.GP15,  # C1
    board.GP14,
    board.GP13,
    board.GP12,
    board.GP11,
    board.GP10,
    board.GP9,  # C7
    board.GP8,
    board.GP7,
    board.GP6,  # C10
    board.GP20,
    board.GP19,
    board.GP18,
    board.GP17,
    board.GP16,  # C15
)

keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Define keys with your specific layout and widths
_______ = KC.TRNS
xxxxxxx = KC.NO

# Keymap based on your JSON input
keyboard.keymap = [
    # Base (Layer 0)
    [
        KC.ESC,   KC.F1,   KC.F2, KC.F3,   KC.F4, KC.F5, KC.F6,    KC.F7, KC.F8, KC.F9,    KC.F10,  KC.F11,    KC.F12,   KC.NLCK,  KC.SLCK, KC.INS,   KC.MUTE,
        KC.GRAVE, KC.N1,   KC.N2, KC.N3,   KC.N4, KC.N5, KC.N6,    KC.N7, KC.N8, KC.N9,    KC.N0,   KC.MINUS,  KC.EQUAL, xxxxxxx,  KC.BSPC, KC.HOME,  xxxxxxx,
        KC.TAB,   xxxxxxx, KC.Q,  KC.W,    KC.E,  KC.R,  KC.T,     KC.Y,  KC.U,  KC.I,     KC.O,    KC.P,      KC.LBRC,  KC.RBRC,  KC.BSLS, KC.PGUP,  xxxxxxx,
        KC.CAPS,  xxxxxxx, KC.A,  KC.S,    KC.D,  KC.F,  KC.G,     KC.H,  KC.J,  KC.K,     KC.L,    KC.SCOLON, KC.QUOTE, KC.ENTER, KC.NO,   KC.PGDN,  xxxxxxx,
        xxxxxxx,  KC.LSFT, KC.Z,  KC.X,    KC.C,  KC.V,  KC.B,     KC.N,  KC.M,  KC.COMMA, KC.DOT,  KC.SLASH,  xxxxxxx,  KC.RSFT,  KC.UP,   KC.END,   xxxxxxx,
        KC.LCTRL, KC.LGUI, KC.NO, KC.LALT, xxxxxxx, xxxxxxx, KC.SPACE, xxxxxxx, xxxxxxx, xxxxxxx, KC.RALT, KC.MO(1), KC.RCTRL, KC.LEFT,  KC.DOWN, KC.RIGHT, xxxxxxx,
    ],

    # Fn (Layer 1)
    [
        xxxxxxx, KC.MUTE, KC.VOLD, KC.VOLU, KC.MPRV, KC.MPLY, KC.MNXT, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, KC.BRID, KC.BRIU, KC.PSCR, KC.PAUS, KC.DEL,  _______,
        xxxxxxx, KC.LSFT, KC.N1, KC.N2,   KC.N3,  KC.N4,  KC.N5,     KC.N6,  KC.N7,  KC.N8,   KC.N9,

COLORS = {
    "reset": "\x1b[0m",
    "black": "\x1b[30m",
    "red": "\x1b[31m",
    "green": "\x1b[32m",
    "yellow": "\x1b[33m",
    "blue": "\x1b[34m",
    "magenta": "\x1b[35m",
    "cyan": "\x1b[36m",
    "white": "\x1b[37m",
    "br_black": "\x1b[90m",
    "br_red": "\x1b[91m",
    "br_green": "\x1b[92m",
    "br_yellow": "\x1b[93m",
    "br_blue": "\x1b[94m",
    "br_magenta": "\x1b[95m",
    "br_cyan": "\x1b[96m",
    "br_white": "\x1b[97m",
    "black_bg": "\x1b[40m",
    "red_bg": "\x1b[41m",
    "green_bg": "\x1b[42m",
    "yellow_bg": "\x1b[43m",
    "blue_bg": "\x1b[44m",
    "magenta_bg": "\x1b[45m",
    "cyan_bg": "\x1b[46m",
    "white_bg": "\x1b[47m",
    "br_black_bg": "\x1b[100m",
    "br_red_bg": "\x1b[101m",
    "br_green_bg": "\x1b[102m",
    "br_yellow_bg": "\x1b[103m",
    "br_blue_bg": "\x1b[104m",
    "br_magenta_bg": "\x1b[105m",
    "br_cyan_bg": "\x1b[106m",
    "br_white_bg": "\x1b[107m"
}


def rgb_escape(r, g, b, background=False):
    return f"\x1b[{4 if background else 3}8;2;{r % 256};{g % 256};{b % 256}m"

def add_dish(menu, name, price):
    if name in menu:
        print(f"{name} already exists in the menu.")
        return
    menu[name] = {"name": name, "price": float(price), "available": True}

def remove_dish(menu, name):
    if name in menu:
        del menu[name]
    else:
        print(f"{name} not found in the menu.")

def update_price(menu, name, new_price):
    dish = menu.get(name)
    if not dish:
        print(f"{name} not found in the menu.")
        return
    dish["price"] = float(new_price)
    dish["available"] = True

def place_order(menu, name):
    dish = menu.get(name)
    if not dish:
        print(f"{name} not found in the menu.")
        return
    if not dish["available"]:
        print(f"{name} is already being prepared.")
        return
    dish["available"] = False

def _status_text(available):
    return "Available" if available else "Ordered"

def display_menu(menu):
    for dish in menu.values():
        print(f"{dish['name']} - ${dish['price']:.2f} - {_status_text(dish['available'])}")

def display_menu_table(menu):
    # Render a simple table without requiring 'tabulate'; use colorama if available for colors.
    try:    
        from colorama import init, Fore, Style
        init(autoreset=True)
        color_enabled = True
    except Exception:
        # colorama not available -> proceed without colors
        color_enabled = False
        # provide no-op color placeholders
        class _NoColor:
            GREEN = ""
            YELLOW = ""
            RESET_ALL = ""
        Fore = Style = _NoColor()

    headers = ["Dish", "Price", "Status"]
    rows = []
    for dish in menu.values():
        status_text = "Available" if dish["available"] else "Ordered"
        if color_enabled:
            status = (Fore.GREEN + status_text + Style.RESET_ALL) if dish["available"] else (Fore.YELLOW + status_text + Style.RESET_ALL)
        else:
            status = status_text
        rows.append([dish["name"], f"${dish['price']:.2f}", status])

    # helper to strip ANSI sequences when measuring widths
    import re
    ansi_escape = re.compile('\x1b\\[[0-9;]*m')

    def _display_len(s):
        return len(ansi_escape.sub('', str(s)))

    # compute column widths
    col_widths = []
    for col in range(len(headers)):
        max_width = _display_len(headers[col])
        for row in rows:
            max_width = max(max_width, _display_len(row[col]))
        col_widths.append(max_width)

    # print header
    header_line = " | ".join(headers[i].ljust(col_widths[i]) for i in range(len(headers)))
    sep_line = "-|-".join("-" * col_widths[i] for i in range(len(headers)))
    print(header_line)
    print(sep_line)
    # print rows
    for row in rows:
        line = " | ".join(str(row[i]).ljust(col_widths[i] + (len(row[i]) - _display_len(row[i]))) for i in range(len(row)))
        print(line)
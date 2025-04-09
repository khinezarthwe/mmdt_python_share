color_values = {'red': ['5'], 'blue': ['0'], 'green': ['']}

# Green:      0
# Blue:         0
# Red:          5
# Opacity:   0

print("Red    ", int(color_values['red'][0]))
print("Blue    ", int(color_values['blue'][0]))
print("Green    ", int(color_values['green'][0] or 0))
print("Opacity    ", int(color_values.get('opacity', [''])[0] or 0))
print("Yellow    ", int(color_values.get('yellow', [''])[0] or 0))

def get_init_value_from_color(color_with_values: dict, color: str, default = 0) -> int:
    """
    get the first str value from dict if exist else return 0
    :param color_with_values:
    :param color:
    :param default:
    :return:
    """
    color_found = color_with_values.get(color, [''])
    if color_found[0]:
        return int(color_found[0])
    else:
        return default


print("Red with function  ", get_init_value_from_color(color_values, 'red'))
print("Blue with function  ", get_init_value_from_color(color_values, 'blue'))
print("Green with function  ", get_init_value_from_color(color_values, 'green'))
print("Opacity with function  ", get_init_value_from_color(color_values, 'opacity'))

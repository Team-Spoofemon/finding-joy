def paint_color_picker(base10text):
    lines = [ele for ele in base10text.splitlines() if ele]
    return f'#{"".join([hex(int(ele))[2:] for ele in lines])}'


dopey = '''228
196
146'''
paint_color_picker(dopey)

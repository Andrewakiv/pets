menu = [
    {'title': "About", 'url_name': 'pts:about'},
    {'title': "Add page", 'url_name': 'pts:add_page'},
    {'title': "Contact", 'url_name': 'pts:contact'},
]


def get_mainmenu(request):
    return {'mainmenu': menu}

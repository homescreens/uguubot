import urlparse
import re
from util import hook, http

@hook.command('isup')
@hook.command
def isdown(inp):
    "isdown <url> -- Checks if the site at <url> is up or down."

    if 'http://' not in inp:
        inp = 'http://' + inp

    inp = 'http://' + urlparse.urlparse(inp).netloc

    # http://mail.python.org/pipermail/python-list/2006-December/589854.html
    try:
        http.get(inp, get_method='HEAD')
        return inp + ' seems to be up'
    except http.URLError:
        return inp + ' seems to be down'

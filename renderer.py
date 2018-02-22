def render(file_name, context=None):
    with open(file_name, 'r') as html_file:
        html = html_file.read()
        if context:
            html = _replacer(context, html)
        return html

def _replacer(context, html):
    """
    html = 'dvdfv{text}sdc{second}sdc'
    context = {'text': '!avt!', 'second': '!aaa!'}
    """
    for k in context.keys():
        ready_key = '{' + k + '}'
        html = html.replace(ready_key, context[k])
    return html

from decorators import address
from helpers import send_response, write_to_db
from renderer import render


@address('about')
def about_handler(request, conn, match=True, data={}):
    template = "about.html"
    abc = render(template)
    resp = """\
    HTTP/1.1 200 OK

    {0}
    """.format(abc)

    send_response(resp, conn, match)



# @address('shop')
# def shop_handler(request, conn, match=True):
#     template = "shop.html"
#     render(template, conn, match)

@address('contacts')
def contact_handler(request, conn, match=True,data={}):
    template = "contacts.html"
    content = render(template)
    resp = """\
    HTTP/1.1 200 OK

    {0}
    """.format(content)
    write_to_db(match,data)
    send_response(resp, conn, match)


@address('products')
def products_handler(request, conn, match=True,data={}):
    resp = """\
    HTTP/1.1 200 OK

    This is product page
    """
    send_response(resp, conn, match)

import urllib.parse

def whatsapp_global(request):

    mensagem = urllib.parse.quote(
        "Olá! Acabei de conhecer o site da GessoPlac e gostaria de receber um orçamento."
    )

    return {

        'whatsapp_site': (
            f"https://wa.me/553432557975?text={mensagem}"
        )
    }
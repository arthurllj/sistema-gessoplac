from django.shortcuts import render
from django.template.loader import render_to_string
from weasyprint import HTML
from django.http import HttpResponse

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


def index(request):
    return render(request, 'orcamento/index.html')


def calcular_orcamento(request):
    return render(request, 'orcamento.html')


def orcamento(request):
    return render(request, 'orcamento.html')

def localizacao(request):
    return render(request, "orcamento/localizacao.html")


def produtos(request):
    produtos = [
        {
            "nome": "Chapas Drywall",
            "descricao": "Chapas utilizadas para paredes, forros e divisórias em sistemas de construção a seco.",
            "imagem": "img/drywall.jpg",
            "alt": "Drywall",
            "beneficios": [
                "Alta resistência",
                "Instalação rápida",
                "Excelente acabamento"
            ],
            "marcas": "Knauf • Placo • Trevo"
        },
        {
            "nome": "Perfis Metálicos",
            "descricao": "Estrutura metálica utilizada para montagem de paredes e forros em drywall.",
            "imagem": "img/perfil.jpg",
            "alt": "Perfis",
            "beneficios": [
                "Alta durabilidade",
                "Estrutura resistente",
                "Compatível com sistemas drywall"
            ]
        },
        {
            "nome": "Parafusos",
            "descricao": "Parafusos específicos para fixação das chapas drywall na estrutura metálica.",
            "imagem": "img/parafuso.jpg",
            "alt": "Parafusos",
            "beneficios": [
                "Alta fixação",
                "Resistência mecânica",
                "Instalação rápida"
            ],
            "marcas": "Âncora • Plaster • Walsywa • Placo • Patta",
            "tamanhos": "13mm • 19mm • 25mm • 35mm • 45mm",
            "tipos": "Ponta agulha • Ponta broca"
        },
        {
            "nome": "Massa para Drywall",
            "descricao": "Utilizada para acabamento e tratamento de juntas entre chapas drywall.",
            "imagem": "img/massa.jpg",
            "alt": "Massa",
            "beneficios": [
                "Acabamento profissional",
                "Fácil aplicação",
                "Alta aderência"
            ],
            "marcas": "Trevo • Placo • Construcril • Multiperfil • Knauf • Placlux",
            "tamanhos": "6kg • 14kg • 25kg"
        },
        {
            "nome": "Fita para Junta",
            "descricao": "Utilizada para reforço e acabamento nas juntas entre chapas drywall.",
            "imagem": "img/fita.jpg",
            "alt": "Fita",
            "beneficios": [
                "Reforço das juntas",
                "Evita fissuras",
                "Melhor acabamento"
            ],
            "marcas": "Âncora • Walsywa • Placo"
        },
        {
            "nome": "Ferramentas",
            "descricao": "Ferramentas profissionais utilizadas na instalação de sistemas drywall.",
            "imagem": "img/ferramenta.jpg",
            "alt": "Ferramentas",
            "beneficios": [
                "Alta durabilidade",
                "Uso profissional",
                "Precisão na instalação"
            ]
        },
        {
            "nome": "Gesso",
            "descricao": "Gesso utilizado para molduras, sancas, acabamentos e aplicações decorativas.",
            "imagem": "img/gesso.jpg",
            "alt": "Gesso",
            "beneficios": [
                "Acabamento decorativo",
                "Fácil moldagem",
                "Alta qualidade"
            ],
            "marcas": "São Francisco",
            "tamanhos": "40kg"
        },
        {
            "nome": "Portas Prontas",
            "descricao": "Portas prontas para instalação rápida em drywall e alvenaria.",
            "imagem": "img/porta.jpg",
            "alt": "Portas",
            "beneficios": [
                "Instalação rápida",
                "Ótimo acabamento",
                "Alta durabilidade"
            ],
            "vãos": "Vão de 60cm • Vão de 70cm • Vão de 80cm • Vão de 90cm",
            "tamanhos": "2,10m",
        },
        {
            "nome": "Lã de Isolamento",
            "descricao": "Lãs minerais para isolamento acústico e térmico em paredes e forros drywall.",
            "imagem": "img/la.jpg",
            "alt": "Lã de isolamento",
            "beneficios": [
                "Isolamento acústico",
                "Isolamento térmico",
                "Melhora o conforto do ambiente"
            ]
        },
        {
            "nome": "Caibros e Estruturas para Telhados",
            "descricao": "Estruturas metálicas e componentes utilizados na montagem de telhados e coberturas.",
            "imagem": "img/caibro.jpg",
            "alt": "Caibros e estruturas para telhados",
            "beneficios": [
                "Alta resistência estrutural",
                "Durabilidade elevada",
                "Ideal para coberturas e telhados"
            ],
            "tipos": "Caibros • Ripas • Terças • Vigas",
            "tamanhos": "Varia conforme o projeto",
            "chapas": "#0,80mm • #0,90mm • #0,95mm"
        },
        {
            "nome": "Placas Cimentícias",
            "descricao": "Placas resistentes à umidade e impactos, ideais para áreas externas e fachadas.",
            "imagem": "img/cimenticia.jpg",
            "alt": "Placas cimentícias",
            "beneficios": [
                "Resistência à umidade",
                "Alta durabilidade",
                "Excelente para áreas externas"
            ],
            "marcas": "Brasilit",
            "tamanhos": "1.20x2.40m",
            "espessuras": "6mm • 8mm • 10mm"
        },
        {
            "nome": "Placa Glasroc",
            "descricao": "Placas especiais para sistemas externos, fachadas e ambientes com alta exposição climática.",
            "imagem": "img/glasroc.jpg",
            "alt": "Placa Glasroc",
            "beneficios": [
                "Alta resistência externa",
                "Proteção contra umidade",
                "Ideal para fachadas drywall"
            ],
            "marcas": "Placo • Trevo",
            "tamanhos": "1.20x2.40m"
        },
    ]

    return render(request, 'orcamento/produtos.html', {'produtos': produtos})

def sobre(request):
    return render(request, "orcamento/sobre.html")

import math


import math


# =====================================================
# ORÇAMENTO
# =====================================================

def calcular_orcamento(request):

    materiais = []
    link_whatsapp = ""

    if request.method == "POST":

        try:

            sistema = request.POST.get("sistema")

            placa = request.POST.get("placa")

            altura = float(request.POST.get("altura"))

            largura = float(request.POST.get("largura"))

            area = altura * largura

            # =====================================================
            # PAREDE DRYWALL
            # =====================================================

            if sistema == "parede":

                # ----------------------------------
                # PERFIL AUTOMÁTICO
                # ----------------------------------

                if altura <= 2.10:

                    perfil = "48"

                else:

                    perfil = "70"

                # ----------------------------------
                # PLACA ESCOLHIDA
                # ----------------------------------

                if placa == "180_st":

                    tipo_chapa = "Placa ST 120x180"
                    coef_placa = 0.486

                elif placa == "180_ru":

                    tipo_chapa = "Placa RU 120x180"
                    coef_placa = 0.486

                else:

                    tipo_chapa = "Placa ST 120x240"
                    coef_placa = 0.364


                # ----------------------------------
                # CÁLCULOS
                # ----------------------------------

                chapas= math.ceil(area * coef_placa) * 2
                

                montantes = math.ceil(area * 0.766)

                guias = math.ceil(area * 0.233)

                fita = math.ceil(area * 0.0325)

                parafuso_13_real = montantes * 4

                parafuso_13 = max(1, math.ceil(parafuso_13_real / 100))

                parafuso_25 = math.ceil((chapas * 40) / 100)
                
                massa_kg = math.ceil(area * 1.2)
                
                if massa_kg <= 6:
                    massa_nome = "Massa Pronta 6kg"
                    massa_qtd = 1

                elif massa_kg <= 14:
                    massa_nome = "Massa Pronta 14kg"
                    massa_qtd = 1

                else:
                    massa_nome = "Massa Pronta 25kg"
                    massa_qtd = math.ceil(massa_kg / 25)

                # ----------------------------------
                # LISTA FINAL
                # ----------------------------------

                materiais = [

                    {
                        "nome": tipo_chapa,
                        "quantidade": f"{chapas} chapas"
                    },

                    {
                        "nome": f"Montante M{perfil}",
                        "quantidade": f"{montantes} barras"
                    },

                    {
                        "nome": f"Guia G{perfil}",
                        "quantidade": f"{guias} barras"
                    },

                    {
                        "nome": "Fita Telada 90m",
                        "quantidade": f"{fita} rolo"
                    },

                    {
                         "nome": "Parafuso PA 13mm",
                        "quantidade": f"{parafuso_13} cento(s)"
                    },

                    {
                        "nome": "Parafuso GN 25mm",
                        "quantidade": f"{parafuso_25} cento(s)"
                    },
                ]

                if massa_kg <= 6:
                    massa_nome = "Massa Pronta 6kg"
                    massa_qtd = 1
                elif massa_kg <= 14:
                    massa_nome = "Massa Pronta 14kg"
                    massa_qtd = 1
                else:
                    massa_nome = "Massa Pronta 25kg"
                    massa_qtd = math.ceil(massa_kg / 25)

                materiais.append({
                    "nome": massa_nome,
                    "quantidade": f"{massa_qtd} unidade{'s' if massa_qtd != 1 else ''}"
                })

                mensagem = "ORÇAMENTO PAREDE:%0A%0A"

            # =====================================================
            # FORRO F530
            # =====================================================

            elif sistema == "forro":

                # ----------------------------------
                # PLACA ESCOLHIDA
                # ----------------------------------

                if placa == "180_st":

                    tipo_chapa = "Placa ST 120x180"
                    coef_placa = 0.486

                elif placa == "180_ru":

                    tipo_chapa = "Placa RU 120x180"
                    coef_placa = 0.486

                else:

                    tipo_chapa = "Placa ST 120x240"
                    coef_placa = 0.364

                # ----------------------------------
                # CÁLCULOS
                # ----------------------------------

                perfil_f530 = math.ceil(area * 0.60)

                placas = math.ceil(area * coef_placa)

                tabica = math.ceil(area * 0.35)

                fita = math.ceil(area * 0.016)

                #----------------------------------
                # 0,5 parafusos por m²
                # multiplicado por dupla fixação

                parafuso_13_real = (area * 0.5) * 2
                parafuso_13 = math.ceil(parafuso_13_real)
                # ----------------------------------
                # 40 parafusos GN25 por chapa
                parafuso_25 = math.ceil((chapas * 40) / 100)

                prego = math.ceil((tabica * 5) / 100)

                regulador = math.ceil(perfil_f530 * 2.5)

                tirante_metros = regulador * 1

                tirante = math.ceil(tirante_metros / 3)

                massa_kg = math.ceil(area * 1.2)

                if massa_kg <= 6:
                    massa_nome = "Massa Pronta 6kg"
                    massa_qtd = 1
                elif massa_kg <= 14:
                    massa_nome = "Massa Pronta 14kg"
                    massa_qtd = 1
                else:
                    massa_nome = "Massa Pronta 25kg"
                    massa_qtd = math.ceil(massa_kg / 25)

                # ----------------------------------
                # LISTA FINAL
                # ----------------------------------

                materiais = [

                    {
                        "nome": "Perfil F530 - 3m",
                        "quantidade": f"{perfil_f530} barras"
                    },

                    {
                        "nome": tipo_chapa,
                        "quantidade": f"{placas} chapas"
                    },

                    {
                        "nome": "Tabica",
                        "quantidade": f"{tabica} barras"
                    },

                    {
                        "nome": "Fita Telada 90m",
                        "quantidade": f"{fita} rolo"
                    },

                    {
                         "nome": "Parafuso PA 13mm",
                        "quantidade": f"{parafuso_13} cento(s)"
                    },

                    {
                        "nome": "Parafuso GN 25mm",
                        "quantidade": f"{parafuso_25} cento(s)"
                    },
                    
                    {
                        "nome": "Prego de Aço 15x15",
                        "quantidade": f"{prego} cento(s)"
                    },

                    {
                        "nome": "Presilha Reguladora F530",
                        "quantidade": f"{regulador} peças"
                    },

                    {
                        "nome": "Tirante",
                        "quantidade": f"{tirante} unidades"
                    },

                    {
                        "nome": massa_nome,
                        "quantidade": f"{massa_qtd} balde(s)"
                    },

                ]

                mensagem = "ORÇAMENTO FORRO:%0A%0A"

            # =====================================================
            # WHATSAPP
            # =====================================================

            for item in materiais:

                mensagem += (
                    f"{item['nome']}: "
                    f"{item['quantidade']}%0A"
                )

            link_whatsapp = (
                f"https://wa.me/553432557975?text={mensagem}"
            )

        except Exception as e:
            print(e)
            materiais = []

    request.session['materiais'] = materiais
    
    return render(
        request,
        "orcamento/orcamento.html",
        {
            "materiais": materiais,
            "link_whatsapp": link_whatsapp
        }
    )
    
def contato(request):
    return render(request, 'orcamento/contato.html')

def gerar_pdf(request):

    materiais = request.session.get('materiais', [])

    html_string = render_to_string(
        'orcamento/pdf.html',
        {
            'materiais': materiais
        }
    )

    html = HTML(string=html_string)

    pdf = html.write_pdf()

    response = HttpResponse(
        pdf,
        content_type='application/pdf'
    )

    response['Content-Disposition'] = \
        'filename="orcamento-gessoplac.pdf"'

    return response
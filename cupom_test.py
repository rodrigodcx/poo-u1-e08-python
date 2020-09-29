# coding: utf-8

import cupom
import pytest


def verifica_campo_obrigatorio_objeto(mensagem_esperada, loja):
    with pytest.raises(Exception) as excinfo:
        cupom.dados_loja_objeto(loja)
    the_exception = excinfo.value
    assert mensagem_esperada == str(the_exception)


# Todas as variaveis preenchidas
NOME_LOJA = "Loja 1"
LOGRADOURO = "Log 1"
NUMERO = 10
COMPLEMENTO = "C1"
BAIRRO = "Bai 1"
MUNICIPIO = "Mun 1"
ESTADO = "E1"
CEP = "11111-111"
TELEFONE = "(11) 1111-1111"
OBSERVACAO = "Obs 1"
CNPJ = "11.111.111/1111-11"
INSCRICAO_ESTADUAL = "123456789"


LOJA_COMPLETA = cupom.Loja(NOME_LOJA, LOGRADOURO, NUMERO, COMPLEMENTO, BAIRRO,
                           MUNICIPIO, ESTADO, CEP, TELEFONE, OBSERVACAO, CNPJ,
                           INSCRICAO_ESTADUAL)

TEXTO_ESPERADO_LOJA_COMPLETA = """Loja 1
Log 1, 10 C1
Bai 1 - Mun 1 - E1
CEP:11111-111 Tel (11) 1111-1111
Obs 1
CNPJ: 11.111.111/1111-11
IE: 123456789"""


def test_loja_completa():
    assert (
        cupom.dados_loja_objeto(LOJA_COMPLETA) == TEXTO_ESPERADO_LOJA_COMPLETA
    )


LOJA_NOME_NULO = cupom.Loja(None, LOGRADOURO, NUMERO, COMPLEMENTO, BAIRRO,
                            MUNICIPIO, ESTADO, CEP, TELEFONE, OBSERVACAO, CNPJ,
                            INSCRICAO_ESTADUAL)

LOJA_NOME_VAZIO = cupom.Loja("", LOGRADOURO, NUMERO, COMPLEMENTO, BAIRRO,
                             MUNICIPIO, ESTADO, CEP, TELEFONE, OBSERVACAO, CNPJ,
                             INSCRICAO_ESTADUAL)

MENSAGEM_NOME_OBRIGATORIO = "O campo nome da loja é obrigatório"


def test_valida_nome():
    verifica_campo_obrigatorio_objeto(MENSAGEM_NOME_OBRIGATORIO,
                                      LOJA_NOME_NULO)
    verifica_campo_obrigatorio_objeto(MENSAGEM_NOME_OBRIGATORIO,
                                      LOJA_NOME_VAZIO)


LOJA_LOGRADOURO_NULO = cupom.Loja(NOME_LOJA, None, NUMERO, COMPLEMENTO, BAIRRO,
                                  MUNICIPIO, ESTADO, CEP, TELEFONE, OBSERVACAO, CNPJ,
                                  INSCRICAO_ESTADUAL)

LOJA_LOGRADOURO_VAZIO = cupom.Loja(NOME_LOJA, "", NUMERO, COMPLEMENTO, BAIRRO,
                                   MUNICIPIO, ESTADO, CEP, TELEFONE, OBSERVACAO, CNPJ,
                                   INSCRICAO_ESTADUAL)

MENSAGEM_LOGRADOURO_OBRIGATORIO = "O campo logradouro do endereço é obrigatório"


def test_valida_logradouro():
    verifica_campo_obrigatorio_objeto(MENSAGEM_LOGRADOURO_OBRIGATORIO,
                                      LOJA_LOGRADOURO_NULO)
    verifica_campo_obrigatorio_objeto(MENSAGEM_LOGRADOURO_OBRIGATORIO,
                                      LOJA_LOGRADOURO_VAZIO)


LOJA_NUMERO_ZERO = cupom.Loja(NOME_LOJA, LOGRADOURO, 0, COMPLEMENTO, BAIRRO,
                              MUNICIPIO, ESTADO, CEP, TELEFONE, OBSERVACAO, CNPJ,
                              INSCRICAO_ESTADUAL)

LOJA_NUMERO_NULO = cupom.Loja(NOME_LOJA, LOGRADOURO, None, COMPLEMENTO, BAIRRO,
                              MUNICIPIO, ESTADO, CEP, TELEFONE, OBSERVACAO, CNPJ,
                              INSCRICAO_ESTADUAL)

LOJA_NUMERO_VAZIO = cupom.Loja(NOME_LOJA, LOGRADOURO, "", COMPLEMENTO, BAIRRO,
                               MUNICIPIO, ESTADO, CEP, TELEFONE, OBSERVACAO, CNPJ,
                               INSCRICAO_ESTADUAL)


TEXTO_ESPERADO_SEM_NUMERO = """Loja 1
Log 1, s/n C1
Bai 1 - Mun 1 - E1
CEP:11111-111 Tel (11) 1111-1111
Obs 1
CNPJ: 11.111.111/1111-11
IE: 123456789"""


def test_valida_numero():
    assert (cupom.dados_loja_objeto(LOJA_NUMERO_ZERO)
            == TEXTO_ESPERADO_SEM_NUMERO)
    assert (cupom.dados_loja_objeto(LOJA_NUMERO_VAZIO)
            == TEXTO_ESPERADO_SEM_NUMERO)
    assert (cupom.dados_loja_objeto(LOJA_NUMERO_NULO)
            == TEXTO_ESPERADO_SEM_NUMERO)


LOJA_COMPLEMENTO_NULO = cupom.Loja(NOME_LOJA, LOGRADOURO, NUMERO, None, BAIRRO,
                                   MUNICIPIO, ESTADO, CEP, TELEFONE, OBSERVACAO, CNPJ,
                                   INSCRICAO_ESTADUAL)

LOJA_COMPLEMENTO_VAZIO = cupom.Loja(NOME_LOJA, LOGRADOURO, NUMERO, "", BAIRRO,
                                    MUNICIPIO, ESTADO, CEP, TELEFONE, OBSERVACAO, CNPJ,
                                    INSCRICAO_ESTADUAL)

TEXTO_ESPERADO_SEM_COMPLEMENTO = """Loja 1
Log 1, 10
Bai 1 - Mun 1 - E1
CEP:11111-111 Tel (11) 1111-1111
Obs 1
CNPJ: 11.111.111/1111-11
IE: 123456789"""


def test_valida_complemento():
    assert (cupom.dados_loja_objeto(LOJA_COMPLEMENTO_NULO)
            == TEXTO_ESPERADO_SEM_COMPLEMENTO)
    assert (cupom.dados_loja_objeto(LOJA_COMPLEMENTO_VAZIO)
            == TEXTO_ESPERADO_SEM_COMPLEMENTO)


LOJA_BAIRRO_NULO = cupom.Loja(NOME_LOJA, LOGRADOURO, NUMERO, COMPLEMENTO, None,
                              MUNICIPIO, ESTADO, CEP, TELEFONE, OBSERVACAO, CNPJ,
                              INSCRICAO_ESTADUAL)

LOJA_BAIRRO_VAZIO = cupom.Loja(NOME_LOJA, LOGRADOURO, NUMERO, COMPLEMENTO, "",
                               MUNICIPIO, ESTADO, CEP, TELEFONE, OBSERVACAO, CNPJ,
                               INSCRICAO_ESTADUAL)

TEXTO_ESPERADO_SEM_BAIRRO = """Loja 1
Log 1, 10 C1
Mun 1 - E1
CEP:11111-111 Tel (11) 1111-1111
Obs 1
CNPJ: 11.111.111/1111-11
IE: 123456789"""


def test_valida_bairro():
    assert (cupom.dados_loja_objeto(LOJA_BAIRRO_NULO)
            == TEXTO_ESPERADO_SEM_BAIRRO)
    assert (cupom.dados_loja_objeto(LOJA_BAIRRO_VAZIO)
            == TEXTO_ESPERADO_SEM_BAIRRO)


LOJA_MUNICIPIO_NULO = cupom.Loja(NOME_LOJA, LOGRADOURO, NUMERO, COMPLEMENTO,
                                 BAIRRO, None, ESTADO, CEP, TELEFONE,
                                 OBSERVACAO, CNPJ, INSCRICAO_ESTADUAL)
LOJA_MUNICIPIO_VAZIO = cupom.Loja(NOME_LOJA, LOGRADOURO, NUMERO, COMPLEMENTO,
                                  BAIRRO, "", ESTADO, CEP, TELEFONE,
                                  OBSERVACAO, CNPJ, INSCRICAO_ESTADUAL)


def test_valida_municipio():
    verifica_campo_obrigatorio_objeto(
        "O campo município do endereço é obrigatório", LOJA_MUNICIPIO_NULO)
    verifica_campo_obrigatorio_objeto(
        "O campo município do endereço é obrigatório", LOJA_MUNICIPIO_VAZIO)


LOJA_ESTADO_NULO = cupom.Loja(NOME_LOJA, LOGRADOURO, NUMERO, COMPLEMENTO,
                              BAIRRO, MUNICIPIO, None, CEP, TELEFONE,
                              OBSERVACAO, CNPJ, INSCRICAO_ESTADUAL)
LOJA_ESTADO_VAZIO = cupom.Loja(NOME_LOJA, LOGRADOURO, NUMERO, COMPLEMENTO,
                               BAIRRO, MUNICIPIO, "", CEP, TELEFONE,
                               OBSERVACAO, CNPJ, INSCRICAO_ESTADUAL)


def test_valida_estado():
    verifica_campo_obrigatorio_objeto(
        "O campo estado do endereço é obrigatório", LOJA_ESTADO_NULO)
    verifica_campo_obrigatorio_objeto(
        "O campo estado do endereço é obrigatório", LOJA_ESTADO_NULO)


LOJA_CEP_NULO = cupom.Loja(NOME_LOJA, LOGRADOURO, NUMERO, COMPLEMENTO,
                           BAIRRO, MUNICIPIO, ESTADO, None, TELEFONE,
                           OBSERVACAO, CNPJ, INSCRICAO_ESTADUAL)
LOJA_CEP_VAZIO = cupom.Loja(NOME_LOJA, LOGRADOURO, NUMERO, COMPLEMENTO,
                            BAIRRO, MUNICIPIO, ESTADO, "", TELEFONE,
                            OBSERVACAO, CNPJ, INSCRICAO_ESTADUAL)

TEXTO_ESPERADO_SEM_CEP = """Loja 1
Log 1, 10 C1
Bai 1 - Mun 1 - E1
Tel (11) 1111-1111
Obs 1
CNPJ: 11.111.111/1111-11
IE: 123456789"""


def test_valida_cep():
    assert cupom.dados_loja_objeto(LOJA_CEP_NULO) == TEXTO_ESPERADO_SEM_CEP
    assert cupom.dados_loja_objeto(LOJA_CEP_VAZIO) == TEXTO_ESPERADO_SEM_CEP


LOJA_TELEFONE_NULO = cupom.Loja(NOME_LOJA, LOGRADOURO, NUMERO, COMPLEMENTO,
                                BAIRRO, MUNICIPIO, ESTADO, CEP, None,
                                OBSERVACAO, CNPJ, INSCRICAO_ESTADUAL)
LOJA_TELEFONE_VAZIO = cupom.Loja(NOME_LOJA, LOGRADOURO, NUMERO, COMPLEMENTO,
                                 BAIRRO, MUNICIPIO, ESTADO, CEP, "",
                                 OBSERVACAO, CNPJ, INSCRICAO_ESTADUAL)

TEXTO_ESPERADO_SEM_TELEFONE = """Loja 1
Log 1, 10 C1
Bai 1 - Mun 1 - E1
CEP:11111-111
Obs 1
CNPJ: 11.111.111/1111-11
IE: 123456789"""


def test_sem_telefone():
    assert cupom.dados_loja_objeto(
        LOJA_TELEFONE_NULO) == TEXTO_ESPERADO_SEM_TELEFONE
    assert cupom.dados_loja_objeto(
        LOJA_TELEFONE_VAZIO) == TEXTO_ESPERADO_SEM_TELEFONE


LOJA_OBSERVACAO_NULA = cupom.Loja(NOME_LOJA, LOGRADOURO, NUMERO, COMPLEMENTO,
                                  BAIRRO, MUNICIPIO, ESTADO, CEP, TELEFONE,
                                  None, CNPJ, INSCRICAO_ESTADUAL)
LOJA_OBSERVACAO_VAZIA = cupom.Loja(NOME_LOJA, LOGRADOURO, NUMERO, COMPLEMENTO,
                                   BAIRRO, MUNICIPIO, ESTADO, CEP, TELEFONE,
                                   "", CNPJ, INSCRICAO_ESTADUAL)

TEXTO_ESPERADO_SEM_OBSERVACAO = """Loja 1
Log 1, 10 C1
Bai 1 - Mun 1 - E1
CEP:11111-111 Tel (11) 1111-1111

CNPJ: 11.111.111/1111-11
IE: 123456789"""


def test_valida_observacao():
    assert cupom.dados_loja_objeto(LOJA_OBSERVACAO_NULA)
    == TEXTO_ESPERADO_SEM_OBSERVACAO
    assert cupom.dados_loja_objeto(LOJA_OBSERVACAO_VAZIA)
    == TEXTO_ESPERADO_SEM_OBSERVACAO


LOJA_CNPJ_NULO = cupom.Loja(NOME_LOJA, LOGRADOURO, NUMERO, COMPLEMENTO,
                            BAIRRO, MUNICIPIO, ESTADO, CEP, TELEFONE,
                            OBSERVACAO, None, INSCRICAO_ESTADUAL)
LOJA_CNPJ_VAZIO = cupom.Loja(NOME_LOJA, LOGRADOURO, NUMERO, COMPLEMENTO,
                             BAIRRO, MUNICIPIO, ESTADO, CEP, TELEFONE,
                             OBSERVACAO, "", INSCRICAO_ESTADUAL)


def test_valida_cnpj():
    verifica_campo_obrigatorio_objeto(
        "O campo CNPJ da loja é obrigatório", LOJA_CNPJ_VAZIO)
    verifica_campo_obrigatorio_objeto(
        "O campo CNPJ da loja é obrigatório", LOJA_CNPJ_NULO)


LOJA_IE_NULA = cupom.Loja(NOME_LOJA, LOGRADOURO, NUMERO, COMPLEMENTO,
                          BAIRRO, MUNICIPIO, ESTADO, CEP, TELEFONE,
                          OBSERVACAO, CNPJ, None)
LOJA_IE_VAZIA = cupom.Loja(NOME_LOJA, LOGRADOURO, NUMERO, COMPLEMENTO,
                           BAIRRO, MUNICIPIO, ESTADO, CEP, TELEFONE,
                           OBSERVACAO, CNPJ, "")


def test_valida_inscricao_estadual():
    verifica_campo_obrigatorio_objeto(
        "O campo inscrição estadual da loja é obrigatório", LOJA_IE_NULA)
    verifica_campo_obrigatorio_objeto(
        "O campo inscrição estadual da loja é obrigatório", LOJA_IE_VAZIA)


LOJA_SEM_NUMERO_SEM_COMPLEMENTO = cupom.Loja(NOME_LOJA, LOGRADOURO, None, None,
                                             BAIRRO, MUNICIPIO, ESTADO, CEP,
                                             TELEFONE, OBSERVACAO, CNPJ,
                                             INSCRICAO_ESTADUAL)

TEXTO_ESPERADO_SEM_NUMERO_SEM_COMPLEMENTO = '''Loja 1
Log 1, s/n
Bai 1 - Mun 1 - E1
CEP:11111-111 Tel (11) 1111-1111
Obs 1
CNPJ: 11.111.111/1111-11
IE: 123456789'''


def test_valida_numero_e_complemento():
    assert cupom.dados_loja_objeto(LOJA_SEM_NUMERO_SEM_COMPLEMENTO)
    == TEXTO_ESPERADO_SEM_NUMERO_SEM_COMPLEMENTO


LOJA_SEM_NUMERO_SEM_COMPLEMENTO_SEM_BAIRRO = Loja(NOME_LOJA, LOGRADOURO, None,
                                                  None, None, MUNICIPIO,
                                                  ESTADO, CEP, TELEFONE,
                                                  OBSERVACAO, CNPJ,
                                                  INSCRICAO_ESTADUAL)

TEXTO_ESPERADO_SEM_NUMERO_SEM_COMPLEMENTO_SEM_BAIRRO = '''Loja 1
Log 1, s/n
Mun 1 - E1
CEP:11111-111 Tel (11) 1111-1111
Obs 1
CNPJ: 11.111.111/1111-11
IE: 123456789'''


def test_valida_numero_complemento_e_bairro():
    assert cupom.dados_loja_objeto(LOJA_SEM_NUMERO_SEM_COMPLEMENTO_SEM_BAIRRO)
    == TEXTO_ESPERADO_SEM_NUMERO_SEM_COMPLEMENTO_SEM_BAIRRO


def test_exercicio2_customizado():

    # Defina seus próprios valores para as variáveis a seguir
    nome_loja = ""
    logradouro = ""
    numero = 0
    complemento = ""
    bairro = ""
    municipio = ""
    estado = ""
    cep = ""
    telefone = ""
    observacao = ""
    cnpj = ""
    inscricao_estadual = ""

    lojaCustomizada = cupom.Loja(nome_loja, logradouro, numero, complemento,
                                 bairro, municipio, estado, cep, telefone,
                                 observacao, cnpj, inscricao_estadual)

    # E atualize o texto esperado abaixo
    assert (cupom.dados_loja_objeto(lojaCustomizada) == """
""")

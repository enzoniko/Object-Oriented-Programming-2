from app.Backend.main import sessoes, sala_mais_vazia
from app.Backend.sala import salas
from app.Backend.helpers import most_empty

## MELHORAR??
def stuff(id_sessao, horario, ingressos):
    session = [sessao for sessao in sessoes if sessao.get_id() == id_sessao][0]
    quantidade_lugares_disponiveis_sala_mais_vazia = most_empty(
        [
            [
                sala.get_cronograma()[
                    f"{id_sessao} {horario}"
                ]
                for sessao in sala.get_sessoes()
                if sessao.get_id() == id_sessao
            ]
            for sala in salas
        ]
    )
    sala = sala_mais_vazia(quantidade_lugares_disponiveis_sala_mais_vazia, session)
    poltronas = sala.get_cronograma()[f"{id_sessao} {horario}"]
    poltronas = [poltronas[i-1][::-1] for i in range(len(poltronas), 0, -1)]
    letras=["o", "n", "m", "l", "k", "j", "i", "h", "g", "f", "e", "d", "c", "b", "a"]
    numeros=["10", "9", "8", "7", "6", "5", "4", "3", "2", "1"]

    poltronas_a_preencher = [letras[int(ingressos[i].split()[0])]+numeros[int(ingressos[i].split()[1])] for i in range(len(ingressos))]
    sala.preencher_poltronas(poltronas_a_preencher, id_sessao, horario)
    sala.printar_poltronas(id_sessao, horario)
    return quantidade_lugares_disponiveis_sala_mais_vazia, session, poltronas
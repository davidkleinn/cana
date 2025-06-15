from typing import List

# Classe que representa um objeto com nome, peso e valor
class Objeto:
    def __init__(self, nome: str, peso: float, preco: float):
        self.nome = nome
        self.peso = peso
        self.preco = preco

    def __repr__(self):
        return f"{self.nome} (R${self.preco}, {self.peso}kg)"

# Função gulosa com mensagens a cada escolha
def mochila_gulosa(capacidade: float, objetos: List[Objeto]):

    # ordenacao gulosa dos itens por valor por peso
    objetos.sort(key=lambda obj: obj.preco / obj.peso, reverse=True)

    peso_total = 0
    valor_total = 0
    itens_na_mochila = []

    print(f"Capacidade da mochila: {capacidade}kg\n")
    print("Iniciando seleção gulosa...\n")

    # decisao gulosa de pegar os itens ou nao
    for obj in objetos:
        print(f"Analisando objeto: {obj.nome} (R${obj.preco}, {obj.peso}kg, "
              f"R${obj.preco / obj.peso:.2f}/kg)")
        if peso_total + obj.peso <= capacidade:
            itens_na_mochila.append(obj)
            peso_total += obj.peso
            valor_total += obj.preco
            print(f"✅ Adicionado à mochila. Peso atual: {peso_total}kg, Valor atual: R${valor_total}\n")
        else:
            print(f"❌ Não adicionado. Ultrapassaria a capacidade (peso atual: {peso_total}kg)\n")

    # Resultado final
    print("======== Resultado Final ========")
    print("Itens colocados na mochila:")
    for item in itens_na_mochila:
        print(f"- {item.nome} (R${item.preco}, {item.peso}kg)")
    print(f"\nValor total: R${valor_total}")
    print(f"Peso total: {peso_total}kg de {capacidade}kg disponíveis")

# Exemplo de uso
if __name__ == "__main__":
    capacidade_mochila = 20  # capacidade em kg
    lista_objetos = [
        Objeto("Notebook", 3, 3000),
        Objeto("Livro", 1.5, 100),
        Objeto("Câmera", 2, 2500),
        Objeto("Fone de ouvido", 0.5, 500),
        Objeto("Garrafa", 1, 80),
        Objeto("Jaqueta", 2, 300),
        Objeto("Tablet", 1.2, 1200)
    ]

    mochila_gulosa(capacidade_mochila, lista_objetos)

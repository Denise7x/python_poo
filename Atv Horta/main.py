from planta import Planta

def main():
    sistema = Planta()

    while True:
        print("\nMenu:")
        print("1. Cadastrar Planta")
        print("2. Consultar Plantas")
        print("3. Deletar Planta")
        print("4. Atualizar Planta")
        print("5. Consultar Planta Individual")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome da planta: ")
            data_plantio = input("Data do plantio (YYYY-MM-DD): ")
            tipo = input("Tipo de planta: ")
            quantidade = int(input("Quantidade: "))
            sistema.cadastrarPlanta(nome, data_plantio, tipo, quantidade)

        elif opcao == "2":
            print("Lista de Plantas:")
            sistema.consultarPlantas()

        elif opcao == "3":
            planta_id = int(input("ID da planta a ser deletada: "))
            sistema.deletarPlanta(planta_id)

        elif opcao == "4":
            planta_id = int(input("ID da planta a ser atualizada: "))
            nome = input("Novo nome (pressione Enter para manter o mesmo): ") or None
            data_plantio = input("Nova data do plantio (pressione Enter para manter o mesmo): ") or None
            tipo = input("Novo tipo (pressione Enter para manter o mesmo): ") or None
            quantidade = input("Nova quantidade (pressione Enter para manter o mesmo): ")
            quantidade = int(quantidade) if quantidade else None
            sistema.atualizarPlanta(planta_id, nome, data_plantio, tipo, quantidade)

        elif opcao == "5":
            planta_id = int(input("ID da planta: "))
            sistema.consultarPlantaIndividual(planta_id)

        elif opcao == "6":
            sistema.close()
            print("Saindo do sistema.")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
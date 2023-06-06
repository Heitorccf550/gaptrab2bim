MAX_PROFESSORES = 100
MAX_ALUNOS = 100

# Vetores para armazenar os dados
professores = []
alunos = []

# Função para cadastrar um professor
def cadastrar_professor():
    nome = input("Digite o nome do professor: ")
    disciplina = input("Digite a disciplina do professor: ")
    professores.append({"Nome": nome, "Disciplina": disciplina})
    print("Professor cadastrado com sucesso!")

# Função para cadastrar um aluno
def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ")
    curso = input("Digite o curso do aluno: ")
    alunos.append({"Nome": nome, "Curso": curso})
    print("Aluno cadastrado com sucesso!")

# Função para alterar os dados de um professor
def alterar_professor():
    nome = input("Digite o nome do professor que deseja alterar: ")
    for professor in professores:
        if professor["Nome"] == nome:
            novo_nome = input("Digite o novo nome do professor: ")
            nova_disciplina = input("Digite a nova disciplina do professor: ")
            professor["Nome"] = novo_nome
            professor["Disciplina"] = nova_disciplina
            print("Dados do professor alterados com sucesso!")
            return
    print("Professor não encontrado.")

# Função para alterar os dados de um aluno
def alterar_aluno():
    nome = input("Digite o nome do aluno que deseja alterar: ")
    for aluno in alunos:
        if aluno["Nome"] == nome:
            novo_nome = input("Digite o novo nome do aluno: ")
            novo_curso = input("Digite o novo curso do aluno: ")
            aluno["Nome"] = novo_nome
            aluno["Curso"] = novo_curso
            print("Dados do aluno alterados com sucesso!")
            return
    print("Aluno não encontrado.")

# Função para exibir os professores cadastrados
def exibir_professores():
    if not professores:
        print("Nenhum professor cadastrado.")
    else:
        for professor in professores:
            print("Nome:", professor["Nome"])
            print("Disciplina:", professor["Disciplina"])
            print("--------------------")

# Função para exibir os alunos cadastrados
def exibir_alunos():
    if not alunos:
        print("Nenhum aluno cadastrado.")
    else:
        for aluno in alunos:
            print("Nome:", aluno["Nome"])
            print("Curso:", aluno["Curso"])
            print("--------------------")

# Função principal
def main():
    while True:
        print("1 - Cadastrar professor")
        print("2 - Cadastrar aluno")
        print("3 - Alterar dados de professor")
        print("4 - Alterar dados de aluno")
        print("5 - Exibir professores cadastrados")
        print("6 - Exibir alunos cadastrados")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_professor()
        elif opcao == "2":
            cadastrar_aluno()
        elif opcao == "3":
            alterar_professor()
        elif opcao == "4":
            alterar_aluno()
        elif opcao == "5":
            exibir_professores()
        elif opcao == "6":
            exibir_alunos()
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()

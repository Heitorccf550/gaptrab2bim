MAX_PROFESSORES = 100
MAX_ALUNOS = 100

# Vetores para armazenar os dados
professores = []
alunos = []

# Variáveis para controle dos códigos
prox_cod_professor = 1
prox_cod_aluno = 1

# Função para cadastrar um professor
def cadastrar_professor():
    global prox_cod_professor

    nome = input("Digite o nome do professor: ")
    disciplina = input("Digite a disciplina do professor: ")
    codigo = prox_cod_professor

    professores.append({"Código": codigo, "Nome": nome, "Disciplina": disciplina})
    prox_cod_professor += 1

    print("Professor cadastrado com sucesso!")

# Função para cadastrar um aluno
def cadastrar_aluno():
    global prox_cod_aluno

    nome = input("Digite o nome do aluno: ")
    curso = input("Digite o curso do aluno: ")
    codigo = prox_cod_aluno

    alunos.append({"Código": codigo, "Nome": nome, "Curso": curso})
    prox_cod_aluno += 1

    print("Aluno cadastrado com sucesso!")

# Função para alterar os dados de um professor
def alterar_professor():
    codigo = int(input("Digite o código do professor que deseja alterar: "))

    for professor in professores:
        if professor["Código"] == codigo:
            nome = input("Digite o novo nome do professor: ")
            disciplina = input("Digite a nova disciplina do professor: ")

            professor["Nome"] = nome
            professor["Disciplina"] = disciplina

            print("Dados do professor alterados com sucesso!")
            return

    print("Professor não encontrado.")

# Função para alterar os dados de um aluno
def alterar_aluno():
    codigo = int(input("Digite o código do aluno que deseja alterar: "))

    for aluno in alunos:
        if aluno["Código"] == codigo:
            nome = input("Digite o novo nome do aluno: ")
            curso = input("Digite o novo curso do aluno: ")

            aluno["Nome"] = nome
            aluno["Curso"] = curso

            print("Dados do aluno alterados com sucesso!")
            return

    print("Aluno não encontrado.")

# Função para exibir os professores cadastrados
def exibir_professores():
    if not professores:
        print("Nenhum professor cadastrado.")
    else:
        for professor in professores:
            print("Código:", professor["Código"])
            print("Nome:", professor["Nome"])
            print("Disciplina:", professor["Disciplina"])
            print("--------------------")

# Função para exibir os alunos cadastrados
def exibir_alunos():
    if not alunos:
        print("Nenhum aluno cadastrado.")
    else:
        for aluno in alunos:
            print("Código:", aluno["Código"])
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

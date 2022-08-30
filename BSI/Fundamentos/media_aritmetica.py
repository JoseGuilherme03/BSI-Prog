#   Recebe as notas das 2 provas e 2 exercícios de programação e retorna se o aluno foi ou não aprovado. As provas têm peso 7 e os exercícios têm peso 3. Cada parcial tem peso igual.  Uma forma de resolver é calcular a 1a parcial, com a média ponderada entre  p1 e ep1, depois calcular a 2a parcial, com as notas de p2 e ep2 e depois       calcular a média aritmética entre a 1a e a 2a parcial.


def media_final_aprovado_reprovado(prova1, prova2, exercicio1, exercicio2):
    media1 = (prova1 * 7 + exercicio1 * 3) / 10
    media2 = (prova2 * 7 + exercicio2 * 3) / 10
    media_final = (media1 + media2) / 2
    print(f"\nA media final do aluno foi {media_final :.2f} ")

    if media_final >= 7:
        print("O aluno está APROVADO.")

    else:
        print("O aluno está REPROVADO.")


prova1 = float(input("Digite a primeira nota: "))
prova2 = float(input("Digite a segunda nota: "))
exercicio1 = float(input("Digite a nota do primeiro exercicio: "))
exercicio2 = float(input("Digite a nota do segundo exercicio: "))

media_final_aprovado_reprovado(prova1, prova2, exercicio1, exercicio2)


     # Essa função diva aqui recebe uma string e retorna um valor booleano
def validar_cpf(cpf: str) -> bool:
    # Remove qualquer caractere que  não seja um número
    cpf = ''.join(filter(str.isdigit, cpf))
    
    # Verifica se o cpf  tem 11 dígitos
    if len(cpf) != 11:
        return False
    
    # Verifica se todos os dígitos são iguais, se for, ele retorna "false", pois o cpf não é válido
    if cpf == cpf[0] * 11:
        return False

    # Calcula o primeiro dígito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito1 = (soma * 10 % 11) % 10

    # Calcula o segundo dígito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito2 = (soma * 10 % 11) % 10

    # Verifica se os dígitos calculados são iguais aos informados
    return cpf[-2:] == f"{digito1}{digito2}"

# Exemplo de uso
if __name__ == "__main__":
    cpf_input = input("Digite o CPF: ")
    if validar_cpf(cpf_input):
        print("CPF válido!")
    else:
        print("CPF inválido!")
cargo = input("digite seu cargo: ")
dia_da_semana = input("digite o dia da semana: ")
   

if cargo == 'gerente':
    print("aceso liberado todos os dias")
elif cargo == 'analista':
    if dia_da_semana in ["segunda", "terca", "quarta", "quinta", "sexta"]:
        dia_da_semana = ("segunda", "terca", "quarta", "quinta", "sexta")
        print("acesso_liberado")
    else:
        print("acesso_negado")
elif cargo == 'estagiario':
    if dia_da_semana in ["segunda", "terca", "quarta", "quinta", "sexta"]:
        dia_da_semana = ("segunda", "terca", "quarta", "quinta", "sexta")
        print("acesso_liberado")
    else:
        print("acesso_negado")
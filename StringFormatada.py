# Strings Formatadas
# Writes John [Smith] is a coder
first = 'john'
last = 'Smith'
message = first + ' [' + last + '] is a coder'
print(message)
# Para fazer uma string formatada usa-se o prefixo: f|usamos essa formatação para ler mais fácil o código criado
first = 'john'
last = 'Smith'
msg = f'{first} [{last}] is a coder'
print(msg)


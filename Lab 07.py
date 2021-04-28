import random

arma01 = 'armadura'
arma02 = 'escudo'
arma03 = 'espada'
arma04 = 'lança'
arma05 = 'capacete'

armas = [arma01,arma02,arma03,arma04,arma05]
random.samples(armas)



armadura = int(20)
escudo = int(5)
espada = int(10)
lanca = int(15)
capacete = int(5)

print('Bem vindo!')
print('Para onde gostaria de ir?')
opcao = input('Entre S para ir à Sala do Trono, ou qualquer outra tecla para ir ao Salão de Festas: ')

if opcao == 'S' or opcao == 's':
    proximo = 'Sala do Trono'
else:
    proximo = 'Salão de Festas'

if proximo == 'Sala do Trono':
    energia = armadura
    print('Bem vindo à Sala do Trono')
    print('Parabéns, você encontrou uma armadura')
    print('Para onde gostaria de ir daqui?')
    opcao = input('Entre S para ir à Suíte Real, ou qualquer outra tecla para ir ao Calabouço: ')
    if opcao == 'S' or opcao == 's':
        proximo = 'Suíte Real'
    else:
        proximo = 'Calabouço'
if proximo == 'Salão de Festas':
    energia = escudo
    print('Bem vindo ao Salão de Festas')
    print('Parabéns, você encontrou um escudo')
    print('Para onde gostaria de ir daqui?')
    opcao = input('Entre S para ir à Masmorra, ou qualquer outra tecla para ir ao Calabouço: ')
    if opcao == 'S' or opcao == 's':
        proximo = 'Masmorra'
    else:
        proximo = 'Calabouço'

if proximo == 'Suíte Real':
    print('Bem vindo à Suíte Real')
    print('Para onde gostaria de ir daqui?')
    opcao = input('Entre qualquer tecla para ir ao Pátio: ')
    proximo = 'Pátio'
if proximo == 'Calabouço':
    if energia == armadura:
        energia = espada + armadura
    else:
        energia = escudo + espada
    print('Bem vindo ao Calabouço')
    print('Parabéns, você encontrou uma espada')
    print('Para onde gostaria de ir daqui?')
    opcao = input('Entre qualquer tecla para ir ao Pátio: ')
    proximo = 'Pátio'
if proximo == 'Masmorra':
    if energia == armadura:
        energia = armadura + lanca
    else:
        energia = escudo + lanca
    print('Bem vindo a Masmorra')
    print('Parabéns, você encontrou uma lança')
    print('Para onde gostaria de ir daqui?')
    opcao = input('Entre S para ir à Torre, ou qualquer outra tecla para ir ao Pátio: ')
    if opcao == 'S' or opcao == 's':
        proximo = 'Torre'
    else:
        proximo = 'Pátio'

if proximo == 'Torre':
    print('Bem vindo à Torre')
else:
    if energia == espada + armadura:
        energia = espada + armadura + capacete
    elif energia == escudo + espada:
        energia = escudo + espada + capacete
    elif energia == armadura + lanca:
        energia = armadua + lança + capacete
    else:
        energia = escudo + lanca + capacete
    print('Bem vindo ao Pátio')
    print('Parabéns, você encontrou um capacete')
    print('Energia Total: ', energia)
    print('Você chegou ao fim do tour.')

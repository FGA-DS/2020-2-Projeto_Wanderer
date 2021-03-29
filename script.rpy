# The script of the game goes in this file.

init python:
    dinheiro = False
    amoras   = False
    espelho  = False
##define config.menu_include_disabled = True

##default allow_choice = False

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define n  = Character("narrador")
define mc = Character("Mago")

image Mapa = "images/Mapa.png"

## personagens
image mc normal  = "images/mc a.png"
image mc bombado = "images/mc.png"
image guarda1    = "images/mamaco.png"
image guarda2    = "images/lobinho2.png"
image porteiro   = "images/PW minotauro.png"
image oseamus    = "images/duende.png"

## backgrounds
image entrada_caos = "images/PW entrada cidadela.jpg"
image caminho_cidadela = "images/PW campo escuro.jpg"
image cidadela1 = "images/PW cidadela.jpg"
image poco = "images/fundo-poco.jpg"
image portao = "images/portao.jpg"
image corredor = "images/corredor.jpg"
image sala_oseamus = "images/sala oseamus.jpg"
image game_over = "images/game_over.jpeg"


# The game starts here.

label start:

    stop music

    play music "musics/inicio_epico.mp3"

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene Mapa

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.



    # These display lines of dialogue.

    n "O ordeiro e generoso povo do Vale dos Salgueiros vive há oito anos sob o terror e medo do
    feiticeiro Balthus Dire."

    n "Terror, porque o poder dele é realmente aterrorizante,  e medo causados
    pela notícia que acabou chegando aos ouvidos desse povo, vinda dos domínios do feiticeiro, de que
    seus ambiciosos planos de conquista começariam pelo próprio Vale."

    n "Um fiel Semi-Elfo enviado em uma missão de espionagem à Torre Negra voltou galopando para o
    Vale há três dias com uma mensagem desesperada."

    n "Do interior das cavernas de Rocha Escarpada,
    Balthus Dire tinha recrutado um exército de Caóticos e se preparava para atacar com eles o Vale
    dentro de uma semana."

    n "O bom Rei Salamon era um homem de ação. Foram enviados mensageiros por todo o Vale no
    mesmo dia para preparar as defesas e convocar os homens para a guerra."

    n "Foram enviados também cavaleiros à Grande Floresta de Yore para avisar aos Semi-Elfos que moravam lá e fazer um apelo
    para que se aliassem às forças. O Rei Salamon era também um homem sábio."

    n "Ele sabia muito bem que as notícias inevitavelmente chegariam aos ouvidos do Grande Mago de Yore, um mestre da
    magia branca de grandes poderes, que vivia nas profundezas da floresta. O mago era velho e não
    resistiria a uma batalha destas proporções."

    n " Mas ele havia ensinado suas artes a vários jovens magos, e talvez um de seus discípulos de magia ajudasse o rei e seus súditos com coragem e ambição."

    show mc normal at center:
        zoom 0.6
    with dissolve

    n "Você é o aluno brilhante do Grande Mago de Yore. Ele tem sido um Mestre duro, e sua própria
    impaciência muitas vezes foi mais forte do que você. Talvez um pouco precipitadamente, você
    partiu de imediato para a corte de Salamon. O rei recebeu-o entusiasticamente e explicou seu plano."

    n "A batalha poderia ser evitada sem derramamento de sangue se Balthus fosse assassinado antes que
    seu exército pudesse ser reunido."

    n "A missão que você tem pela frente é extremamente perigosa. Balthus Dire está cercado, em sua  Cidadela,
    por uma multidão de criaturas assombrosas. Embora a Magia seja a sua arma mais forte,  haverá momentos em que você terá que confiar em sua espada para sobreviver."

    n "O Rei Salamon expôs a você como seria a sua missão e o advertiu dos perigos que estavam à sua  frente.
    Há um caminho melhor para atravessar a Cidadela. Se você o descobrir, terá êxito com um  mínimo de risco para a sua pessoa.
    Talvez você precise de várias viagens para descobrir o caminho  mais fácil para atravessar a Cidadela"

    n "antes da sua saida, o rei te chama e te entraga um saco de couro com um punhado de moedas de ouro para auxiliar na sua jornada."

    $renpy.notify("adquiriu dinheiro!")

    play sound "musics/efeito_sonoro/item encontrado.mp3"

    n "Você deixa o Vale dos Salgueiros na longa caminhada para a Torre Negra. No sopé da colina de  Rocha Escarpada,
    você pode ver sua silhueta contra o céu escuro... "

    $dinheiro = True

    jump um

    return

label um:

    hide Mapa
    hide mc

    play music "musics/Keys of Moon - Enchanted.mp3"

    scene caminho_cidadela:
        zoom 1.5

    n "O sol se põe. Enquanto o crepúsculo se transforma em escuridão, você começa a subir a colina na  direção da ameaçadora forma que se desenha contra o céu noturno.
    A Cidadela fica a menos de uma  hora de escalada."

    n "A uma certa distância de seus muros, você pára para descansar - um erro, uma vez que, dessa  posição, ela parece um espectro medonho do qual não se pode escapar.
    Os cabelos no seu pescoço  se arrepiam enquanto você a observa."

    n "Mas você se envergonha de seus medos. Com inflexível decisão, você marcha adiante na direção do  portão principal, onde você sabe que encontrará guardas à sua espera.
    Você considera suas opções. "

    n " Já pensou em se apresentar como um especialista em plantas medicinais que veio tratar de um  guarda com febre. Poderia também se dizer um comerciante ou artesão talvez um carpinteiro.
    Poderia até mesmo ser um nômade que buscasse abrigo para a noite."

    scene entrada_caos:
        zoom 1.8

    n "Enquanto você pondera as possibilidades, e as histórias que terá que contar aos guardas, acaba  chegando à trilha principal que conduz aos portões.
    Duas lanternas brilham em cada um dos lados da porta levadiça. "

    play sound "musics/efeito_sonoro/macacor.mp3"

    show guarda1 at left:
        zoom 1.3
    with dissolve

    n "Você ouve grunhidos abafados ao se aproximar, e vê duas criaturas de aparência absurda. Do lado  esquerdo está uma criatura horrível, um grande macaco,
    flexionando seus braços fortíssimos."

    play sound "musics/efeito_sonoro/lobor.mp3"

    show guarda2 at right:
        zoom 0.9
    with dissolve

    n "Do outro lado, encontra-se de fato o seu oposto, um cachorro grande. Este último guarda se aproxima nas suas quatro  patas.
    Para a alguns metros de distância diante de você, ergue-se sobre as patas traseiras e dirige a  palavra a você. "

    n "Por qual das histórias você optará?"

    menu:
        "Você se apresentará como um especialista
        em plantas medicinais?(ainda em desenvolvimento)":
            jump dois61
        "Você dirá que é um comerciante? (ainda em desenvolvimento)":
            jump dois30
        "Você pedirá abrigo para pernoitar?":
            jump dois0

label dois61: ##incompleto

label dois30: ##incompleto

label dois0:

    n "O Macaco-Cachorro diz que não é permitido a ninguém entrar na Torre Negra depois que anoitece -
    você terá que procurar abrigo em outro lugar."


    n "Você pode se resignar a lutar. Ou pode pegar uma pedra e lançar um Encanto do Ouro dos Tolos sobre ela, oferecendo-a como uma pepita
    de ouro, para suborná-los, convencendo-os a deixar você entrar"
    menu teste:
        "se preparar para lutar?":
            jump dois88
        "tentar suborno? ":
            if dinheiro:
                jump suborno
            else:
                $renpy.notify("você não possui esse item!")
                jump teste
        "usar encanto? (teste de sorte)":
            jump nove6

label dois88:

    n "os guardas avançam em sua direçao!"

    play music "musics/Makai Symphony - Dragon Castle.mp3"

    jump batalha_guardas

label suborno:
    n "os guardas regojizam-se com o pequeno punhado de moedas de ouro que você entregou e o deixam passar"

    $renpy.notify("dinheiro retirado!")

    play sound "musics/efeito_sonoro/item perdido.mp3"

    jump dois51

label nove6:

    play sound "musics/efeito_sonoro/dados.mp3"

    $ d20roll = renpy.random.randint(1, 20)

    if (d20roll>=12):
        $renpy.notify("sucesso de sorte")
        play sound "musics/efeito_sonoro/sorte-sucesso.mp3"
        n "Eles aceitam a sua oferta e convocam o porteiro, que abre uma pequena porta dentro da porta
        levadiça para deixar você entrar. Você os deixa discutindo por causa da pepita de ouro."
        jump dois51
    else:
        $renpy.notify("fracasso de sorte")
        play sound "musics/efeito_sonoro/sorte-fracasso.mp3"
        n "os guardas nao caem na ilusão e partem em sua direção prontos para lutar"
        jump dois88

label dois51:

    play music "musics/yt1s.com - Magic Fantasy Music  The Mystic  Beautiful Violin.mp3"

    scene cidadela1:
        zoom 1.0

    n "Você caminha em frente, entrando em um pátio aberto e espaçoso, circundado por grandes muros.
    Há várias tochas queimando, e grupos de figuras se movimentam na escuridão."

    n "Há um monumento de algum tipo no centro do pátio - talvez uma fonte. Olhando para o outro lado do pátio, você
    consegue ver o que parece ser a entrada principal da torre. Você:"

    menu:
        "Esgueira-se pela parede na direção da torre, contornando o pátio?":
            jump um4
        "Caminha decididamente, atravessando o pátio? (ainda em desenvolvimento)":
            jump um79
        "Vai na ponta dos pés pelas sombras, na direção de um dos grupos? (ainda em desenvolvimento)":
            jump tres21

label um79: ##incompleto

label tres21: ##incompleto

label um4:
    n "A sombra do muro dificulta muito a visão. Uma pedra solta desliza, e você perde o equilíbrio,
    oscilando à beira do que você tem consciência de que deve ser um poço profundo."

    n "Teste a sua Sorte. Se você tiver sorte, recupera o equilíbrio e caminha em segurança."

    play sound "musics/efeito_sonoro/dados.mp3"

    $ d20roll = renpy.random.randint(1, 20)

    if (d20roll>= 10):
        $renpy.notify("sucesso de sorte")
        play sound "musics/efeito_sonoro/sorte-sucesso.mp3"
        n "você vê uma corda e se segura nela, recobrando o equilíbrio"
        jump sete9

    else:
        $renpy.notify("fracasso de sorte")

        play sound "musics/efeito_sonoro/sorte-fracasso.mp3"

        jump um00

label um00:
    n "tente usar um feitiço de levitação para nao cair! teste sua sorte!"

    play sound "musics/efeito_sonoro/dados.mp3"

    $ d20roll = renpy.random.randint(1, 20)

    if (d20roll>= 14):
        $renpy.notify("sucesso de sorte")
        play sound "musics/efeito_sonoro/sorte-sucesso.mp3"
        n "você volta para a fora do poço e segue seu caminho"
        jump sete9

    else:
        $renpy.notify("fracasso de sorte")
        play sound "musics/efeito_sonoro/sorte-fracasso.mp3"
        jump dois76

label dois76:

    scene poco:
        zoom 2.0

    n "Você cai no fundo de um poço profundo – possivelmente um manancial de água tapado. Você se
    recompõe e parece estar inteiro."

    n "Mas como você vai sair? Cavar apoios para os pés nas paredes do
    poço com sua espada levaria um tempo enorme."

    n "Você poderia lançar um Encanto da Força para
    ajudá-lo nessa tarefa ou poderia gritar, pedindo ajuda."

    menu:

        "usar encanto! teste de sorte.":
            play sound "musics/efeito_sonoro/dados.mp3"

            $ d20roll = renpy.random.randint(1, 20)

            if (d20roll>= 12):
                $renpy.notify("sucesso de sorte")
                play sound "musics/efeito_sonoro/sorte-sucesso.mp3"
                jump um65

            else:
                $renpy.notify("fracasso de sorte")
                play sound "musics/efeito_sonoro/sorte-fracasso.mp3"
                n "voce fracassa no uso do feitiço e quando começa a escalar cai de volta torçendo o pé, apenas lhe restanto gritar por ajuda"
                jump dois02

        "gritar pedindo ajuda":
            jump dois02

label um65:
    n "Quando você sente a força se espalhar pelo seu corpo desembainha a espada e crava na muralha
    terrosa. Dessa forma você faz um apoio para os pés, para depois utilizá-lo enquanto cava o próximo,
    assim consegue subir pelas paredes bem rapidamente com o aumento de força que recebeu."

    n "Na metade do caminho, contudo, sua força começa a diminuir, e você compreende que está retornando
    ao normal. Se você deixar que isso aconteça, cairá para trás dentro do poço mais uma vez."

    n "Você pode lançar outro Encanto da Força para dar a energia suficiente para completar a sua escada ou gritar pedindo ajuda."

    menu:
        "usar encanto! teste de sorte.":
            play sound "musics/efeito_sonoro/dados.mp3"

            $ d20roll = renpy.random.randint(1, 20)

            if (d20roll>= 10):
                $renpy.notify("sucesso de sorte")
                play sound "musics/efeito_sonoro/sorte-sucesso.mp3"
                jump tres98

            else:
                $renpy.notify("fracasso de sorte")
                play sound "musics/efeito_sonoro/sorte-fracasso.mp3"
                n "voce fracassa no uso do feitiço e quando volta a escalar cai de volta quebrando a perna, apenas lhe restanto gritar por ajuda"
                jump dois02

        "gritar pedindo ajuda":
            jump dois02

label tres98:
    n "Você lança o encanto, e sua força retorna, permitindo que você acabe de subir os degraus. Quando
    você chega no alto, os efeitos desaparecem mais uma vez. Você pode agora seguir ao longo da
    muralha na direção da Torre Negra."

    jump sete9

label dois02:
    n "Depois de vários minutos de gritaria, você ouve vozes que se aproximam, falando em uma língua
    estranha. Para seu alívio, você vê quatro cabeças que espiam dentro do poço se desenharem contra o
    céu. Você berra para que eles consigam alguma corda."

    n "Eles conversam entre si e desaparecem.
    Finalmente, você ouve suas passadas rápidas retornando. Eles param mais uma vez no alto do poço
    e jogam sobre você, não uma corda de socorro, mas o conteúdo de um caldeirão de óleo fervente!"

    n "Você terá que olhar com mais cuidado por onde anda na sua próxima aventura, porque esta está
    terminada. E lembre-se - estranhos não são bem-vindos na Cidadela do Caos..."

    jump final_ruim

label sete9:

    scene cidadela1

    n "No canto mais distante do pátio, você encontra um arbusto diferente, com galhos contorcidos a
    partir da haste central, como se estivesse em agonia."

    n "As folhas têm a forma de diamantes, com pequenas amoras por baixo, chatas e com forma de pastilhas. Você pode levar algumas amoras com
    você na sua aventura e avançar um pouco mais ao longo do muro para a entrada principal da
    Cidadela."

    $renpy.notify("adquiriu amoras!")

    play sound "musics/efeito_sonoro/item encontrado.mp3"

    $amoras = True

    jump dois18

label dois18:

    play music "musics/sb_phoenix.mp3"

    scene portao

    n "Há uma grande porta de madeira à sua frente, firmemente trancada. Você pode bater três vezes para
    chamar o guarda ou usar um Encanto da Força para tentar abri-la."

    menu:
        "chamar o guarda":
            jump um18
        "encanto força(ainda em desenvolvimento)":
            jump nove4

label um18:

    play sound "musics/efeito_sonoro/batendo-porta.mp3"

    n "A porta abre e uma criatura grande e abrutalhada sai. sua aparencia remete a de uma besta e
    sua pele parece ser recoberta de armadura."

    show porteiro at center:
        zoom 1.5
    with dissolve

    play sound "musics/efeito_sonoro/minotauro.mp3"

    n "Rosna para saber o que você quer e exige a senha antes
    de deixar que você entre. Você sabe a senha?"
    menu:
        "Ganjees (ainda em desenvolvimento)":
            jump dois55
        "Kraken (ainda em desenvolvimento)":
            jump quatro9
        "Cimitarra":
            jump tres71
        "tentar se passar como especialista em ervas (ainda em desenvolvimento)":
            jump um98

label nove4: ##incompleto

label dois55: ##incompleto

label quatro9: ##incompleto

label tres71:

    play sound "musics/efeito_sonoro/minotauro.mp3"

    n "A criatura grunhe e abre a porta para deixar você entrar."

    jump um77

label um98: ##incompleto

label um77:

    scene corredor:
        zoom 1.8

    n "Você está em um corredor estreito. Ele continua por alguns metros e termina em uma porta."

    n " A meio caminho, descendo a passagem, pode-se ver um arco, de onde alguns degraus levam para baixo.
    Você vai prosseguir na direção da porta ou se arriscará a descer as escadas?"
    menu:
        "seguir na direção da porta (ainda em desenvolvimento)":
            jump cinco
        "descer as escadas":
            jump tres44

label cinco: ##incompleto

label tres44:
    n "Você desce os degraus. O ar está fresco e estagnado. Há uma porta ao pé da escadaria. Você tentará
    a porta ou subirá as escadas de volta para ir até a porta para o andar térreo?"
    menu:
        "abrir a porta":
            jump sete
        "subir as escadas e voltar":
            jump cinco

label sete:

    n "A porta está trancada. Você pode tentar pô-la abaixo, batendo nela com o ombro, ou
    pode lançar um Encanto da Força sobre você mesmo e tentar arrancar a porta das suas dobradiças."

    menu:
        "bater na porta com o ombro":
            jump dois68
        "usar encanto para arrancar a porta (teste de sorte)":
            play sound "musics/efeito_sonoro/dados.mp3"

            $ d20roll = renpy.random.randint(1, 20)

            $renpy.notify("sucesso de sorte")
            play sound "musics/efeito_sonoro/sorte-sucesso.mp3"
            jump um16

label dois68:

    n"Quando você golpeia a porta, a madeira racha um pouco, mas não cede. Você tenta de novo, e dessa
    vez a madeira se parte ao meio. Você abre caminho e entra no aposento do outro lado."

    jump dois10

label um16:

    n "Suas mãos super poderosas agarram a maçaneta e puxam. Ela sai na sua mão. Você fecha a mão e
    desfere um soco no meio da porta. A madeira racha e quebra, permitindo que você entre no
    aposento do outro lado."

    jump dois10

label dois10:

    scene sala_oseamus at center:
        zoom 1.5

    n "Você agora está em um aposento grande. É Iluminado por uma única tocha, presa a uma
    das paredes. Não há mobília no aposento,exceto uma mesa de madeira rústica e uma cadeira no
    centro."

    show oseamus at center:
        zoom 0.8
        ypos 850

    n "Flutuando acima da mesa - dormindo profundamente - há um homem muito pequeno,
    vestido com pantalonas e camisa. Ele não chega a ter mais de um metro de altura, e você não
    consegue acreditar que ele esteja ainda dormindo depois de sua entrada barulhenta!"

    n "Você ouve um rangido e vira-se para a direita a tempo de ver uma pequena catapulta disparar um projétil de algum
    tipo direto na sua direção. Vai atingir você, a não ser que você use um Encanto do Escudo!"

    menu:
        "usar encanto de escudo":

            play sound "musics/efeito_sonoro/dados.mp3"

            $ d20roll = renpy.random.randint(1, 20)

            if (d20roll>=12):
                $renpy.notify("sucesso de sorte")
                play sound "musics/efeito_sonoro/sorte-sucesso.mp3"
                n "você lança o encanto com sucesso"
                jump um92
            else:
                $renpy.notify("fracasso de sorte")
                play sound "musics/efeito_sonoro/sorte-fracasso.mp3"
                n "sob pressao do projetil te atingir, você erra algumas palavras do encanto,
                fazendo com que ele seja eficaz!"
                jump tres59

        "nao usar encanto de escudo":
            jump tres59

label um92:

    play sound "musics/efeito_sonoro/yt1s.com - Tomato Splat Sound Effect.mp3"

    n "Você lança o Encanto bem na hora. O projétil atinge o seu escudo mágico e se espatifa contra ele,
    escorrendo para o solo. Você examina a pasta que ficou no escudo para ver o que era."
    n "Você quase foi atingido por um tomate! No centro do aposento, a figura adormecida está se mexendo."

    jump dois9

label tres59:
    n "Você tenta se esquivar, mas não consegue evitar o impacto em cheio do projétil, que atinge você na
    testa e se derrama por toda a sua cara."

    play sound "musics/efeito_sonoro/yt1s.com - Tomato Splat Sound Effect.mp3"

    n "Você fica imóvel, esperando talvez pelo início de algum tipo de reação ácida, mas o líquido pastoso simplesmente pinga do seu rosto no chão. Cautelosamente,
    você o toca, primeiro com o dedo, depois com a língua."
    n "Você acaba de ser atingido por um tomate maduro! Mais uma vez, você se volta para enfrentar a figura adormecida."

    jump dois9

label dois9:
    n "Cautelosamente, você se aproxima do homenzinho. Ao chegar perto, um único olho se abre e olha
    diretamente no seu rosto. Um sorriso largo se espalha de orelha a orelha na criatura e ela
    desaparece!"
    n "'Bom dia para você!' diz uma vozinha chilreante atrás de você, e, ao voltar-se, você o
    vê ali, ainda sorrindo."
    n "'Sou O'Seamus, o Duende!', ele diz, dando risinhos, e estende a mão para
    você. Ele parece suficientemente amigável - você aperta a mão dele e tenta fazer amizade ou desembainha sua espada?"

    menu:
        "você aperta a mão dele e tenta fazer amizade":
            jump dois71
        "desembainha sua espada":
            jump um31

label dois71:
    n "Você aperta a mão dele e se apresenta - e grita quando os nervos da sua mão e braço ficam
    dormentes! O'Seamus se escangalha de rir. Você está ficando aborrecido, mas o homenzinho continua a
    apertar a sua mão e rir."

    n "Uma risada vem de trás de você, e você se vira e vê o brincalhão flutuando
    no ar, sorrindo. Mas você está ainda apertando a mão dele diante de você... ou não está?"

    n " Na realidade, você compreende agora que está freneticamente apertando a mão de um boneco
    empalhado que balança juntamente com seu braço enquanto você se movimenta.Você atira o
    boneco no chão - mas ele está grudado na sua mão!"

    n "A situação é ridícula, e você está ficando muito
    zangado. 'Só uma brincadeirinha', diz o Duende. 'Agora, o que posso fazer por você?' Você
    perguntará a ele o caminho para seguir adiante (vá para 348) ou desembainhará a sua espada (volte
    para 131)?"

    menu:
        "perguntar a ele o caminho":
            jump tres48
        "puxar sua espada!":
            jump um31

label um31:
    n "Você rapidamente desembainha a sua espada, apontando-a na direção do Duende. Ele lança um
    olhar para a lâmina e, para seu horror, ela verga molemente a partir do cabo, pendendo para baixo
    como se fosse um cinto de couro."
    n "Parece que você não irá muito longe agindo com agressividade.
    Talvez seja melhor você perguntar a ele o caminho para seguir adiante."

    jump tres48

label tres48:
    n "'Oh, eu não iria nesta direção', diz O'Seamus. 'Não é uma região agradável.' Estas três portas são
    o único caminho para seguir adiante. Duas delas são muito perigosas, e a terceira tem um cheiro
    muito forte. No lado oposto do aposento, há três portas."
    n " Uma tem uma maçaneta de latão, outra tem uma maçaneta de cobre, e a terceira tem uma maçaneta de bronze. Qual delas você escolherá:"
    n "o que você faz?"
    menu:
        "abrir a porta com maçaneta de latao?":
            jump dois07
        "abrir a porta com maçaneta de cobre?":
            jump dois2
        "abrir a porta com maçaneta de bronze?":
            jump tres54
        "pedir conselho ao doende?":
            jump seis8

label dois07:

    n "Você abre a porta e espia a escuridão à sua frente. Você dá uns dois passos adiante, dando tempo
    para que seus olhos se acostumem ao escuro. Você fecha a porta atrás de você, dizendo adeus ao
    Duende."

    jump um88

label dois2:

    n "Você abre a porta e sai em um corredor longo e escuro."

    jump um88

label tres54:

    n "Você abre a porta e entra em outro aposento, feliz por ter deixado para trás a aborrecida criaturinha."

    jump um88

label seis8:
    n "'Por qual eu iria, hein?' ele considera. 'Vamos ver... eu não iria por uma das duas portas à esquerda
    da porta de maçaneta de cobre, nem a porta à direita da de maçaneta de bronze.' Qual delas você
    escolherá:"

    menu:
        "abrir a porta com maçaneta de latao?":
            jump dois07
        "abrir a porta com maçaneta de cobre?":
            jump dois2
        "abrir a porta com maçaneta de bronze?":
            jump tres54

label um88:
    n "Um clarão de luz súbito e intenso irrompe à sua frente. Você protege os olhos e depois os esfrega -
    mas não consegue ver nada!"
    n "Você entra em pânico ao ouvir um ruído como um rosnado baixo.
    Passos de pés peludos se aproximam, e você grita de dor quando esta criatura que você não pode
    ver ruge e crava seus dentes aguçados na sua perna.Você:"
    menu:
        "usa encanto de fraqueza? (teste de sorte)":
            play sound "musics/efeito_sonoro/dados.mp3"

            $ d20roll = renpy.random.randint(1, 20)

            if (d20roll>=12):
                $renpy.notify("sucesso de sorte")
                play sound "musics/efeito_sonoro/sorte-sucesso.mp3"
                n "você lança o encanto com sucesso"

                jump um59
            else:
                $renpy.notify("fracasso de sorte")
                play sound "musics/efeito_sonoro/sorte-fracasso.mp3"
                n "sob o efeito da dor extrema, você erra o feitiço, tornando a criatura mais forte ao inves de fraca!"

                jump dois80
        "puxa sua espada para atacar?":
            jump cinco1

label um59:
    n "Você lança seu Feitiço da Fraqueza e deixa transcorrer um tempo na esperança de que a força da
    criatura diminua. Mas, como seus dentes continuam a ferir você, você fica desalentado ao descobrir
    que o ataque da criatura está cada vez mais feroz. Você já não consegue sentir a perna."
    n "A dor é intensa. Você se sente fraco e perde a consciência quando as mandíbulas se fecham na sua garganta."
    jump tres23

label dois80:
    n "A criatura está atacando você impiedosamente, e não há nada que você possa fazer para evitar isso.
    Sua perna está coberta de sangue, e a dor é arrasadora. Você luta com a cabeça que não está vendo,
    mas não adianta nada."

    n "A criatura salta sobre o seu pescoço, e sua última lembrança, antes de perder
    os sentidos, é de suas mandíbulas se fechando sobre a sua garganta."

    jump tres23

label cinco1:
    n "Você distribui loucamente golpes com sua espada, mas não consegue atingir a criatura. Ou ela é
    extremamente rápida, ou não possui um corpo sólido que possa ser atingido."

    n "Seus dentes estão agora rasgando a sua carne, e você sente sangue na perna. Você terá que se proteger com sua
    mágica ou enfrentar uma morte certa, trazida por esta criatura que não se vê. Você lançará um Encanto da Fraqueza ou aceitará seu destino?"

    menu:
        "usar encanto de fraqueza? (teste de sorte)":
            play sound "musics/efeito_sonoro/dados.mp3"

            $ d20roll = renpy.random.randint(1, 20)

            if (d20roll>=12):
                $renpy.notify("sucesso de sorte")
                play sound "musics/efeito_sonoro/sorte-sucesso.mp3"
                n "você lança o encanto com sucesso"

                jump um59
            else:
                $renpy.notify("fracasso de sorte")
                play sound "musics/efeito_sonoro/sorte-fracasso.mp3"
                n "sob o efeito da dor extrema, você erra o feitiço, tornando a criatura mais forte ao inves de fraca!"

                jump dois80
        "aceitar seu destino e ver no que dá?":
            jump dois80

label tres23:
    n "Você desperta e olha em torno de si. À medida que sua memória volta, você fica admirado de estar
    vendo. A sua perna está sensível, mas não há ferimento!"

    n "Você ouve um risinho frouxo vindo de um
    lugar acima de você e subitamente a coisa toda faz sentido..."

    n "Autuando acima de você está O'Seamus, agora rindo alto. A coisa toda foi uma grande brincadeira!
    Você fica furioso e salta de pé, mas, ao olhar para o engraçado homenzinho que rola pelo ar em
    gargalhadas histéricas, você não outra opção a não ser ver o lado engraçado da coisa também."
    n "Você dá um risinho, depois mais uma risada, e acaba rindo alto. Por algum tempo, vocês dois se acabam
    de dar gargalhadas, até que as lágrimas rolam pelos seus rostos."

    n "Quando os dois conseguem se controlar, vocês acabam se sentando para conversar. Ele é um
    homenzinho agradável. Antes de você sair, ele diz: 'Você é realmente um cara legal. O caminho à
    sua frente, porém, está cheio de perigos. Mas talvez isto possa ajudá-lo.'"
    n " Com um movimento da mão, ele faz com que apareça um prato na mesa. O prato é, na realidade, um Espelho de Prata de excelente
    qualidade. Saia do aposento pela:"

    $renpy.notify("adquiriu espelho!")

    play sound "musics/efeito_sonoro/item encontrado.mp3"

    $espelho = True

    menu:
        "abrir a porta com maçaneta de latao?":
            jump tres86
        "abrir a porta com maçaneta de cobre?":
            jump um44
        "abrir a porta com maçaneta de bronze?":
            jump tres38

label tres86:
    n "Do lado de fora da porta, a passagem continua em declive, e você a segue por algum tempo. Você
    repara que há um cheiro desagradável que fica cada vez mais forte à medida que você avança.
    Afinal, você chega a uma abertura."
    n "Olhando por ela, e tapando o nariz, você pode ver um grande
    esgoto a descoberto que corre transversalmente à passagem. Há uma corda que pende do teto."
    n "Você atravessará o esgoto ou tentará agarrar a corda e se valer dela para passar para o
    outro lado?"
    menu:
        "atravessar o esgoto?":
            jump dois04
        "agarrar a corda e se balançar para o outro lado?":
            jump um08


label final_ruim:

    play music "musics/Savfk - Deep.mp3"

    scene game_over:
        zoom 1.5

    $renpy.notify("fim de jogo")

    n "voce falhou em sua missão e Balthus Dire agora avança em direção a sua terra natal, que destino a espera?"

    return


label batalha_guardas:

    hide guarda1
    hide guarda2

    show mc normal at left:
        zoom 0.6
    with fade

    show guarda1 at right:
        zoom 1.3
    with dissolve

    show guarda2:
        xpos 1050
        ypos 400
        zoom 0.9
    with dissolve

    $ oponente_max_hp = 30
    $ mago_max_hp = 50
    $ oponente_hp = oponente_max_hp
    $ mago_hp = mago_max_hp
    $ elixir_left = 13

    show screen batalha_generica

    while (oponente_hp > 0):

        if mago_hp > 0:
            menu:

                "Ataque com espada (2 a 3 de dano)":

                    play sound "musics/efeito_sonoro/ataque espada.mp3"

                    $ mago_damage = renpy.random.randint(2, 3)
                    $ oponente_hp -= mago_damage
                    mc "Raaaaah!!!!! (dano causado - [mago_damage]hp)"


                "Bola de fogo (3 a 7 de dano)":

                    play sound "musics/efeito_sonoro/bola de fogo.mp3"

                    $ mago_damage = renpy.random.randint(3, 7)
                    $ oponente_hp -= mago_damage
                    mc "Bola de fogo!!!!! (dano causado - [mago_damage]hp)"



                "Raio arcano (3 a 10 de dano)":

                    play sound "musics/efeito_sonoro/raio arcano.mp3" volume 0.7

                    $ mago_damage = renpy.random.randint(3, 10)
                    $ oponente_hp -= mago_damage
                    mc "Raio arcano!!!!! (dano causado - [mago_damage]hp)"

                "tomar elixir da vida (tem [elixir_left] elixires)" if elixir_left > 0:
                    $ mago_hp = min(mago_hp+5, mago_max_hp)
                    $ elixir_left -= 1
                    n "{i}*você sente suas feridas cicatrizarem!*{/i} (vida curada - 5 hp)"
        else:
            jump final_ruim

        if(oponente_hp > 0):
            $ oponente_damage = renpy.random.randint(2, 6)

            $ mago_hp -= oponente_damage

            n " {i}*os guardas te atacam!*{/i} (dano recebido - [oponente_damage]hp)"

            play sound "musics/efeito_sonoro/gemido-combate.mp3"

    hide screen batalha_generica
    'oponentes derrotados!!!'
    jump dois51

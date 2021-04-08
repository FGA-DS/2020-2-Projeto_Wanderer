# The script of the game goes in this file.

init python:
    dinheiro       = False
    amoras         = False
    espelho        = False
    chave_cobre    = False
    escova_cabelo  = False
    vidro_ungento  = False
    aranha_garrafa = False
    velo_ouro      = False

define flash = Fade(.25, 0, .75, color="#fff")

##define config.menu_include_disabled = True

##default allow_choice = False

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define n  = Character("narrador")
define mc = Character("Mago")
define b  = Character("Balthus")

image Mapa = "images/Mapa.png"

## personagens
image mc normal  = "images/mc a.png"
image mc bombado = "images/mc.png"
image mc invertido     = "images/mc invertido.png"
image guarda1    = "images/mamaco.png"
image guarda2    = "images/lobinho2.png"
image gremlim1 = "images/gremlim1.png"
image tentaculo = "images/tentaculos.png"
image hydra = "images/hydra.png"
image homem1 = "images/homem1.png"
image homem2 = "images/homem2.png"
image goblin1 = "images/goblin1.png"
image goblin2 = "images/goblin2.png"
image orca = "images/orca.webp"
image anao = "images/anao.png"
image velha = "images/velha.png"
image porteiro   = "images/PW minotauro.png"
image oseamus    = "images/duende.png"
image pedroso    = "images/pedra.png"
image morena     = "images/morena.png"
image morena2    = "images/PW succubus4"
image goblins    = "images/Goblin_Troop.png"
image mordomo = "images/mordomo macabro.png"
image gark = "images/gark.png"
image bibliotecario = "images/bibliotecario.png"
image orcs = "images/orcs.png"
image maguito = "images/maguito.png"
image leviata = "images/leviata.png"
image heitoba = "images/heitoba.png"
image calacorm = "images/calacorm.png"
image balthus normal = "images/balthus.png"
image balthus bombado = "images/balthus 2.png"
image giras            = "images/giras.png"
image velha1           = "images/velha1.png"
image velha2           = "images/velha2.png"
image velha3           = "images/velha3.png"
image devlin           = "images/devlin.png"
image cria1            = "images/cria1.png"
image cria2            = "images/cria2.png"

## backgrounds
image entrada_caos     = "images/PW entrada cidadela.jpg"
image caminho_cidadela = "images/PW campo escuro.jpg"
image cidadela1        = "images/PW cidadela.jpg"
image poco             = "images/fundo-poco.jpg"
image portao           = "images/portao.jpg"
image corredor         = "images/corredor.jpg"
image sala_oseamus     = "images/sala oseamus.jpg"
image game_over        = "images/game_over.jpeg"
image templo           = "images/temple.jpg"
image aposento         = "images/PW dentro fortaleza.jpg"
image templo_floresta  = "images/templo_floresta.jpg"
image fumaca           = "images/fumaca.jpg"
image bg               = "images/bg.jpg"
image corredor_escuro  = "images/corredor escuro.png"
image esgoto           = "images/esgoto.jpg"
image passagem_esgoto  = "images/passagem esgoto.jpg"
image sala_golem       = "images/rodiney.jpg"
image sala_jantar      = "images/sala de jantar.jpg"
image portais          = "images/portais.jpg"
image quarto_morena    = "images/quarto morena.jpg"
image quarto_goblin    = "images/quarto goblins.jpg"
image bg2              = "images/bg2.jpg"
image bg3              = "images/PW dentro fortaleza3.jpg"
image bg5              = "images/bg5.jpg"
image biblioteca       = "images/biblioteca.jpg"
image salao            = "images/PW dentro fortaleza4.jpg"
image prisao           = "images/prisao.jpg"
image topo_torre       = "images/topo da torre.jpg"
image arena_final1     = "images/PW arena final.jpg"
image arena_final2     = "images/campo etereo.jpg"
image fim_sub          = "images/submissao.jpg"
image fim_lorde        = "images/trono lorde do caos.jpg"
image fim_alvor        = "images/alvorecer.jpg"
image escada           = "images/escadas.jpg"
image quarto_escuro    = "images/escuro.jpg"
image bg6              = "images/bg6.jpg"
image bg7              = "images/bg7.jpg"
image bg8              = "images/bg8.jpg"
image bg9              = "images/bg9.jpg"
image bg10             = "images/bg10.jpg"
image bg11             = "images/bg11.jpg"
image bg12             = "images/bg12.jpg"
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
        em plantas medicinais?":
            jump dois61
        "Você dirá que é um comerciante?":
            jump dois30
        "Você pedirá abrigo para pernoitar?":
            jump dois0

label dois61:
    n "O Macaco-Cachorro pede para ver as suas ervas. Por sorte, você tinha apanhado alguns punhados de ervas no caminho, e você mostra isso a eles."

    n "Inclinando a cabeça para um lado, a criatura olha para você com desconfiança.
    Pergunta a você então o nome do guarda que veio tratar, uma coisa que não estava nos seus planos!"

    n "Você pensa rapidamente em um nome para enganar a criatura:"
    menu:
        "Kylltrog":
            jump oito1
        "Pincus":
            jump um75
        "Blag":
            jump tres94

label oito1:
    n "O Macaco-Cachorro ri e diz a você que Kylltrog é um preguiçoso que não serve para nada, e que não vale a pena salvá-lo.
    Você solta um suspiro de alívio quando ele caminha de volta e grita para chamar o porteiro.
    Alguns momentos depois, o porteiro aparece e abre uma pequena porta para deixar você entrar."
    jump dois51

label um75:
    n "A criatura nunca ouviu falar de nenhum Pincus no interior da Cidadela. O Cachorro que está segurando a clava rosna e dá um passo adiante."
    menu:
        "Escolher outro nome rapidamente (Teste de sorte)":
            jump um10
        "Lutar contra eles":
            jump dois88

label um10:

    $ d20roll = renpy.random.randint(1, 20)

    if (d20roll>= 10):
        $renpy.notify("sucesso de sorte")
        play sound "musics/efeito_sonoro/sorte-sucesso.mp3"
        n "Você obteve sucesso para falar outro nome conhecido pelos guardas, e o porteiro permitiu a sua passagem."
        jump dois51

    else:
        $renpy.notify("fracasso de sorte")
        play sound "musics/efeito_sonoro/sorte-fracasso.mp3"
        n "Você não teve sorte e terá que lutar contra os guardas."
        jump dois88

label tres94:
    n "As criaturas se olham, como se o nome não fosse estranho para eles, mas elas não conseguiram se lembrar exatamente de onde o conheciam.
    Você rapidamente acrescenta que ele está na turma do primeiro andar."
    n "Eles dão de ombros e acabam por decidir que você deve estar falando a verdade. O Macaco-Cachorro chama o porteiro, que finalmente aparece para deixar você entrar."
    jump dois51

label dois30:
    n "'Veio ganhar algum dinheiro, né?!', diz o Macaco. 'Bem, você pode dividir um pouco dos seus lucros conosco!'"
    n "Como você não tem nada para oferecer a eles:"
    menu:
        "Lançar um Encanto do Ouro dos Tolos sobre uma pedra e oferecer a eles (Teste de sorte)":
            jump nove6

        "Prepare-se para a batalha!":
            jump dois88

label dois0:

    n "O Macaco-Cachorro diz que não é permitido a ninguém entrar na Torre Negra depois que anoitece
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
                play sound "musics/efeito_sonoro/nao tem o item.mp3"
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
        "Caminha decididamente, atravessando o pátio? ":
            jump um79
        "Vai na ponta dos pés pelas sombras, na direção de um dos grupos? ":
            jump tres21

label um79:
    stop music
    play music "musics/sb_phoenix.mp3"
    n "Quando você sai das sombras na direção do centro do pátio, uma voz no vento grita: 'Pare! Fique onde está!'
    Você olha a sua volta, mas não consegue ver ninguém que esteja se dirigindo a você."
    n "Você dá mais dois passos. A voz sinistra ordena de novo que você parem, e, dessa vez, uma flecha zune pelo ar e cai próximo ao seu pé esquerdo.
    Você pula para trás. Porém, ainda assim não vê ninguém e não pode se mexer."
    n "Dessa forma, você: "
    menu:
        "Seguirá adiante, muito cuidadosamente":
            jump tres78
        "Disparará na direção do monumento no meio do pátio":
            jump um25
        "Lançará um Encanto do Escudo à sua volta e seguirá avançando":
            jump tres41

label um25:
    n "Quando você começa a correr, três flechas partem em sua direção, vindas de nenhum lugar, testando a sua sorte."
    $ d20roll = renpy.random.randint(1, 20)

    if (d20roll>= 10):
        $renpy.notify("sucesso de sorte")
        play sound "musics/efeito_sonoro/sorte-sucesso.mp3"
        n "Você foi muito sortudo e todas as flechas não o acertaram, e, com isso, conseguiu chegar ileso sob a cobertura do monumento."
        jump dois09

    else:
        $renpy.notify("Fracasso de sorte")
        play sound "musics/efeito_sonoro/sorte-fracasso.mp3"
        n "Ao correr, uma das flechas o acertou no ombro ao chegar atrás do monumento. Assim você descansa por uns minutos para se recuperar do ferimento."
        play sound "musics/efeito_sonoro/gemido-combate.mp3"
        jump dois09

label tres41:
    n "Você lança o Encanto em torno de si mesmo e avança. Quatro ou cinco flechas voam em sua direção, mas param no ar a um metro de distância antes de te atingirem, caindo inofensivamente
    no chão."
    n "Dessa forma, você consegue chegar atrás do monumento ileso."
    jump dois09

label tres78:
    n "Você dá alguns passos adiante, e uma outra flecha erra por pouco o seu pé."
    n "Mais uns poucos passos e uma flecha rasga a sua túnica, arranhando o seu antibraço.
    Você ainda não consegue ver ninguém, nem de onde as flechas estão vindo."
    n "Depois de alguns passos, surge mais uma flecha, mas essa rasga a sua perna. Você grita alto"
    play sound "musics/efeito_sonoro/gemido-combate.mp3"
    scene templo at truecenter:
        zoom 1.3
    n "Como você já estava perto do monumento, dá um salto para frente e se esconde atrás dele até as flechas pararem de vir."
    jump dois09

label dois09:
    scene templo at truecenter with fade:
        zoom 1.3
    n "Você pousa os olhos sobre a estranha estrutura. Não parece ser uma fonte, mas alguma espécie de templo, em que você:"
    menu:
        "Verá uma porta, de um lado, e poderá investigar":
            jump tres62
        "Poderá seguir em frente para a Cidadela propriamente dita.":
            jump um56

label tres62:
    scene aposento at truecenter:
        zoom 1
    show gremlim1 at center:
        ypos 1000
        zoom 0.7

    n "A porta abre, e o pequeno aposento no interior é iluminado a luz de vela. Cautelosamente, você olha lá para dentro e vê uma cena estranha.
    Sobre uma mesa de madeira no canto do aposento, há três recipientes, cada um contendo um líquido de cor diferente: um claro, outro vermelho e outro leitoso."
    n "Há uma pequena criatura alada, semelhante a gremlin, que está em torno da mesa, chilreando excitadamente.
    De vez em quando, ele vai para a mesa e toma um gole do líquido leitoso."
    n "A porta aberta range nas dobradiças e assusta o ser. Ele dá uma volta para olhar você e fica muito excitado. Com isso, você:"

    menu:
        "Pode entrar no cômodo":
            jump cinco8
        "Fechar a porta rapidamente e prosseguir em direção à Cidadela":
            hide aposento with fade
            jump um56

label cinco8:
    "Quando você entra, o Gremlin esvoaça e guincha excitado, depois voa, passando por você e saindo pela porta noite adentro. Você agora está sozinho
    com os recipientes. Arriscará beber algum?"
    #hide gremlim1
    #hide gremlim2
    #hide gremlim3
    menu:
        "O líquido claro":
            jump dois98
        "O líquido vermelho":
            jump dois67
        "O líquido leitoso":
            jump nove2
        "Caso não, prosseguirá na direção da Cidadela":
            hide aposento with fade
            jump um56

label um56:
    #hide aposento with fade
    #hide gremlim1 with fade
    #hide gremlim2 with fade
    #hide gremlim3 with fade
    scene templo_floresta at truecenter with fade:
        zoom 1
    show mc normal at left:
        zoom 0.6
    with fade

    show tentaculo at right with dissolve:
        zoom 0.8
        ypos 1050

    n "Enquanto você caminha pelo pátio ao ar livre, repara que está andando ao longo de uma pequena elevação, quase que como um encanamento enterrado que fosse da Torre Negra para o templo."

    n "Você se abaixa para investigar isso, poderia ter sido feito por algum tipo de toupeira?"
    n "Quando você toca na elevação, ela se retrai e, para seu horror, um longo tentáculo cinzento irrompe do solo
    e se enrosca em torno de sua perna!"
    n "Como você lutará com esta 'coisa'?"
    menu:
        "Desembainhará a sua espada":
            jump sete1
        "Lançará um Encanto da Levitação":
            jump dois84
        "Lançara um Encanto do Fogo":
            jump um14

label dois98:
    n "Quando suas mãos se fecham em torno do cálice, ele começa a efervescer e a espumar, respingando em você quando você o ergue até seus lábios. Você tem certeza de quer experimentar isso?"
    menu:
        "Sim! Estou Determinado!":
            jump um41
        "Acho melhor não, vou tomar uma decisão melhor.":
            jump cinco8

label um41:
    n "O líquido tem um gosto salgado, e você começa a suar frio quando engole. Em seguida, você tem tremores e tenta se aprumar na mesa. Porém, você cai para frente, derrubando os outros dois recipientes
    no chão e derramando os outros líquidos."
    scene fumaca at truecenter with dissolve:
        zoom 4
    n "Você também acaba caindo no chão, sentindo-se extremamente mal e com a visão turva. Como em um sonho, você tem uma visão de uma estranha criatura musculosa várias cabeças,
    uma calda comprida e uma pele de escamas amareladas."
    show hydra at center with pixellate:
        zoom 2.5
        ypos 900
    n "Tem nas mãos um grande molho de chaves. Um rato atravessa a mesa em que ela está sentada e ela grita alto..."
    n "O grito acorda você com um sobressalto e você toma consciência de onde está. Você reúne suas forças e tateia em busca da maçaneta da porta."
    n "Você precisa de ar fresco! Assim, sai da câmara, descansa alguns momentos e parte em direção da Cidadela..."
    hide hydra
    hide fumaca
    hide aposento with fade
    jump um56

label dois67:
    n "Quando você segura o cálice, o líquido fica verde, e depois marrom sujo, diante de seus olhos. Cheira a podre, mas você toma um gole. Com uma careta, você cospe tudo, pois descobriu que é água lamacenta!!"
    n "Você sai da câmara e se dirige à Cidadela."
    hide aposento with fade
    jump um56

label nove2:
    n "O líquido leitoso cheira bem. Você toma um gole e começa a sorrir. Dá um gole maior e explode em gargalhadas, por motivo nenhum!"
    n "Não é de se estranhar que os pequenos Gremlins estivessem gostando tanto. Com a cabeça leve e de bom humorm você sai do aposento para continuar em seu caminho para a Cidadela."
    hide aposento with fade
    jump um56

label sete1:
    n "Você desembainha a espada e vai golpear o tentáculo! O tentáculo tenta te arrastar para o grande buraco que está se abrindo em torno da base dele!"
    jump batalha_tentaculo

label dois84:
    n "Você lança o encanto e começa a sair do chão. O tentáculo não solta, e a dor em sua perna se torna insuportável. Você resolve retornar ao solo antes que a sua perna seja arrancada do corpo."
    n "Você terá que escolher outra maneira de passar pelo tentáculo."
    $encanto_levitacao = False
    menu:
        "Desembainhar a espada e lutar contra o tentáculo":
            jump sete1
        "Lançar um feitiço de fogo":
            jump um14

label um14:
    n "Você aponta para a base do tentáculo e lança o encanto. Um rolo de fumaça e um clarão luminoso irrompem do buraco no solo. Um tremor percorre o tentáculo, e, felizmente, ele afrouxa."
    n "Quando ele retorna para dentro do solom você esfrega sua perna para recuperar a circulação e depois na direção da entrada principal da Cidadela novamente."
    $encanto_fogo = False
    jump dois18

label tres21:
    n "Cautelosamente, e mantendo-se fora da área visível, você se esgueira pelas bordas do pátio na escuridão. Há dois grupos de criaturas à sua frente."
    show homem2 at right:
        zoom 0.9
    show homem1 at center:
        xpos 1300
        zoom 1.9
    n "À direita, você pode ver duas figuras de aparência humana conversando sob uma tocha presa à parede."
    show orca at left:
        zoom 1.2
    show anao at left:
        zoom 0.5
        xpos 450
    show goblin1 at left
    show goblin2 at left:
        zoom 0.2
        ypos 1027
    n "À esquerda, um grupo criaturas, de variadas formas e de tamanhos, estão sentados em volta de uma fogueira comendo."
    n "Você irá abordar o grupo da esquerda ou a dupla da direita?"
    menu:
        "Grupo da esquerda":
            jump tres39
        "Dupla da direita":
            jump dois69

label dois69:
    hide orca
    hide anao
    hide goblin1
    hide goblin2
    n "Os dois homens estão sujos e maltrapilhos. Quando se aproxima, você pode ouvi-los discutindo em
    voz alta sobre o preço de um punhal. O mais alto deles está obviamente tentando vender o punhal
    para o outro."
    n "Ele argumenta que o punhal é encantado, e vale mais do que o outro está disposto a
    pagar por ele. Quando você chega mais perto, ele pega você pelo braço e pergunta sua opinião sobre
    o preço da arma. O que você dirá:"
    menu:
        "Cinco Peças de Ouro?":
            jump dois05
        "Dez Peças de Ouro?":
            jump dois25

label dois05:
    hide homem1 with fade
    n "O comerciante fica indignado com o baixo preço que você colocou para o punhal dele e desembainha a sua espada, você age da mesma forma e se prepara para a batalha."
    jump batalha_contra_um

label dois25:
    n "Os dois ficam nervosos com o tom que você usa ao falar, e acham que foi muito arrogante. Assim ambos vão te
    ameaçar e você age igualmente. Prepare-se para lutar contra os dois oponentes!"
    jump batalha_contra_dois

label tres39:
    hide homem1 with dissolve
    hide homem2 with dissolve
    n "Há um time eclético sentado em volta do fogo. Uma orca está distribuindo magros bocados de carne mal passada para os outros."
    n "Um anão de pele gastada rosna e reclama do tamanho do seu pedaço, enquanto dois globins, homem e mulher, estão se acariciando. Eles riem e se sacodem, e de
    vez em quando ela dá um tapa na cara feia do macho, causando ainda mais risos."
    n "Quando você se aproxima, eles param e olham para você com rostos poucos amigáveis. Olham com desprezo para a sua aparência asseada, e a Globin fêmea
    cochicha algum comentário para seu companheiro."
    n "Na frente do anão você pode ver uma caixa aberta e com dificuldade distingue um frasco de líquido dentro dela."
    n "Dessa forma, você:"
    menu:
        "Sentará com eles em torno do fogo":
            jump um34
        "Perguntará se você pode se unir a eles":
            jump um49

label um34:
    n "Eles ficam admirados com a sua audácia. Ao invés de esperar que eles falem, você age agressivamente e exige saber como entrar na Cidadela. Eles apontam para a entrada principal,
    obviamente um tanto espantados com seu modo confiante e cochicham entre eles."
    n "A orca diz a você que será preciso uma senha, 'CIMITARRA', para entrar. Você pergunta a respeito do frasco de líquido dentro da caixa, o que faz com que eles fiquem agitados, então você:"
    menu:
        "Os pressiona para obter mais informações sobre o frasco":
            jump seis0
        "Segue adiante na direção da Torre Negra":
            jump dois45

label seis0:
    n "As criaturas ficam desconfiadas quando você as pressiona buscando informações. O anão salta rapidamente de pé, brandindo uma clava de madeira, enquanto o goblin
    e a orca pegam espadas e olham com raiva de você."
    n "A namorada do goblin grita e recua vários passos, enquanto os outros avançam na sua direção. Você terá que lutar contra eles."
    jump batalha_criaturas

label dois45:
    hide mc normal
    hide anao
    hide orca
    hide goblin1
    scene bg at truecenter:
        zoom 2
    n "Você parte na direção da Cidadela. Embora o ar da noite esteja calmo, você ouve um assobio fraco,
    que rapidamente fica cada vez mais alto, até que uma forte lufada de vento subitamente atinge você
    com tamanha força, que você mal consegue se mexer no sentido contrário."
    show velha at right
    n "Você protege os olhos, até que a ventania diminui um pouco, e, quando você os abre, vê uma face fantasmagórica de
    mulher dentro do que parece ser um Redemoinho vivo."
    n "Ela move os lábios, dizendo palavras que você não consegue distinguir, mas, alguns segundos depois de ela ter terminado de falar, a
    mensagem chega até você."
    n "Ela parece considerar a sua aparência como ofensiva e está desafiando você com palavras agressivas. Você segura a sua espada, mas ela ri. Assim:"
    menu:
        "Você conversará com ela":
            jump tres90
        "Usará a sua magia para se livrar dela":
            jump quatro7

label tres90:
    n "Estranhamente a conversa flui, e, após algum tempo, ela lhe deixa e você prossegue a sua jornada."
    jump dois18

label quatro7:
    n "Com a pressão gerada pela situação, teste sua sorte ao conjurar o Encanto."
    $ d20roll = renpy.random.randint(1, 20)

    if (d20roll>= 10):
        $renpy.notify("sucesso de sorte")
        play sound "musics/efeito_sonoro/sorte-sucesso.mp3"
        n "Ela observa espantada o aparecimento de uma réplica perfeita dela mesma entre vocês dois. Ela recua um pouco, e você orienta a sua criação para o ataque."
        n "Mas, quando elas se aproximam uma da outra, acontece uma coisa estranha."
        n "Elas parecem ser incapazes de chegar perto uma da outra, como duas extremidades giratórias, e sempre separam-se bruscamente de um salto."
        n "Porém, sua própria cópia pelo menos forçou a criatura a se afastar de você para uma certa distância, permitindo quevocê corra para a entrada principal da Cidadela."
        jump dois18

    else:
        $renpy.notify("fracasso de sorte")
        play sound "musics/efeito_sonoro/sorte-fracasso.mp3"
        n "Você recua em direção ao centro do pátio para se esconder dela."
        jump dois09

label um49:
    n "Eles não estão interessados em sua companhia e sugerem que você siga o seu caminho. Então você:"
    menu:
        "Prosseguirá em direção à Torre Negra":
            jump dois18
        "Sentará ao fogo de qualquer maneira":
            jump um34

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
        "seguir na direção da porta":
            jump cinco
        "descer as escadas":
            jump tres44

label cinco:
    n "Você experimenta a maçaneta da porta e ela gira, abrindo para um outro corredor. Logo adiante, a
    passagem vira para a direita e termina pouco depois em outra porta. Nesta porta há um letreiro que
    diz 'Por Favor Toque a Campainha para Chamar o Mordomo'. Uma corda - evidentemente a
    campainha - pende ao lado da porta."
    menu:
        "Você toca a campainha conforme indicado":
            jump quatro0
        "Experimenta a maçaneta da porta":
            jump tres61



label tres61:
    n "A porta abre novamente mas, quando você faz isso, ouve o ruído ensurdecedor de uma campainha
de alarme! Teste a sua Sorte."
    play sound "musics/efeito_sonoro/dados.mp3"

    $ d20roll = renpy.random.randint(1, 20)

    if (d20roll>=13):
        $renpy.notify("sucesso de sorte")
        play sound "musics/efeito_sonoro/sorte-sucesso.mp3"
        n "..."
        jump dois97
    else:
        $renpy.notify("fracasso de sorte")
        play sound "musics/efeito_sonoro/sorte-fracasso.mp3"
        n "..."
        jump um26

label dois97:
    hide corredor
    scene bg6 at truecenter:
        zoom 1.5
    n "Você bate a porta, fechando-a atrás de você, e, juntamente como alarme estridente, você ouve o som
de passos, correndo rapidamente e se aproximando. Você conseguiu fugir a tempo e escapar das criaturas."
    jump dois20

label um26:
    hide corredor with fade
    show bg6 at truecenter:
        zoom 1.5
    show giras at left:
        xpos 220
        ypos 950
        zoom 1.3
    with dissolve
    n "Você para para considerar a situação, em pânico. À sua frente, a passagem se bifurca para a
esquerda e para a direita. Enquanto você está tentando decidir que direção tomar, três criaturas
surgem da passagem do lado esquerdo."
    n "Chamar os ruídos que você ouviu de 'passos' não é inteiramente preciso, como você verá."
    jump tres16

label tres16:
    n "As passadas que você ouviu - que realmente deveriam ser chamadas de 'mãozadas' – pertencem a
três GIRAS, que agora rolam descendo a passagem na sua direção, o que faz com que você recue de
volta para a porta."
    n "Estas criaturas são animais peculiares que têm, ao invés de pernas, um segundo
par de mãos. Eles se deslocam dando cambalhotas a um ritmo bem acelerado. Suas cabeças - ou
pelo menos seus rostos - estão colocados no centro do peito."
    n "Embora não sejam muito prático como
espadachins, tendo em vista seus meios de movimentação inadequados, são excelentes lançadores de facas."
    n "Pegando facas em seus cintos enquanto se movimentam em círculos, eles podem dispará-
las em velocidade de fogo rápido, como rodas-de-santa-catarina. No momento, três facas desse tipo
estão cruzando o ar na sua direção."
    n "Você usará um Encanto do Escudo para se proteger (Teste de sorte)."
    play sound "musics/efeito_sonoro/dados.mp3"

    $ d20roll = renpy.random.randint(1, 20)

    if (d20roll>=13):
        $renpy.notify("sucesso de sorte")
        play sound "musics/efeito_sonoro/sorte-sucesso.mp3"
        n "As facas atingem o seu escudo mágico e caem ao chão. Você conseguiu escapar das criaturas."
        jump dois20
    else:
        $renpy.notify("fracasso de sorte")
        play sound "musics/efeito_sonoro/sorte-fracasso.mp3"
        n "sob pressão, você erra algumas palavras do encanto,
        fazendo com que ele não seja eficaz, e você parte para a batalha!"
        jump tres46

label tres46:
    n "Quando os Giras vêem você desembainhar a sua espada, param e tagarelam com muita agitação.
    Um deles - evidentemente o líder - manda o menor subir a passagem de volta (presumivelmente
    para buscar ajuda). Os outros dois puxam facas e rolam lentamente na sua direção."
    n "Prepare-se para a batalha!"

    jump batalha_giras

label batalha_giras:
    show mc invertido at right:
        zoom 0.9
        xpos 2350
    with dissolve
    #show giras
    $ oponente_max_hp = 30
    $ mago_max_hp = 50
    $ oponente_hp = oponente_max_hp
    $ mago_hp = mago_max_hp
    $ elixir_left = 13

    show screen batalha_generica1

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
            hide screen batalha_generica
            jump final_ruim

        if(oponente_hp > 0):
            $ oponente_damage = renpy.random.randint(2, 6)

            $ mago_hp -= oponente_damage

            n " {i}*o oponente te arrasta para o seu covil!*{/i} (dano recebido - [oponente_damage]hp)"

            play sound "musics/efeito_sonoro/gemido-combate.mp3"

    hide screen batalha_generica
    #hide mc
    #hide giras
    'Oponente derrotado e você parte em direção às passagens!'
    jump dois20

label dois20:
    n "Você poderá tomar a passagem do lado esquerdo, ou a passagem do lado direito."
    menu:
        "Passagem pela esquerda":
            jump dois43
        "Passagem pela direita":
            jump dois

label dois:
    scene bg7 at truecenter:
        zoom 2.2
    n "Um pouco adiante na passagem há uma porta do lado direito. Esta porta está coberta por estranhos
caracteres, em uma linguagem que você não compreende. Dessa forma, você:"
    menu:
        "Tentará abrir a porta":
            jump um42
        "Seguirá a passagem":
            jump tres43

label um42:
    n "Você experimenta a maçaneta, e ela gira. Você não consegue ouvir nada vindo do interior do
aposento, por isso você abre a porta para dar uma olhada."
    n "O aposento é pequeno, com um castiçal dourado em cima de uma mesa... mas, de repente, você ouve um rangido vindo do assoalho! Tarde
demais, você compreende que as pedras sob os seus pés estão se mexendo para revelar um alçapão!"
    n "Você cai primeiro em um poço. Quando atinge o fundo, você rola para o lado, descendo outra
passagem, e continua rolando para baixo. Por mais que você tente, não consegue impedir que você
role sem parar, até que acaba por chegar a uma pequena câmara, onde finalmente pára."
    n "Mas o choque foi demais para você. Enquanto o mundo escurece à sua volta, você ouve uma tagarelice
excitada, e depois desmaia."
    jump dois34

label tres43:
    scene bg8 at truecenter:
        zoom 1.2
    n "Seguindo o caminho após a passagem. Você se depara com um beco sem saída. Dessa forma, você procura por passagens secretas."
    jump um0

label um0:
    n "Você tateia pela rocha e acaba por encontrar uma pequena alavanca. Ao puxar esta alavanca, a face
da rocha esfarela um pouco e aparece uma pequena abertura."
    n "Você sobe por esta abertura e chega a uma passagem. Descendo a passagem para a esquerda, você pode ver uma porta e resolve
investigar."
    jump dois49

label dois49:
    scene bg9 at truecenter:
        zoom 1.5
    n "A passagem termina à sua frente em uma porta de madeira. Há um letreiro afixado nela, dizendo
'DESPENSA'. Você cola os ouvidos junto a ela, mas não ouve nada. A porta está trancada."
    menu:
        "Se você tiver uma Chave de Cobre, poderá tentar usá-la aqui":
            if (chave_cobre == True):
                n "a chave gira e a porta abre!"
                jump um96
            else:
                play sound "musics/efeito_sonoro/nao tem o item.mp3"
                $renpy.notify("você não possui esse item!")
                n "Você se lembra que não tem a chave e terá que arrombar a porta."
                jump dois31
        "Tentar arrombar a porta":
            jump dois31

label dois31:
    n "Você bate na porta com o ombro para derrubá-la (Teste de sorte)."
    play sound "musics/efeito_sonoro/dados.mp3"

    $ d20roll = renpy.random.randint(1, 20)

    if (d20roll>=13):
        $renpy.notify("sucesso de sorte")
        play sound "musics/efeito_sonoro/sorte-sucesso.mp3"
        n "A porta cede e abre."
        jump um96
    else:
        $renpy.notify("fracasso de sorte")
        play sound "musics/efeito_sonoro/sorte-fracasso.mp3"
        n "Mesmo a pancada sendo muito forte, a porta apenas tremeu e você machucou muito seu ombro!"
        jump nove99

label nove99:
    n "Após alguns instantes se recuperando, você ouve um estrondo."
    n "Milagrosamente, a porta cedeu e você conseguirá prosseguir a sua jornada."
    jump um96

label um96:
    scene bg10
    n "Ao entrar, o aposento é de fato uma despensa. Num primeiro momento, os cheiros estranhos - uma mistura de
comida doce, temperada e azeda - pegam você de surpresa. Há vários tipos de carne pendurada sem
ganchos ao longo de uma das paredes."
    n "Uma prateleira de queijos contém mais ou menos uma dúzia
de variedades de queijo, e você torce o nariz de nojo como cheiro forte dos, digamos, que estão
'maduros demais'."
    n "Você poderá sair pela porta na parede do lado esquerdo, ou pela porta na parede do lado direito"
    menu:
        "Porta do lado esquerdo":
            jump um3
        "Porta do lado direito":
            jump dois81

label um3:
    n "A maçaneta gira e você abre a porta para um outro aposento, onde há bastante atividade. Três
velhas feias, com narizes e queixos compridos, circulam pelo aposento - que parece ser alguma
espécie de cozinha - pegando vários ingredientes dos armários e acrescentando-os a um caldo
dentro de um grande caldeirão."
    scene bg11 at truecenter
    show velha1 at center:
        zoom 0.5
        xpos 850
    show velha2 at center:
        zoom 0.3
        xpos 650
    show velha3 at center:
        xpos 1300

    n "Há um pedaço de carne assando em um espeto, embaixo de uma
grande chaminé. Olhando mais atentamente, você descobre que a carne, na verdade, não é de um
animal, mas sim um Anão inteiro que escurece ao fogo."
    n "Uma das mulheres olha para você e diz: 'Ah, você deve ser o novo empregado...ou é a próxima refeição?', com o que todas as três
começam a dar gargalhadas e gritos enquanto riem."
    menu:
        "Você deixará que elas acreditem que você é o novo empregado que elas estão esperando":
            jump tres02
        "Investigar o aposento mais devagar":
            jump dois15

label tres02:
    n "Elas ordenam que você leve uma bandeja de comida por uma porta na parede do outro lado para o
Grande Salão e a deixe na mesa, pois os Ganjees logo estarão lá para ceia."
    n "Elas também advertem
você para que não espere pelo Ganjees, ou provavelmente você terminará sendo a próxima refeição.
Você leva a bandeja e sai pela porta distante."
    n "Feliz por ter saído da repulsiva cozinha delas, você segue uma passagem adiante, pára para deixar a bandeja e continua para uma outra porta. Você
experimenta a maçaneta e ela gira."
    jump um69

label dois15:
    n "Você terá que inventar alguma história para estas mulheres horrorosas. Você dirá a elas que o
Capitão da Guarda ordenou que se fizesse uma inspeção na cozinha delas, depois de uns dois casos
de intoxicação alimentar"
    jump um36

label um36:
    n "Todas elas protestam veementemente, mas você explica que tem suas ordens e começa a circular
pela cozinha."
    n "Você investigará:"
    menu:
        "Inspecionar os armários":
            jump um7
        "O espeto sendo assado":
            jump tres89

label um7:
    hide devlin with dissolve
    hide mc normal
    n "Ao investigar os armários todos os tipos de alimentos estranhos podem ser encontrados. Globos oculares, línguas,
lagartixas, frascos de líquidos, ervas e frutos silvestres de diferentes formas e tamanhos."
    n "Uma garrafa em especial, contendo um líquido verde transparente, chama a sua atenção. Você não tem
tempo para ler o rótulo no momento, por isso você a põe no bolso rapidamente, enquanto elas não
estão olhando."
    n "Você lhes diz que a cozinha parece estar em ordem e sai pela porta do lado oposto da cozinha."
    jump nove3

label nove3:
    n "Do lado de fora, você olha para sua garrafa. É uma garrafa de Essência de Erva de Porco,
aparentemente útil para repelir criaturas de base em pedra."
    n "Isso pode ser útil, e você a guarda cuidadosamente em sua mochila. Seguindo em frente pelo corredor, você chega a uma outra porta,
que abre, deixando que você passe para um grande aposento."
    jump um69

label tres89:
    n "Quando você se aproxima do espeto, uma das velhas joga um pó no fogo, e as três se afastam,
dando risadas. Você está em guarda. Você observa o fogo começando a rugir, e as chamas
crescendo ameaçadoramente."
    hide velha1 with dissolve
    hide velha2
    hide velha3
    n "Subitamente, várias das labaredas saltam do fogo e tomam a forma de
um DEVLIN, uma criatura do tamanho de um Anão, feita do próprio fogo! As três bruxas apontam
para você, e o Devlin avança. Assim você:"
    show devlin at right:
        zoom 0.7
        xpos 2300
    menu:
        "Usa magia (Teste de sorte).":
            play sound "musics/efeito_sonoro/dados.mp3"

            $ d20roll = renpy.random.randint(1, 20)

            if (d20roll>=13):
                $renpy.notify("sucesso de sorte")
                play sound "musics/efeito_sonoro/sorte-sucesso.mp3"
                n "Você lança o encanto com sucesso, e o Devlin se apaga. Você ganha a chance de inspecionar outro item da cozinha."
                jump um36
            else:
                $renpy.notify("fracasso de sorte")
                play sound "musics/efeito_sonoro/sorte-fracasso.mp3"
                n "sob pressão, você erra algumas palavras do encanto,
                fazendo com que ele não seja eficaz, e você parte para a batalha!"
                jump batalha_devlin

label batalha_devlin:
    n "Você avança com sua espada e parte para a batalha!"
    show mc normal at left:
        zoom 0.6
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
            hide screen batalha_generica
            jump final_ruim

        if(oponente_hp > 0):
            $ oponente_damage = renpy.random.randint(2, 6)

            $ mago_hp -= oponente_damage

            n " {i}*o oponente te arrasta para o seu covil!*{/i} (dano recebido - [oponente_damage]hp)"

            play sound "musics/efeito_sonoro/gemido-combate.mp3"

    hide screen batalha_generica
    'Oponente derrotado e você ganha a chance de inspecionar outro item da cozinha!'
    jump um7

label dois81:
    scene bg12 at truecenter:
        zoom 1.7
    show cria1 at right:
        xpos 1600
        ypos 820
        zoom 0.8
    show cria2 at right
    n "Você abre a porta para outro aposento e surpreende duas pequenas criaturas.
Elas te olham rapidamente, chocadas com a sua chegada. Você:"
    menu:
        "Inicia um combate":
            jump tres82
        "Tenta entabular uma conversa":
            jump tres56
        "Diz que está só de passagem":
            jump dois85

label tres82:
    n "Eles correm pelo aposento em pânico, esbarrando uns nos outros e gritando: 'Ai, meu Deus, ai,
minha nossa, este estranho parece malvado, onde estão as nossas armas?'"
    n "Você ri da desordem deles e guarda a sua espada. Eles se acalmam e ficam olhando para você. Você pode seguir adiante ou conversar com eles"
    menu:
        "Seguir adiante":
            jump dois85
        "Conversar com eles":
            jump tres56

label tres56:
    n "Eles ficam um tanto aliviados por saber que você não tem intenção de fazer mal a eles e voltam a
sentar-se no chão, convidando você para se juntar a eles."
    n "O aposento é pequeno e simples, com folhagens espalhadas pelas paredes, possivelmente com o intuito de servir de decoração, embora as
folhas estejam agora murchas e há muito tempo mortas. Um pequeno fogo arde em um dos cantos,
embaixo de um orifício no teto."
    n "Há duas portas na parede de fronte a você; uma à esquerda, a outra
à direita. Você senta para bater um papo. Você descobre que as pequenas criaturas magérrimas se
denominam ESCOTEIROS e são de fato um grupo agradável, que brinca e ri com você."
    n "Você resolve não se arriscar a dizer muito sobre a sua missão, mas faz perguntas genéricas sobre o lugar.
Balthus Dire é o senhor da casa e passa a maior parte do tempo lá no alto na Cidadela."
    n "A senhora sua esposa é uma feiticeira lindíssima que é muito vaidosa e aprecia as coisas que o dinheiro e o
poder podem proporcionar. Há muitas criaturas cruéis no interior da Cidadela, mas é preciso tomar
cuidado especial com os Ganjees, que vagueiam pela Torre à noite."
    n "Você acaba levantando, agradece pela conversa e se prepara para seguir adiante."
    n "Os Escoteiros oferecem também a você o direito de receber deles um favor antes de ir embora, pois eles também
apreciaram a sua companhia. Você pode:"
    menu:
        "Levar a sério a oferta deles":
            jump um46
        "Não aceitar e seguir adiante":
            jump dois85

label um46:
    n "Como favor, você pergunta como pode derrotar Balthus Dire."
    jump dois47

label dois47:
    n "Eles ficam chocados com seu pedido. Você pragueja ao compreender que não deveria ter revelado
sua verdadeira missão a eles. Todos eles tagarelam agitados, por algum tempo, depois voltam-se na
sua direção. Juntos, todos eles sopram com força."
    n "Para sua surpresa, o sopro deles é como um vento de tempestade, e você é atirado para trás de encontro à parede. Sua cabeça bate na parede áspera e
rochosa, e você perde os sentidos."
    hide bg12 with dissolve
    hide cria1
    hide cria2
    jump dois34

label dois85:
    n "Há duas portas na parede oposta. As pequenas criaturas dizem que você pode seguir adiante em seu caminho tanto por uma ponta
quanto pela outra. Você escolhe a porta da esquerda ou a porta da direita"
    menu:
        "Porta da esquerda":
            jump um85
        "Porta da direita":
            jump dois3

label um85:
    hide cria1 with dissolve
    hide cria2
    n "A porta se abre para um corredor estreito, que faz uma curva fechada para a esquerda, continua por
vários metros e então termina por fim em uma porta. Você põe a mão na maçaneta."
    jump um3

label dois3:
    hide cria1 with dissolve
    hide cria2
    n "Você abre a porta e sai em uma passagem que continua direto para frente por algum tempo. Vira
para a esquerda, depois para a direita, até que você chega a um arco à sua frente que dá para um
grande aposento. Você caminha na direção do aposento e entra nele."
    jump um69















label quatro0:
    scene bg2 at truecenter:
        zoom 1.5
    show mordomo at center:
        zoom 1.3
    n "Depois de vários minutos, a porta se abre lentamente, e uma criatura corcunda e deformada, com
    dentes podres, cabelos desgrenhados e roupas esfarrapadas, aparece na sua frente. 'Sim senhor (heh, heh) - o que posso
    fazer pelo senhor?' rosna a criatura semi-humana."
    n "'Estou sendo esperado', você responde e passa por ele, atravessando a porta com confiança. Ele fica um pouco surpreso com seu
    comportamento e gagueja, sem saber se entra em conflito com você ou não."
    n "'Onde é a recepção?' você pergunta. Ele olha para você de soslaio com um dos olhos e faz um gesto na direção de uma
    bifurcação para a esquerda, a pouca distância dali."
    n "Você, de maneira receosa, acreditará nele e tomará a bifurcação para a esquerda"
    hide mordomo
    jump dois43

label dois43:
    hide giras
    hide mc normal
    n "A passagem se estende por vários metros e depois termina em uma porta. Você escuta junto à porta
    e ouve uma respiração profunda e pesada vindo lá de dentro, como se alguma criatura de grande
    porte estivesse dormindo ali."
    n "Cuidadosamente, você experimenta a maçaneta, e a porta abre. Logona entrada, embora o aposento
    esteja escuro, você consegue ver uma criatura muito grande, semelhante a um Goblin, adormecida no chão."
    n "Você pode se arriscar a entrar no aposento na ponta dos pés"
    jump tres52

label tres52:
    scene bg3
    show gark at right:
        zoom 1.3
    n "Você entra no aposento na ponta dos pés. Está escuro lá dentro, e o ar está úmido. Há um poste de
    madeira rústica pregado em uma das paredes, com diversos ganchos nele. Há duas portas na parede do outro
    lado que levam adiante."
    n "No poste, pendurado, há um espelho improvisado, mas, quando sua tocha ilumina o espelho,
    seu reflexo é projetado sobre os olhos do gigante adormecido, que grunhe e se mexe."
    n "Um dos olhos se abre, depois o outro, ele salta de pé! Ele pega uma acha, que usava como travesseiro, e
    rapidamente retira a bainha de couro, revelando uma afiada cabeça de bronze."
    n "Esta criatura gigantesca é um GARK! Grandes e brutos, os Garks são meio Goblins, meio
    Gigantes, cruzados por senhores feiticeiros por sua índole agressiva."
    n "Embora um tanto estúpidos, são criaturas bastante violentas e de natureza guerreira. Você:"
    menu:
        "Vai dar uma corrida na direção das portas?":
            jump dois03
        "Desembainhará a espada, pronto para a luta?":
            jump um6
        "Pedirá desculpas por perturbar a criatura?":
            jump dois16
        "Vai se preparar para usar um Encanto":
            jump um1

label dois03:
    n "Ao correr para as portas, você tropeça, permitindo que a criatura ganhe terreno. Ela agarra seu braço
    com uma das mãos e atira você para o outro lado do aposento."
    n "Dessa forma, não havendo outra saída, você se vê forçado à usar o Encanto da Fraqueza no Gark."
    jump um52

label um52:
    n "Você lança seu Encanto da Fraqueza, e a criatura interrompe seus passos, sem entender o que aconteceu com ela."
    n "Com algum esforço, ela apanha seu machado e vem na sua direção, mas evidentemente não é um
    adversário tão forte quanto era antes."
    jump um6

label um6:
    n "Ao desembainhar a espada, o gark parte em sua direção!"
    jump batalha_gark

label um1:
    n "Você opta por usar o Encanto da Fraqueza para tentar o atordoar e, assim, conseguirá seguir adiante em direção a porta."
    play sound "musics/efeito_sonoro/dados.mp3"

    $ d20roll = renpy.random.randint(1, 20)

    if (d20roll>=13):
        $renpy.notify("sucesso de sorte")
        play sound "musics/efeito_sonoro/sorte-sucesso.mp3"
        n "você lança o encanto com sucesso, o gark fica fraco e cai, enquanto você parte em direção às portas."
        jump nove9
    else:
        $renpy.notify("fracasso de sorte")
        play sound "musics/efeito_sonoro/sorte-fracasso.mp3"
        n "sob pressão, você erra algumas palavras do encanto,
        fazendo com que ele não seja eficaz, e você parte para a batalha!"
        jump um6

label dois16:
    n "Qual será sua tática?"
    menu:
        "Você dirá à criatura que você é um convidado":
            jump dois94
        "Tentará subornar o Gark, oferecendo três Peças de Ouro":
            jump tres91
        "Tentará lançar um Encanto de Ouro dos Tolos para subornar a criatura (Teste de sorte)":
            jump tres6

label dois94:
    n "O Gark se recompõe, abaixa o machado e começa a se desculpar com você por estar dormindo no
    posto."
    n "Por insistência dele, você concorda em não dizer nada a ninguém. A criatura se oferece para
    levar a sua túnica, mas você recusa o oferecimento e segue em frente."
    jump nove9

label tres91:
    n "O Gark pega as suas três Peças de Ouro, coloca-as em uma bolsa presa em volta da cintura e mostra
    o caminho para seguir na direção das portas."
    #$ dinheiro retirado (notify)
    jump nove9

label tres6:

    $ d20roll = renpy.random.randint(1, 20)

    if (d20roll>=13):
        $renpy.notify("sucesso de sorte")
        play sound "musics/efeito_sonoro/sorte-sucesso.mp3"
        n "você lança o encanto com sucesso, o gark acredita no ouro falso e permite a sua passagem, apontando a direção das portas."
        jump nove9
    else:
        $renpy.notify("fracasso de sorte")
        play sound "musics/efeito_sonoro/sorte-fracasso.mp3"
        n "sob pressao, você erra algumas palavras do encanto,
        fazendo com que ele não seja eficaz, e você parte para a batalha!"
        jump um6

label nove9:

    hide gark
    hide bg3

    scene bg5

    n "Ao chegar nas duas portas, você escolhe para qual entrar"
    menu:
        "Porta da direita (biblioteca)":
            jump tres8

        "Porta da esquerda (salão de jogos)":
            jump cinco2

label tres8:
    n "A porta abre para uma passagem curta, calçada com pedras pequenas. A uma pequena distância
    mais adiante, uma porta elaboradamente entalhada assinala o fim da passagem."
    n "Você se aproximada porta, tentando escutar quaisquer sinais de vida do lado de dentro.
    Quando sua mão toca a maçaneta, uma voz diz: 'Não bata; simplesmente entre!' vinda de dentro."
    n "Dessa forma, você:"
    menu:
        "Entrará no aposento conforme as instruções":
            jump um32
        "Resolverá desistir, voltar e entrar na porta da esquerda":
            jump cinco2

label um32:

    scene biblioteca
    show bibliotecario at right:

    n "Ao entrar, há livro do chão até o teto em cada uma das paredes, e diversas mesas e cadeiras
    estão alinhadas no centro do aposento. Do outro lado, há um homem de pele escura sentado, que levanta os olhos de um livro para olhar
    para você por cima de óculos estreitos."
    n "Há uma porta atrás dele. 'Sim, o que é?', ele diz. 'Que livro você está procurando?'. Você examina as várias
    estantes, que possuem legendas. Você pedirá a ele:"
    menu:
        "Biografias de Balthus Dire?":
            jump um8
        "Segredos da Torre Negra?":
            jump dois38
        "Criaturas do Reino da Rocha Escarpada?":
            jump tres75

label um8:
    n "Ele aponta para uma seção logo acima do chão, que você examina. Finalmente, você escolhe um
    volume e senta para ler."
    n "Balthus Dire aparentemente é o terceiro de uma linhagem de Feiticeiros Senhores da Guerra que governa a Torre
    Negra e o Reino da Rocha Escarpada. Chegou ao poder depois da morte de seu pai, Craggen Dire, há alguns anos atrás."
    n "Os Dires são mestres de Magia Negra há gerações, mas sua força e poder duram somente no período noturno; a luz do sol é uma
    espécie de veneno para eles."
    n "Pouco tempo depois da morte de seu pai, Balthus Dire casou-se com Lady Lucretia, ela também uma Feiticeira de Magia Negra, e desde então eles vem reinando juntos
    sobre o Reino da Rocha Escarpada."
    n "Ao terminar o livro, você repara que o bibliotecário está com a mão junto ao ouvido, aparentemente escutando alguma coisa. Ele dirige a você um olhar
    inquisitivo."
    menu:
        "Você pode procurar outro livro útil, que possa ajudá-lo na sua empreitada":
            hide bibliotecario
            jump oito4
        "Ou tentar sair da biblioteca pela porta atrás dele":
            hide bibliotecario
            jump tres1

label oito4:
    n "Ao examinar as prateleiras, você ouve uma grande movimentação atrás de você. Você se vira rapidamente, a tempo de ver criaturas
    semelhantes a Orcas, armadas e em guarda, materializaram-se uma após a outra diante de você."
    show orcs at center:
        zoom 0.5
    n "Elas avançam e cercam você. O mais alto chega o rosto perto do seu e solta um bafo de respiração diretamente sobre os seus olhos."
    n "O aposento gira e você desaba no chão, inconsciente."
    hide orcs
    hide biblioteca
    with fade
    jump dois34

label tres1:
    n "Você sai do aposento pela porta do outro lado, a qual abre para uma passagem curta que termina em uma grande porta de madeira.
    A maçaneta desta porta gira, deixando que você entre em uma grande câmara."
    jump um69

label dois38:
    n "Ele indica uma seção das estantes, e você leva um livro para uma das mesas para ler. O livro é extremamente informativo, traçando a história da Cidadela.
    A Torre Negra foi construída pelo avô de Balthus Dire."
    n "À medida em que foi se tornando um santuário para as forças do mal, a lei e a ordem foram gradualmente dando lugar ao caos, devido à luta das criaturas monstruosas para
    ascender na hierarquia do poder. O avô de Dire acabou se vendo na necessidade de se proteger de seus próprios seguidores, criando vários sistemas de segurança entre as criaturas e seus próprios
    aposentos, destacando-se entre eles a Armadilha do Poço da Perdição e uma Fechadura de Combinação mágica na porta de seu próprio quarto. A combinação da fechadura é 217."
    n "Você lê mais sobre a Cidadela e então escolhe perguntar ao homem:"
    menu:
        "Sobre a seção dedicada a Balthus Dire":
            jump um8
        "Sobre a seção das Criaturas de Rocha Escarpada":
            jump tres75
        "Ou simplesmente sai do aposento pela porta do outro lado":
            jump tres1

label tres75:
    n "Ele indica um livro na prateleira que é uma lista alfabética de todos os tipos de criaturas. Você
    consultará a seção sobre Ganjees"
    jump seis3

label seis3:
    n "Você vai até o índice remissivo e verifica a referência. Ao chegar à página correta, você fica
    decepcionado ao descobrir que a seção foi arrancada do livro!"
    n "Dessa forma, você decide sair do aposento pela porta do outro lado."
    jump tres1

label cinco2:
    scene salao at truecenter:
        zoom 1.5
    show maguito at left:
        xpos 500
        ypos 1000
        zoom 1.2
    show leviata at right:
        zoom 1.7
    show heitoba at center:
        ypos 1000
        zoom 0.2
    n "A porta abre e você segue adiante, batendo-a para que se feche atrás de você. Pouca distância à frente, você chega a um cruzamento de três caminhos,
    no qual você toma a passagem que vai na direção norte."
    n "Ela continua por vários metros, conduzindo a uma outra porta. Você pode ouvir risos e vozes alegres do outro lado. Cautelosamente, você abre
    a porta que dá para um grande aposento, onde um grupo de mais ou menos doze criaturas, de todas as formas, tamanhos e cores, estão se divertindo com jogos."
    n "Quando você entra no aposento, uma voz grita: 'Olhem esse deve ser Glaz-Doz-Fut!', com o que todos eles cumprimentam você,  convidando-o para juntar-se à
    brincadeira.Evidentemente eles estão esperando alguém e confundiram você com o convidado que está faltando."
    menu:
        "Você continua fingindo e junta-se a eles":
            jump tres85
        "Dirá a eles que estão enganados e tentará chegar até a porta do outro lado do aposento":
            jump dois27

label tres85:
    n "Você consegue se enturmar com sucesso e, após algum tempo, conseguirá sair pela porta do outro lado do salão."
    jump tres1

label dois27:
    n "Eles começam a ficar muito zangados com seus modos. Os ânimos se exaltam, e eles começam a gritar."
    n "Repentinamente, você é dominado por eles. Você luta, mas um deles golpeia você na cabeça com o cabo da espada. Sua cabeça roda, e
    o aposento escurece, quando você perde a consciência."
    jump dois34

label dois34:
    hide maguito
    hide leviata
    hide heitoba
    hide salao
    with fade
    scene prisao at truecenter:
        zoom 2.8
    n "Você acorda em um aposento sujo, com paredes ásperas cortadas na rocha. As barras de ferro na janela e na porta confirmam que você está em algum tipo de cela de prisão, conforme você
    desconfiava. Não há muito que você possa fazer, além de ficar sentado no colchão de palha que está em um canto até que alguém apareça."
    n "Mais ou menos uma hora depois, você ouve o barulho de alguma coisa que se arrasta do lado de fora. Olhando através das barras da porta, você pode ver uma
    criatura com aparência de lagarto que se arrasta descendo o corredor, trazendo nas mãos uma moringa e uma terrina."
    show calacorm at center:
        zoom 1.5
    n "O animal tem duas cabeças que conversam entre si enquanto ele caminha. Sua pele é cinzenta e coberta de escamas, e uma cauda longa se estende pela passagem atrás dele."
    n "Ele para na sua porta e empurra a moringa e a terrina por uma pequena abertura para dentro de sua cela, e depois se afasta para sentar-se a uma mesa do outro lado do corredor. Você recebeu pão e
    caldo."
    hide calacorm
    menu:
        "Você vai comer e beber?":
            jump tres97
        "Ou irá chamar esta criatura, um CALACORM?":
            jump seis9

label tres97:
    n "Não é uma refeição muito farta, mas você estava com fome e com sede, sentindo-se renovado."
    n "O que fará em seguida?"
    menu:
        "Usar um Encanto para sair da situação (Teste de Sorte)":
            jump um93
        "Chamar o Calacorm":
            jump seis9

label um93:
    play sound "musics/efeito_sonoro/dados.mp3"

    $ d20roll = renpy.random.randint(1, 20)

    if (d20roll>=12):
        $renpy.notify("sucesso de sorte")
        play sound "musics/efeito_sonoro/sorte-sucesso.mp3"
        n "Você oferece a ele as pedrinhas que se transformaram em ouro. Ele desabafa sobre a vida pacata que ele leva na prisão, e, rapidamente te libera de sua cela"
        show calacorm at center:
            zoom 1.5
        jump um74
    else:
        $renpy.notify("fracasso de sorte")
        play sound "musics/efeito_sonoro/sorte-fracasso.mp3"
        n "Infelizmente, já tentaram subornar a critura, e ela não cai no seu Encanto!"
        jump batalha_calacorm

label seis9:
    n "A criatura não é de muita conversa, mas você consegue descobrir que está nas masmorras dos subterrâneos da Torre Negra e que provavelmente nunca será libertado,
    a não ser que se já dado aos Ganjees para o divertimento deles."
    n "Dessa forma, você se lembra sobre um estudo que você fez e conclui que talvez se a ofendesse, isso te traria uma oportunidade."
    n "De maneira incessante, você consegue atingir seu objetivo e a criatura engaja com você num combate."
    jump batalha_calacorm

label um74:
    n "A porta de saída está logo ali!"
    jump sete

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

    n "Você agora está em um aposento grande. É Iluminado por algumas tochas, presa a uma
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
                fazendo com que ele seja ineficaz!"
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
    perguntará a ele o caminho para seguir adiante ou desembainhará a sua espada?"

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

    scene corredor_escuro at center:
        zoom 3.0

    n "Você abre a porta e espia a escuridão à sua frente. Você dá uns dois passos adiante, dando tempo
    para que seus olhos se acostumem ao escuro. Você fecha a porta atrás de você, dizendo adeus ao
    Duende."

    jump um88

label dois2:

    scene corredor_escuro at center:
        zoom 3.0

    n "Você abre a porta e sai em um corredor longo e escuro."

    jump um88

label tres54:

    scene corredor_escuro at center:
        zoom 3.0

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

    scene corredor_escuro at center:
        zoom 3.0
    with flash

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
        "aceitar seu destino e não resistir":
            jump dois80

label tres23:

    scene sala_oseamus at center:
        zoom 1.5

    show oseamus at center:
        zoom 0.8
        ypos 850
    with dissolve
    play music "musics/Nikos Spiliotis - Love Waltz.mp3"

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

    scene esgoto at center:
    play music "musics/passagem esgoto.mp3"

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

label um44: ##incompleto

label tres38: ##incompleto

label um08:
    n "Você agarra a corda firmemente, recua e toma impulso na direção do rio pútrido. Subitamente, a
    corda passa a se movimentar e se contorcer com vontade própria! Você a larga rapidamente e cai no
    chão."
    n "A corda cai por cima de você e se enrola em volta de você. Você compreende que não é uma
    corda, mas, na realidade, uma longa COBRA DE ESGOTO, que se enrosca em torno do seu corpo e
    de seu pescoço."

    jump sete3

label sete3:
    n "voce pode lutar contra a criatura ou usar um encanto"
    menu:
        "preparar para lutar?":
            jump batalha_cobras
        "usar encanto de fogo?":

            $ d20roll = renpy.random.randint(1, 20)

            if (d20roll>= 10):
                $renpy.notify("sucesso de sorte")
                play sound "musics/efeito_sonoro/sorte-sucesso.mp3"
                n "você teve sucesso ao lançar o encanto e as chamas vao em direção à cobra do esgoto"
                play sound "musics/efeito_sonoro/bola de fogo.mp3"
                jump dois82

            else:
                $renpy.notify("fracasso de sorte")
                play sound "musics/efeito_sonoro/sorte-fracasso.mp3"
                n "Você não teve sucesso ao lançar o encanto e a cobra continua a pressionar seu pescoço"
                n "se prepare para lutar!"
                jump batalhas_cobras

label dois82:
    n "Você lança uma pequena bola de fogo diretamente sobre a Cobra de Esgoto, que queima seu corpo,
    cortando-a em duas metades. As duas metades agora atacam você e estão esmagando o seu peito."
    n "Tentando uma estratégia diferente, você cria chamas que
    queimam em cada mão e as esfrega sobre os anéis de seu corpo enroscado. A criatura se contorce
    violentamente e afrouxa a pressão!"
    n "Você encontra sua cabeça e a espreme com as suas mãos
    flamejantes, queimando-a fatalmente."
    jump um12

label dois04: ##imcompleto

label um12:

    n "Você se desvencilha da Cobra de Esgoto morta e tenta atravessar a água. Você chega do outro lado
    sem maiores incidentes, mas está com certeza ansioso para tomar um banho rápido!"
    n " Você continua ao longo da passagem até chegar a uma encruzilhada, onde pode seguir em frente ou tomar a
    passagem da esquerda."
    menu:
        "ir para a esquerda?":
            jump dois12
        "seguir em frente?":
            jump tres67

label dois12: ##incompleto

label tres67:
    scene passagem_esgoto at center:
        zoom 2.0

    n "Alguma distância adiante na passagem, você chega a uma junção de quatro caminhos. Você toma o
    caminho do norte, que acaba chegando a urna grande porta de madeira."
    n "Você não consegue ouvir nada escutando pelo buraco da fechadura. Você tentará abrir a porta lentamente e sem ruído ou derrubá-la à força?"
    menu:
        "abrir a porta com cautela?":
            jump tres08
        "abrir a porta na força?":
            jump um21

label tres08:

    n "A maçaneta gira e você entra em um cômodo às escuras."
    jump dois57

label um21:

    n "Quando você parte para a porta, ela abre repentinamente à sua frente. Impossibilitado de travar seu
    impulso, você entra pelo aposento de cabeça e acaba tropeçando e rolando pelo chão até parar."
    jump dois57

label dois57:

    scene sala_golem:
        zoom 1.3

    show pedroso:
        ypos 100
        zoom 1.5
    with dissolve

    n "Você olha à sua volta no aposento. Está iluminado somente pela sua tocha. Embora seja um
    aposento bastante grande, possui pouca mobília, com apenas uma grande rocha, cortada de modo a
    servir de mesa, e uma rocha menor com o formato de uma banqueta."
    n "Em um dos cantos, há uma pilha de rochas unidas por uma camada de lama. Você não consegue imaginar qual é a serventia
    disso, embora haja três arcas de madeira sobre ela. Então, você pula de susto quando sua tocha
    ilumina uma grande criatura, aparentemente também ela própria feita de rocha, de pé junto a uma
    porta."
    n "Possui aproximadamente uma forma humana, ainda que um tanto maior. Seus olhos estão
    dirigidos diretamente para você, mas você não consegue ter certeza de que ela esteja de fato vendo
    você! Você:"
    menu:
        "correr para a porta do outro lado do aposento?":
            jump dois37
        "tentar falar com a criatura?":
            jump tres57
        "avançar lentamente na direção das caixas no canto?":
            jump dois00

label dois37:

    n "Você abre a porta e sai em uma passagem que segue na direção leste por vários metros, terminando
    ao pé de uma escadaria. Você sobe as escadas e acaba chegando em uma passagem estreita."
    n "A uma pequena distância mais adiante, você pode ver uma abertura para um aposento grande e bem
    iluminado. Você segue nessa direção."

    jump um69

label tres57: ##incompleto

label dois00: ##incompleto

label um69:

    scene sala_jantar
    n "O aposento em que você está é uma espécie de grande salão de jantar. Uma mesa longa, de tamanho
    suficiente para que quarenta ou cinquenta pessoas sentem, ocupa o centro, ladeada por cadeiras."
    n "Há várias portas e passagens que dão saída do aposento, mas você está particularmente interessado em
    duas escadarias largas que levam, uma por cada um dos lados, até uma sacada no alto de onde se
    pode observar o salão."
    n "Quadros e armaduras decoram as paredes. O aposento está vazio. Você:"
    menu:
        "toma escadaria do lado esquerdo e sobe?":
            jump um9
        "toma escadaria do lado direito e sobe?":
            jump um97
        "investiga os quadros?":
            jump tres17
        "investiga as armaduras?":
            jump um51

label um9:

    n "A escada geme quando você põe o pé nela. Você tenta subir o mais silenciosamente possível, mas a
    madeira velha range sob o seu peso."
    n "De repente, um dos degraus estala, como se acionasse um
    dispositivo de algum tipo. Para sua surpresa, todos os degraus: viram para baixo! Você está agora
    de pé em uma rampa lisa e inclinadíssima! Por mais que você tente, não consegue manter o
    equilíbrio e acaba escorregando pela rampa, rolando de ponta cabeça."
    n "Se você quiser usar um
    Encanto da Levitação, poderá voar e descer, fora de perigo, na sacada em cima."
    menu:
        "usar encanto de levitação? (teste de sorte)":
            $ d20roll = renpy.random.randint(1, 20)

            if (d20roll>= 10):
                $renpy.notify("sucesso de sorte")
                play sound "musics/efeito_sonoro/sorte-sucesso.mp3"
                n "Você obteve sucesso ao conjurar o encanto e consegue subir a rampa!"
                jump tres63

            else:
                $renpy.notify("fracasso de sorte")
                play sound "musics/efeito_sonoro/sorte-fracasso.mp3"
                n "Você errou uma palavra do encanto e começa a escorregar pela rampa mais rapido que o normal!"
                jump dois54

        "nao usar o encanto?":
            jump dois54

label dois54:

    n "Você rola escada abaixo, atravessa o aposento e finalmente se choca contra a parede do outro lado
    do salão. Você torce o cotovelo seriamente.depois sobe pela outra escadaria."

    jump um97

label um97:

    n "As escadas estão bastante gastas e estalam sob o seu peso. Cuidadosamente, você sobe até a sacada."
    jump tres63

label tres17: ##incompleto

label um51: ##incompleto

label tres63:

    scene portais at center:
        zoom 2.0

    n "Há três portais ao longo da sacada. Você experimentará:"
    menu:
        "o portal da esquerda?":
            jump dois28
        "o portal do centro?":
            jump seis4
        "o portal da direita?":
            jump tres04

label dois28:

    n "A porta trancada é muito forte e feita de carvalho sólido. Não é provável que você consiga arrombá-
    la, mas você pode tentar."
    n "Do contrário, você pode usar um Encanto da Força para arrebentá-la. A
    fechadura é de cobre, e você poderia tentar usar uma Chave de Cobre, se tiver uma. O que você
    escolherá:"

    menu porta:
        "tentar arrombar?":
            $ d20roll = renpy.random.randint(1, 20)

            if (d20roll>= 10):
                $renpy.notify("sucesso de sorte")
                play sound "musics/efeito_sonoro/sorte-sucesso.mp3"
                n "a porta abre e voce acessa a sala!"
                jump dois92
            else:
                $renpy.notify("fracasso de sorte")
                play sound "musics/efeito_sonoro/sorte-fracasso.mp3"
                n "você nao conseguiu abrir a porta e volta para a porta do centro"
                jump seis4
        "usar encanto de força?":
            $ d20roll = renpy.random.randint(1, 20)

            if (d20roll>= 7):
                $renpy.notify("sucesso de sorte")
                play sound "musics/efeito_sonoro/sorte-sucesso.mp3"
                n "a porta abre e voce acessa a sala!"
                jump dois92
            else:
                $renpy.notify("fracasso de sorte")
                play sound "musics/efeito_sonoro/sorte-fracasso.mp3"
                n "você nao conseguiu abrir a porta e volta para a porta do centro"
                jump seis4

        "usar chave de cobre?":
            if (chave_cobre == True):
                n "a chave gira e a porta abre!"
                jump dois92
            else:
                play sound "musics/efeito_sonoro/nao tem o item.mp3"
                $renpy.notify("você não possui esse item!")
                jump porta

label seis4:

    scene portais at center:
        zoom 2.0


    n "Você ouve junto à porta e consegue escutar vozes esganiçadas rindo e brigando. Você experimenta
    a maçaneta e a porta abre. O lado de dentro é um aposento de cores vivas."
    scene quarto_goblin

    n "Há umas poucas camas pequenas em um canto, e, espalhados pelo chão, há pequenos bonecos de várias criaturas brutas.
    Junto à parede do lado direito há uma caixa, e logo adiante da caixa uma porta."

    show goblins at center:
    with dissolve

    n "No meio do assoalho, e olhando para você com curiosidade, estão algumas pequenas criaturas. Têm aparência
    humana, mas possuem pele verde, orelhas pontudas e olhos muito apertados. Qual será a sua
    atitude? Você:"
    menu:
        "Desembainhará a sua espada e se preparará para lutar contra eles?":
            jump dois86
        "Procurará em sua mochila alguma coisa para oferecer a eles?":
            jump tres
        "Caminhará confiantemente através do aposento para a porta do outro lado?":
            jump tres66

label dois86:

    n "As pequenas criaturas guincham e se amontoam quando você se aproxima. Você passa todas a fio
    de espada, mas eles não oferecem nenhuma resistência!"
    n "Você fica um pouco desconfiado com essa
    batalha tão fácil e dirige-se para a porta do outro lado do aposento."
    jump um40

label tres: ##incompleto

label tres66: ##incompleto

label um40:

    scene escadas at center

    n "Você sai do aposento e segue por um corredor curto. Alguns metros adiante, você se encontra ao pé
    de uma escada. É uma escada em espiral que leva diretamente ao interior da Torre da Cidadela."
    n "Você sobe os degraus cautelosamente e acaba chegando em uma pequena plataforma com duas
    portas à sua frente. você testa a porta da direita primeiro, esta que esta extremamente emperrada, apenas lhe restando seguir pela esquerda"
    jump dois5

label dois5:

    n "A porta abre, dando para um aposento grande e circular. Você coça a cabeça, intrigado."
    n "No centro do aposento, vê uma pequena 'ilha', cercada por um fosso largo, na qual está uma arca, trancada
    por ferrolhos metálicos."
    n "O fosso é largo demais para ser pulado e é muito fundo. Logo na entrada,
    há um pedaço de corda. Existe uma outra porta do outro lado do aposento, dando para fora dele.
    Você:"
    menu:
        "Ignora a caixa e contorna o fosso até a outra porta?":
            jump dois06
        "Lança um Encanto da Força e salta sobre o fosso? (teste de sorte)":
            jump um33
        "Pega a corda e formula um plano?":
            jump dois39

label dois06:
    n "Você sai pela porta e se encontra ao pé de outra escada em espiral que leva ao interior da Terra
    Negra."
    n "Subindo a escadaria, você acaba chegando a uma plataforma onde uma única porta é a
    maneira que existe para seguir adiante, sem outra opção. Você experimenta a porta. Ela abre
    lentamente."
    jump um82

label um33: ##incompleto

label dois39: ##incompleto

label um82:

    scene quarto_escuro at center

    n "Você se sente sugado para o interior do aposento. Como que por um passe de mágica, sua tocha
    tremula e se apaga. O aposento está escuro como breu. De nenhum lugar, mas ainda assim de toda
    parte, vem um riso de escárnio que enche o aposento."
    n "'Aventureiro tolo', diz uma outra voz, que altera o tom de alto para baixo enquanto fala, 'Bem-vindo à casa dos GANJEES! Infelizmente, será
    o último lugar que você verá na sua vida... Ah, mas é claro, você não está vendo nada, está?"
    n "' Mas nós estamos vendo você, não estamos irmãos?' Vozes que riem chegam de toda parte à sua volta.
    De repente, um rosto luminoso, branco e fantasmagórico, vem voando na sua direção."
    n "Você se encolhe horrorizado, atira-se no chão e começa a se sentir muito assustado. Por causa desse medo extremo, qualquer batalha contra essas criaturas vai ser de extrema dificuldade!"
    n "você pensa nas seguintes opções:"
    menu:
        "usar encanto?":
            jump oito5
        "desembainhar a sua espada?":
            jump dois48
        "procurar um artefato na mochila?":
            jump tres22

label oito5: ##incompleto

label dois48: ##incompleto

label tres22:

    n "O que você vai tirar de sua mochila?"
    menu ganjees:
        "aranha em um vidro?":
            if (aranha_garrafa == True):
                jump tres9
            else:
                play sound "musics/efeito_sonoro/nao tem o item.mp3"
                $renpy.notify("você não possui esse item!")
                jump ganjees
        "tentar falsificar um artefato? (teste de sorte)":
            $ d20roll = renpy.random.randint(1, 20)

            if (d20roll>= 1):
                $renpy.notify("sucesso de sorte")
                play sound "musics/efeito_sonoro/sorte-sucesso.mp3"
                n "as ganjees aceitam seu artefato e deixam você passar"
                jump dois91
            else:
                $renpy.notify("fracasso de sorte")
                play sound "musics/efeito_sonoro/sorte-fracasso.mp3"
                n "você nao consegue um artefato e as Ganjees te atacam sugando sua alma, esse foi seu fim!"
                jump final_ruim
        "vidro de ungento?":
            if (vidro_ungento == True):
                jump dois91
            else:
                play sound "musics/efeito_sonoro/nao tem o item.mp3"
                $renpy.notify("você não possui esse item!")
                jump ganjees

label tres9: ##incompleto

label dois91:

    n "'O que é isso?' pergunta uma voz fantasmagórica. Você negocia com eles. Você deixará que eles
    fiquem com o unguento, se eles deixarem você passar pelo aposento, já que você não está
    interessado neles."
    n "Uma fantasmagórica mão aparece do nada e tenta arrancar o vidro da sua mão,
    mas você o guarda rapidamente. 'É de fato o Unguento da Cura', você ouve uma das vozes dizendo
    baixo."
    n "'Aceitamos a sua oferta', diz uma voz. 'Deixe o Vidro onde você está e saia do aposento por
    esta porta'. Uma porta do outro lado brilha suavemente. Você não confia neles e leva o Vidro com
    você até a porta."
    n "Quando você abre a porta, atira o Vidro para o outro lado do aposento e sai
    rapidamente."

    jump tres28

label tres28:
    n "Você fecha a porta atrás de você e chega ao pé de outra escadaria, que sobe em espirais para o
    interior da torre. Subindo os degraus, você chega a uma outra sacada, onde uma única porta é a
    alternativa que existe para seguir adiante."
    n "Ao experimentar a porta, ela abre facilmente. Mas,
    quando você empurra a porta, um ruído alto de silvos vem lá de dentro. Você entra e fica gelado, ao
    ver uma imensa HIDRA de seis cabeças se arrastando na sua direção sobre os corpos das vítimas
    anteriores!"
    n "Suas seis cabeças de serpente atacam você com seus dentes aguçados e cruéis. Você fica
    encurralado em um canto. O que você fará:"
    menu hidra:
        "Desembainhará a sua Espada e lutará contra a criatura?":
            $ d6roll = renpy.random.randint(1, 6)

            if (d6roll==3):
                $renpy.notify("sucesso de sorte")
                play sound "musics/efeito_sonoro/sorte-sucesso.mp3"
                n "Você começa a sua luta contra a criatura. Seu primeiro golpe é certeiro e corta uma das seis
                cabeças. fazendo com que as outras comecem a definhar! parabens, cortou a cabeça primordial!"
                n "você segue em direção à porta rumo ao vinal da sua jornada!"
                jump dois29
            else:
                $renpy.notify("fracasso de sorte")
                play sound "musics/efeito_sonoro/sorte-fracasso.mp3"
                n "Você começa a sua luta contra a criatura. Seu primeiro golpe é certeiro e corta uma das seis
                cabeças. As outras cinco avançam sobre você e, para seu horror, mais duas cabeças crescem onde
                estava antes a cabeça morta!"
                jump seis7

        "usar encanto copia de criatura?":
            jump um43
        "usar veu de ouro?":
            if (velo_ouro):
                jump tres7
            else:
                play sound "musics/efeito_sonoro/nao tem o item.mp3"
                $renpy.notify("você não possui esse item!")
                jump hidra

label dois29:
    n "Você bate a porta, fechando-a ao passar. Você segue por uma passagem curta e estreita, que dá
    muitas voltas e conduz você ao pé de outra escadaria, levando diretamente ao topo da Cidadela. Um
    letreiro na parede diz: 'PARE. Ninguém poderá passar, a não ser com ordem de Balthus Dire.'"
    n"Você percebe que está chegando a seu objetivo. Cautelosamente, você sobe as escadas até o
    próximo patamar, penetrando na torre superior da Cidadela. Há uma porta de metal sólido à sua
    frente. Você tenta a maçaneta, mas a porta está trancada."
    n "Você levanta a sua mão em direção a porta e se concentra, gerando um poderoso raio arcano que estilhaça a fechadura,
    permitindo você seguir para o final da sua jornada. você vai ser capaz de salvar a sua terra?"
    jump dois17

label seis7:
    n "Uma das cabeças morde profundamente o seu braço. e você se prepara para uma batalha ate a morte com a hidra!"
    jump batalha_hidra

label um43:
    $ d20roll = renpy.random.randint(1, 20)

    if (d20roll>= 10):
        $renpy.notify("sucesso de sorte")
        play sound "musics/efeito_sonoro/sorte-sucesso.mp3"
        n "Você se concentra e lança seu Encanto. aparece uma hidra que, para sua surpresa,
        ela surgiu com um padrao de cor exotico!"
        n "Você lembra de ter estudado com seu mestre, são chamadas de hidras reversas,
        essas que possuem o dobro da força das hidras normais!"
        n "a sua hidra avança em direção a hidra original"
        jump batalha_hidra_vs_hidra
    else:
        $renpy.notify("fracasso de sorte")
        play sound "musics/efeito_sonoro/sorte-fracasso.mp3"
        n "Você falha na conjuração do feitiço, de forma que aparece apenas uma cabeça de hidra caida ao chão!"
        n "você fica extremamente nervoso e tem apenas duas opções, procurar algo na sua mochila ou tentar ir para a batalha você mesmo!"
        menu hidra2:
            "pegar veu de ouro?":
                if (velo_ouro):
                    jump tres7
                else:
                    play sound "musics/efeito_sonoro/nao tem o item.mp3"
                    $renpy.notify("você não possui esse item!")
                    jump hidra2
            "puxar sua espada da bainha e ir para a luta?":
                jump batalha_hidra

label tres7:
    n "Você puxa a pele e a criatura solta silvos altos. Todas as suas cabeças recuam,e ela permanece
    quieta, observando você. Há uma porta do outro lado do aposento, e você lentamente se desloca na
    direção dela."
    n "Quando você está na metade do caminho, uma das cabeças se projeta e arranca o velo
    das suas mãos. Mas, ao invés de atacar você, a Hidra se encolhe de volta em um dos cantos. Você
    segue para a porta cautelosamente."
    jump dois29

label dois92:

    scene quarto_morena at center:

    show morena at center:
        ypos 900

    n "O aposento é um elegante quarto de dormir suntuosamente decorado com rendas finas e um tapete
    de pele. No centro do aposento, há uma grande cama de quatro colunas."
    n "Sentada e recostada na cama, evidentemente acordada pela agitação toda, está uma linda mulher, com uma aparência de
    sílfide, longos cabelos negros e olhos profundos e penetrantes. 'Que direito você tem de entrar
    aqui?' ela grita."
    n "Com estas palavras seus olhos ficam vermelhos como sangue e dois jatos de fogo
    líquido jorram deles diretamente sobre você. Você:"

    menu quarto:
        "usar encanto de escudo para se proteger?":
            jump tres76
        "sai do aposento rapidamente e experimente a porta ao lado?":
            jump seis4
        "diz ter um presente especial para ela? (escova de cabelo)":
            if (escova_cabelo == True):
                n "ela aceita o presente"
                jump quatro2
            else:
                play sound "musics/efeito_sonoro/nao tem o item.mp3"
                $renpy.notify("você não possui esse item!")
                jump quarto

label tres76:

    n "Você lança seu Encanto do Escudo. Que lástima, este Encanto não faz efeito contra armas mágicas!"
    n "Você percebe que dialogo nao vai adiantar e se prepara para lutar"
    jump batalha_morena

label quatro2: ##incompleto

label tres04: ##incompleto

label dois17:
    scene topo_torre
    show balthus normal at center:
        zoom 0.7
    with dissolve
    n "Balthus dire finalmente está a sua frente,seu poder emana e sua pressão é enorme
    seu próximo passo definirá o destino do Vale do Salgueiro, e o seu futuro,o que você fará"
    menu:
        "confessará que deseja servir o lorde do caos e nao desafia-lo?":
            jump final_submissao
        "Lutar contra Balthus":
            jump despertar

label final_ruim:

    play music "musics/Savfk - Deep.mp3"

    scene game_over:
        zoom 1.5

    $renpy.notify("fim de jogo")

    n "voce falhou em sua missão e Balthus Dire agora avança em direção a sua terra natal, que destino a espera?"

    return

label final_submissao:

    play music "musics/yt1s.com - No Copyright Music Whisper In The Deep  Royalty Free Music.mp3"

    n "você abaixa sua arma e explica que na verdade voce nao buscava a morte do lorde do caos, mas servi-lo.A esperança era de obter a liberdade de decidir oque fazer com a sua vida,
    algo que voce nunca sentiu ter, com tudo sempre por decisão de seu antigo mestre, o grande mago de Yore."

    b "Ora ora... O unico capaz de adentrar não só minha cidadela mas minha torre deseja juntra-se a mim!!!
    HA HA HA HA HAAAAAAAAA!!! O destino favorece aos detentores do poder e você, meu jovem,entendeu isso muito bem!"

    b "Agora vamos,aquele vale patético tem muito gado esperando para ser controlado,e nós seremos seus pastores!"

    hide balthus normal

    scene fim_sub at center:
        zoom 1.5

    n "A tirania se espalhou e Balthus se tornou supremo graças a você,todos que conhecia foram mortos,você estava livre das suas antigas amarras,
    mas ainda se sentia acorrentado. Porquê?
    Você se aproxima para falar com Balthus sobre sua parceria com ele"

    show balthus normal at center:
        zoom 0.7
    with dissolve

    b "Ah, meu jovem nada tema!Sua ansiedade é injustificada,afinal..."

    play sound "musics/efeito_sonoro/facada.mp3"

    n "O lorde do caos invoca rapidamente uma adaga e te esfaqueia!"

    b "Um rei governa sozinho!Seus serviços nao são mais necessários! Lacaios,joguem esse corpo na vala!"

    n "Antes da morte,sua vida passa diante de seus olhos, você retribiu seus traumas da infância e juventude com violência, o vazio é tudo que lhe restou..."

    scene game_over:
        zoom 1.5

    $renpy.notify("fim de jogo")

    n "Sua jornada termina aqui..."
    return

label despertar:

    play music "musics/Makai Symphony - The Army of Minotaur.mp3" volume 0.5

    hide balthus normal
    show mc normal at center:
        zoom 0.7
    with dissolve


    n "Este é o momento para o qual você treinou tanto, sofreu tanto! Não importa o preco que terá de pagar,voce dará tudo de si!
    Você retira o colar do selamento, dado a você pelo seu antigo mestre, o grande mago de Yore."

    n "Seus poderes antes suprimidos para garantir sua discrição para infiltrar-se na cidadela agora são seus para utilizar!"

    play sound "musics/efeito_sonoro/poderes liberados.mp3"
    show mc bombado at center:
        zoom 0.7
    with flash
    with dissolve


    b "Quem diria! O desgracado que invade minha cidadela! minha torre! Ousa me desafiar com esse nível de poder?!Ridículo!"

    jump batalha_balthus1

label despertar_balthus:

    hide mc

    show balthus normal at center:
        zoom 0.7
    with dissolve

    b "Ridículo!!!! Não serei derrotado por um moleque arrogante!!!Biotáille ársa yore, oibrigh an fhoirm chinniúnach seo i ldabaoth!!!!!"

    play sound "musics/efeito_sonoro/tranformacao Balthus.mp3"

    show balthus bombado at center:
        ypos 1500
        zoom 1.5
    with flash
    with dissolve

    play music "musics/fase 2.mp3"

    n "O lorde do caos havia lancado um encantamento antigo e proibido, os anos de estudo do mago garatiram que ele sabia do que se tratava.
    'Atigos espirítos de Yore,transformem essa forma decadente em ldabaoth',Balthus havia desistido de sua forma humana para tentar a vitória,a luta continua!"

    jump batalha_balthus2

label fim_batalha:

    hide balthus

    scene topo_torre

    n "Voce se encontra novamente no aposento de Balthus na torre, o trono jaz vazio a sua frente. Há tambem uma varanda que indica um nascer do sol próximo.
    Agora que Balthus está morto, você se tornou o mago...não... o ser mais poderoso de todo o continente, o destino de tudo e todos é seu,entao:"
    menu:
        "Se dirige a varanda, e contempla a paz conquistada":
            jump final_alvorecer
        "Se dirige ao trono, e planeja oque fará como novo lorde do caos":
            jump final_lorde

label final_alvorecer:

    play music "musics/Neverland+-+320bit.mp3"

    scene fim_alvor:
        zoom 2.2
    n "Você se dirige a varanda e contempla, tudo isso seria destruido caso você tivesse falhado, tal realização te enche de orgulho,seu sofrimento não foi em vão,
    é hora de voltar para casa e abracar todos aqueles que ama!
    Sua jornada termina aqui,mas sempre que houver escuridao, o mago escuridão,o mago retornará!"

    $renpy.notify("fim de jogo")

    return

label final_lorde:

    scene fim_lorde

    play music "musics/final lorde.mp3"

    $renpy.notify("fim de jogo")

    n "Sua jornada jamais terá fim lorde do caos, para aqueles que anseiam pelo poder, as correntes da avareza, da arrogância jamais te deixarâo livre,vida longa ao novo governante!"

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
            hide screen batalha_generica
            jump final_ruim

        if(oponente_hp > 0):
            $ oponente_damage = renpy.random.randint(2, 6)

            $ mago_hp -= oponente_damage

            n " {i}*os guardas te atacam!*{/i} (dano recebido - [oponente_damage]hp)"

            play sound "musics/efeito_sonoro/gemido-combate.mp3"

    hide screen batalha_generica
    'oponentes derrotados!!!'
    jump dois51

label batalha_criaturas:
    #hide guarda1
    hide goblin2

    show mc normal at left:
        zoom 0.6
    with dissolve

    show orca at right:
        zoom 1.2
        ypos 1050
    show anao at right:
        zoom 0.5
        xpos 1600
    show goblin1 at right:
        xpos 2050

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
            hide screen batalha_generica
            jump final_ruim

        if(oponente_hp > 0):
            $ oponente_damage = renpy.random.randint(2, 6)

            $ mago_hp -= oponente_damage

            n " {i}*As criaturas te atacam!*{/i} (dano recebido - [oponente_damage]hp)"

            play sound "musics/efeito_sonoro/gemido-combate.mp3"

    hide screen batalha_generica
    'oponentes derrotados!!!'
    jump dois45

label batalha_tentaculo:

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
            hide screen batalha_generica
            jump final_ruim

        if(oponente_hp > 0):
            $ oponente_damage = renpy.random.randint(2, 6)

            $ mago_hp -= oponente_damage

            n " {i}*o oponente te arrasta para o seu covil!*{/i} (dano recebido - [oponente_damage]hp)"

            play sound "musics/efeito_sonoro/gemido-combate.mp3"

    hide screen batalha_generica
    'oponente derrotado!!!'
    jump dois18

label batalha_contra_um:
    #hide guarda1
    #hide guarda2

    show mc normal at left:
        zoom 0.6
    with fade

    #show guarda1 at right:
        #zoom 1.3
    #with dissolve

    #show guarda2:
        #xpos 1050
        #ypos 400
        #zoom 0.9
    #with dissolve

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
            hide screen batalha_generica
            jump final_ruim

        if(oponente_hp > 0):
            $ oponente_damage = renpy.random.randint(2, 6)

            $ mago_hp -= oponente_damage

            n " {i}*O vendedor te ataca!*{/i} (dano recebido - [oponente_damage]hp)"

            play sound "musics/efeito_sonoro/gemido-combate.mp3"

    hide screen batalha_generica
    'oponente derrotado!!!'
    n "Dessa forma, você prossegue a sua jornada para a Torre Negra"
    $renpy.notify("Punhal pilhado!")
    jump dois18

label batalha_contra_dois:
    #hide guarda1
    #hide guarda2

    show mc normal at left:
        zoom 0.6
    with fade

    #show guarda1 at right:
        #zoom 1.3
    #with dissolve

    #show guarda2:
        #xpos 1050
        #ypos 400
        #zoom 0.9
    #with dissolve

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
            hide screen batalha_generica
            jump final_ruim

        if(oponente_hp > 0):
            $ oponente_damage = renpy.random.randint(2, 6)

            $ mago_hp -= oponente_damage

            n " {i}*Os oponentes te atacam!*{/i} (dano recebido - [oponente_damage]hp)"

            play sound "musics/efeito_sonoro/gemido-combate.mp3"

    hide screen batalha_generica
    'oponentes derrotados!!!'
    $renpy.notify("Punhal pilhado!")
    n "Dessa forma, você prosseguirá com a sua jornada para a Torre Negra."
    jump dois18

label batalha_calacorm:
    n "A criatura entra em seu aposento e parte para cima de você!"
    show mc normal at left:
        zoom 0.6
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

            n " {i}*o oponente te arrasta para o seu covil!*{/i} (dano recebido - [oponente_damage]hp)"

            play sound "musics/efeito_sonoro/gemido-combate.mp3"

    hide screen batalha_generica
    "Oponente derrotado e você parte em fuga!"
    jump um74

label batalha_gark:
    show mc normal at left:
        zoom 0.6
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
            hide screen batalha_generica
            jump final_ruim

        if(oponente_hp > 0):
            $ oponente_damage = renpy.random.randint(2, 6)

            $ mago_hp -= oponente_damage

            n " {i}*o oponente te arrasta para o seu covil!*{/i} (dano recebido - [oponente_damage]hp)"

            play sound "musics/efeito_sonoro/gemido-combate.mp3"

    hide screen batalha_generica
    'Oponente derrotado e você parte em direção às portas!'
    jump nove9

label batalha_cobras: ##incompleto

label batalha_hidra:

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
            hide screen batalha_generica
            jump final_ruim

        if(oponente_hp > 0):
            $ oponente_damage = renpy.random.randint(2, 6)

            $ mago_hp -= oponente_damage

            n " {i}*o oponente te arrasta para o seu covil!*{/i} (dano recebido - [oponente_damage]hp)"

            play sound "musics/efeito_sonoro/gemido-combate.mp3"

    hide screen batalha_generica
    'oponente derrotado!!!'
    jump dois29

label batalha_hidra_vs_hidra:

label batalha_balthus1:

    scene arena_final1

    with dissolve

    show mc bombado at left:
        zoom 0.6
    with dissolve

    show balthus normal at right:
        zoom 0.7
    with dissolve

    $ oponente_max_hp = 30
    $ mago_max_hp = 50
    $ oponente_hp = oponente_max_hp
    $ mago_hp = mago_max_hp
    $ elixir_left = 13

    show screen batalha_balthus

    while (oponente_hp > 0):

        if mago_hp > 0:
            menu:

                "estilo yore tormenta das espadas (2 a 3 de dano)":

                    play sound "musics/efeito_sonoro/ataque espada.mp3"

                    $ mago_damage = renpy.random.randint(2, 3)
                    $ oponente_hp -= mago_damage
                    mc "Raaaaah!!!!! (dano causado - [mago_damage]hp)"


                "estilo yore rugido do dragao (3 a 7 de dano)":

                    play sound "musics/efeito_sonoro/bola de fogo.mp3"

                    $ mago_damage = renpy.random.randint(3, 7)
                    $ oponente_hp -= mago_damage
                    mc "estilo yore! rugido do dragao!!!!! (dano causado - [mago_damage]hp)"



                "estilo yore desabrochar arcano (3 a 10 de dano)":

                    play sound "musics/efeito_sonoro/raio arcano.mp3" volume 0.7

                    $ mago_damage = renpy.random.randint(3, 10)
                    $ oponente_hp -= mago_damage
                    mc "estilo yore! desabrochar arcano!!!!! (dano causado - [mago_damage]hp)"

                "tomar elixir da vida (tem [elixir_left] elixires)" if elixir_left > 0:
                    $ mago_hp = min(mago_hp+5, mago_max_hp)
                    $ elixir_left -= 1
                    n "{i}*você sente suas feridas cicatrizarem!*{/i} (vida curada - 5 hp)"
        else:
            hide screen batalha_balthus
            jump final_ruim

        if(oponente_hp > 0):
            $ oponente_damage = renpy.random.randint(2, 6)

            $ mago_hp -= oponente_damage

            n " {i}*o grande Balthus te ataca !*{/i} (dano recebido - [oponente_damage]hp)"

            play sound "musics/efeito_sonoro/gemido-combate.mp3"

    hide screen batalha_balthus
    'Balthus derrotado!!!'
    jump despertar_balthus

label batalha_balthus2:
    scene arena_final2:
        zoom 1.3
    with dissolve

    show mc bombado at left:
        zoom 0.6
    with dissolve

    show balthus bombado at right:
        ypos 1500
        zoom 1.5
    with dissolve

    $ oponente_max_hp = 30
    $ mago_max_hp = 50
    $ oponente_hp = oponente_max_hp
    $ mago_hp = mago_max_hp
    $ elixir_left = 13

    show screen batalha_balthus

    while (oponente_hp > 0):

        if mago_hp > 0:
            menu:

                "estilo yore tormenta das espadas (2 a 3 de dano)":

                    play sound "musics/efeito_sonoro/ataque espada.mp3"

                    $ mago_damage = renpy.random.randint(2, 3)
                    $ oponente_hp -= mago_damage
                    mc "Raaaaah!!!!! (dano causado - [mago_damage]hp)"


                "estilo yore rugido do dragao (3 a 7 de dano)":

                    play sound "musics/efeito_sonoro/bola de fogo.mp3"

                    $ mago_damage = renpy.random.randint(3, 7)
                    $ oponente_hp -= mago_damage
                    mc "estilo yore! rugido do dragao!!!!! (dano causado - [mago_damage]hp)"



                "estilo yore desabrochar arcano (3 a 10 de dano)":

                    play sound "musics/efeito_sonoro/raio arcano.mp3" volume 0.7

                    $ mago_damage = renpy.random.randint(3, 10)
                    $ oponente_hp -= mago_damage
                    mc "estilo yore! desabrochar arcano!!!!! (dano causado - [mago_damage]hp)"

                "tomar elixir da vida (tem [elixir_left] elixires)" if elixir_left > 0:
                    $ mago_hp = min(mago_hp+5, mago_max_hp)
                    $ elixir_left -= 1
                    n "{i}*você sente suas feridas cicatrizarem!*{/i} (vida curada - 5 hp)"
        else:
            hide screen batalha_balthus
            jump final_ruim

        if(oponente_hp > 0):
            $ oponente_damage = renpy.random.randint(2, 6)

            $ mago_hp -= oponente_damage

            n " {i}*o grande Balthus te ataca !*{/i} (dano recebido - [oponente_damage]hp)"

            play sound "musics/efeito_sonoro/gemido-combate.mp3"

    hide screen batalha_balthus
    'Balthus derrotado!!!'
    jump fim_batalha

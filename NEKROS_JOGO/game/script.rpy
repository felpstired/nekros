define mc = Character("[mcname]", color="#cc0000")


# P jogo começa aqui

label start: 

    $ pnome1 = "Elu"

    $ pnome2 = "Delu"

    stop music

    scene bg caveira_hover
    with fade

    $ mcname = renpy.input("Qual o seu nome?", length=25)

    $ mcname = mcname.strip()

    if mcname == "":
        $ mcname = "Robin"

    #tem como definir a aparência do mc com as skins e sexos

    #image character = Composite(

    #    (846, 1028),
    #    (0, 0), "personagem/body-skin-[skin_color.png]"
    #    (0, 0), "personagem/body-sex-[sexo.png]"
    #)

    #$sexos = ["feminino", "masculino","sem definição"]
    #$skin_colors= ["branco", "pardo", "negro"]



    # ANOTAÇÃO DA ANALU UAU UAU UAU


    "Quais pronomes melhor te representa?"
    
    menu:
    
        "Ela/Dela":
            $ pnome1 = "Ela"
            $ pnome2 = "Dela"

        "Ele/Dele":
            $ pnome1 = "Ele"
            $ pnome2 = "Dele"

        "Elu/Delu":
            $ pnome1 = "Elu"
            $ pnome2 = "Delu"


    # FIM DA ANOTAÇÃO DA ANALU YIPPIE



    #$skin_color = skin_color[1]
    #$sexo = sexo[1]

    #sumir com a caveira

    #imagem capítulo 1

    "Abro os olhos em um local desconhecido, assustado, me levanto rapidamente do local onde estava deitado. "

    scene bg vinho
    with fade
    
    "Sinto uma dor aguda na cabeça e pressiono minha têmpora para tentar diminuir a dor."

    show protag pain_terno at left
    with moveinbottom

    #dissolve para mudar as expressões dos personagens
    # fade para mudar as cenas de bg
    # move + direção junta "moveinright" para expecificar o movimento de entrada do personagem em cena

    mc "Hãn…"

    "Eu estava em um banco de madeira antes de me levantar, o local ao redor é uma praça."

    scene bg praca
    with fade

    mc "Acho que perdi algo muito importante, mas não lembro do que seja. Minhas memórias estão confusas… "

    show bg vinho
    with fade
    
    "Tento me lembrar de qualquer coisa, mas meu cérebro dói muito." 

    scene bg praca
    with fade

    "Olhando para baixo depois da dor, vejo que estou usando um terno."
    
    "Procuro então dentro dos bolsos do terno para conseguir alguma informação sobre quem sou e onde estou." 

    "No bolso direito eu sinto algo e retiro, no bolso tinha um celular e uma carteira." 
    
    label choices:

    #default learned é para mudar a conversa de um personagem de acordo com sua escolha dentro do jogo

    #default learned = False

    mc "Hm?"

    #olhar para baixo vendo o terno

    menu: 
        "Tentar desbloquear o celular":
            jump choices1_a

        "Abrir a carteira":
            jump choices1_b

    label choices1_a:

        show bg mao_desbloqueando_celular
        with dissolve 

        "Pego o celular e tento desbloquear ele."

        mc "Tem senha..."

        show bg vinho
        with dissolve

        "Tento me lembrar da senha mas a cabeça dói muito na tentativa e desisto."

        scene bg praca
        with dissolve

        jump choices1_b

    label choices1_b:

        show bg carteira 
        with dissolve 

        "Abro então a carteira e procuro por alguma informação útil." 
        
        "Tem um documento de identidade."

        #som de dor 1

        show bg vinho
        with dissolve
        
        "Quando vejo a foto na identidade, sinto uma dor aguda novamente."

        #som de dor 2 - agudo

        show bg preto
        with dissolve

        "Imagens começam a aparecer na minha cabeça enquanto uma dor muito forte engloba todos os meus sentidos." 

        #som de dor 2 - dissolve

        scene bg praca
        with dissolve

        "Sinto familiaridade com algumas imagens e relembro quem sou."



        #mc recebe nome e escolhe o sexo
        
        "Sou [mcname], sexo,\" e o local em que estou é uma praça perto de onde eu moro. "

        "Pego meu celular para poder saber que data é hoje."
        
        mc "Hoje é dia 06/12/2012..."

        jump choices1_common

    label choices1_common:

        "Lembro de que deixei meu carro perto da praça." 
        
        "Pego a chave que está em meu bolso e caminho na direção de onde me lembro de ter estacionado o carro."

        #barulho de chaves

        # mostrar imagem praça fora + carro dessa marca aí

        "Chegando na área, vejo um Renault Scenic, aperto o botão da chave e escuto um apito. Caminho até o carro e abro a porta do mesmo."

        #barulho de apito de carro

        # mostrar cena de dor rapidamente

        "O cheiro familiar dentro do carro relembra mais memórias com a mesma dor anterior." 

        #som de carro ligando e funcionando

        "Com as memórias recém-relembradas dirijo até minha casa."
        
        "Me perco no caminho algumas vezes, mas consigo encontrar o caminho de volta."

        "Estaciono então no local de sempre e tranco o carro."

        "Entro dentro da casa com a chave e o cheiro da mesma me enche de familiaridade. Olho para a sapateira que está no hall de entrada e caminho até ela."

        "Em cima dela há quadros com fotos, pego então um dos quadros que repousa nela e olho para a imagem dentro."

        mc "Ugh.."

        #tela preta

        "Quando vejo a imagem, minha cabeça dói ainda mais que as vezes anteriores, parecendo que partiria no meio. "

        #som agudo para representar a dor
        
        "Sem aguentar a dor, caio no chão em posição fetal enquanto seguro a cabeça com força gemendo de dor."

        "Suando de dor, tudo se apaga e desmaio."

        "Acordo todo empapado, olho para o quadro que caiu no chão quando caí em posição fetal."

        mc "Ainda bem que não quebrou…"
        
        "Começo a chorar sem perceber ao olhar a gravura das duas pessoas no quadro." 

        #mc chorando 

        "A imagem tem eu e mais  'sexo da pessoa',"

        
        #mostrar cena do quadro na mão + imagem de 2 pessoas dependendo dos sexos escolhidos
        
        "Sinto que essa pessoa é extremamente importante para mim, mas não me lembro o nome dela e nem o rosto, apesar de que algumas memórias com essa pessoa foram aparecendo em minha mente."

        "Me levanto segurando o quadro com as novas memórias desbloqueadas e vou até a sala onde sento-me no sofá."

        # mostrar cena da ida até a sala

        # mostrar mc do sofá sentado

        "Enquanto olho o quadro, tento organizar minhas memórias que vieram com a dor insuportável."

        "Pego o celular e o desbloqueio, olho a data que está nele"

        #cena do celular com horário mão
        
        mc "09 de dezembro de 2012… fiquei 3 dias inconsciente???!"
        mc "Isso justifica a fome, mas essa dor de cabeça anormal e a falta de memórias… com certeza tem algo errado comigo… " 

        # imagem de celular na mão para tirar o texto
        
        "Digo enquanto olho o celular em minha mão."

        mc "Preciso marcar um médico, não estou bem."

        # lembrança preta e branca da cozinha com a geladeira cehia de anotações

        "Lembrei que haviam muitos contatos de hospitais e doutores grudados na geladeira."        
        
        "Levantei e fui para a cozinha, na geladeira possuía vários números, dentre eles haviam contatos de hospitais e médicos, procurei um que parecia próximo." 

        # mostrar cena cozinha com geladeira com anotações atuais

        "Já estava de noite, então deixei para ligar no dia seguinte."

        "Fiz algo para comer com o que havia na geladeira porque estava com uma enorme fome de 3 dias e resolvi descobrir quem é a pessoa da gravura e porque meu coração doía tanto ao ver ela."
        
        "Peguei o celular novamente e procurei na galeria sobre fotos da pessoa, a galeria estava lotada delas."

        # celular com imagens de casal com sexo escolhido se movendo +  a cada imagem batida de coração forte e intensificada com as cores das imagens ficando mais avermelhadas
        
        "A cada imagem passando meu coração doía mais e meus olhos começaram a encher de lágrimas que começaram a escapar."
        
        "O sentimento era extremamente forte, mas eu não me lembrava, não conseguia me lembrar da pessoa, doía muito tentar lembrar."

        #sexo palavra muda de acordo com o sexo do parceiro escolhido

        "O mais óbvio é que essa pessoa com certeza era 'minha esposa / meu esposo'."
        
        "Mesmo olhando para o rosto dela no quadro e nas imagens, em minhas memórias estava tudo apagado. Como se houvesse uma névoa tampando minha mente"       

        mc "O que aconteceu com 'ele/a'? Nos separamos?" 
        
        # mostrar mc chorando

        "Lágrimas fugiam pela incapacidade de lembrar alguém tão importante e pela dor semelhante àquela que tive ao desmaiar que estava ressurgindo a cada imagem"
        
        mc "Sinto que se eu tentar lembrar mais dela neste momento, minha cabeça vai se abrir em duas."

        "Desisti de procurar saber sobre a pessoa pelo momento. Procurei então mais informações sobre mim."
        
        "Na galeria tinha muitas fotos de nós que passei rapidamente para não causar gatilhos, muitas fotos de paisagens e algumas imagens engraçadas também, não tinha muita informação útil sobre eu como pessoa em si."
        
        "Passei o resto do dia procurando mais informações de quem eu sou no resto da casa."
        
        mc "Sou um médico…? Me lembro de usar um jaleco e estar em um local branco com pessoas ao redor..."

        mc "Me lembro de que estávamos com um paciente na mesa… algumas cirurgias e lembro-me que estava de férias."

        # ainda não se lembra do local onde trabalhava 

        "Outras memórias insignificantes do dia-a-dia também estavam em minha cabeça, mas nada extremamente relevante."

        #cena de andar até o banheiro

        #cena do banheiro

        #som de abrir o box 

        "Estressado por estar com amnésia e sentir dor sempre que tento me lembrar ou me lembro de algo, vou ao banheiro tomar um banho quente"
        
        #som de tomar banho + cena de banho no chuveiro

        #cena antes de abrir a torneira do chuveiro + som

        "Sinto muita dor e ardência no meu rosto e braço quando a água encosta na pele."

        #cena depois de abrir a torneira do chuveiro + som de banho
        
        mc "Parece que eu sofri um acidente… seria essa a causa da minha amnésia?"

        "Termino o banho, me enxugo e abro o box."
        
        #som de abrir o box do banheiro + passos sem sapatos 

        # cena do espelho

        "Me olho no espelho."

        #cena no espelho com o mconista se olhando

        # cena do espelo com o mconista de aproximando do espelho para ver a cicatriz

        mc "..."

        "No espelho vejo meu reflexo, meu rosto está ferido com 4 arranhões que vem da esquerda do rosto até o nariz, que rasgaram muito a pele."

        #cena do espelho com o mconista perto do espelho tocando a ferida

        mc "Ouch… " 
        
        mc "Parece recente… como isso ocorreu?"
        
        "Sem memórias do ocorrido, procuro uma pomada para machucados e a passo em meu rosto."

        #cena do espelho com o mconista perto do espelho tocando a ferida e com pomada na pia e no machucado

        "Após esse dia mentalmente exaustivo, vou para o quarto dormir novamente"
        
        "Apesar de ter ficado desmaiado 3 dias, não me sinto nem um pouco descansado"
        
        mc "Sinto como se tivesse corrido várias maratonas... Tô todo amassado."

        #iamgem de guarda-roupas
        #som de abrir guarda-roupas

        "Abro o guarda-roupas e percebo que há conjuntos de roupas que são familiares mas que obviamente não são meus. Lapsos leves de outra pessoa usando algumas daquelas roupas aparecem em minha mente causando dor novamente."

        #tela vermelha + imagens da pessoa usando as roupas no guarda roupa

        #cena mc da cama

        mc "Ugh… Não tenho paz nem após o banho…" 
        
        "Digo indignado indo dormir com enxaqueca."

        #som de alarme

        #imagem do quarto

        #10 de dezembro de 2012

        "No dia seguinte liguei então para um hospital e marquei um horário, apenas possuíam disponibilidade para daqui a 2 dias, então aceitei."

        #imagem do quarto de noite
        #imagem do quarto de tarde
        #imagem do quarto de manhã
        #imagem do quarto de tarde
        #imagem do quarto de noite
        #imagem do quarto de manhã

        "Os 2 dias seguintes passaram rapidamente, fiquei principalmente vendo televisão e lendo livros."

        #12 de dezembro de 2012
        
        "Estive tentando me lembrar das coisas, mas ainda sim nada muito importante veio em minhas memórias nestes 3 dias, estranhamente não me lembro muito de meu trabalho ou 'da pessoa'."

        "Sempre que tento me lembrar do trabalho nada importante vem e quando tento me lembrar dela, dói muito, então resolvi deixar meu cérebro descansar até o exame."
        
        "Outro mistério é esta cicatriz, não tenho a menor lembrança de como esse arranhão ocorreu, nenhuma das coisas dentro de casa me lembrou sobre como consegui esse machucado."

        mc "Hoje já é o dia do exame... espero que não seja nada sério..."
        
        "Me arrumei para ir ao médico olhar minha situação, coloquei um cachecol para tentar esconder onde estava o arranhão, e saí de casa."

        #som de carro

        "Dirigi até o hospital." 

        # cena de chegada ao hospital

        #cena recepção hospital c/ atendente

        "No hospital fui até a atendente informar soobre minha consulta e fui me sentar esperando ser chamado"

        # cena hospital esperando ser atendido, cheio de pessoas doentes 

        "extra - Me pergunto se está havendo uma epidemia de gripe. O tempo esfriou ultimamente…" 
        
        "Disse uma pessoa sentada."

        #som de pessoas tossindo / espirrando + pessoas conversando

        #som de hospital

        "Enquanto estava esperando, percebi que o hospital estava bem mais cheio do que normalmente ficava. Muitas pessoas estavam tossindo e pareciam amareladas."

        "Outras pessoas estavam em macas."

        "'Nome mc'!! O Doutor Patrick está na sala 3, virando a direita." "Me chamaram e fui direcionado até a sala do doutor." 

        #cena de corredor de hospital + pessoas em macas

        #cena do consultorio 

        "O doutor fez alguns testes básicos em mim, falei para ele da amnésia e das dores de cabeça. Informei também que não me lembrava de como consegui esse machucado."

        "Ele informou que casos de amnésia mais comuns são quando existe algum tipo de traumatismo craniano."

        #cena raio-x
        
        "Fui levado/a para a sala de raio-x para poder confirmar se eu possuía algum tipo de sinal na cabeça equivalente a um traumatismo devido a queda ou algo do gênero."

        #cena do consultorio 

        "Enquanto esperávamos o resultado do raio-x sair, ele confirmou o estado da ferida e receitou algumas pomadas e a forma de tratar para evitar uma cicatriz."
        
        "Quando o resultado saiu, ele confirmou que não havia nenhuma contusão."
        
        "Então me informou que a causa da amnésia muito provavelmente era psicológica e que eu poderia estar realizando acompanhamento com um psiquiatra que induz a hipnose para ajudar a relembrar as memórias perdidas."
        
        "Ele recomendou descansar o máximo possível para poder curar a ferida e para que o cérebro se recupere de quaisquer tipos de traumas que tenham ocorrido dos quais ainda não me lembro."

        "Agradeci ao doutor e saí da sala dele."

        #cena fora do consulório, corredor

        #senhora extra infectada malzão entra na cena
        #senhora extra infectada 

        mc "Ouf..." 

        "Alguém esbarrou em mim com força. Olhei para quem foi e a pessoa me olhou de volta."
        
        "Estranhei a senhora que me encarava e fiquei assustado com a forma com que os olhos dela estavam super proeminentes e vermelhos como se fossem sair da cara dela."

        "A cor da pele dela estava bastante acinzentada também."        

        "Ela continuou andando, mas enquanto ela se distanciava de mim, fiquei encarando as costas dela."
        
        "Senti um estranho arrepio na espinha quando ela saiu da minha vista."

        mc "Hipotireoidismo é foda viu?"

        "No caminho para fora do hospital olhei para algumas pessoas que estavam em macas, e parecia que realmente havia uma nova doença rondando no ar"
        
        "Entretando, essa doença parecia atingir principalmente pessoas mais velhas, já que a maioria das pessoas que estavam nas macas eram idosos."

        #cena da farmácia

        "Voltei para meu carro e então dirigi para a farmárcia mais próxima comprar os remédios que me foram receitados."

        "A farmárcia também estava lotada de pessoas que pareceiam estar doentes."

        "Comprei os remédios da receita e então voltei para minha casa."

        "Dentro de casa não havia nada para fazer."

        "Além de ser amnésico, estou entediado. Sensacional…"
        
        "Procuro então algo para fazer."

        label choices2:

        #default learned é para mudar a conversa de um personagem de acordo com sua escolha dentro do jogo

        #default learned = False

        "Procuro então algo para fazer."

    menu: 
        "Assistir televisão":
            jump choices2_a

        "Ler um livro":
            jump choices2_b

        "Sair para passear":
            jump choices2_c

    #Assistir televisão
    label choices2_a:

        #Cena mc iluminação tarde sofa com tv desligada
        
        #som de tv ligando 

        "Peguei o controle e liguei a televisão."

        #Cena mc iluminação tarde sofa com tv ligada

        #Cena mc iluminação tarde sofa com tv passando santana acabe com ela

        "Novela - Voz feminina - Não, me mate também."

        "Novela - Voz feminina - Me mata"

        "Novela - Voz masculina - É isso que você quer?"

        "Novela - Voz masculina - Santana, acabe com ela."

        "Novela - Voz feminina - Ai!"

        #Cena mc iluminação tarde sofa com tv ligada mostrando jornalista conversando
        #Cena mc iluminação tarde sofa com tv ligada
        
        "Boa tarde. Interrompemos sua programação para informar de uma possível epidemia. Casos de uma nova cepa de H1N1 foram encontrados na cidade A, pelos cientistas da Universidade A na Cidade C." 
        
        "A doença se alastrou rapidamente neste tempo frio."

        "Dentre os sintomas podemos citar febre alta (acima de 38ºC), suor excessivo, exaustão mental e muscular, irritação e acentuamento no tamanho dos olhos, tosse persistente, coloração da pela amarela ou meio acinzentada, boca extremamente seca e dor de garganta."
        
        mc "Talvez a idosa no hospital... e essa doença..." 

        "Avisamos que essa é uma doença potencialmente fatal, 10 pessoas que estavam em acompanhamento para observar essa doença faleceram dentro das últimas 48 horas."
        
        "A doença está se espalhando rapidamente, então, para evitar mais casos de contaminação, recomendamos a todos que evitem sair de casa e usem máscaras."

        "A cepa mutada do H1N1 parece contaminar através de feridas e contato com a mucosa e sangue de pessoas contaminadas." 
        
        "Enquanto não há uma cura disponível para a variável, os cientistas continuam a buscar uma cura para a mesma."

        "Ainda bem que estou de férias… ficar em casa neste momento parece ser o ideal. Talvez ficar amnésico não seja tão ruim neste momento…"

        #(3) … 

        #(3a) Desligo a televisão

        #(3b) Continuar a assistir televisão

        #(3c) Mantenho a televisão ligada


        #se escolher (3a):



        #se escolher (3b):



        #se escolher (3c):



        #cena comum:


    jump choices2_common

    #Ler um livro
    label choices2_b:

        #o livro depende do sexo de ambos os personagens

        "Você pega um livro da estante que parece meio gasto, “P.S: Eu te amo”. Esse livro traz memórias com aquela dor já familiar."

        "A cena de uma pessoa deitada no sofá, com o sol da tarde tocando sua pele enquanto ela lê este livro aparece como flashback."

        "Sem perceber você começa a sorrir com a memória." 

        "Você então coloca música que lembrou tocando e recupera mais memórias doces apesar da dor."

        #cenas românticas com livros, danças e músicas

        "Começa a ler o livro."

        #Não sabe sobre o surto de zumbis mas sente uma terrível saudade da pessoa amada.


    jump choices2_common


    #Sair para passear
    label choices2_c:

        "Você coloca uma roupa de frio e se prepara para sair,
observa a cena."

        #relembra memórias, encontra com uma pessoa infectada transformada.



        "2 opções:

        4a - se aproximar

        mais 2 opções:

        pode ser mordido ou nao

        encontra um item se não for mordido


        4b - não se aproximar e continuar no caminho

        não será mordido mas vai estranhar muito a pessoa

        encontra um item

        volta pra casa

        entra na casa

        mudança para a 

        cena comum:"

        jump choices2_common



    label choices2_common:    


        "cena comum"







    # Jogo finaliza aqui.

    return

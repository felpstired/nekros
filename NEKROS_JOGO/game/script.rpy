# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.



define protag = Character('Protag', color="#cc0000")


# The game starts here.

label start: 

    stop music

    #O jogo começa

    "Abro os olhos em um local desconhecido, assustado, me levanto rapidamente do local onde estava deitado. "

    scene bg vinho
    with fade
    
    "Sinto uma dor aguda na cabeça e pressiono minha têmpora para tentar diminuir a dor."

    show protag pain_terno at left
    with moveinbottom

    #dissolve para mudar as expressões dos personagens
    # fade para mudar as cenas de bg
    # move + direção junta "moveinright" para expecificar o movimento de entrada do personagem em cena

    protag "Hãn…"

    "Eu estava em um banco de madeira antes de me levantar, o local ao redor é uma praça."

    scene bg praca
    with fade

    protag "Acho que perdi algo muito importante, mas não lembro do que seja. Minhas memórias estão confusas… "

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

    protag "Hm?"

    menu: 
        "Tentar desbloquear o celular":
            jump choices1_a

        "Abrir a carteira":
            jump choices1_b

    label choices1_a:

        "Pego o celular e tento desbloquear ele."

        protag "Tem senha..."

        show bg vinho
        with dissolve

        "Tento me lembrar da senha mas a cabeça dói muito na tentativa e desisto."

        scene bg praca
        with dissolve

        jump choices1_b

    label choices1_b:

        "Abro então a carteira e procuro por alguma informação útil." 
        
        "Tem um documento de identidade."

        show bg vinho
        with dissolve
        
        "Quando vejo a foto na identidade, sinto uma dor aguda novamente."

        show bg preto
        with dissolve

        "Imagens começam a aparecer na minha cabeça enquanto uma dor muito forte engloba todos os meus sentidos." 

        scene bg praca
        with dissolve

        "Sinto familiaridade com algumas imagens e relembro quem sou."



        #protag recebe nome e escolhe o sexo
        
        "Sou \" nome, sexo,\" e o local em que estou é uma praça perto de onde eu moro. "

        "Pego meu celular para poder saber que data é hoje"
        
        protag "Hoje é dia 06/12/2012..."

        jump choices1_common

    label choices1_common:

        "Lembro de que deixei meu carro perto da praça." 
        
        "Pego a chave que está em meu bolso e caminho na direção de onde me lembro de ter estacionado o carro."

        




    # This ends the game.

    return

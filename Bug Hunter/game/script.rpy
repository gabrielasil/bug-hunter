define debora = Character("Débora Debug")
define carlos = Character("Carlos Cavalcante", color="#ff0000")
define paula = Character("Paula Pereira", color="#00FF00")
define bruno = Character("Bruno Barreto", color="#0000FF")


transform midright:
    xalign 1.5

transform midleft:
    xalign -0.5

label start:
    scene bg quarto
    debora "Hoje é meu primeiro dia como estagiária de requisitos... Estou um pouco nervosa."

    scene bg escritorio
    show paula
    paula "Oi, Débora! Pronta para começar? Você vai adorar trabalhar aqui!"
    
    debora "Oi, Paula! Estou animada, mas um pouco apreensiva."
    hide paula

    show carlos
    carlos "Bom dia, Débora! Venha comigo. Vou te apresentar à equipe."

    carlos "Aqui está o nosso time. Cada um desempenha um papel essencial no desenvolvimento."

    show paula at midleft
    show bruno at midright
    debora "É ótimo conhecer todos!"

    hide paula
    hide bruno
    carlos "Vou te passar sua primeira tarefa. Você precisa revisar um documento sobre a funcionalidade de login do sistema."

    debora "Claro! Vou fazer isso agora."

    hide carlos
    debora "..."

    debora "Preciso entender como o usuário interage com o sistema... Vamos esboçar um fluxo de autenticação."

    debora "Hmm... O critério de autenticação não está claro. É só login e senha? Ou tem autenticação por OTP?"

    debora "A especificação da senha diz que deve ter pelo menos oito caracteres, um número e um caractere especial. As mensagens de erro estão bem definidas também."

    debora "Mas... em quais dispositivos e navegadores o login deve funcionar? Não sei isso ainda."

    # Opções para a jogadora
    menu:
        "Pedir ajuda ao Carlos":

            debora "Carlos, você pode me ajudar a definir alguns pontos que estão faltando?"
            jump carlos_feliz

        "Preencher as lacunas sozinha":

            debora "Acho que posso tentar preencher as lacunas sozinha."

            debora "..."
            jump carlos_triste


label carlos_feliz:
        show carlos
        carlos "Bom trabalho, Débora! Você fez as perguntas certas."
        jump final_ato1

label carlos_triste:
        show carlos
        carlos "Você foi ousada, mas espero que tenha sido cuidadosa. Vamos revisar seu trabalho."
        jump final_ato1

label final_ato1:

    debora "Obrigada, Carlos! Estou animada para aprender mais."

    show paula at midleft
    paula "E não se esqueça, estamos aqui para ajudar! Vamos fazer isso juntos!"

    show bruno at midright
    bruno "Só não se esqueça: um requisito mal formulado é a origem de todos os bugs."

    debora "Isso eu não vou esquecer!"

    return

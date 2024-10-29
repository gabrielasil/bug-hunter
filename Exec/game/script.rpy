define debora = Character("Débora Debug")
define carlos = Character("Carlos Cavalcante", color="#ff0000")
define paula = Character("Paula Pereira", color="#00FF00")
define bruno = Character("Bruno Barreto", color="#0000FF")

default estilo = 0

transform midright:
    xalign 1.5

transform midleft:
    xalign -0.5

label start:

    scene bg quarto
    debora "Hoje é meu primeiro dia como estagiária de requisitos... Estou um pouco nervosa."

    debora "Já estou no quinto periodo da minha faculdade, mas é a primeira vez que vou colocar meus conhecimentos a prova..."

    debora "Eita, a hora! Melhor eu correr, se não vou perder meu ônibus!"

    scene black
    scene bg rua
    debora "Espero me acostumar com a nova rotina."

    debora "Só a faculdade já é puxado, conciliar com o estágio vai ser mais complicado..."

    debora "Mas tenho certeza que vai valer a pena no final."

    scene bg escritorio

    debora "Ufa, quase me atrasei no primeiro dia"

    paula "Eai!!! Você que é a estagiária nova?"
    
    scene bg escritorio with hpunch
    debora "{size=+20}A{/size}{size=+15}a{/size}{size=+10}a{/size}{size=+5}a{/size}a oi. Perdão, não te vi chegando. Sou eu sim, Débora Debug, prazer!"

    "{i}* Estendo minha mão pra ela. *"

    show paula

    paula "Oi, Débora! Eu sou a Paula. Pronta pra começar? Você vai adorar trabalhar aqui!"

    "Ela aperta minha mão calorosamente. Ai!"

    debora "Oi, Paula! Estou animada, mas um pouco apreensiva."

    paula "Vai dar tudo certo! O chefão tá vindo ai pra fazer teu onboarding, boa sorte!"

    hide paula

    show carlos
    carlos "Bom dia, Débora! Venha comigo. Vou te apresentar à equipe."

    show paula at midleft

    carlos "Aqui está seu novo time. A Paula, que você já conheceu, é a nossa desenvolvedora."

    show bruno at midright

    carlos "E esse aqui é o Bruno, nosso testador. Ele é o responsável por atrasar nossas entregas por conta de um pixel fora do lugar. Hahah."

    show bruno with hpunch 

    bruno "Ei. Não escute ele. E seja bem vinda, Débora."

    debora "É ótimo conhecer todos!"

    hide paula
    hide bruno

    show carlos
    carlos "Bom, agora que já conheceu o time, vou te passar sua primeira tarefa."

    carlos "Você precisa revisar um documento sobre a funcionalidade de login do sistema."

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

            debora "Bom, se o login não está especificado, imagino que seja um fluxo padrão de login e senha..."

            debora "Vou atualizar o documento com as informações e pedir a opinião do Carlos."

            jump carlos_triste

        "Pedir mais informações ao time":

            debora "Acho que deve ter alguma documentação mais completa sobre isso..."

            debora "Ei Paula, você pode me tirar uma dúvida?"

            show paula
            paula "Claro! Do que precisa?"

            hide paula
            scene black
            "Passado um tempo..."

            scene bg escritorio
            show paula
            debora "Obrigada Paula! Essa documentação me ajudou muito a sanar minhas dúvidas."

            debora "Vou pedir a opinião do Carlos sobre minhas mudanças."

            paula "To aqui pra isso camarada!"
            hide paula

            jump carlos_satisfeito


label carlos_feliz:
        $ estilo = 1

        show carlos

        carlos "Claro, Débora! Vamos discutir isso."

        hide carlos
        scene black

        "Passado um tempo..."

        scene bg escritorio

        show carlos

        carlos "Bom trabalho, Débora! Você foi atenta aos requisitos e fico feliz que tenha me procurado para tirar suas dúvidas."

        jump final_ato1

label carlos_triste:
        $ estilo = 2
        show carlos
        carlos "Você foi ousada, mas espero que tenha sido cuidadosa. Vamos revisar seu trabalho."

        jump final_ato1

label carlos_satisfeito:
        $ estilo = 3
        show carlos
        carlos "Parabéns, Débora. Mandou bem em consultar a Paula pra te ajudar. Vamos discutir o resultado."
        jump final_ato1

label final_ato1:

    debora "Obrigada, Carlos! Estou animada para aprender mais."

    show paula at midleft
    paula "E não se esqueça, estamos aqui para ajudar! Vamos fazer isso juntos!"

    show bruno at midright
    bruno "Só não se esqueça: um requisito mal formulado é a origem de todos os bugs."

    debora "Isso eu não vou esquecer!"

    hide bruno
    hide paula
    hide carlos

    scene black

    "Seu estilo de trabalho foi..."

    nvl clear

    if estilo == 1:
        """Cautelosa: 
            Você pediu ajuda ao seu chefe para definir como preencher as lacunas. É uma escolha segura para quem está começando."""
    elif estilo == 2:
        """Proativa:
            Você decidiu resolver o problema com suas próprias mãos. Cuidado, isso pode ser arriscado se você não tiver contexto do produto."""
    else:
        """Conservadora: 
            Você preferiu buscar por mais informações antes de tomar uma decisão. Essa é uma boa escolha!"""


    return

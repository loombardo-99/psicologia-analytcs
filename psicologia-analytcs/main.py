#dados usuario


print("Para inicializar o Quiz preciso que responda abaixo")
print("balcbsdivgdsivgfisuhfiduvidsgfvisdahfaiuhfgdsfb1t6b1fg65n1dy86tn4651g65sbaivwebiucajcvfiaghjosavcoih FWF fyf yyf ye yfefye8 fy8wefywe8fywgftwefwecb9 8f ew8f we fwef ef ewf w8e9f9w78fgjzxk fw74ft78qft7823fgbcahmw f3gf 78 7tf g78dscv jhgv3ut ")
name = input("Informe seu nome: ")
age = input("Informe sua idade: ")

# Questões e respostasa

questions = [
    "1. Você sabe identificar as emoções que sente?\n(A) Sempre\n(B) Frequentemente\n(C) De vez em quando\n(D) Raramente\n(E) Nunca",
    "2. Você sabe se acalmar quando se sente inquieto ou chateado?\n(A) Sempre\n(B) Frequentemente\n(C) De vez em quando\n(D) Raramente\n(E) Nunca",
    "3. Você define metas a longo prazo?\n(A) Sempre\n(B) Frequentemente\n(C) De vez em quando\n(D) Raramente\n(E) Nunca",
    "4. Você procura entendimento mútuo nas questões?\n(A) Sempre\n(B) Frequentemente\n(C) De vez em quando\n(D) Raramente\n(E) Nunca",
    "5. Você é um bom ouvinte?\n(A) Sempre\n(B) Frequentemente\n(C) De vez em quando\n(D) Raramente\n(E) Nunca",
    "6. Você persiste na busca por seus objetivos, apesar dos obstáculos?\n(A) Sempre\n(B) Frequentemente\n(C) De vez em quando\n(D) Raramente\n(E) Nunca",
    "7. Você consegue admitir facilmente que cometeu um erro?\n(A) Sempre\n(B) Frequentemente\n(C) De vez em quando\n(D) Raramente\n(E) Nunca",
    "8. Você sabe suas qualidades e defeitos?\n(A) Sempre\n(B) Frequentemente\n(C) De vez em quando\n(D) Raramente\n(E) Nunca",
    "9. Você promove conversas difíceis para resolver problemas?\n(A) Sempre\n(B) Frequentemente\n(C) De vez em quando\n(D) Raramente\n(E) Nunca",
    "10. Você tenta enxergar as situações pela perspectiva dos outros?\n(A) Sempre\n(B) Frequentemente\n(C) De vez em quando\n(D) Raramente\n(E) Nunca",
    "11. Você tem ânimo para atingir seus objetivos?\n(A) Sempre\n(B) Frequentemente\n(C) De vez em quando\n(D) Raramente\n(E) Nunca",
    "12. Você consegue pensar claramente quando está sob pressão?\n(A) Sempre\n(B) Frequentemente\n(C) De vez em quando\n(D) Raramente\n(E) Nunca",
    "13. Você utiliza as críticas para crescer?\n(A) Sempre\n(B) Frequentemente\n(C) De vez em quando\n(D) Raramente\n(E) Nunca",
    "14. Você acha fácil ler as emoções dos outros?\n(A) Sempre\n(B) Frequentemente\n(C) De vez em quando\n(D) Raramente\n(E) Nunca",
    "15. Você lida com pessoas e situações difíceis com delicadeza?\n(A) Sempre\n(B) Frequentemente\n(C) De vez em quando\n(D) Raramente\n(E) Nunca",
    "16. Você se orienta pelos seus valores e objetivos?\n(A) Sempre\n(B) Frequentemente\n(C) De vez em quando\n(D) Raramente\n(E) Nunca",
    "17. Você supera facilmente o sentimento de frustração?\n(A) Sempre\n(B) Frequentemente\n(C) De vez em quando\n(D) Raramente\n(E) Nunca",
    "18. Você reconhece como seu comportamento afeta os outros?\n(A) Sempre\n(B) Frequentemente\n(C) De vez em quando\n(D) Raramente\n(E) Nunca",
    "19. Você consegue ouvir sem julgar?\n(A) Sempre\n(B) Frequentemente\n(C) De vez em quando\n(D) Raramente\n(E) Nunca",
    "20. Você presta atenção aos seus relacionamentos?\n(A) Sempre\n(B) Frequentemente\n(C) De vez em quando\n(D) Raramente\n(E) Nunca"
]

# Resultados das respostas
results = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
    "E": 1
}

# Função para executar o teste
def run_test(questions, results):
    score = 0
    for question in questions:
        while True:  # Loop para garantir uma resposta válida
            print(question)
            answer = input("Resposta: ").upper()
            if answer in results:
                score += results[answer]
                break  # Sai do loop se a resposta for válida
            else:
                print("Opção inválida. Por favor, escolha uma opção válida.")
    return score

# Executando o teste
score = run_test(questions, results)

# Exibindo o resultado
if score >=20 and score <=39:
    print("Seu score", name.upper(), "é:", score, " : Você precisa trabalhar para desenvolver sua inteligência emocional. Apesar de sua sinceridade ser admirável,\n é provável que você se sinta sobrecarregado por suas emoções e lute para gerenciar emoções. Reagir a isso,\n explodindo, ou, pelo contrário, não expressando suas emoções, é igualmente prejudicial.\n Suas respostas às pressões comuns da vida podem estar baseadas no medo e na insegurança - em vez de \npaixão e propósito. No entanto, isto não precisa ser algo definitivo! A inteligência emocional não vem do\n nascimento: ela pode ser desenvolvida. \n\nTrabalhe sua autoconsciência, porque ela é o primeiro fundamento da inteligência emocional. Se parece muito \ndifícil, não hesite em pedir ajuda para quem você considera ter muito conhecimento relacionado a oferecer.\n A intenção de desenvolver a inteligência emocional é o primeiro – e mais importante – passo. \n")

elif score >=40 and score <=59:
    print("Seu score", name.upper, "é:", score, " : Seu nível de inteligência emocional ainda é um pouco baixo. Você tem mais dificuldade nas situações que \nexigem mais habilidades de interação social. É provável que se sinta frequentemente frustrado com colegas, \nou até entes queridos por ter um “amortecedor” para lidar com situações e relacionamentos difíceis menos \ndesenvolvido.\n Comece a trabalhar o autoconhecimento. Entenda quais habilidades são mais difíceis para você - pode ser a \nempatia, receber críticas, ou social skills básicas - e pratique-as. Olhe também para o que você já faz de bom \ne procure entender como consegue, para aplicar seus métodos bem-sucedidos aos novos aprendizados.\n ")

elif score >=60 and score <=79:
    print("Seu score", name.upper, "é:", score, " : Bom nível de inteligência emocional. É bem provável que você seja sensível às emoções dos que estão \nao seu redor - colegas, amigos, familiares e clientes. Você também tem consciência sobre o efeito do seu \ncomportamento nos outros. \nEnquanto ser adepto a colocar as outras pessoas e suas necessidades a frente das suas é algo admirável, nem \nsempre é o melhor a se fazer. Não tenha medo de se comunicar honestamente e mostrar seus sentimentos, \ndesde que com habilidade. Este é um dos aspectos mais importantes para desenvolver a inteligência \nemocional. \n")

else: 
    print("Seu score", name.upper, "é:", score, " : Se seus resultados estão neste intervalo, há duas possibilidades: ou você tem um nível de inteligência \nemocional extremamente alto, ou baixíssimo. \nComo isso é possível? Esses resultados podem refletir elevado grau de autoconhecimento - neste caso, \nótimo! Mas não pare de buscar oportunidades de aprendizado. Ou, pelo contrário: podem ser consequência \nde uma grande falta de autoconhecimento, porque é preciso ser autoconsciente para se avaliar com precisão. \nA autoconsciência é a capacidade fundamental da inteligência emocional, porque ela reflete diretamente nas \noutras. É preciso ter noção sobre si próprio para mudar qualquer comportamento. Então, ou você chegou ao \ntopo, ou tem um longo caminho pela frente.\n")
                                              
#20-39 pontos: Você precisa trabalhar para desenvolver sua inteligência emocional. Apesar de sua sinceridade ser admirável,\n é provável que você se sinta sobrecarregado por suas emoções e lute para gerenciar emoções. Reagir a isso,\n explodindo, ou, pelo contrário, não expressando suas emoções, é igualmente prejudicial.\n Suas respostas às pressões comuns da vida podem estar baseadas no medo e na insegurança - em vez de \npaixão e propósito. No entanto, isto não precisa ser algo definitivo! A inteligência emocional não vem do\n nascimento: ela pode ser desenvolvida. \n\nTrabalhe sua autoconsciência, porque ela é o primeiro fundamento da inteligência emocional. Se parece muito \ndifícil, não hesite em pedir ajuda para quem você considera ter muito conhecimento relacionado a oferecer.\n A intenção de desenvolver a inteligência emocional é o primeiro – e mais importante – passo. \n

#40-59 pontos: Seu nível de inteligência emocional ainda é um pouco baixo. Você tem mais dificuldade nas situações que \nexigem mais habilidades de interação social. É provável que se sinta frequentemente frustrado com colegas, \nou até entes queridos por ter um “amortecedor” para lidar com situações e relacionamentos difíceis menos \ndesenvolvido.\n Comece a trabalhar o autoconhecimento. Entenda quais habilidades são mais difíceis para você - pode ser a \nempatia, receber críticas, ou social skills básicas - e pratique-as. Olhe também para o que você já faz de bom \ne procure entender como consegue, para aplicar seus métodos bem-sucedidos aos novos aprendizados.\n 

#60-79 pontos: Bom nível de inteligência emocional. É bem provável que você seja sensível às emoções dos que estão \nao seu redor - colegas, amigos, familiares e clientes. Você também tem consciência sobre o efeito do seu \ncomportamento nos outros. \nEnquanto ser adepto a colocar as outras pessoas e suas necessidades a frente das suas é algo admirável, nem \nsempre é o melhor a se fazer. Não tenha medo de se comunicar honestamente e mostrar seus sentimentos, \ndesde que com habilidade. Este é um dos aspectos mais importantes para desenvolver a inteligência \nemocional. \n

#80-100 pontos: Se seus resultados estão neste intervalo, há duas possibilidades: ou você tem um nível de inteligência \nemocional extremamente alto, ou baixíssimo. \nComo isso é possível? Esses resultados podem refletir elevado grau de autoconhecimento - neste caso, \nótimo! Mas não pare de buscar oportunidades de aprendizado. Ou, pelo contrário: podem ser consequência \nde uma grande falta de autoconhecimento, porque é preciso ser autoconsciente para se avaliar com precisão. \nA autoconsciência é a capacidade fundamental da inteligência emocional, porque ela reflete diretamente nas \noutras. É preciso ter noção sobre si próprio para mudar qualquer comportamento. Então, ou você chegou ao \ntopo, ou tem um longo caminho pela frente.\n
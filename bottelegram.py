import telebot


CHAVE_API ='5990689547:AAEZGVZz8RROMLIwF-U-vPcPI_tFQqE7g24'
bot = telebot.TeleBot(CHAVE_API) 


@bot.message_handler(commands=["pizza"])
def pizza(mensagem):
    bot.send_message(mensagem.chat.id, "Saindo sua pizza, tempo estimado de entrega em 20min")


@bot.message_handler(commands=["hamburguer"])
def hamburguer(mensagem):
    bot.send.mensagem(mensagem.chat.id, "Saindo o brabo: em 10min chega ai")


@bot.message_handler(commands=["salada"])
def salada(mensagem):
    bot.send_message(mensagem.chat.id, "Não tem salada não, Clique aqui para iniciar: /iniciar")



@bot.message_handler(commands=["opcao1"])
def opcao1(mensagem):
    texto = """
    O que vc quer? (Clique na opção):
    /pizza Pizza
    /hamburguer Hamburguer
    /salada Salada"""
    bot.send_message(mensagem.chat.id,texto)

@bot.message_handler(commands=["opcao2"])
def responder(mensagem):
    bot.send_message(mensagem.chat.id , "Para enviar uma reclamação entre em contato com o email: reclamacao@teste.com")


@bot.message_handler(commands=["opcao3"])
def responder(mensagem):
    bot.send_message(mensagem.chat.id, "Valeu!!!O lira mandou abraço de volta <3")




def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    
    texto = """
    Escolha uma opção para continuar (Clique no item):
    /opcao1 Fazer um pedido
    /opcao2 Reclamar de um pedido
    /opcao3 Mandar um abraço pro Lira
    Responder, qualquer outra coisa não vai funcionar, 
    Clique em uma das opções
"""
    bot.reply_to(mensagem, texto)

bot.polling()

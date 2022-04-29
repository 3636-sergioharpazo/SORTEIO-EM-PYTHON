
from tkinter import *
import random
import pyttsx3
from tkinter import messagebox
from telesign.messaging import MessagingClient



speaker = pyttsx3.init()  # inicia serviço biblioteca
voices = speaker.getProperty('voices')  # metodo de voz

#for voice in voices:
 #   print(voice, voice.id)  # traz os idiomas de voz instalados em sua maquina

speaker.setProperty('voice', voices[0].id)  # define a voz padrao, no meu caso o portugues era o[2] (iniciando do zero)
rate = speaker.getProperty('rate')
speaker.setProperty('rate', rate - 25)  # muda velocidade da leitura, quando menor mais lento
# escreve o texto na tela
def ganhador():

    with open('aluno.txt','r') as f:
        alunos = f.readlines()
   ##     print(f"O(a) ganhador(a) foi: {random.choice(alunos)}")
    aluno = random.choice(alunos)
    texto_resposta['text'] = f'''Ganhador(a): {aluno}'''
    ouvir = (f'O ganhador do sorteio é: {aluno}, Parabéns !')
    speaker.say(ouvir)  # define o texto que será lido
    speaker.runAndWait()
    f.close()  # fecha o modo deleitura do arquivo txt
    msg = ouvir
    EnviarSMS(msg,aluno)


def EnviarSMS(msg,aluno):
    customer_id = "COLOQUE AQUI O ID DO telesign"
    api_key = "COLOQUE AQUI O kye DO telesign"

    ## phone_number = "55" + txtNumero.get()
    phone_number = "seu telefone cadastrado e validado para receber o sms"
    message = msg
    message_type = "ARN"
    messaging = MessagingClient(customer_id, api_key)
    response = messaging.message(phone_number, message, message_type)
    if response.status_code == 200:
       ## messagebox.showinfo("success", "SMS Enviado Com Sucesso")
        speaker.say(f"{aluno}, Veja no celular do professor Antonio o Ganhador, eu mandei um SMS agora")  # define o texto que será lido
        speaker.runAndWait()
    else:
        messagebox.showerror("error", "Falha ao enviar SMS, Verifique o Numero é tente novamente")


janela = Tk()

janela.title("Sorteio")
texto = Label(janela, text="Clique no botão para saber  que é o ganhador(a)")
texto.grid(column=0, row=0, padx=20, pady=20)

botao = Button(janela, font='14',text="Saber Ganhador", command=ganhador)
botao.grid(column=0, row=1, padx=10, pady=10)

texto_resposta = Label(janela,font='20', text="")
texto_resposta.grid(column=0, row=0, padx=20, pady=20)


janela.mainloop()
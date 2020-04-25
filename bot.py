from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
#
# instance chatbot
chatbot = ChatBot('bot')
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train('chatterbot.corpus.portuguese')
trainerer = ListTrainer(chatbot)


dir_path = os.getcwd()
chrome_option2 = Options()
chrome_option2.add_argument(r"user-data-dir ="+dir_path+"/profile/wpp")


driver = webdriver.Chrome(dir_path+'/chromedriver.exe', chrome_options = chrome_option2)
driver.get('https://web.whatsapp.com/')
driver.implicitly_wait(15)

def take_the_chat():
    try:
        post = driver.find_element_by_class_name("_3zb-j")
        last = len(post)-1
        the_text = post[last].find_element_by_css_selector("span._3FXB1.selectable-text").text
        return the_text
    except:
        pass

def sendMessage(message):
    input_text = driver.find_element_by_class_name("_2S1VP")
    caixadetexto = driver.find_elements_by_xpath($0)
    respond = "*EU:*"+str(message)


    for part in respond.split("\n"):
        input_text.send_keys(part)
        # ActionChains.driver.send_keys
        ActionChains.driver.send_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.SHIFT).perfom()
    time.sleep(0.5)
    botton_send = driver.find_element_by_class_name("_35EW6")

    driver.find_element_by
    botton_send.click()
#
# treining message
def train(message):
    response = 'Como respondo isso? Me ensina com *//* e a resposta que devo aprender, ou ! para desactivar meu aprendizado'+str(message)
    sendText(response)
    novo = [] #add treining
    try:
        while True:
            last_message = take_the_chat()
            if last_message == "!":
                sendMessage("Voce desactivou meu aprendizado :'( ")
                break
            elif last_message.replace("//", "") != "" and last_message != message and last_message[0] == "//":
                auxiliar = last_message

                novo.append(message.lower().strip())
                novo.append(last_message.replace("//", "").strip())
                trainerer.train(novo)
                print(message.lower().strip())
                print(last_message.replace('//', '').strip())
                sendMessage("Aprendi com sucesso")
                break
    except:
        pass

salva = take_the_chat()

while True:
    try:
        if take_the_chat() != "" and take_the_chat()[:4] != "Eu: " and take_the_chat() != salva and take_the_chat() != "!" and take_the_chat() != "//":
            texto = str(take_the_chat().lower().strip())
            responder = chatbot.get_response(texto)
            if float(responde.confidence) < 0.5 :
                train(take_the_chat())
            else:
                sendMessage(resposta)
        else:
            pass
    except:
        pass

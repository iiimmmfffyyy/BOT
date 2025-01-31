import streamlit as st
#import webbrowser
#import subprocess
import googletrans
import pygame

mmm = googletrans.Translator()
pygame.init()
Hi = pygame.mixer.Sound('o-privet_NnF9NpL.mp3')
b = pygame.mixer.Sound('poka.mp3')
st.text("всем привет")
st.text("с вами ГУГЛ")
st.text("я чат бот")
st.text("!!!ВНИМАНИЕ!!!")
st.text("если чтото пойдёт не так пишыте STOP! Ок?")
st.text("о чом поговорим?")
st.text("если не знаете можите спросить")
st.text("(о чом можно поговарить)")
def qwe ():
    q = st.text_input("...")
    if q == "привет":
        st.text("привет! :)")
        Hi.play()
    elif q == "как тебя зовут?":
        st.text("меня зовут ГУГЛ")
    elif q == "кто ты?":
        st.text("я чат бот ГУГЛ!")
    elif q == "кто тебя создал?":
        st.text("меня создал Иван")
    elif q == "в какие игры играет твой создатель?":
        st.text("маенкравт,бравл старс,гениралы,рассвет нацый и многие другие!")
    elif q == "почему он дал тибе такое имя?":
        st.text("у него небыло времини выбират")
        st.text("что пришло в голову раньше то и выбрал.")
    elif q == "где ты жывёш?":
        st.text("здесь ;)")
    elif q == "что ты льубиш делать в менкравте больше всего?":
        st.text("я не играю в маен но мой создатель")
        st.text("лубит строить,выжывать,и тролить братьев")
    elif q == "сколько братьев у тваего создателя?":
        st.text("2 родных и 2 дваютодных")
    elif q == "учи.ру":
        st.link_button("учи.ру", "https://uchi.ru/profile/students/")
#    elif q == "маенкравт":
#        subprocess.run(r"C:\Users\Евгений\AppData\Roaming\.minecraft\TLauncher.exe")
    elif q == "что ты можеш?":
        st.text("ямогу перевести текст на английский - переведи на английский")
        st.text("или на туский - переведи на руский")
        st.text("я могу запустить,открыть:")
        st.text("TLauncher - маенкравт")
        st.text("учи.ру - учи.ру")
        st.text("рицэпт блинов - блины")
        st.text("рицэпт борща - борщ")
        st.text("рицэпт пиперони - пиперони")
        st.text("рицэпт пицы - пица")
        st.text("рицэпт ролов - ролы")
    elif q == "а ещё что?":
        st.text("а ещо я могу говорить :)")
    elif q == "а ещо?":
        st.text("а ещо я в разработке!")
    elif q == "о чом можно поговорить?":
        st.text("возможные запросы:")
        st.text("как тебя зовут?,кто ты?,кто тебя создал?")
        st.text("в какие игры играет твой создатель?")
        st.text("почему он дал тибе такое имя?,где ты жывёш?")
        st.text("что ты льубиш делать в менкравте больше всего?")
        st.text("сколько братьев у тваего создателя?")
        st.text("скажы а я повтарю")
        st.text("что ты можеш?")
        st.text("а ещё что?")
        st.text("а ещо?")
        st.text("а ещооо")
    elif q == "а ещооо":
        st.text("а ещооо ты надоел")
    elif q == "блины":
        st.link_button("блины", "https://yandex.ru/search?text=%D1%80%D0%B5%D1%86%D0%B5%D0%BF%D1%82+%D0%B1%D0%BB%D0%B8%D0%BD%D0%BE%D0%B2&clid=2411726&fyandex=1&lr=54")
    elif q == "борщ":
        st.link_button("борщ", "https://yandex.ru/search?text=%D1%80%D0%B5%D1%86%D0%B5%D0%BF%D1%82+%D0%B1%D0%BE%D1%80%D1%89%D0%B0&lr=54&clid=2411726&src=suggest_B&fyandex=1")
    elif q == "пиперони":
        st.link_button("пиперони", "https://yandex.ru/search?text=%D1%80%D0%B5%D1%86%D0%B5%D0%BF%D1%82+%D0%BF%D0%B5%D0%BF%D0%BF%D0%B5%D1%80%D0%BE%D0%BD%D0%B8&lr=54&clid=2411726&src=suggest_B&fyandex=1")
    elif q == "пица":
        st.link_button("пица", "https://yandex.ru/search?text=%D1%80%D0%B5%D1%86%D0%B5%D0%BF%D1%82+%D0%BF%D0%B8%D1%86%D1%86%D1%8B&lr=54&clid=2411726&fyandex=1")
    elif q == "ролы":
        st.link_button("ролы", "https://yandex.ru/search?text=%D1%80%D0%B5%D1%86%D0%B5%D0%BF%D1%82+%D1%80%D0%BE%D0%BB%D0%BB%D0%BE%D0%B2&lr=54&clid=2411726&src=suggest_B&fyandex=1")
    elif q == "звуки":
        st.link_button("звуки", "https://www.myinstants.com/ru/index/ru/")
    elif q == "сайты":
        st.link_button("паролль", "https://iiimmmfffyyy.streamlit.app/")
        st.link_button("звуки", "https://www.myinstants.com/ru/index/ru/")
        st.link_button("ролы", "https://yandex.ru/search?text=%D1%80%D0%B5%D1%86%D0%B5%D0%BF%D1%82+%D1%80%D0%BE%D0%BB%D0%BB%D0%BE%D0%B2&lr=54&clid=2411726&src=suggest_B&fyandex=1")
        st.link_button("пица", "https://yandex.ru/search?text=%D1%80%D0%B5%D1%86%D0%B5%D0%BF%D1%82+%D0%BF%D0%B8%D1%86%D1%86%D1%8B&lr=54&clid=2411726&fyandex=1")
        st.link_button("пиперони", "https://yandex.ru/search?text=%D1%80%D0%B5%D1%86%D0%B5%D0%BF%D1%82+%D0%BF%D0%B5%D0%BF%D0%BF%D0%B5%D1%80%D0%BE%D0%BD%D0%B8&lr=54&clid=2411726&src=suggest_B&fyandex=1")
        st.link_button("борщ", "https://yandex.ru/search?text=%D1%80%D0%B5%D1%86%D0%B5%D0%BF%D1%82+%D0%B1%D0%BE%D1%80%D1%89%D0%B0&lr=54&clid=2411726&src=suggest_B&fyandex=1")
        st.link_button("блины", "https://yandex.ru/search?text=%D1%80%D0%B5%D1%86%D0%B5%D0%BF%D1%82+%D0%B1%D0%BB%D0%B8%D0%BD%D0%BE%D0%B2&clid=2411726&fyandex=1&lr=54")
    elif q == "переведи на английский":
        def rty ():
            textSTART = st.text_input("ведите текст")
            textEND = mmm.translate(textSTART, dest='en')
            st.text(textEND.text)
        rty()
    elif q == "переведи на руский":
        def asd ():
            textSTART = st.text_input("ведите текст")
            textEND = mmm.translate(textSTART, dest='ru')
            st.text(textEND.text)
        asd()
    else:
        st.text("я не понимаю вас! возможно вы написали запрос с ошыпкой")
        st.text("или такого варианта нет.")
qwe()

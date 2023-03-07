from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
import random
from selenium.webdriver.common.keys import Keys

def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=1200,800', '--incognito']
    for argument in arguments:
        chrome_options.add_argument(argument)

    chrome_options.add_experimental_option('prefs', {
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1,

    })
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()), options=chrome_options)

    return driver

def type_equals_human(text,element):
    for word in text:
        element.send_keys(word)
        sleep(random.randint(1, 5)/30)

driver = iniciar_driver()

#driver.get('https://cursoautomacao.netlify.app/')

#ir até o site do facebook
driver.get('https://facebook.com/')
driver.maximize_window()
sleep(5)
#achar o campo de login e digitar o e-mail
login = driver.find_element(By.XPATH,"//input[@id='email']")
type_equals_human('belezaexplosao@gmail.com', login)
sleep(1)
#achar o campo de senha e digitar a senha
password = driver.find_element(By.XPATH, "//input[@id='pass']")
type_equals_human('teste123', password)
sleep(1)
#achar botao acessar
button_login = driver.find_element(By.XPATH,"//button[@name='login']")
button_login.click()
sleep(10)
#cicla no botão iniciar para confirma o local do post
pag = driver.find_element(By.XPATH,"//a[@aria-label='Página inicial']")
pag.click()
sleep(5)
#achar o campo de digitar o post
post = driver.find_element(By.XPATH,"//div[@class='x1i10hfl x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x16tdsg8 x1hl2dhg xggy1nq x87ps6o x1lku1pv x1a2a7pz x6s0dn4 xmjcpbm x107yiy2 xv8uw2v x1tfwpuw x2g32xy x78zum5 x1q0g3np x1iyjqo2 x1nhvcw1 x1n2onr6 xt7dq6l x1ba4aug x1y1aw1k xn6708d xwib8y2 x1ye3gou']")
post.click()
sleep(3)
#escrever o post
message = 'Quem não sabe o que quer, às vezes, perde o que tem, e às vezes descobre que perdeu exatamente o que queria ter.'
post2 = driver.find_element(By.XPATH,"//p[@class='xdj266r x11i5rnm xat24cr x1mh8g0r x16tdsg8']")
type_equals_human(message, post2)
sleep(3)
#publicar post
push = driver.find_element(By.XPATH,"//div[@class='x1n2onr6 x1ja2u2z x78zum5 x2lah0s xl56j7k x6s0dn4 xozqiw3 x1q0g3np xi112ho x17zwfj4 x585lrc x1403ito x972fbf xcfux6l x1qhh985 xm0m39n x9f619 xn6708d x1ye3gou xtvsq51 x1r1pt67']")
push.click()
sleep(2)

input('')
driver.close()
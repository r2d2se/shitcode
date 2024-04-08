import time, random, string,os

import sqlite3 as sq
import logging

from transliterate import translit
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import Select
from get_data_from_database import (
    family,
    name,
    surname,
    date,
    number_phone,
    gender,
    root,
    job_title,
    departament,
    id,
)

firefox_options = Options()
firefox_options.add_argument("--headless")
driver = webdriver.Firefox(options=firefox_options)


def perehod_na_str(link):
    driver.get(link)


# with open(txt_file, encoding="utf-8") as f:
# family = f.readline().split()
# name = f.readline().split()
# surname = f.readline().split()
# date = f.readline().split()
# number_phone = f.readline().split()
# job_title = f.readline().split()
# department = f.readline().split()
# gender = f.readline().split()
# root = f.readline().split()
# rabota = " ".join(job_title[1:10])
# interior_number = ""  # тут должен стоять номер октела, перезаписать
# root = " ".join(root[3:6])
# Читаем файл построчно и разбиваем на список из сторонней инфы и нужной [фамилия:значение]


def generate_password():
    alphabet = string.ascii_letters + string.digits
    generate_password = []
    generate_password += random.choice(string.ascii_letters)
    generate_password += random.choice(string.ascii_letters)
    generate_password += random.choice(string.digits)
    generate_password += random.choice(string.digits)
    generate_password += random.choice("!@#$&?")
    generate_password += random.choice("!@#$&?:")
    generate_password += random.choice(alphabet)
    generate_password += random.choice(alphabet)
    random.shuffle(generate_password)
    generate_password = "".join(
        generate_password
    )  # Лучшая генерация случайных паролей, настолько случайно, что нужно переделать(наверное)
    return generate_password


generate_password = generate_password()
mail_user_generate = translit(
    family + "." + name, "ru", reversed=True
)  # собираем почту из фамилии и имени
mail_user = str(mail_user_generate)
mail_user = mail_user.lower()
login_adm_mail = os.environ["LOGIN_ADM_MAIL"]
password_adm_mail = os.environ["PASSWORD_ADM_MAIL"]  # нужно будет передать в переменные окружения пароли и логины от админки или найти иной безопасный вариант
login_bit_adm = os.environ["LOGIN_ADM_BITRIX"]
password_adm_bitrix = os.environ["PASSWORD_ADM_BITRIX"]

time.sleep(5)
perehod_na_str("https://adm-ui.mail.autotracker.site")
email_form = driver.find_element(By.ID, "fUsername")
email_form.send_keys(login_adm_mail)
password_form = driver.find_element(By.ID, "fPassword")
password_form.send_keys(password_adm_mail)
button = driver.find_element(By.XPATH, "/html/body/div/div/div/form/div[4]/button")
button.click()
time.sleep(5)
perehod_na_str(
    "https://adm-ui.mail.autotracker.site/edit.php?table=mailbox&domain=stavtrack.ru"
)
time.sleep(5)
area_mail = driver.find_element(
    By.XPATH, "/html/body/div/form/div/div[2]/div[1]/div/input"
)
area_password = driver.find_element(
    By.XPATH, "/html/body/div/form/div/div[2]/div[3]/div/input"
)
area_apply_password = driver.find_element(
    By.XPATH, "/html/body/div/form/div/div[2]/div[4]/div/input"
)
area_mail.send_keys(mail_user_generate.lower())
area_password.send_keys(generate_password)
area_apply_password.send_keys(generate_password)
create_box = driver.find_element(
    By.XPATH, "/html/body/div/form/div/div[3]/div/div/input"
)

create_box.click()  # Создание почтового ящика
time.sleep(10)

perehod_na_str("https://portal.stavtrack.ru/bitrix/admin/user_admin.php?lang=ru")
driver.find_element(
    By.XPATH, "/html/body/div[1]/table/tbody/tr/td/form/div/div/div/div[3]/div[2]/input"
).send_keys(login_bit_adm)
driver.find_element(
    By.XPATH, "/html/body/div[1]/table/tbody/tr/td/form/div/div/div/div[4]/div[2]/input"
).send_keys(password_adm_bitrix)
driver.find_element(
    By.XPATH, "/html/body/div[1]/table/tbody/tr/td/form/div/div/div/div[4]/input"
).click()
time.sleep(5)

driver.find_element(By.XPATH, '//*[@id="tbl_user_search"]').send_keys(root)
time.sleep(5)

get_id = driver.find_element(
    By.XPATH,
    "/html/body/div[1]/table/tbody/tr[2]/td[2]/div/div[3]/div/form/div[2]/div[1]/div[6]/table/tbody/tr[2]/td[10]/div/span/a",
).text
perehod_na_str(
    f"https://portal.stavtrack.ru/bitrix/admin/user_edit.php?lang=ru&COPY_ID={get_id}]"
)
time.sleep(10)

driver.find_element(
    By.XPATH,
    "/html/body/table/tbody/tr[2]/td[2]/div/form/div/div[2]/div[1]/div[2]/table/tbody/tr[4]/td[2]/input",
).send_keys(Keys.CONTROL + "a", Keys.BACKSPACE)
driver.find_element(
    By.XPATH,
    "/html/body/table/tbody/tr[2]/td[2]/div/form/div/div[2]/div[1]/div[2]/table/tbody/tr[4]/td[2]/input",
).send_keys(name)

driver.find_element(
    By.XPATH,
    "/html/body/table/tbody/tr[2]/td[2]/div/form/div/div[2]/div[1]/div[2]/table/tbody/tr[5]/td[2]/input",
).send_keys(Keys.CONTROL + "a", Keys.BACKSPACE)
driver.find_element(
    By.XPATH,
    "/html/body/table/tbody/tr[2]/td[2]/div/form/div/div[2]/div[1]/div[2]/table/tbody/tr[5]/td[2]/input",
).send_keys(family)

driver.find_element(
    By.XPATH,
    "/html/body/table/tbody/tr[2]/td[2]/div/form/div/div[2]/div[1]/div[2]/table/tbody/tr[6]/td[2]/input",
).send_keys(Keys.CONTROL + "a", Keys.BACKSPACE)
driver.find_element(
    By.XPATH,
    "/html/body/table/tbody/tr[2]/td[2]/div/form/div/div[2]/div[1]/div[2]/table/tbody/tr[6]/td[2]/input",
).send_keys(surname)

driver.find_element(
    By.XPATH,
    "/html/body/table/tbody/tr[2]/td[2]/div/form/div/div[2]/div[1]/div[2]/table/tbody/tr[7]/td[2]/input",
).send_keys(Keys.CONTROL + "a", Keys.BACKSPACE)
driver.find_element(
    By.XPATH,
    "html/body/table/tbody/tr[2]/td[2]/div/form/div/div[2]/div[1]/div[2]/table/tbody/tr[7]/td[2]/input",
).send_keys(mail_user + "@stavtrack.ru")

driver.find_element(
    By.XPATH,
    "/html/body/table/tbody/tr[2]/td[2]/div/form/div/div[2]/div[1]/div[2]/table/tbody/tr[8]/td[2]/input",
).send_keys(Keys.CONTROL + "a", Keys.BACKSPACE)
driver.find_element(
    By.XPATH,
    "/html/body/table/tbody/tr[2]/td[2]/div/form/div/div[2]/div[1]/div[2]/table/tbody/tr[8]/td[2]/input",
).send_keys(mail_user + "@stavtrack.ru")

driver.find_element(
    By.XPATH,
    "/html/body/table/tbody/tr[2]/td[2]/div/form/div/div[2]/div[1]/div[2]/table/tbody/tr[10]/td[2]/input",
).send_keys(Keys.CONTROL + "a", Keys.BACKSPACE)
driver.find_element(
    By.XPATH,
    "/html/body/table/tbody/tr[2]/td[2]/div/form/div/div[2]/div[1]/div[2]/table/tbody/tr[10]/td[2]/input",
).send_keys(generate_password)

driver.find_element(
    By.XPATH,
    "/html/body/table/tbody/tr[2]/td[2]/div/form/div/div[2]/div[1]/div[2]/table/tbody/tr[11]/td[2]/input",
).send_keys(Keys.CONTROL + "a", Keys.BACKSPACE)
driver.find_element(
    By.XPATH,
    "/html/body/table/tbody/tr[2]/td[2]/div/form/div/div[2]/div[1]/div[2]/table/tbody/tr[11]/td[2]/input",
).send_keys(generate_password)
time.sleep(10)
driver.find_element(By.XPATH, '//*[@id="tab_cont_edit3"]').click()
time.sleep(3)
select_gender = Select(driver.find_element(By.NAME, "PERSONAL_GENDER"))
if gender == "👨‍🎓":
    select_gender.select_by_value("M")
elif gender == "👩‍🎓":
    select_gender.select_by_value("F")
else:
    select_gender.select_by_value("")

driver.find_element(
    By.XPATH,
    "/html/body/table/tbody/tr[2]/td[2]/div/form/div/div[2]/div[4]/div[2]/table/tbody/tr[5]/td[2]/div/input",
).send_keys(Keys.CONTROL + "a", Keys.BACKSPACE)
driver.find_element(
    By.XPATH,
    "/html/body/table/tbody/tr[2]/td[2]/div/form/div/div[2]/div[4]/div[2]/table/tbody/tr[5]/td[2]/div/input",
).send_keys(date)

driver.find_element(
    By.XPATH,
    "/html/body/table/tbody/tr[2]/td[2]/div/form/div/div[2]/div[4]/div[2]/table/tbody/tr[8]/td[2]/input",
).send_keys(Keys.CONTROL + "a", Keys.BACKSPACE)
driver.find_element(
    By.XPATH,
    "/html/body/table/tbody/tr[2]/td[2]/div/form/div/div[2]/div[4]/div[2]/table/tbody/tr[8]/td[2]/input",
).send_keys(number_phone)

driver.find_element(
    By.XPATH,
    "/html/body/table/tbody/tr[2]/td[2]/div/form/div/div[2]/div[4]/div[2]/table/tbody/tr[10]/td[2]/input",
).send_keys(Keys.CONTROL + "a", Keys.BACKSPACE)
driver.find_element(
    By.XPATH,
    "/html/body/table/tbody/tr[2]/td[2]/div/form/div/div[2]/div[4]/div[2]/table/tbody/tr[10]/td[2]/input",
).send_keys(number_phone)
driver.find_element(By.XPATH, '//*[@id="tab_cont_edit4"]').click()
time.sleep(5)

driver.find_element(
    By.XPATH,
    "/html/body/table/tbody/tr[2]/td[2]/div/form/div/div[2]/div[5]/div[2]/table/tbody/tr[3]/td[2]/input",
).send_keys(Keys.CONTROL + "a", Keys.BACKSPACE)

driver.find_element(
    By.XPATH,
    "/html/body/table/tbody/tr[2]/td[2]/div/form/div/div[2]/div[5]/div[2]/table/tbody/tr[3]/td[2]/input",
).send_keys(departament)

driver.find_element(
    By.XPATH,
    "/html/body/table/tbody/tr[2]/td[2]/div/form/div/div[2]/div[5]/div[2]/table/tbody/tr[4]/td[2]/input",
).send_keys(Keys.CONTROL + "a", Keys.BACKSPACE)
driver.find_element(
    By.XPATH,
    "/html/body/table/tbody/tr[2]/td[2]/div/form/div/div[2]/div[5]/div[2]/table/tbody/tr[4]/td[2]/input",
).send_keys(job_title)


driver.find_element(By.NAME, "WORK_PHONE").send_keys(Keys.CONTROL + "a", Keys.BACKSPACE)
driver.find_element(By.NAME, "WORK_PHONE").send_keys(number_phone)

driver.find_element(
    By.XPATH, "/html/body/table/tbody/tr[2]/td[2]/div/form/div/div[1]/span[13]"
).click()
time.sleep(5)

select_otdel = Select(driver.find_element(By.NAME, "UF_DEPARTMENT[]"))
select_otdel.select_by_value("4261")

driver.find_element(By.NAME, "UF_PHONE_INNER").send_keys(
    Keys.CONTROL + "a", Keys.BACKSPACE
)
driver.find_element(By.NAME, "UF_PHONE_INNER").send_keys("1111")

driver.find_element(By.NAME, "UF_EMPLOYMENT_DATE").send_keys(
    Keys.CONTROL + "a", Keys.BACKSPACE
)

driver.find_element(
    By.XPATH,
    "/html/body/table/tbody/tr[2]/td[2]/div/form/div/div[3]/div[13]/div[2]/table/tbody/tr[34]/td[2]/table/tbody/tr/td/input",
).send_keys(Keys.CONTROL + "a", Keys.BACKSPACE)

driver.find_element(
    By.XPATH,
    "/html/body/table/tbody/tr[2]/td[2]/div/form/div/div[3]/div[13]/div[2]/table/tbody/tr[35]/td[2]/table/tbody/tr/td/input",
).send_keys(Keys.CONTROL + "a", Keys.BACKSPACE)
driver.find_element(
    By.XPATH,
    "/html/body/table/tbody/tr[2]/td[2]/div/form/div/div[3]/div[13]/div[2]/table/tbody/tr[27]/td[2]/table/tbody/tr/td/input",
).send_keys(Keys.CONTROL + "a", Keys.BACKSPACE)

driver.find_element(By.NAME, "apply").click()
# создание юзверя в битриксе

driver.get("https://portal.stavtrack.ru")
time.sleep(5)
driver.find_element(By.ID, "bx-im-bar-search").click()
driver.find_element(
    By.XPATH,
    "/html/body/div[8]/div/div[1]/div/div/div[2]/div/div/div[2]/div[1]/div/input",
).send_keys("Краснобаева Валерия")
time.sleep(5)
driver.find_element(
    By.XPATH,
    "/html/body/div[8]/div/div[1]/div/div/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div[1]/div[2]/div/div[2]",
).click()
driver.find_element(By.CLASS_NAME, "bx-messenger-textarea-input").send_keys(
    mail_user
    + "@stavtrack.ru"
    + "\n"
    + generate_password
    + "\n"
    + "https://ui.mail.autotracker.site"
    + "\n"
    + "https://portal.stavtrack.ru"
)
driver.find_element(
    By.XPATH,
    "/html/body/div[8]/div/div[1]/div/div/div[2]/div/div/div[3]/div[6]/div[5]/div[5]/a",
).click()
# отправка логина и пароля в личку


logging.basicConfig(filename="app.log", level=logging.INFO)
logging.info(f"Учётка создана {id}")


driver.close()
driver.quit()

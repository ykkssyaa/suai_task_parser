from Task import Task

from selenium import webdriver as wd
from selenium.webdriver.edge.options import Options

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

log = "YOUR_LOGIN"
pas = "YOUR_PASSWORD"

edge_options = Options()
# edge_options.add_experimental_option("detach", True)
edge_options.add_argument("--headless")
browser = wd.Edge(options=edge_options)


def tasks() -> list[Task]:
    browser.get("https://pro.guap.ru/inside/student/tasks/")

    login = browser.find_element(By.ID, "username")
    login.send_keys(log)

    password = browser.find_element(By.ID, "password")
    password.send_keys(pas)

    browser.find_element(By.ID, "kc-login").click()

    wait = WebDriverWait(browser, timeout=5)

    elements_count_select = browser.find_element(By.NAME, 'perPage')
    wait.until(lambda d: elements_count_select.is_displayed())
    select = Select(elements_count_select)

    select.select_by_value("100")

    browser.implicitly_wait(200)
    browser.find_element(By.XPATH,
                         '//*[@id="inside_student_tasks_index"]/div[1]/div/button').click()
    browser.implicitly_wait(2)

    tasks_elems = browser.find_elements(By.CLASS_NAME, "odd")

    res = list()

    for task in tasks_elems:
        cols = task.find_elements(By.TAG_NAME, "td")

        new_task = Task(subject=cols[1].text,
                        number=cols[2].text,
                        name=cols[3].text,
                        typee=cols[6].text,
                        deadline=cols[7].text,
                        points=cols[5].text,
                        status=cols[4].text,
                        date=cols[8].text,
                        ref=cols[0].find_element(By.TAG_NAME, 'a').get_attribute("href"))

        res.append(new_task)

    return res

# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_add_contact(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        self.wd.implicitly_wait(60)
    
    def test_test_add_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.add_new_contact(wd, "middleName", "firstName", "lastName", "nickName",
                             "C:\\Users\\motoy\\Downloads\\Starinnyi-velosiped-s-bol1shim-perednim-kolesom.jpg",
                             "title", "company", "address", "homeTelephone", "mobileTelephone", "workTelephone",
                             "faxTelephone", "email1@email.com", "email2@email.com", "email3@email.com", "homepage.com",
                             23, 6, "1988", "1988", 5, 6, 5, "address2", "home", "notes")
        self.return_to_home_page(wd)
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def return_to_home_page(self, wd):
        wd.find_element_by_link_text("home").click()

    def add_new_contact(self, wd, middle_name, first_name, last_name, nick_name, image, title, company, address,
                        home_telephone, mobile_telephone, work_telephone, fax_telephone, email, email2, email3,
                        homepage, birth_date, birth_month, birth_year, anniversary_year, anniversary_day,
                        anniversary_month, group, address2, home, notes):
        wd.find_element_by_link_text("add new").click()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").send_keys(first_name)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").send_keys(middle_name)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").send_keys(last_name)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").send_keys(nick_name)
        wd.find_element_by_name("photo").send_keys(image)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").send_keys(title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").send_keys(company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").send_keys(address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").send_keys(home_telephone)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").send_keys(mobile_telephone)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").send_keys(work_telephone)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").send_keys(fax_telephone)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").send_keys(email)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").send_keys(email2)
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").send_keys(email3)
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").send_keys(homepage)
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option["+str(birth_date + 2) + "]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option["+str(birth_date + 2) + "]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option["+str(birth_month + 1) + "]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option["+str(birth_month + 1) + "]").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").send_keys(birth_year)
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option["+str(anniversary_day + 2) + "]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option["+str(anniversary_day + 2) + "]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option["+str(anniversary_month + 1) + "]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option["+str(anniversary_month + 1) + "]").click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").send_keys(anniversary_year)
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[5]//option["+str(group + 1) + "]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[5]//option["+str(group + 1) + "]").click()
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").send_keys(address2)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").send_keys(home)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").send_keys(notes)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def login(self, wd, username, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()

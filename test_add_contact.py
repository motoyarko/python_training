# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from contact import Contact

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
    
    def test_add_contact(self):
        wd = self.wd
        self.login(wd, username="admin", password="secret")
        self.add_new_contact(wd, Contact(middle_name="middleName", first_name="firstName", last_name="lastName", nick_name="nickName",
                             image="C:\\Users\\motoy\\Downloads\\Starinnyi-velosiped-s-bol1shim-perednim-kolesom.jpg",
                             title="title", company="company", address="address", home_telephone="homeTelephone", mobile_telephone="mobileTelephone",
                             work_telephone="workTelephone", fax_telephone="faxTelephone", email="email1@email.com",
                             email2="email2@email.com", email3="email3@email.com", homepage="homepage.com",
                             birth_date=23, birth_month=6, birth_year=1988, anniversary_year=1988, anniversary_day=5, anniversary_month=6,
                             group=5, address2="address2", home="home", notes="notes"))
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def return_to_home_page(self, wd):
        wd.find_element_by_link_text("home").click()

    def add_new_contact(self, wd, contact):
        self.return_to_home_page(wd)
        wd.find_element_by_link_text("add new").click()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").send_keys(contact.first_name)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").send_keys(contact.middle_name)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").send_keys(contact.last_name)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").send_keys(contact.nick_name)
        wd.find_element_by_name("photo").send_keys(contact.image)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").send_keys(contact.title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").send_keys(contact.home_telephone)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").send_keys(contact.mobile_telephone)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").send_keys(contact.work_telephone)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").send_keys(contact.fax_telephone)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").send_keys(contact.email)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").send_keys(contact.email2)
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").send_keys(contact.email3)
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").send_keys(contact.homepage)
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option["+str(contact.birth_date + 2) + "]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option["+str(contact.birth_date + 2) + "]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option["+str(contact.birth_month + 1) + "]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option["+str(contact.birth_month + 1) + "]").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").send_keys(contact.birth_year)
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option["+str(contact.anniversary_day + 2) + "]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option["+str(contact.anniversary_day + 2) + "]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option["+str(contact.anniversary_month + 1) + "]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option["+str(contact.anniversary_month + 1) + "]").click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").send_keys(contact.anniversary_year)
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[5]//option["+str(contact.group + 1) + "]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[5]//option["+str(contact.group + 1) + "]").click()
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").send_keys(contact.address2)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").send_keys(contact.home)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").send_keys(contact.notes)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def login(self, wd, username, password):
        self.open_home_page(wd)
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

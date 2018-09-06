
class ContactHelper:

    def __init__(self, app):
        self.app = app

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def create(self, contact):
        wd = self.app.wd
        self.return_to_home_page() # added for minimize risks. e.g. if user on other page
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.return_to_home_page() # added for minimize risks. e.g. if web application will be changed and user on other page

    def delete_first_contact(self):
        wd = self.app.wd
        self.return_to_home_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.return_to_home_page()

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.return_to_home_page() # added for minimize risks. e.g. if user on other page
        self.select_first_contact()
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_name("update").click()
        self.return_to_home_page()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.first_name)
        self.change_field_value("middlename", contact.middle_name)

        self.change_field_value("lastname", contact.last_name)

        self.change_field_value("nickname", contact.nick_name)

#        self.change_field_value("photo", contact.image)  need update "change_field_value" method
        if contact.image is not None:
            wd.find_element_by_name("photo").send_keys(contact.image)

        self.change_field_value("title", contact.title)

        self.change_field_value("company", contact.company)

        self.change_field_value("address", contact.address)

        self.change_field_value("home", contact.home_telephone)

        self.change_field_value("mobile", contact.mobile_telephone)

        self.change_field_value("work", contact.work_telephone)

        self.change_field_value("fax", contact.fax_telephone)

        self.change_field_value("email", contact.email)

        self.change_field_value("email2", contact.email2)

        self.change_field_value("email3", contact.email3)

        self.change_field_value("homepage", contact.homepage)

        if contact.birth_date is not None:
            if not wd.find_element_by_xpath(
                    "//div[@id='content']/form/select[1]//option[" + str(contact.birth_date + 2) + "]").is_selected():
                wd.find_element_by_xpath(
                    "//div[@id='content']/form/select[1]//option[" + str(contact.birth_date + 2) + "]").click()

        if contact.birth_month is not None:
            if not wd.find_element_by_xpath(
                    "//div[@id='content']/form/select[2]//option[" + str(contact.birth_month + 1) + "]").is_selected():
                wd.find_element_by_xpath(
                    "//div[@id='content']/form/select[2]//option[" + str(contact.birth_month + 1) + "]").click()

        self.change_field_value("byear", contact.birth_year)

        if contact.anniversary_day is not None:
            if not wd.find_element_by_xpath(
                    "//div[@id='content']/form/select[3]//option[" + str(contact.anniversary_day + 2) + "]").is_selected():
                wd.find_element_by_xpath(
                    "//div[@id='content']/form/select[3]//option[" + str(contact.anniversary_day + 2) + "]").click()

        if contact.anniversary_month is not None:
            if not wd.find_element_by_xpath(
                    "//div[@id='content']/form/select[4]//option[" + str(contact.anniversary_month + 1) + "]").is_selected():
                wd.find_element_by_xpath(
                    "//div[@id='content']/form/select[4]//option[" + str(contact.anniversary_month + 1) + "]").click()

        self.change_field_value("ayear", contact.anniversary_year)

        self.change_field_value("address2", contact.address2)

        self.change_field_value("phone2", contact.home)

        self.change_field_value("notes", contact.notes)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()

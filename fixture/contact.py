from model.contact import Contact
import re


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def return_to_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_name("Send e-Mail")) > 0):
            wd.find_element_by_link_text("home").click()

    def create(self, contact):
        wd = self.app.wd
        self.return_to_home_page() # added for minimize risks. e.g. if user on other page
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.return_to_home_page() # added for minimize risks. e.g. if web application will be changed and user on other page
        self.contact_cache = None

    def delete_first_contact(self):
        wd = self.app.wd
        self.return_to_home_page()
        self.select_contact_by_index(0)
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.return_to_home_page()
        self.contact_cache = None

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.return_to_home_page()
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.return_to_home_page()
        self.contact_cache = None

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.return_to_home_page() # added for minimize risks. e.g. if user on other page
        self.select_first_contact()
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_name("update").click()
        self.return_to_home_page()
        self.contact_cache = None

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.return_to_home_page() # added for minimize risks. e.g. if user on other page
        self.open_contact_to_edit_by_index(index)
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_name("update").click()
        self.return_to_home_page()
        self.contact_cache = None

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.first_name)
        self.change_field_value("middlename", contact.middle_name)

        self.change_field_value("lastname", contact.last_name)

        self.change_field_value("nickname", contact.nick_name)

        self.change_field_value("photo", contact.image)
#        if contact.image is not None:
#            wd.find_element_by_name("photo").send_keys(contact.image)

        self.change_field_value("company", contact.company)

        self.change_field_value("title", contact.title)

        self.change_field_value("address", contact.address)

        self.change_field_value("home", contact.home_telephone)

        self.change_field_value("mobile", contact.mobile_telephone)

        self.change_field_value("work", contact.work_telephone)

        self.change_field_value("fax", contact.fax_telephone)

        self.change_field_value("email", contact.email)

        self.change_field_value("email2", contact.email2)

        self.change_field_value("email3", contact.email3)

        self.change_field_value("homepage", contact.homepage)

        self.change_field_value("birth_date", contact.birth_date)
#        if contact.birth_date is not None:
#            if not wd.find_element_by_xpath(
#                    "//div[@id='content']/form/select[1]//option[" + str(contact.birth_date + 2) + "]").is_selected():
#                wd.find_element_by_xpath(
#                    "//div[@id='content']/form/select[1]//option[" + str(contact.birth_date + 2) + "]").click()

        self.change_field_value("birth_month", contact.birth_month)
#        if contact.birth_month is not None:
#            if not wd.find_element_by_xpath(
#                    "//div[@id='content']/form/select[2]//option[" + str(contact.birth_month + 1) + "]").is_selected():
#                wd.find_element_by_xpath(
#                    "//div[@id='content']/form/select[2]//option[" + str(contact.birth_month + 1) + "]").click()

        self.change_field_value("byear", contact.birth_year)

        self.change_field_value("anniversary_day", contact.anniversary_day)
#        if contact.anniversary_day is not None:
#            if not wd.find_element_by_xpath(
#                    "//div[@id='content']/form/select[3]//option[" + str(contact.anniversary_day + 2) + "]").is_selected():
#                wd.find_element_by_xpath(
#                    "//div[@id='content']/form/select[3]//option[" + str(contact.anniversary_day + 2) + "]").click()

        self.change_field_value("anniversary_month", contact.anniversary_month)
#        if contact.anniversary_month is not None:
#            if not wd.find_element_by_xpath(
#                    "//div[@id='content']/form/select[4]//option[" + str(contact.anniversary_month + 1) + "]").is_selected():
#                wd.find_element_by_xpath(
#                    "//div[@id='content']/form/select[4]//option[" + str(contact.anniversary_month + 1) + "]").click()

        self.change_field_value("ayear", contact.anniversary_year)

        self.change_field_value("address2", contact.address2)

        self.change_field_value("phone2", contact.home)

        self.change_field_value("notes", contact.notes)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if field_name is "photo":
            if text is not None:
                wd.find_element_by_name(field_name).send_keys(text)
                return
            else:
                return

        if field_name is "birth_date":
            if text is not None:
                if not wd.find_element_by_xpath(
                        "//div[@id='content']/form/select[1]//option[" + str(text + 2) + "]").is_selected():
                    wd.find_element_by_xpath(
                        "//div[@id='content']/form/select[1]//option[" + str(text + 2) + "]").click()

                return
            else:
                return

        if field_name is "birth_month":
            if text is not None:
                if not wd.find_element_by_xpath(
                        "//div[@id='content']/form/select[2]//option[" + str(text + 1) + "]").is_selected():
                    wd.find_element_by_xpath(
                        "//div[@id='content']/form/select[2]//option[" + str(text + 1) + "]").click()

                return
            else:
                return

        if field_name is "anniversary_day":
            if text is not None:
                if not wd.find_element_by_xpath(
                        "//div[@id='content']/form/select[3]//option[" + str(text + 2) + "]").is_selected():
                    wd.find_element_by_xpath(
                        "//div[@id='content']/form/select[3]//option[" + str(text + 2) + "]").click()
                return
            else:
                return

        if field_name is "anniversary_month":
            if text is not None:
                if not wd.find_element_by_xpath(
                        "//div[@id='content']/form/select[4]//option[" + str(text + 1) + "]").is_selected():
                    wd.find_element_by_xpath(
                        "//div[@id='content']/form/select[4]//option[" + str(text + 1) + "]").click()
                return
            else:
                return
# previous if-else constructions are needed because these fields are using xpath or custom update logic
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.select_contact_by_index(index)  # click on checkbox
        row = wd.find_elements_by_name("entry")[index]  # select needed row
        cell = row.find_elements_by_tag_name("td")[7]  # select column 8
        cell.find_element_by_tag_name("a").click()  # click on Pencil button

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def count(self):
        wd = self.app.wd
        self.return_to_home_page()
        return int(wd.find_element_by_id("search_count").text)

    contact_cache = None

    def get_contact_list(self):  # /!\this method works not correctly if contact doesn't have some fields on home page/!\
        if self.contact_cache is None:
            wd = self.app.wd
            self.return_to_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                td_tags = element.find_elements_by_tag_name("td")
                last_name = clear(td_tags[1].text)
                first_name = clear(td_tags[2].text)
                id = element.find_element_by_name("selected[]").get_attribute("value")
                all_phones = td_tags[5].text
                all_emails = td_tags[4].text
                address = clear(td_tags[3].text)
                self.contact_cache.append(Contact(first_name=first_name, last_name=last_name, id=id,
                                                  all_phones_from_home_page=all_phones,
                                                  all_emails_from_home_page=all_emails, address=address))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.app.open_home_page()  # it needs for case if system isn't on the home page
        self.open_contact_to_edit_by_index(index)
        first_name = wd.find_element_by_name("firstname").get_attribute("value")
        last_name = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        home_telephone = wd.find_element_by_name("home").get_attribute("value")
        mobile_telephone = wd.find_element_by_name("mobile").get_attribute("value")
        work_telephone = wd.find_element_by_name("work").get_attribute("value")
        home = wd.find_element_by_name("phone2").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(first_name=first_name, last_name=last_name, home_telephone=home_telephone,
                       mobile_telephone=mobile_telephone, work_telephone=work_telephone, home=home,
                       id=id, email=email, email2=email2, email3=email3)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_page_by_index(index)
        text = wd.find_element_by_id("content").text
        home_telephone = re.search("H: (.*)", text).group(1)
        mobile_telephone = re.search("M: (.*)", text).group(1)
        work_telephone = re.search("W: (.*)", text).group(1)
        home = re.search("P: (.*)", text).group(1)
        return Contact(home_telephone=home_telephone, mobile_telephone=mobile_telephone, work_telephone=work_telephone,
                       home=home)

    def open_contact_view_page_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()


# it's needed for cases when fields on home page contain " "
# but doesn't work for cases if e.g. first name contains double spaces, coz every new line on home page trims spaces
# at the beginning of each string.
# works in most cases but needs refactoring in the future
def clear(s):
    return s.strip().rstrip('\n ').rstrip('\n\r')

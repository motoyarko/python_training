import pymysql.cursors
from model.group import Group
from model.contact import Contact
from datetime import datetime


class DbFixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password)
        self.connection.autocommit(True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:  #photo in db looks strange - need to investigate
            cursor.execute("select  id, firstname, middlename, lastname, nickname, company, title, address, home, mobile, work, fax, email, email2, email3, homepage, bday, bmonth, byear, aday, amonth, ayear, address2, phone2, notes, photo, deprecated from addressbook")
            for row in cursor:
                (id, firstname, middlename, lastname, nickname, company, title, address, home, mobile, work, fax, email, email2, email3, homepage, bday, bmonth, byear, aday, amonth, ayear, address2, phone2, notes, photo, deprecated) = row
                if deprecated == "0000-00-00 00:00:00":  # this check later can be added to mysql request
                    list.append(Contact(middle_name=middlename, first_name=firstname, last_name=lastname, nick_name=nickname, image=photo, title=title, company=company, address=address,
                     home_telephone=home, mobile_telephone=mobile, work_telephone=work, fax_telephone=fax, email=email, email2=email2, email3=email3,
                     homepage=homepage, birth_date=bday, birth_month=bmonth, birth_year=byear, anniversary_year=ayear, anniversary_day=aday,
                     anniversary_month=amonth, group=None, address2=address2, home=home, notes=notes, id=id))
        finally:
            cursor.close()
        return list

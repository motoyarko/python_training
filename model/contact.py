from sys import maxsize


class Contact:
    def __init__(self, middle_name=None, first_name=None, last_name=None, nick_name=None, image=None, title=None, company=None, address=None,
                 home_telephone=None, mobile_telephone=None, work_telephone=None, fax_telephone=None, email=None, email2=None, email3=None,
                 homepage=None, birth_date=None, birth_month=None, birth_year=None, anniversary_year=None, anniversary_day=None,
                 anniversary_month=None, group=None, address2=None, home=None, notes=None, id=None, all_phones_from_home_page=None,
                 all_emails_from_home_page=None):
        self.middle_name = middle_name
        self.first_name = first_name
        self.last_name = last_name
        self.nick_name = nick_name
        self.image = image
        self.title = title
        self.company = company
        self.address = address
        self.home_telephone = home_telephone
        self.mobile_telephone = mobile_telephone
        self.work_telephone = work_telephone
        self.fax_telephone = fax_telephone
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.birth_date = birth_date
        self.birth_month = birth_month
        self.birth_year = birth_year
        self.anniversary_year = anniversary_year
        self.anniversary_day = anniversary_day
        self.anniversary_month = anniversary_month
        self.group = group
        self.address2 = address2
        self.home = home
        self.notes = notes
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.first_name, self.last_name)

    def __eq__(self, other): #The None check for name is needed for cases when we don't update first_name, last_name for contact
        return (self.id is None or other.id is None or self.id == other.id) and (self.first_name == other.first_name or self.first_name is None or other.first_name is None) and (self.last_name == other.last_name or self.last_name is None or other.last_name is None)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

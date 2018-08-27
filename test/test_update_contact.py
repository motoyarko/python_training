
from model.contact import Contact


def test_update_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.update_first_contact(Contact(middle_name="middleName_Updated", first_name="firstName_Updated", last_name="lastName_Updated", nick_name="nickName_Updated",
                       image="C:\\Users\\motoy\\Downloads\\Starinnyi-velosiped-s-bol1shim-perednim-kolesom.jpg",
                       title="title_Updated", company="company_Updated", address="address_Updated", home_telephone="homeTelephone_Updated", mobile_telephone="mobileTelephone_Updated",
                       work_telephone="workTelephone_Updated", fax_telephone="faxTelephone_Updated", email="email1_Updated@email.com",
                       email2="email2_Updated@email.com", email3="email3_Updated@email.com", homepage="homepage_Updated.com",
                       birth_date=24, birth_month=8, birth_year=1989, anniversary_year=1989, anniversary_day=6, anniversary_month=8,
                       group=4, address2="address2_Updated", home="home_Updated", notes="notes_Updated"))
    app.session.logout()
from model.contact import Contact


def test_modify_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="createdForUpdateContact"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(middle_name="middleName_Updated", first_name="firstName_Updated", last_name="lastName_Updated", nick_name="nickName_Updated",
                                             image="C:\\Users\\motoy\\Downloads\\Starinnyi-velosiped-s-bol1shim-perednim-kolesom.jpg",
                                             title="title_Updated", company="company_Updated", address="address_Updated", home_telephone="homeTelephone_Updated", mobile_telephone="mobileTelephone_Updated",
                                             work_telephone="workTelephone_Updated", fax_telephone="faxTelephone_Updated", email="email1_Updated@email.com",
                                             email2="email2_Updated@email.com", email3="email3_Updated@email.com", homepage="homepage_Updated.com",
                                             birth_date=24, birth_month=8, birth_year=1989, anniversary_year=1989, anniversary_day=6, anniversary_month=8,
                                             group=4, address2="address2_Updated", home="home_Updated", notes="notes_Updated"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_modify_contact_middle_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(middle_name="createdForUpdateContact"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(middle_name="middleName_Updated"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_modify_contact_first_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(last_name="createdForUpdateContact"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(first_name="firstName_Updated"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_modify_contact_anniversary_day(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(nick_name="createdForUpdateContact"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(anniversary_day=27))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)

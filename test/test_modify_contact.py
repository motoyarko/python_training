from model.contact import Contact
from random import randrange

def test_modify_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="createdForUpdateContact"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(middle_name="middleName_Updated", first_name="firstName_Updated", last_name="lastName_Updated", nick_name="nickName_Updated",
                                             image="C:\\Users\\motoy\\Downloads\\Starinnyi-velosiped-s-bol1shim-perednim-kolesom.jpg",
                                             title="title_Updated", company="company_Updated", address="address_Updated", home_telephone="homeTelephone_Updated", mobile_telephone="mobileTelephone_Updated",
                                             work_telephone="workTelephone_Updated", fax_telephone="faxTelephone_Updated", email="email1_Updated@email.com",
                                             email2="email2_Updated@email.com", email3="email3_Updated@email.com", homepage="homepage_Updated.com",
                                             birth_date=24, birth_month=8, birth_year=1989, anniversary_year=1989, anniversary_day=6, anniversary_month=8,
                                             group=4, address2="address2_Updated", home="home_Updated", notes="notes_Updated")
    contact.id = old_contacts[0].id
    app.contact.modify_first_contact(contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_modify_contact_middle_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(middle_name="middleName_Updated"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(middle_name="middleName_Updated")
    contact.id = old_contacts[0].id
    app.contact.modify_first_contact(contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_modify_contact_first_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="createdForUpdateContact"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(first_name="firstName_Updated")
    contact.id = old_contacts[0].id
    app.contact.modify_first_contact(contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_modify_contact_anniversary_day(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(anniversary_day=6))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(anniversary_day=6)
    contact.id = old_contacts[0].id
    app.contact.modify_first_contact(contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_modify_some_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(last_name="for random edit test"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(last_name="after random edit test")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
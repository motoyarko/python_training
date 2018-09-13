# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(middle_name="middleName", first_name="firstName", last_name="lastName", nick_name="nickName",
                       image="C:\\Users\\motoy\\Downloads\\Starinnyi-velosiped-s-bol1shim-perednim-kolesom.jpg",
                       title="title", company="company", address="address", home_telephone="homeTelephone", mobile_telephone="mobileTelephone",
                       work_telephone="workTelephone", fax_telephone="faxTelephone", email="email1@email.com",
                       email2="email2@email.com", email3="email3@email.com", homepage="homepage.com",
                       birth_date=24, birth_month=7, birth_year=1988, anniversary_year=1989, anniversary_day=2, anniversary_month=3,
                       group=5, address2="address2", home="home", notes="notes")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

# -*- coding: utf-8 -*-

from model.contact import Contact
import pytest
import random
import string


#  fuction can be updated with removing "string.punctuation" for more stable tests coz we have an error if contact
#  contains "'" symbol
def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(middle_name="", first_name="", last_name="", nick_name="",
                    image="",
                    title="", company="", address="", home_telephone="", mobile_telephone="",
                    work_telephone="", fax_telephone="", email="",
                    email2="", email3="", homepage="", birth_date=None, birth_month=None, birth_year=None,
                    anniversary_year=None, anniversary_day=None, anniversary_month=None, group=None, address2="", home="",
                    notes="")] + [
    Contact(middle_name=random_string("middle_name", 10),
            first_name=random_string("first_name", 20),
            last_name=random_string("last_name", 20),
            nick_name=random_string("nick_name", 20),
            title=random_string("title", 20),
            company=random_string("company", 20),
            address=random_string("address", 20),
            home_telephone=random_string("home_telephone", 20),
            mobile_telephone=random_string("mobile_telephone", 20),
            work_telephone=random_string("work_telephone", 20),
            fax_telephone=random_string("fax_telephone", 20),
            email=random_string("email", 20),
            email2=random_string("email2", 20),
            email3=random_string("email3", 20),
            birth_date=random.randrange(1, 31),
            birth_month=random.randrange(1, 12),
            birth_year=random.randrange(1, 3000),
            anniversary_year=random.randrange(1, 3000),
            anniversary_day=random.randrange(1, 31),
            anniversary_month=random.randrange(1, 12),
            address2=random_string("address2", 20),
            home=random_string("home", 20),
            notes=random_string("notes", 20),
            homepage=random_string("homepage", 20),
            image="C:\\Users\\motoy\\Downloads\\Starinnyi-velosiped-s-bol1shim-perednim-kolesom.jpg",
            group=5)
    for i in range(4)
    ]


# asert checks doesn't work for cases if e.g. first name contains double spaces, coz every new line on home page trims
# spaces at the beginning of each string.
# works in most cases but needs refactoring in the future
# also tests failed if fields contain special characters like "'", coz contact can't be created
@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

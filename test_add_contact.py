# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.add_new_contact(Contact(middle_name="middleName", first_name="firstName", last_name="lastName", nick_name="nickName",
                             image="C:\\Users\\motoy\\Downloads\\Starinnyi-velosiped-s-bol1shim-perednim-kolesom.jpg",
                             title="title", company="company", address="address", home_telephone="homeTelephone", mobile_telephone="mobileTelephone",
                             work_telephone="workTelephone", fax_telephone="faxTelephone", email="email1@email.com",
                             email2="email2@email.com", email3="email3@email.com", homepage="homepage.com",
                             birth_date=23, birth_month=6, birth_year=1988, anniversary_year=1988, anniversary_day=5, anniversary_month=6,
                             group=5, address2="address2", home="home", notes="notes"))
    app.return_to_home_page()
    app.logout()

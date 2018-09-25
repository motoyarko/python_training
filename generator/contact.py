import string
import random
from model.contact import Contact
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


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
    for i in range(5)
    ]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)
with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
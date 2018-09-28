from model.group import Group
from random import randrange
#import random


def test_modify_some_group_db(app, db, check_ui):
    if app.group.count() == 0:
        app.group.create(Group(name="createdForModify"))
    old_groups = db.get_group_list()
    index = randrange(len(old_groups))  # maybe it's possible to do tests without index and use old_groups.remove(old_group) then old_groups.append(group_new_data). anyway, we use assert with sorted lists. but need to check later.
    group_old = old_groups[index]
    group_new_data = Group(name="New group updated1olala", id=group_old.id)
    app.group.modify_group_by_id(group_old.id, group_new_data)
    new_groups = db.get_group_list()
    old_groups[index] = group_new_data
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

# need to check what is wrong in this implementation
# def test_temp_bd(app, db, check_ui):
#     if app.contact.count() == 0:
#         app.contact.create(Group(name="for random edit test"))
#     group = Group(name="after random edit test_DB")
#     old_groups = db.get_group_list()
#     random_group = random.choice(old_groups)
#     old_groups.remove(random_group)
#     group.id = random_group.id
#     app.group.modify_group_by_id(random_group.id, group)
#     new_contacts = db.get_contact_list()
#     old_groups.append(group)
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_contacts, key=Group.id_or_max)
#     if check_ui:
#         assert sorted(old_groups, key=Group.id_or_max) == sorted(app.contact.get_contact_list(), key=Group.id_or_max)


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="createdForModify"))
    old_groups = app.group.get_group_list()
    group = Group(name="New group updated1")
    group.id = old_groups[0].id
    app.group.modify_first_group(group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(header="createdForModify"))
    old_groups = app.group.get_group_list()
    group = Group(header="New group header updated1")
    group.id = old_groups[0].id
    app.group.modify_first_group(group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_modify_group_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(footer="createdForModify"))
    old_groups = app.group.get_group_list()
    group = Group(footer="New group updated1")
    group.id = old_groups[0].id
    app.group.modify_first_group(group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_modify_some_group(app):
    if app.group.count() == 0:
        app.group.create(Group(footer="createdForModify"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(footer="New group updated1")
    group.id = old_groups[index].id
    app.group.modify_group_by_index(index, group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
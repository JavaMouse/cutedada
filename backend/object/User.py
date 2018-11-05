# coding=utf-8

class User(object):

    def __init__(self,
                 username=None,
                 password=None,
                 nickname=None,
                 is_admin=0
                 ):
        self.username = username
        self.password = password
        self.nickname = nickname
        self.is_admin = is_admin

    def __str__(self):
        return "User:{username=%s,nickname=%s,is_admin=%d}" % (self.username or '',self.nickname or '',self.is_admin)


# coding=utf-8

class User(object):

    def __init__(self,
                id=None,
                 username=None,
                 password=None,
                 nickname=None,
                 group_id=None,
                 avatar=None,
                 ):
        self.id = id,
        self.username = username
        self.password = password
        self.nickname = nickname
        self.group_id = group_id
        self.avatar = avatar

    def __str__(self):
        return "User:{username=%s,nickname=%s,group_id=%d}" % (self.username or '',self.nickname or "",self.group_id)


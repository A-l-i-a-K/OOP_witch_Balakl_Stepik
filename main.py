class Viber():

    mess = {}

    @classmethod
    def add_message(cls, msg):
        cls.mess[id(msg)] = msg

    @classmethod
    def remove_message(cls, msg):
        if id(msg) in cls.mess:
            cls.mess.pop(id(msg))

    @classmethod
    def set_like(cls, msg):
        if id(msg) in cls.mess:
            msg.fl_like = not msg.fl_like


    @classmethod
    def show_last_message(cls, num):
        for m in tuple(cls.mess.values())[-num:]:
            print(m)

    @classmethod
    def total_messages(cls):
        return len(cls.mess)

class Message():
    def __init__(self, text, fl_like=False):
        self.text = text
        self.fl_like = fl_like

msg = Message("Всем привет!")
Viber.add_message(msg)
Viber.add_message(Message("Это курс по Python ООП."))
Viber.add_message(Message("Что вы о нем думаете?"))
Viber.add_message(Message("1Что вы о нем думаете?"))
Viber.add_message(Message("2Что вы о нем думаете?"))
Viber.add_message(Message("3Что вы о нем думаете?"))
Viber.set_like(msg)
Viber.remove_message(msg)


print(Viber.show_last_message(1))
print(Viber.total_messages())



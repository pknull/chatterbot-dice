from __future__ import unicode_literals
from chatterbot.logic.logic_adapter import LogicAdapter
from dice_roller.DiceThrower import DiceThrower


class RollAdapter(LogicAdapter):

    def __init__(self, **kwargs):
        super(RollAdapter, self).__init__(**kwargs)

    def process(self, statement):
        from chatterbot.conversation import Statement

        word_list = statement.text.split()
        try:
            if word_list[0].lower() == 'roll':
                dice = DiceThrower()
                result = dice.throw(word_list[1])
            else:
                return 0, Statement('')

            if result:
                return 1, Statement(result)
            else:
                return 0, Statement('')
        except Exception as inst:
            print('ouch')
            print(type(inst))
            print(inst)
            return 0, Statement('')
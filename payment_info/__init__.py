from otree.api import *
import random



doc = """
This application provides a webpage instructing participants how to get paid.
Examples are given for the lab and Amazon Mechanical Turk (AMT).
"""


class C(BaseConstants):
    NAME_IN_URL = 'payment_info'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    finishCode = models.IntegerField()
    pass


# FUNCTIONS
# PAGES
class PaymentInfo(Page):
    form_model = 'player'
    form_fields = ['finishCode']

    @staticmethod
    def vars_for_template(player: Player):
        participant = player.participant
        player.finishCode = random.randint(100000, 999999)
        return dict(redemption_code=participant.label or participant.code,
                    finishCode=player.finishCode
                    )
    
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.finished = True


page_sequence = [PaymentInfo]

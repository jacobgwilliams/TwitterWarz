import random

def determine_outcome(attack, defense):
    if len(attack) > len(defense):
        return "attacker wins"
    else:
        return "defender wins"

def battle(attacker, defender):
    result = Battle(attacker_id = attacker.id, defender_id = defender.id)
    a_twammo = attacker.tweet_set.all()
    d_twammo = defender.tweet_set.all()
    attack_obj = random.choice(a_twammo)
    defense_obj = random.choice(d_twammo)
    attack = attack_obj.content
    defense = defense_obj.content
    if determine_outcome(attack, defense) == "attacker wins":
        result.winner_id = attacker.id
        result.loser_id = defender.id
        result.save()
        print "attacker wins"
        print(attacker.twitter_handle)
    else:
        result.winner_id = defender.id
        result.loser_id = attacker.id
        result.save()
        print "defense wins"
        print(defender.twitter_handle)
    attack_obj.delete()
    defense_obj.delete()

def personal_record(user):
    wins = 0
    losses = 0
    for battle in Battle.objects.all():
        if battle.winner_id == user.id:
            wins += 1
        if battle.loser_id == user.id:
            losses += 1
    print "Record for:"
    print user.twitter_handle
    print "Wins: {kwarg} Losses: {kwang}!".format(kwarg=wins, kwang=losses)

def view_twammo(user):
    print user.tweet_set.count()

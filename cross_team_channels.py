from flask import Flask, request
import hashlib
import requests

app = Flask(__name__)


def link(teams, form):
    """
    Code that handles linking the messages between the teams
    :param teams: Dict with the team name as the key, and the incoming webhook as the valule. IE:
    {"team1" => "https://hooks.slack.com/services/teamid/someid/token",
    "team2" => "https://hooks.slack.com/services/teamid/someid/token"}
    :param form: The webhook data from slack, from request.form
    :return: Error message if invalid team, otherwise an empty reply
    """
    message = dict((key, form[key]) for key in form.keys())
    if message['team_domain'] not in list(teams.keys()):
        return "Your team is not configured. Please contact an Admin"
    elif message['user_id'] == "USLACKBOT":
        return ('', 204)
    else:
        for team in teams:
            if team != message["team_domain"]:
                hash = hashlib.sha224(message['user_id'].encode()).hexdigest()
                payload = {
                    "text": message["text"],
                    "icon_url": "http://www.gravatar.com/avatar/{0}?d=retro".format(hash),
                    "username": "{0} - {1}".format(message["username"], message["team_domain"])
                }
                requests.post(teams[team], json=payload)
        return ('', 204)

"""
Template for making this work. App route and the name of the view is up to you.
@app.route('/cross_team/', methods=["POST"])
def cross_team():
    teams = {
        "team1_domain": "https://hooks.slack.com/services/URL/TO/WEBHOOK_1",
        "team2_domain": "https://hooks.slack.com/services/URL/TO/WEBHOOK_2"
    }
    return link(teams, request.form)
"""

if __name__ == '__main__':
    app.run()

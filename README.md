# Cross Team Channels
A simple flask app designed to allow for cross team communication using the popular Slack chat platform.

## Usage

Create a view method within the flask app using the following template.
```python
@app.route('/cross_team/', methods=["POST"])
def cross_team():
    teams = {
        "team1_domain": "https://hooks.slack.com/services/URL/TO/WEBHOOK_1",
        "team2_domain": "https://hooks.slack.com/services/URL/TO/WEBHOOK_2"
    }
    message = dict((key, request.form[key]) for key in request.form.keys())
    return link(teams, request.form)
```

If you want to link more than two slack teams you can add in more values to the dictionary.


## Requirements

 - requests
 - flask

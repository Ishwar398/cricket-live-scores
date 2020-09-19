from flask import Flask, request, render_template
from werkzeug.exceptions import Forbidden, HTTPException, NotFound, RequestTimeout, Unauthorized
from pycricbuzz import Cricbuzz
import json

c=Cricbuzz()
app = Flask(__name__)


@app.route("/GetMatchDetails",methods=['POST'])
def GetMatchDetails():
    matchId=request.form.get('matchId')
    jsonObj_matchInfo = c.matchinfo(matchId)
    return {'success':True,'data':jsonObj_matchInfo}, 200, {'ContentType':'application/json'} 

@app.route("/GetMatchLiveScore",methods=['POST'])
def GetMatchLiveScore():
    matchId=request.form.get('matchId')
    jsonObj_matchLiveScore = c.livescore(matchId)
    return {'success':True,'data':jsonObj_matchLiveScore}, 200, {'ContentType':'application/json'} 

@app.route("/GetMatchScoreCard",methods=['POST'])
def GetMatchScoreCard():
    matchId=request.form.get('matchId')
    jsonObj_matchScoreCard = c.scorecard(matchId)
    return {'success':True,'data':jsonObj_matchScoreCard}, 200, {'ContentType':'application/json'} 

@app.route("/GetMatchCommentry",methods=['POST'])
def GetMatchCommentry():
    matchId=request.form.get('matchId')
    jsonObj_matchCommentry = c.commentary(matchId)
    return {'success':True,'data':jsonObj_matchCommentry}, 200, {'ContentType':'application/json'} 

@app.route("/GetOnGoingMatches",methods=['POST'])
def GetOnGoingMatches():
    matches = c.matches()
    return {'success':True,'data':matches}, 200, {'ContentType':'application/json'} 

@app.errorhandler(NotFound)
def page_not_found_handler(e: HTTPException):
    return render_template('404.html'), 404


@app.errorhandler(Unauthorized)
def unauthorized_handler(e: HTTPException):
    return render_template('401.html'), 401


@app.errorhandler(Forbidden)
def forbidden_handler(e: HTTPException):
    return render_template('403.html'), 403


@app.errorhandler(RequestTimeout)
def request_timeout_handler(e: HTTPException):
    return render_template('408.html'), 408


app.run()



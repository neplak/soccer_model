from flask import Flask, request, render_template,redirect,url_for
import jinja2
from soccer import Game,Team, TeamFromDict
from forms import TeamForm
from loadsave import loadTeams,saveTeams
from shcedule import GameSchedule, pfg, pfg111
import json

teamList=[]
schedule=None


app=Flask(__name__)
app.config['SECRET_KEY']='my super secret key'
app.config['UPLOAD_FOLDER']='data'

@app.route("/")
def index():
    messages=None
    try:
        messages = request.args['messages']
    except:
        pass
    if not messages:
        messages="No errors were sent"
    return render_template('index.jinja2',heading='Title',version='1.0.0',teamlist=teamList,messages=messages)

@app.route("/restart")
def restart():
    global schedule
    global teamList
    schedule=None
    teamList=[]
    return redirect(url_for('index',messages="Restarted"))

@app.route("/teamlist")
def displayTeamlist():
    return render_template('teamlist.jinja2',teamlist=teamList)

@app.route('/team',methods=['GET','POST'])
def teamCreate():
    form=TeamForm()
    if form.validate_on_submit():
        teamList.append(Team(form.name.data,form.location.data,form.force.data))
        return redirect(url_for('displayTeamlist'))
    return render_template('team.jinja2',form=form)


@app.route('/editteam/<teamnumber>', methods=['GET', 'POST'])
def editTeam(teamnumber):
    try:
        tn=int(teamnumber)
    except:
        return redirect(url_for('index',messages="Team number must be integer"))
    
    if tn>=len(teamList):
        return redirect(url_for('index', messages="Team number too big"))
    team=teamList[tn]
    form=TeamForm(obj=team)
    if form.validate_on_submit():
        form.populate_obj(teamList[tn])
        #teamList[tn]=Team(team.name,team.location,team.force)
        return redirect(url_for('displayTeamlist'))
    return render_template('team.jinja2', form=form)

@app.route('/teamlist/load', methods=['GET', 'POST'])
def loadTeamList():
    global teamList
    #tl=loadTeams('data/rfpl.json')
    teamList = loadTeams('data/rfpl.json')
    return redirect(url_for('displayTeamlist'))

@app.route('/teamlist/save', methods=['GET', 'POST'])
def saveTeamList():
    global teamList
    #tl=loadTeams('data/rfpl.json')
    saveTeams('data/rfpl.json',teamList)
    return redirect(url_for('displayTeamlist'))

@app.route('/schedule', methods=['GET', 'POST'])
def generateSchedule():
    global schedule
    global teamList
    if len(teamList)<2:
        return redirect(url_for('index', messages="Not enough teams for generating schedule. Add more teams"))
    if not schedule:
        schedule=GameSchedule(teamList)
        schedule.generateRound()
    return render_template('schedule.jinja2',schedule=schedule)


@app.route('/playTour', methods=['GET', 'POST'])
def playTour():
    global schedule
    if not schedule:
        return redirect(url_for('index', messages="No schedule!"))
    schedule.nextTour()
    return redirect(url_for('gamesResults'))
    

@app.route('/results', methods=['GET', 'POST'])
def gamesResults():
    global schedule
    if not schedule:
        return redirect(url_for('index',messages="Not created schedule yet"))
    if not schedule.toursPlayed:
        return redirect(url_for('index', messages="None games played yet"))
    view=request.args.get('view')
    if view=='a':
        return render_template('results-a.jinja2',gameschedule=schedule)
    else:
        return render_template('results.jinja2', gameschedule=schedule)



@app.route('/table', methods=['GET', 'POST'])
def tournamentTable():
    global schedule
    if not schedule:
        return redirect(url_for('index', messages="Not created schedule yet"))
    if not schedule.toursPlayed:
        return redirect(url_for('index', messages="None games played yet"))
    return render_template('TournamentTable.jinja2', ttable=schedule.currentTable(pfg111))

if __name__ == "__main__":
    app.run(debug=True,port=8080)

from models import Intent, IntentMessage, Template, Story, StoryStep, Slot, Action, db
from flask import Flask, render_template, request
import os


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db.init_app(app)


########## Creating a sample intent 
#db.create_all()

# nameInt = Intent(name="greet")
# db.session.add(nameInt)
# db.session.commit()


# intentId = Intent.query.filter_by(name='greet').first().id

# mess1 = IntentMessage(message = "Hello", intent_id = intentId)
# mess2 = IntentMessage(message = "Hey",  intent_id = intentId)

# db.session.add(mess1)
# db.session.add(mess2)
# db.session.commit()


##Creating a text template
# greetTemplate = Template(text = "I am Stark. I love you 3000", name="Welcome greeting")
# db.session.add(greetTemplate)
# db.session.commit()





## Creating a story
# greetStory = Story(name = "Greeting story")
# db.session.add(greetStory)
# db.session.commit()

# storyId = Story.query.filter_by(name = "Greeting story").first().id

# a = StoryStep(isIntent = True,story_id =  storyId    ,  int_or_temp_id = Intent.query.filter_by(name='greet').first().id)

# b = StoryStep(isIntent = False,story_id =  storyId    ,  int_or_temp_id = Template.query.filter_by(name='Welcome greeting').first().id)


# db.session.add(a)
# db.session.add(b)
# db.session.commit()

@app.route('/')
def hello_world():
   return render_template("home.html")


@app.route('/viewIntents')
def viewIntents():
	intents = Intent.query.all()
	return render_template("viewIntents.html", intents=intents)


@app.route('/getIntentDetails/<int:intentId>')
def showIntentDetails(intentId):
	intent_obj = Intent.query.filter_by(id=intentId).first()
	intent_name = intent_obj.name

	messages = []

	for m in IntentMessage.query.filter_by(intent_id = intentId).all():
		messages.append(m.message)
	return render_template("intent_detail.html", intent_name=intent_name, messages = messages)


@app.route("/viewStories")
def showStories():
	stories = Story.query.all()
	return render_template("viewStories.html", stories=stories)



@app.route("/getStoryDetails/<storyName>/<int:storyId>")
def showStoryDetails(storyName, storyId):
	story_steps = StoryStep.query.filter_by(story_id=storyId).all()
	m = []
	for x in story_steps:
		if(x.isIntent == 1):
			m.append("Intent *" + Intent.query.filter_by(id = x.int_or_temp_id).first().name)
		elif(x.isIntent == 2):
			m.append("--------- Text: "+Template.query.filter_by(id=x.int_or_temp_id).first().name)
		else:
			m.append('--------- Action: ' + Action.query.filter_by(id=x.int_or_temp_id).first().name)


	return render_template("story_detail.html", storyName=storyName, story_steps=story_steps, m=m)

@app.route("/showFacts")
def showFacts():

	facts = []

	intents = Intent.query.all()
	
	for intent in intents:
		if(intent.isFact):
			target = Template.query.filter_by(id=intent.templateId).first().text
			facts.append(intent.name +" >>> " + target)

	return render_template("showFacts.html", facts=facts)


@app.route('/viewTemplates')
def showTemplates():

	templates = Template.query.all()
	return render_template("showTemplates.html", templates=templates)



@app.route('/newIntent')
def newIntent():
	return render_template("newIntent.html")

@app.route('/createIntent', methods = ['POST'])
def createIntent():
	rowcount = int(request.form['rowcount'])
	intent_name = request.form['intent_name']
	if(len(intent_name)!=0):
		intObj = Intent(name=intent_name, isFact = False, templateId = -1)
		db.session.add(intObj)
		db.session.commit()

		intentId = Intent.query.filter_by(name=intent_name).first().id
		
		for i in range(rowcount):
			mess = request.form['message' + str(i)]
			if(len(mess)!=0):
				temp = IntentMessage(message=mess, intent_id = intentId)
				db.session.add(temp)
				db.session.commit()
			else:
				continue
		return render_template("success.html", message="Intent created successfully")
	else:

		return render_template("success.html", message="Dont leave the intent name blank")



@app.route("/newTemplate")
def newTemplate():
	return render_template("newTemplate.html")

@app.route("/createTemplate", methods=['POST'])
def createTemplate():
	try:
		temp_name = request.form['temp_name']
		temp_text = request.form['temp_text']
		temp_obj = Template(name=temp_name, text = temp_text)
		db.session.add(temp_obj)
		db.session.commit()
		return render_template("success.html", message="Template created successfully")
	except Exception as msg:
		return render_template("success.html", message=str(msg))

@app.route("/newStory")
def newStory():
	intents = Intent.query.all()
	templates = Template.query.all()
	actions = Action.query.all()

	return render_template("newStory.html", intents = intents, templates=templates, actions=actions)


# जन्मदिन मुबारक नयाज़ भाई

	
@app.route('/createStory', methods=['POST'])
def createStory():
	story_name = request.form['story_name']
	rowcount = request.form['rowcount']

	story_obj = Story(name=story_name)
	db.session.add(story_obj)
	db.session.commit()
	story_obj_id = Story.query.filter_by(name = story_name).first().id

	for i in range(int(rowcount)):
		foo = request.form['row' + str(i)]
		if(foo.split()[0] == 'intent'):
			foobar = StoryStep(isIntent=1, story_id=story_obj_id, int_or_temp_id = int(foo.split()[1]))
			db.session.add(foobar)
			db.session.commit()
		elif(foo.split()[0] == 'template'):
			foobar = StoryStep(isIntent=2, story_id=story_obj_id, int_or_temp_id = int(foo.split()[1]))
			db.session.add(foobar)
			db.session.commit()
		else:
			foobar = StoryStep(isIntent=3, story_id=story_obj_id, int_or_temp_id = int(foo.split()[1]))
			db.session.add(foobar)
			db.session.commit()

	return render_template("success.html", message="Story created")





@app.route('/newFact')
def newFact():
	intents = Intent.query.all()
	templates = Template.query.all()




	return render_template("newFact.html", intents = intents, templates=templates)


@app.route('/createFact', methods=['POST'])
def createFact():

	intent_id = int(request.form['row0'].split()[1])
	template_id = int(request.form['row1'].split()[1])

	intentObj = Intent.query.filter_by(id = intent_id).first()
	intentObj.isFact = True
	intentObj.templateId = template_id

	db.session.commit()



	return render_template("success.html", message="Added fact to DB")

@app.route("/newSlot")
def newSlot():
	return render_template("newSlot.html")


@app.route("/createSlot", methods=["POST"])
def createSlot():
	slot_name = request.form['slot_name']
	slot_type = request.form['slot_type']
	slot_obj = Slot(name=slot_name, type_slot = slot_type)
	db.session.add(slot_obj)
	db.session.commit()

	return render_template("success.html", message="Added slot to DB")


def convertNameToCamel(name):
	res = name[0].upper()
	convert = False
	for c in name[1:]:
		if(c == "_"):
			convert = True
			continue
		else:
			if(convert):
				res += c.upper()
				convert = False
			else:
				res += c
	return res



@app.route("/newAction")
def newAction():
	return render_template("newAction.html")


@app.route("/createAction", methods=["POST"])
def createAction():
	action_name = "action_" + request.form['action_name']
	actionObj = Action(name=action_name)
	conv_action_name = convertNameToCamel(action_name)
	code_content = '''
class %s(Action):

    def name(self) -> Text:
        return "%s"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        #use tracker.get_slot to retrieve slot values if they are set
        #foo = tracker.get_slot('your_slot_name')

        #use dispatcher.utter_message to return the message the chatbot should output
        dispatcher.utter_message("Hello World!")

        return []
'''%(conv_action_name, action_name)
	f = open("actions.py", "a")
	f.write(code_content)
	f.close()

	db.session.add(actionObj)
	db.session.commit()

	return render_template("success.html", message="Action created. Open actions.py to add custom code.")
    



@app.route('/train')
def train():

	f = open("data/nlu.md", "w")
	all_intents = Intent.query.all()

	for intent in all_intents:
		f.write("\n## intent:" + intent.name + '\n')
		all_messages = IntentMessage.query.filter_by(intent_id=intent.id).all()
		for message in all_messages:
			f.write("- " + message.message +'\n')

	f.close()

	f = open("data/stories.md", "w")
	all_stories = Story.query.all()
	for story in all_stories:
		f.write("\n## " + story.name + "\n")
		for step in StoryStep.query.filter_by(story_id=story.id).all():
			if(step.isIntent==1):
				f.write("* " + Intent.query.filter_by(id=step.int_or_temp_id).first().name + "\n")
			elif(step.isIntent == 2):
				temp = Template.query.filter_by(id=step.int_or_temp_id).first().name.replace(" ", "_")
				f.write("  - utter_" + temp + "\n")
			else:
				temp = Action.query.filter_by(id=step.int_or_temp_id).first().name.replace(" ", "_")
				f.write("  - " + temp + "\n")
		f.write("  - action_restart")


	f.close()

	templates = Template.query.all()
	actions = Action.query.all()
	slots = Slot.query.all()


	f = open("domain.yml", "w")
	f.write("intents:\n")
	for intent in all_intents:
		if(intent.isFact):  
			f.write("  - " + intent.name + ": {triggers: utter_"  + Template.query.filter_by(id=intent.templateId).first().name +"}\n" )
		else:
			f.write("  - " + intent.name + "\n")


	f.write("\nactions:\n")
	for template in templates:
		f.write("  - utter_" + template.name.replace(" ", "_") + "\n")

	for action in actions:
		f.write("  - " + action.name + '\n')

	if(not(len(slots) == 0)):
		f.write("\nslots:\n")
		for slot in slots:
			f.write("  " + slot.name + ":\n")
			f.write("    type: " + slot.type_slot + "\n")


	f.write("\ntemplates:\n")
	for template in templates:
		f.write("  utter_" + template.name.replace(" ", "_") + ":\n")
		f.write('  - text: "' + template.text + '"\n\n')

	temp_f = open("defaultMessage.txt", "r")
	f.write('  utter_default:\n  - text: "' + temp_f.read() + '"\n')
	temp_f.close()




	f.close()
	train_cmd = "rasa train"
	#os.system(train_cmd)

	return render_template("success.html", message="Done training")

if __name__ == '__main__':
	
	app.run(debug=True)

   


# all_intents = Intent.query.all()

# for intent in all_intents:
# 	print("## " + intent.name)
# 	all_messages = IntentMessage.query.filter_by(intent_id=intent.id).all()
	
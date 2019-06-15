# rasabot_automation
This project helps you to train a rasa bot(verison 1.1.3) through a simple web application on Flask. You can create intents, text responses/templates, stories, actions etc through this UI.  



### Installation
1. Clone this repo and change into the project directory

2. Install the required pacakges by using the following command
`pip install -r requirements.txt`

3. The project requires a spacy language model. Install this with the following commands

`python -m spacy download en_core_web_md`  

 `python -m spacy link en_core_web_md en`
 
 4. To create a database (this project uses SQLite) to store the intents, stories and other components of the bot, run 
 `python createDB.py`
 
 5. To launch the web app to train the chatbot, run
 `python app.py`
 This will start the flask server on port 5000. Go to localhost:5000 to launch the application and train your model.

### Training
The home page contains buttons with names suggesting what they are supposed to do.

**Creating new intents.**: 
Give an appropriate name to identify what kind of messages this intent corresponds to.
Click on the add new message to add more messages that correspond to that intent. Click on Create Intent once you've added all the messages as per your requirement. This will add the intents to the DB only (the training is not done yet).

**Creating response messages**: 
Give a name and the response message. This will create an 'utter' text. 

**Creating stories**: 
Stories create a conversation. They begin with an intent followed by one or more responses. You can add as many intents and responses you want by clicking on the appropriate buttons. The dropdowns will show intents or templates( and actions too) that are in the database only. So make sure you first create all the intents, responses/templates and actions before you create a story.

**Creating actions**: 
Give the action a suitable name and click on create action. This will create the action class in actions.py file at the project root. Customise the code in the run() method of the class.

**Creating slots**: 
Give the slot a name and leave the type field as text if you are not sure. A slot is a memory unit that the chatbot can remember in a conversation. Once a slot is created, you can use it for entity classification while creating intents.

Visit Rasa Docs for a better understanding of slots, actions, stories.

For example, to create a chatbot that can answer how many centuries a cricketer has made, follow these steps.

1. Create a slot with the name 'cricketer'. This slow will contain which cricketer the user wants to know about
![alt text](https://textract-console-us-east-1-f1845175-fc78-475d-9b50-a287c2cf3cd0.s3.amazonaws.com/slot.PNG "cricketer slot")

2. Create an intent with all the messages on how a user might ask the chatbot about the centuries of a cricketer.
Example: How many centuries did \[entity value\]\(entity name\) score?
Rasa NLU will automatically check for slots with the same name as the entity name and populate that slot with the detected entity value.
![alt text](https://textract-console-us-east-1-f1845175-fc78-475d-9b50-a287c2cf3cd0.s3.amazonaws.com/intent_with_slots.PNG "cricketer intent")


3. Create an action that would ideally use some api to fetch the required info. (Code for the action class will be auto generated in the actions.py file)  
![alt text](https://textract-console-us-east-1-f1845175-fc78-475d-9b50-a287c2cf3cd0.s3.amazonaws.com/actions.PNG "cricketer action")

4. Edit the run method of your actions class in actions.py. 
![alt text](https://textract-console-us-east-1-f1845175-fc78-475d-9b50-a287c2cf3cd0.s3.amazonaws.com/actionscode.PNG "cricketer action code")

5. Create a story to put all this together.
![alt text](https://textract-console-us-east-1-f1845175-fc78-475d-9b50-a287c2cf3cd0.s3.amazonaws.com/story.PNG "cricketer story")

6. Click on the train button to train your model. Navigate to the project root and use the command `rasa shell` to start talking to your bot. You can ask the bot 'How many centuries did Virat Kohli make?' and see the bot in action.

## Additional notes

1. The config.yml of the project are edited to use the Spacy model for intent and entity classification. You can choose other models if you wish.

2. You can also modify what your chatbot says when it doesnt understand a user's message by adding your own text to the 'defaultMessage.txt' file. 

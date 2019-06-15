# rasabot_automation
This project helps you to train a rasa bot(verison 1.1.3) through a simple web application on Flask. 

### Installation
1. Clone this repo and change into the project directory

2. Install the required pacakges by using the following command
`pip install -r requirements.txt`

3. The project requires a spacy language model. Install this with the following commands
`python -m spacy download en_core_web_md
 python -m spacy link en_core_web_md en`
 
 4. To create a database to store the intents, stories and other components of the bot, run 
 `python createDB.py`
 
 5. To launch the web app to train the chatbot, run
 `python app.py`
 This will start the flask server on port 5000. Go to localhost:5000 to launch the application and train your model.


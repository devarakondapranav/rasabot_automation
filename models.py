from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Intent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    isFact = db.Column(db.BOOLEAN, unique=False, nullable=True)
    templateId = db.Column(db.Integer, unique=False, nullable=True)
    

    def __repr__(self):
        return '<Intent %r>' % self.name

class IntentMessage(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	message = db.Column(db.String(400), unique=True, nullable=False)
	intent_id = db.Column(db.Integer, db.ForeignKey('intent.id'))


class Template(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), unique=True, nullable=True)
	text = db.Column(db.String(1000), unique=False, nullable=True)


class Story(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), unique=True, nullable=False)



class StoryStep(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	story_id = db.Column(db.Integer, db.ForeignKey('story.id'))
	isIntent = db.Column(db.BOOLEAN, unique=False, nullable=False)
	int_or_temp_id = db.Column(db.Integer, nullable=False)

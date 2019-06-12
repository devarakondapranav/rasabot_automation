from models import Intent, IntentMessage, Template, Story, StoryStep, Action ,Slot,db
from flask import Flask, render_template, request

db.create_all()

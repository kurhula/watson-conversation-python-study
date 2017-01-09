from pymongo import Connection
from app import config
conn = Connection('localhost', 27017)
    
def getDbConnection():
    db = conn[config.get("MongoDb", "DATABASE")]
    return db

def listScores():
    db = getDbConnection()
    scores = list(db["score"].find())
    return scores

def addScore(inputText, message, intents, entities, score):
    db = getDbConnection()
    db["score"].insert({
        "inputText": inputText,
        "message": message,
        "intents": intents,
        "entities": entities,
        "score": score
    })
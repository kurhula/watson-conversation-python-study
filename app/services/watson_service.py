import json
from app import config

from watson_developer_cloud import ConversationV1

conversation = ConversationV1(
  username=config.get("WatsonConversation", "USERNAME"),
  password=config.get("WatsonConversation", "PASSWORD"),
  version='2016-09-20'
)
workspace_id = config.get("WatsonConversation", "WORKSPACE")

contexts = {}
def sendMessage(context_id, message):
    context = None
    contextExists = contexts.has_key(context_id)
    if(contextExists):
        context = contexts[context_id]
    response = conversation.message(
        workspace_id=workspace_id,
        message_input={'text': message},
        context=context
    )
    
    if not(contextExists):
        contexts[context_id] = response["context"]

    return {
        "text": "\n".join(response["output"]["text"]),
        "intents":  response["intents"],
        "entities": response["entities"]
    }
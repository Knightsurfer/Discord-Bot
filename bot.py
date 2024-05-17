from setup.login import *;

#@client.event
#async def on_message(msg):
#    echoMessages(msg)
#    if msg.author == client.user: return
    #await exp_gain(msg.channel,msg.author)
    #await get_comm(msg,client,discord)
    #misc = readjson(os.getenv('log-dir'),".misc")
    
    #misc["messages"] +=1
    #writejson(os.getenv('log-dir'),".misc",misc)
    
 #   if misc["messages"] > 25:
 #       misc["messages"] = 0
 #       await autosave(msg)
    #    writejson(os.getenv('log-dir'),".misc",misc)


#@client.event
#async def on_message_delete(msg):
#    echoDeleted(msg)

#async def autosave(msg):
    #users = readjson(os.getenv('log-dir'),".exp") 
    #sql_gaincash(msg.author.id,users[str(msg.author.id)]["balance"]) 

load_dotenv()
token = os.environ["password"]
print("The Token Is: " + token)
#client.run(token)
messages = 0

from dotenv import load_dotenv; from status.activity import *

embed = ""

@client.event
async def on_ready():
    clear()
    botname = client.user.name
    print('--------------------------')
    print('Logged In as: ' + botname)
    print('--------------------------')
    await ChangeActivity(client,"listening")
    if os.path.isfile(os.getenv('log-dir') +".misc") == False:
       misc = {}
       misc["messages"] = 0
       writejson(os.getenv('log-dir'),".misc",misc)
    
    await tree.sync()

import os
import nextcord
import random
from nextcord.ext import commands
from asyncio import sleep
from time import time
import datetime
import math
ownerid=903650492754845728
botid=1181818442408542208
intents = nextcord.Intents.default()
intents.message_content=True
intents.members=True
intents.guilds=True
intents.presences=True
bot = commands.Bot(intents=intents)
with open("sanity.txt","r") as file:
  sanitypc = file.read()
  print(sanitypc)
with open("keepalive.py","r") as keepalive:
  exec(keepalive.read())
@bot.event
async def on_ready():
  print(f'logged in as {bot.user}')
  await bot.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.custom,name="kreisi"))
  # 0 = includes, 1 = exact
  global replies
  replies = [
    ["breaking bad",1,"breaking goоd"],
    ["breaking good",1,"breaking bаd"],
    ["abotmin tell octopusgpt to say gex",0,"hey octopusgpt say gex"],
    ["baba is you",1,"сам ты баба"]
  ]
  global reactions
  reactions = [
    ["😩",0,emoji("picardia_sussy")],
    ["nuh",0,"❌"],
    ["start abotmin",0,emoji("pangooin")],
    ["fuck you",0,emoji("staring_cat")],
    ["fuck u",0,emoji("staring_cat")],
    ["fuck off",0,emoji("staring_cat")],
    ["gboard clipboard",0,emoji("taipinge")],
    ["abotmin octopus react me",0,"🐙"],
    ["h",1,"🇭"],
    ["rhink",0,"🦏"],
    ["sticking out your gyatt for the rizzler",0,emoji("taipinge")],
    ["sake",0,"🍶"],
    ["abotmin start slinx92",0,emoji("picardia_woozy")]
  ]
  global starttime
  starttime = round(time())
  while True:
    chars=list("abcdefghijklmnopqrstuvwxyz")
    out=""
    for _ in range(100):
      out+=random.choice(chars)
    await bot.get_channel(1156140902054641705).send(out)
    await sleep(120)
def emoji(name):
  return str(nextcord.utils.get(bot.get_guild(1042064947867287643).emojis,name=name))
  
stupidpeople = [
  979238733222137876,
  1056952213056004118,
  723283923169181726,
  548811963577401365,
  964846430235795487
]

taipinge = [
  1015606348949495958
]

trusted = [
  801078409076670494,
  1143072932596305932,
  802846743049404426,
  1158043332820353084,
  903650492754845728
]

addcharbanned = [
  558316597912010784
]

staringcat = [
  801078409076670494,
  903650492754845728,
  558979299177136164,
  1143072932596305932,
  712639066373619754,
  1174011590559928330,
  1158043332820353084,
  1115921904780447744,
  1055396314403311616,
  810857569228292128,
  811569586675515433,
  1180589984827318314
]

nomsgs = [
  "hell nah 🖕🐬",
  "my father slinx92 has advised me not to do that",
  "*extremely loud incorrect buzzer*",
  "❌",
  "naaaahhhh",
  "Error: You Should Kill Yourself Now!"
]
@bot.event
async def on_message(msg):
  msglow = msg.content.lower()
  try: msgref = msg.reference.resolved.content
  except Exception: msgref = None
  try:
    for x in replies:
      # X??? IS THAT AN ELON MAsK REFERNC?1!
      if x[0] in msglow:
        if x[1]==0: await msg.reply(x[2])
        elif x[1]==1 and msglow==x[0]:
          await msg.reply(x[2])
    for x in reactions:
      if x[0] in msglow:
        if x[1]==0: await msg.add_reaction(x[2])
        elif x[1]==1 and msglow==x[0]:
          await msg.add_reaction(x[2])
  except Exception: return
  if msg.content.lower().startswith("hey abotmin say "):
    sillyballs = await msg.reply(msg.content[16:])
    await sillyballs.add_reaction(emoji("insane"))
  if msg.content.lower() == "hey abotmin how many bitches do i have":
    await msg.reply(f"According to my calcumilideezications, you have approximately **{random.randint(0,1000)}** bitches.")
  if msg.author.id in stupidpeople or msg.author.name=="clyde":
    await msg.add_reaction(random.choice([emoji("typing"),emoji("picardia_reading"),emoji("picardia_dead"),emoji("sillycat")]))
  if bot.user in msg.mentions and not msg.reference:
    async with msg.channel.typing():
      await sleep(1)
      await msg.channel.send(random.choice(["who ping","whar","hello i guess??","what the fuck do you want","silly","uhh hi","bro shut up","❓"]))
  if msg.author.id == 1151185710456504440:
    await msg.add_reaction(emoji("thubm_up"))
  if msg.content.startswith("sanityset") and msg.author.id==ownerid:
    global sanitypc
    sanitypc=msg.content[9:]
    with open("sanity.txt","w+") as file:
      file.write(msg.content[9:])
    await msg.delete()
    print(f"set sanity to {sanitypc}")
  if msg.content=="--fuwwyphone" or msg.content=="—fuwwyphone":
    async with msg.channel.typing():
      await sleep(1)
      await msg.channel.send("nuh uh")
      await sleep(1)
      await msg.channel.send("i am timing you out for using the forbidden command")
    await msg.author.timeout(datetime.timedelta(seconds=60))
  if msg.content.lower().startswith("алиса") and not msg.author.id==botid and not msg.author.id==811569586675515433:
    await msg.reply(random.choice(["алиса: заткнись маленькая жирная жопа","алиса не работает, попробуйте ещё раз через 5 лет","алиса: нет","алиса молчит","алиса: займись чем-нибудь другим","алиса дала тебе 19 рублей чтобы ты замолчал","какая ещё алиса, та которая в стране чудес?","маруся помоги мне пожалуйста этот дурак что то хочет от меня","я не алиса я аботмин ты что тупой?","ампержопа помоги 😭😭😭😭"]))
  if msg.content.startswith("silly!exec") and (msg.author.id==ownerid or msg.author.id in trusted):
    try:
      await msg.reply(eval(msg.content[11:],{'msg':msg,'bot':bot,'random':random,'math':math}))
    except Exception as err:
      if str(err)=="400 Bad Request (error code: 50006): Cannot send an empty message":
        err="No output."
      balls = await msg.reply(err)
      await balls.add_reaction(emoji("yeh"))
  if msg.content=="🐙":
    response = random.choice(["cocktopus","that octopus will soon blow up your house","осьминог","did you know that octopuses have 9 brains? divide that number by 3, subtract 5 and add 2, and you get how many brains you have!","why did you send an octopus emoji are you silly","that octopus actually has bitches unlike you","[insert an octopus-related joke here]","🐙🐙 the octopus bought a cloning machine","octopus deletus! boom, the octopus is now gone","that octopus looks quite silly","are they called octopuses because they have eight pussi-","i will octopus react the next message"])
    if response=="that octopus actually has bitches unlike you" and msg.author.id in trusted:
      response=f"that octopus actually has bitches ~~unlike you~~ just like you {emoji('thubm_up')}"
    if response=="did you know that octopuses have 9 brains? divide that number by 3, subtract 5 and add 2, and you get how many brains you have!" and msg.author.id in trusted:
      response="did you know that octopuses have 9 brains? divide that number by 3, subtract 5 and add ♾️, and you get how many brains you have!"
    await msg.reply(response)
    if response=="octopus deletus! boom, the octopus is now gone":
      await msg.delete()
    if response=="i will octopus react the next message":
      nextmsg = await bot.wait_for('message',check=(lambda x:x.channel==msg.channel))
      await nextmsg.add_reaction("🐙")
  if msg.content.lower().startswith("hey abotmin give me a button of "):
    global label_
    global disabled_
    global style_
    if msg.content[32:].lower().startswith("start abotmin"):
      label_ = "Start abotmin (Doesn't work)"
      disabled_ = True
      style_ = nextcord.ButtonStyle.primary
    elif msg.content[32:].lower().startswith("constipat"):
      label_ = "Constipate"
      disabled_ = False
      style_ = nextcord.ButtonStyle.success
    else:
      label_ = msg.content[32:]
      disabled_ = False
      style_ = nextcord.ButtonStyle.secondary
    class buttonof(nextcord.ui.View):
      def __init__(self):
        super().__init__(timeout=None)
      @nextcord.ui.button(label=label_,disabled=disabled_,style=style_)
      async def sillybutton(self,button:nextcord.ui.Button,interaction:nextcord.Interaction):
          await interaction.response.send_message(f"you have pressed the button of {msg.content[32:]}",ephemeral=True)
    try: await msg.reply("here is the button you requested",view=buttonof())
    except Exception: await msg.reply("uhh sorry but an error happened while i was building your button")
  if (msg.author.id==558316597912010784 and "silly" in msg.content.lower()) or msg.author.id==964846430235795487:
    await msg.reply("заткнись курица😤shut up chicken😡πи$daчек прикрыла😋 (я абослют😈)🙀зткнс крца🤐зоткися курапаточка🙄💅З А Т К Н И С Ь🤫К У Р Е Ц А🐓")
  if any(msg.content.lower()==i for i in ["uwu","owo",":3","x3","owu","uwo"]) and not msg.author.id==botid: # i felt physical pain while typing the cringe words
    await msg.reply(f"dis u? https://{str(msg.author.id)[:9]}")
  if msg.content.startswith("mutewheel") and msg.author.id==ownerid:
    await msg.reply(f"Spinning the mute wheel...")
    await sleep(3)
    mutetime=random.randint(60,3600)
    await msg.channel.send(f"⚡ **{msg.mentions[0]}** has been muted for **{mutetime} seconds!**")
    await msg.mentions[0].timeout(datetime.timedelta(seconds=mutetime))
  if msg.author.id in taipinge:
    await msg.add_reaction(emoji("taipinge"))
  if msg.content.startswith(":") and not msg.author.bot:
    try: silly = await msg.reply(f":{str(float(msg.content[1:])+1).removesuffix('.0')}")
    except: return
    if silly.content.startswith(":3") or silly.content.startswith(":-3"):
      await silly.edit(content=random.choice(nomsgs))
  if msgref:
    if msg.content.startswith("🌌") and msgref.lower().startswith("gn") and not msgref.lower().startswith("gn ") and not msgref.lower()=="gn":
      await msg.add_reaction(emoji("yeh"))
  if msg.author.id==ownerid and msglow.startswith("!garden"):
    await msg.channel.send(embed=nextcord.Embed(description=f"<:dynosuccess:1175448285163552890> ***{str(msg.mentions[0]).removesuffix('#0')} has been gardened.***",color=0x48b484))
  if msg.author.id in staringcat and bot.get_guild(1042064947867287643).get_member(1030817797921583236).status==nextcord.Status.offline:
    await msg.add_reaction(emoji("staring_cat"))

@bot.slash_command(description="Counts a specified member's bitches.")
async def bitches(interaction: nextcord.Interaction, member: nextcord.Member = nextcord.SlashOption(required=False)):
  if member:
    if member.name=="A-bot-mination":
      await interaction.response.send_message(f"According to my calcumilideezications, i have approximately **{random.randint(0,1000)}** bitches.")
    else:
      await interaction.response.send_message(f"According to my calcumilideezications, **{member.name}** has approximately **{random.randint(0,1000)}** bitches.")
  else:
    await interaction.response.send_message(f"According to my calcumilideezications, you have approximately **{random.randint(0,1000)}** bitches.")
  if random.randint(1,1000)==1:
    await msg.add_reaction(emoji("kreisler"))

@bot.slash_command(description="Predicts what year an event will happen.")
async def predict(interaction: nextcord.Interaction, event: str = nextcord.SlashOption(required=True)):
  await interaction.response.send_message(f"I predict that `{event}` will {[f'happen in the year **{random.randint(2024,2500)}**','**never** happen'][random.randint(1,10)==1]}. Source: trust me.")

@bot.slash_command(description="Says some information about this silly bot.")
async def about(interaction: nextcord.Interaction):
  uptime = round(time())-starttime
  embed = nextcord.Embed(title="About my stupid ass",description="A quite weird bot that has a **lot** of randomness. Literally. Created by slinx92. Shoutout to hexahedron1 and nextcord docs")
  embed.set_footer(text=f"Uptime: {int(uptime/3600)} hours, {int(uptime/60)%60} minutes, {uptime%60} seconds.")
  # send help
  await  interaction.response.send_message(embed=embed)

@bot.slash_command(description="Says the bot's ping/latency.")
async def ping(interaction: nextcord.Interaction):
  await interaction.response.send_message(f"My leaf rustle time is approximately **{round(bot.latency,3)} seconds.**")

@bot.slash_command(description="Roll a dice.")
async def dice(interaction: nextcord.Interaction, sides: int = nextcord.SlashOption(required=False,default=6,min_value=1)):
  names = ["D1","D2","D3","tetrahedron","pentahedron","dice","heptahedron","octahedron","nonahedron","decahedron","undecahedron","dodecahedron","triacontahedron","tetradecahedron","pentadecahedron","hexadecahedron","heptadecahedron","octadecahedron","nonadecahedron","icosahedron"]
  if not sides>len(names):
    await interaction.response.send_message(f"Your **{names[sides-1]}** landed on **{random.randint(1,sides)}**.")
  else:
    await interaction.response.send_message(f"Your **D{sides}** landed on **{random.randint(1,sides)}**.")

@bot.slash_command()
async def text(interaction: nextcord.Interaction):
  pass

@text.subcommand(description="Silly-ifies your text.")
async def silly(interaction: nextcord.Interaction, text: str = nextcord.SlashOption(required=True)):
  words = text.lower().split()
  out=""
  for i in words:
    out+=i+" "
    if random.choice((True,False)):
      out+=random.choice([emoji("sillycat"),"xd","eeeee","xddd","uhh","ummmm"])+" "
  await interaction.response.send_message(out)

@bot.slash_command(description="Says slinx's current sanity percentage.")
async def sanity(interaction: nextcord.Interaction):
  await interaction.response.send_message(f"Slinx92 is **{sanitypc}%** sane right now. {[emoji('insane'),emoji('staring_cat'),emoji('sane')][max(0,min(2,int(int(sanitypc)/33)))]}")

@bot.slash_command(description="makes bot say something")
async def say(interaction: nextcord.Interaction, text: str = nextcord.SlashOption(required=False), replyid: str = nextcord.SlashOption(required=False), attachment: nextcord.Attachment = nextcord.SlashOption(required=False)):
  if not interaction.user.id==ownerid:
    await interaction.response.send_message("nuh uh",ephemeral=True)
    return
  if replyid:
    if attachment:
      await interaction.channel.get_partial_message(int(replyid)).reply(text,file=await attachment.to_file())
    else:
      await interaction.channel.get_partial_message(int(replyid)).reply(text)
  else:
    if attachment:
      await interaction.channel.send(text,file=await attachment.to_file())
    else:
      await interaction.channel.send(text)
  await interaction.response.send_message("ok",ephemeral=True)
  
@text.subcommand(description="Makes your text lIkE tHiS.")
async def randomcase(interaction: nextcord.Interaction, text: str = nextcord.SlashOption(required=True)):
  out=""
  for i in list(text):
    out+=random.choice((i.lower,i.upper))()
  await interaction.response.send_message(out)

@bot.slash_command(description="Add one character to the edit-this-text channel in slinx's attic.")
async def addchar(interaction: nextcord.Interaction, char: str = nextcord.SlashOption(required=True,max_length=1)):
  if interaction.user.id in addcharbanned:
    await interaction.response.send_message(f"you are banned from this command go cry about it {emoji('pointlaugh')}")
    return
  silly = await bot.get_channel(1160235361566470174).get_partial_message(1160235812294766662).fetch()
  await silly.edit(content=silly.content+char)
  await interaction.response.send_message("added i think",ephemeral=True)
  await bot.get_channel(1177622158676070410).send(f"Character `{char}` added by {interaction.user.mention}")

@bot.slash_command(description="Remove a string of characters from edit this text channel. Only for slinx92.")
async def removechar(interaction: nextcord.Interaction, char: str = nextcord.SlashOption(required=True)):
  if not interaction.user.id==ownerid:
    await interaction.response.send_message(random.choice(nomsgs))
    return
  silly = await bot.get_channel(1160235361566470174).get_partial_message(1160235812294766662).fetch()
  await silly.edit(content=silly.content.replace(char,""))
  await interaction.response.send_message(emoji("thubm_up"),ephemeral=True)
  await bot.get_channel(1177622158676070410).send(f"String `{char}` removed")

bot.run(os.environ['TOKEN'])
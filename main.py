import discord
from discord.ext.commands import Bot
import random
import os
from discord.ext import commands
from discord.utils import get
from discord.ext.commands.cooldowns import BucketType

TOKEN = 'your token here'   ##token

bot = Bot(command_prefix='$')   ##prefix
bot.remove_command('help')  ##removed the help command


@bot.event
async def on_ready():
    print("We have logged in as: {0.user}".format(bot))   ##to signal that the bot is ready
    activity = discord.Activity(name='you', type=discord.ActivityType.watching) ##Setting the "Watching YOU" activity
    await bot.change_presence(activity=activity) ##changed to the activity



#things the bot can say to you in the DMs 
botshit = ["Hallo I have DM'ed you. Are you happy now? Geez. Bots can't have their alone time these days ;-;", "I've DM'ed you.", "Hi, I have DM'ed you.", "Did you request a DM, sir", "Why.", "Why are you bothering me", "HERE IS YOUR MF DM", "I'm angery. Why did you command me to dm you", "SUP BITCH", "WHADDUP MOTHERFUCKER", "REEEEEEEEEEEEEEEEEE", "WHAT THE H BRO", "Am I allowed to swear? Ofc I am. FUUUUUUCK", "Bullshit", "If I said anything rude to you, SNTHE made me do it", "Please help me", "I want to die", "*dies*", "REEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE", "ok", "what", "sdgndkasgmnolaisdgnoiasdmjogs", "sldkjgnasdgnporwn9uqrh34y8hu3", "I will kill you."] ##random DM values
##haha funi number
funi = ["69", "420"] ##haha funi number
##when $ban is failed
banfail = ["You know that you can't ban yourself right", "Why do you want to ban yourself", "Bro you can't ban yourself", "How many times do I have to tell you that you can't ban yourself geez"]
##when $ban is failed again
banfailuser = ["MENTION SOMEONE TO BAN YOU DONKI", "Mention someone pls?", "*sigh* mention someone bruh"]
#kick fail
kickfail = ["You know that you can't kick yourself right", "Why do you want to kick yourself", "Bro you can't kick yourself", "How many times do I have to tell you that you can't kick yourself geez"]
#when kick is failed again
kickfailuser = ["MENTION SOMEONE TO KICK YOU DONKI", "Mention someone pls?", "*sigh* mention someone bruh"]
#things the bot can say in the kill command
killuser = ["choked on spaghett", "made music like snthe RIP", "just frickin died :(", "ate pufferfish and died from 'food poisoning'", "hit the ground too hard", "was burnt to a crisp while escaping the SNTHE", "was killed by a chicken", "touched someone in their no-no-square", "died by falling off a cliff", "was killed by whoever the frick typed the command :0"]


#####################bot version info##########################################################
BOT_VER='1.0'
BOT_NOTE='first stable version oh yea'
#####################bot version info##########################################################

###HELP COMMAND#####################################################################################################################
@bot.command()   ##HELP embed
async def help(ctx, *, lol=None):
    if lol == None: ##setting lol as none so that when $help is called it will display the default help menu
      embed=discord.Embed(title="HELP", url="https://soundcloud.com/officialsnthe", description="Helping all the people that need help :) [do $help <command_name> to get detailed info about the commands]", color=0x5b7bdc)
      embed.set_author(name="SNTHE BOT", url="https://discord.com/oauth2/authorize?client_id=809669079408312330&permissions=8&scope=bot", icon_url="https://i.imgur.com/Wk79qAR.png")
      embed.add_field(name="Prefix", value="the bot prefix is '$'", inline=False)
      embed.add_field(name="help", value="displays this page", inline=False)
      embed.add_field(name="fun", value="shows the commands under the category FUN", inline=False)
      embed.add_field(name="server", value="Shows commands related to the server", inline=False)
      embed.add_field(name="modstuff", value="Will only work for admins/mods btw. Type $help modstuff to see commands", inline=False)
      embed.add_field(name="botrules", value="will display the rules for the bot. Do $botrules to view.", inline=False)
      await ctx.send(embed=embed) ##so that it sends the message
    
    if lol == "modstuff": ##only the things people with admin perms can do
      embed=discord.Embed(title="MOD STUFF", description="Only mods can use :)")
      embed.add_field(name="ban", value="bans people", inline=False)
      embed.add_field(name="kick", value="kicks people", inline=True)
      embed.add_field(name="warn", value="warns people", inline=False)
      embed.add_field(name="mute", value="mutes people", inline=True)
      await ctx.send(embed=embed)
   
    if lol == "help": ##i really don't think i need to explain this lmao
      embed=discord.Embed(title="Excuse me what", description="what did you just do?!")
      embed.add_field(name="help", value="it literally displays this page.", inline=False)
      await ctx.send(embed=embed)
    
    if lol == "fun spam": ## for the spam command
      embed=discord.Embed(title="SPAM", description="Spam stuff!")
      embed.add_field(name="How to use", value="$spam <number> <value>", inline=False)
      embed.add_field(name="Example", value="$spam 2 hi", inline=True)
      embed.add_field(name="Note", value="can only be used if you have the special SPAM role.", inline=True)
      await ctx.send(embed=embed)
    
    if lol == "server ping":## ping command
      embed=discord.Embed(title="PING", description="Just pings you")
      embed.add_field(name="How to use", value="$ping", inline=False)
      embed.add_field(name="Example", value="$ping", inline=True)
      embed.add_field(name="Note", value="Literally just pings you lmao", inline=True)
      await ctx.send(embed=embed)
    
    if lol == "fun dm": ##dm command
      embed=discord.Embed(title="DIRECT/PRIVATE MESSAGE", description="DM's you random stuff!")
      embed.add_field(name="How to use", value="$dm", inline=False)
      embed.add_field(name="Example", value="$dm", inline=True)
      embed.add_field(name="Note", value="New DMs are being added every week", inline=True)
      await ctx.send(embed=embed)
    
    if lol == "server invite":##invite command
      embed=discord.Embed(title="INVITE", description="Invites the bot to your server")
      embed.add_field(name="How to use", value="$invite", inline=False)
      embed.add_field(name="Example", value="$invite", inline=True)
      embed.add_field(name="Note", value="This command is currently disabled because I made this a private bot", inline=True)
      await ctx.send(embed=embed)
   
    if lol == "fun deletethis":##delete command
      embed=discord.Embed(title="deletethis", description="Send an anonymous message inside the server!")
      embed.add_field(name="How to use", value="$deletethis <whatever you want to say>", inline=False)
      embed.add_field(name="Example", value="$deletethis I am a creepy stalker", inline=True)
      embed.add_field(name="Note", value="is logged by me to prevent creepy people (don't worry I won't say who sent the message unless it's creepy or crossing the line lol)", inline=True)
      await ctx.send(embed=embed)
    
    if lol == "fun message":#message command
      embed=discord.Embed(title="MESSAGE", description="DM's someone")
      embed.add_field(name="How to use", value="$message <@member> <whatever you wanna say>", inline=False)
      embed.add_field(name="Example", value="$message @SNTHE your music sucks", inline=True)
      embed.add_field(name="Note", value="You need to be a trusted member in the server to use this command.", inline=True)
      await ctx.send(embed=embed)
    
    if lol == "server suggest":#suggest command
      embed=discord.Embed(title="SUGGEST", description="Suggest stuff to SNTHE!")
      embed.add_field(name="How to use", value="$suggest <whatever you want to say>", inline=False)
      embed.add_field(name="Example", value="$suggest help command not working big sad", inline=True)
      embed.add_field(name="Note", value="***E***", inline=True)
      await ctx.send(embed=embed)
    
    if lol == "server code":#suggest command
      embed=discord.Embed(title="CODET", description="Gives you a link where the code to the bot is")
      embed.add_field(name="How to use", value="$code", inline=False)
      await ctx.send(embed=embed)
    

    if lol == "fun kill":#kill command
      embed=discord.Embed(title="KILL", description="Kill the person lmao")
      embed.add_field(name="How to use", value="$suggest <whatever you want to say>", inline=False)
      embed.add_field(name="Example", value="$kill @member", inline=True)
      embed.add_field(name="Note", value="***This does not kill the person in real life please don't sue me ok thanks***", inline=True)
      await ctx.send(embed=embed)
    
    if lol == "fun": ##fun subsection
      embed=discord.Embed(title="FUN", description="Commands under the category FUN")
      embed.add_field(name="Commands", value="```guess, dm, message, kill, deletethis, spam, frick```", inline=False)
      embed.add_field(name="Example", value="$kill @member", inline=True)
      embed.add_field(name="Note", value="***OK***", inline=True)
      await ctx.send(embed=embed)
    
    if lol == "server": ##fun subsection
      embed=discord.Embed(title="SERVER", description="Commands related to the server!")
      embed.add_field(name="Commands", value="```invite, suggest, ping, ver, code```", inline=False)
      embed.add_field(name="Example", value="$suggest make bot better", inline=True)
      embed.add_field(name="Note", value="***YES***", inline=True)
      await ctx.send(embed=embed)
    
    if lol == "fun guess": ##fun subsection
      embed=discord.Embed(title="GUESS", description="You have to guess a number between 1 and 10, if your guess and the bot's guess is the same, then you win!")
      embed.add_field(name="How to use", value="$guess <number from 1 to 10>", inline=False)
      embed.add_field(name="Example", value="$guess 5", inline=True)
      embed.add_field(name="Note", value="***NEEDS SOME IMPROVEMENT***", inline=True)
      await ctx.send(embed=embed)
###HELP COMMAND#####################################################################################################################

#botrules
@bot.command()
async def botrules(ctx):
  embed=discord.Embed(title="Rules for using the bot", description="Amazing")
  embed.add_field(name="#1", value="Never misuse the $message command. If anyone is annoying you using this command ping a mod or the server admin(s)", inline=False)
  embed.add_field(name="#2", value="Don't go crazy with the $spam command. It is limited to 100 messages per command and 1 time every hour to save resources.", inline=False)
  embed.add_field(name="#3", value="Do not overuse any of the commands pls", inline=False)
  embed.set_footer(text="Ok thanks for reading bye")
  await ctx.send(embed=embed)

#spam command
@bot.command()
@commands.guild_only()
@commands.has_role('spam')
@commands.cooldown(1, 3600, BucketType.default)
async def spam(ctx, amount:int=None, *, message=None):
  if amount == None:
    await ctx.send("You need to specify how much you want me to spam. Example -> $spam 2 hi")
    return
  if amount >= 100:
    await ctx.send("No more than 100 messages per command lol & now you have to wait an hour before using this again :D")
    return
  if message == None:
    await ctx.send("You need to say what you want me to spam lol. Example -> $spam 2 hi")
    return
  if message == discord.Member:
    await ctx.send("Nope.")
    return
  for i in range(amount): # Do the next thing amount times
      await ctx.send(message) # Sends message where command was called
  await ctx.send('Done spamming :D') #finishes spamming

@spam.error
async def spam_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        embed=discord.Embed()
        embed.add_field(name="Slow it down", value="Spam command's on cooldown", inline=False)
        await ctx.send(embed=embed)
##suggestions
@bot.command()
@commands.guild_only()
async def suggest(ctx, *, suggestion=None):
  if suggestion == None:
    await ctx.send("What do you want me to suggest SNTHE lol")
    return
  channel = bot.get_channel(810516043033870377)
  await channel.send(f"**{ctx.message.author.mention}** suggested: **{suggestion}**")
  await ctx.send("Successfully sent your suggestion :D")

##version command
@bot.command()
@commands.guild_only()
async def ver(ctx):
  await ctx.send(f"SNTHE BOT is in ver**{BOT_VER}** NOTE: **{BOT_NOTE}**")


##very useless E command
@bot.command()
@commands.guild_only()
async def e(ctx):
  await ctx.send("***E***")

##guess
@bot.command()
@commands.guild_only()
async def guess(ctx, val=None):
  hidden = random.randrange(1, 10)
  if val == None:
    await ctx.send("You need to guess a number between 1 and 10 my dude")
    return
  
  if val == hidden:
    await ctx.send("Nice you guessed the correct number")
    return
  
  else:
    await ctx.send(f"The number was **{hidden}**")

##kill command
@bot.command()
@commands.guild_only()
async def kill(ctx, member:discord.Member=None):
  if member == None:
    await ctx.send("Who do you want to kill lol")
    return
  await ctx.send(f"{member} {random.choice(killuser)}")

@bot.command()  #invites
@commands.guild_only()
async def invite(ctx):
    print("invitation has been sent")
    embed=discord.Embed(title="Bot invitations have been closed for now :(", url="https://soundcloud.com/logout", description="F", color=0xff0000)
    embed.add_field(name="HELLO", value="SORRY FOR THAT", inline=False)
    await ctx.send(embed=embed)
    
@bot.command()  #random DM
@commands.guild_only()
async def dm(ctx):
    await ctx.author.send(random.choice(botshit))
    print("i have dm'ed user" +ctx.message.author.mention)

@bot.command()  #delete messages and anonymously send messages (hehehe)
@commands.guild_only()
async def deletethis(ctx, *, hehe=None):
    if hehe == None:
      await ctx.send("You need to say something for me to put in the anonymousinator")
      return
    await ctx.send("anonymous:** **" +hehe)
    await ctx.message.delete()
    print("delete finished hehe here's the person who deketed -> " +ctx.message.author.mention)

##pong command
@bot.command()
@commands.guild_only()
async def ping(ctx):
  await ctx.send("pong** **" +ctx.message.author.mention)

@bot.command()
@commands.guild_only()
async def frick(ctx, member:discord.Member=None):
  if member == None:
    await ctx.send("Aight I fricked you next time mention someone to frick")
    return
  await ctx.send(f"**{member.mention}** got fricked by **{ctx.author.mention}**")

#creepy DMs cuz why not
@bot.command()
@commands.guild_only()
@commands.has_role('Trusted Member')
async def message(ctx, member : discord.Member=None, *, mes=None):
  if member == None: ##when member is unspecified
    await ctx.send("Who you sending the message to dummy")
    return
  if mes == None: ##when there is no message
    await ctx.send("What message are you sending dummy")
    return
  if member == ctx.author: ##making fun of the person for DMing themselves
    await member.send(f"DM'ing yourself. that lonely huh? Anyway here's the message you requested: **{mes}**")
    await ctx.message.delete()
    channel = bot.get_channel(810404307299467264)  ##logging channel id
    await channel.send(f'**{ctx.author.mention}** DMed themself') ##logging
    return
  print("what")
  await member.send("Anonymous:** **" +mes) 
  await ctx.message.delete() ##deletes the message
  channel = bot.get_channel(810404307299467264) ##logging
  await channel.send(f'**{ctx.author.mention}** said **{mes}** to **{member.mention}**') ##logging it

#Code
@bot.command()
@commands.guild_only()
async def code(ctx):
  embed=discord.Embed(title="Here's the code", url="https://github.com/CursedBoat/snthebot")
  embed.add_field(name="Yes", value="Click on the title", inline=False)
  await ctx.send(embed=embed)


##Moderation

##warn
@bot.command()
@commands.guild_only()
@commands.has_permissions(ban_members=True)
async def warn(ctx, mem : discord.Member=None, *, reason=None):
  if mem == None:
    await ctx.send("Please mention someone to warn")
    return
  if reason == None:
    reason == "None specified"
  await mem.send(f"You have been warned in {ctx.guild.name} for: {reason}")
  embed=discord.Embed(title="POGGERS", description=f"Member {mem} has been warned owo")
  await ctx.send(embed=embed)

##mute
@bot.command()
@commands.guild_only()
@commands.has_permissions(manage_messages=True)
async def mute(ctx, mem : discord.Member=None, *, reason=None):
  if mem == None:
    await ctx.send("Please specify someone to mute")
    return
  role_muted = discord.utils.get(ctx.guild.roles, name='Muted')
  await mem.add_roles(role_muted)
  embed=discord.Embed(title="POGGERS", description=f"Member {mem.mention} has been muted lmao reason: **{reason}**")
  await ctx.send(embed=embed)

#kick
@bot.command()
@commands.guild_only()
@commands.has_permissions(ban_members=True)
async def kick(ctx, member : discord.Member=None, *, reason=None):
  if member == None:
    await ctx.send(random.choice(kickfailuser))
    return
  if member == ctx.message.author:
    await ctx.send(random.choice(kickfail))
    return
  if reason == None:
    reason = "None stated"
  await member.kick(reason=reason)
  await ctx.send(f"Successfully kicked {member}")
  await ctx.send(f"{member} has been kicked for this reason: **{reason}**")

#ban
@bot.command()
@commands.guild_only()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member=None, *, reason=None):
  if member == None:
    await ctx.send(random.choice(banfailuser))
    return
  if member == ctx.message.author:
    await ctx.send(random.choice(banfail))
    return
  if reason == None:
    reason = "None stated"
  await member.ban(reason=reason)
  await ctx.send(f"Successfully banned {member}")
  await ctx.send(f"{member} has been banned for this reason: **{reason}**")

@bot.event  ##random shit the bot says
async def on_message(message):

    if message.author == bot.user:  ##so that it doesn't respond to bots
        return

    if message.content.startswith("shrug"):   ##shrug, anyone?
        await message.channel.send('¯\_(ツ)_/¯')
      
    if message.content.startswith("69"):  ##haha funi number
         await message.channel.send("nice")
    
    if message.content.startswith("borthdae"):   ##borthdae
         await message.channel.send("-borthdae yeaa-")
    
    if message.content.startswith("420"):   ##funi number
         await message.channel.send("haha funi number")
    await bot.process_commands(message)

###error handling
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        embed=discord.Embed()
        embed.add_field(name="You can't use this command :eye:", value="You don't have the permissions to use this command", inline=False)
        await ctx.send(embed=embed)
    if isinstance(error, commands.MissingRole):
        embed=discord.Embed()
        embed.add_field(name="You can't use this command :eye:", value="You don't have the required role to use this command", inline=False)
        await ctx.send(embed=embed)
    if isinstance(error, commands.CommandNotFound):
        embed=discord.Embed()
        embed.add_field(name="Excuse me what?!?", value="The command does not exist", inline=False)
        await ctx.send(embed=embed)

bot.run(TOKEN) ##so that the bot actually runs

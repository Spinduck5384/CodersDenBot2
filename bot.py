"""
Importing all Modules Needed
"""
import discord #Discord Module
from discord.ext import commands #Importing the Discord commands from the discord.py module
from discord.ext.commands import cooldown, BucketType, CommandOnCooldown #Importing cooldown, buckettype and commandoncooldown. Will be used for command cooldowns 
import random #Importing the Random module for the Reddit Commands, and Guessnumber command
import praw #Importing Praw to access the Reddit API and pull information from there


"""
General Setup
"""
client = commands.Bot(command_prefix=".", case_insensitive=True) #Creating the 'client' variable, and setting the prefix to '.'

token = 'your token here' #Creating my token variable. I got the token from my bot

client.remove_command("help") #Remove default help command

"""
Help
"""


@client.command()
async def help(ctx, page = 1):
    if page == 1:
        em = discord.Embed(
            title = "Bot Commands, Admin Only: Moderation",
            color = discord.Color.dark_blue()
        )
        em.add_field(name = ban, value = "Ban a member from your server [.ban <@member> <'reason'> (Example = .ban @Impact Violating Rule 1)]", inline = False)
        em.add_field(name = unban, value = "Unban a member from your server [.unban <member#userid> (Example = .unban Impact#1704)]", inline = False)
        em.add_field(name = kick, value = "Kick a member from your server [.kick <@member> <'reason'> (Example = .kick @Impact Violating Rule 1)]", inline = False)
        em.add_field(name = mute, value = "Mute a member in your server [.mute <@member> (Example = .mute @Impact#1704)]", inline = False)
        em.add_field(name = unmute, value = "Unmute a member in your server [.unmute <@member> (Example = .unmute @Impact#1704)]", inline = False)
        em.add_field(name = addrole, value = "Give a member a role [.addrole <@member> <'Role'> (Example = .addrole @Impact Gamer)]", inline = False)
        em.add_field(name = derole, value = "Remove a role from a member [.derole <@member> <'Role'> (Example = .derole @Impact Gamer)]", inline = False)
        em.add_field(name = slowmode, value = "Set a slowmode for a channel in which the command is called [.slowmode 10 (Sets slowmode of 10 seconds)]", inline = False)
        em.add_field(name = clear, value = "Purge a specified number of messages [.clear <number> (Example = .clear 10)]", inline = False)
        em.set_footer(text = f"Page {page}/5")
        await ctx.send(embed = em)

    elif page == 2:
        em = discord.Embed(
            title = "Bot Commands: Reddit (Coding Related)",
            color = discord.Color.red()
        )
        em.add_field(name = webdev, value = "Get a post from the Hot section of the r/webdev subreddit [.webdev]", inline = False)
        em.add_field(name = frontend, value = "Get a post from the Hot section of the r/Frontend subreddit [.frontend]", inline = False)
        em.add_field(name = css, value = "Get a post from the Hot section of the r/CSS subreddit [.css]", inline = False)
        em.add_field(name = javascript, value = "Get a post from the Hot section of the r/javascript subreddit [.javascript]", inline = False)
        em.add_field(name = learnjavascript, value = "Get a post from the Hot section of the r/learnjavascript subreddit [.learnjavascript]", inline = False)
        em.add_field(name = php, value = "Get a post from the Hot section of the r/PHP subreddit [.php]", inline = False)
        em.add_field(name = wordpress, value = "Get a post from the Hot section of the r/wordpress subreddit [.wordpress]", inline = False)
        em.add_field(name = prowordpress, value = "Get a post from the Hot section of the r/prowordpress subreddit [.prowordpress]", inline = False)
        em.add_field(name = rails, value = "Get a post from the Hot section of the r/rails subreddit [.rails]", inline = False)
        em.add_field(name = python, value = "Get a post from the Hot section of the r/python subreddit [.python]", inline = False)
        em.add_field(name = learnpython, value = "Get a post from the Hot section of the r/learnpython subreddit [.learnpython]", inline = False)
        em.add_field(name = pygame, value = "Get a post from the Hot section of the r/pygame subreddit [.pygame]", inline = False)
        em.add_field(name = coding, value = "Get a post from the Hot section of the r/coding subreddit [.coding]", inline = False)
        em.add_field(name = codinghelp, value = "Get a post from the Hot section of the r/codinghelp subreddit [.codinghelp]", inline = False)
        em.add_field(name = learnprogramming, value = "Get a post from the Hot section of the r/learnprogramming subreddit [.learnprogramming]", inline = False)
        em.set_footer(text = f"Page {page}/5")
        await ctx.send(embed = em)
    
    elif page == 3:
        em = discord.Embed(
            title = "Bot Commands: Reddit (Fun)",
            color = discord.Color.teal()
        )
        em.add_field(name = programmerhumor, value = "Get a post from the Hot section of the r/programmerhumor subreddit [.programmerhumor]", inline = False)
        em.add_field(name = programmerdadjoke, value = "Get a post from the Hot section of the r/programmerdadjokes subreddit [.programmerdadjoke]", inline = False)
        em.add_field(name = meme, value = "Get a post from the Hot section of the r/meme subreddit [.meme]", inline = False)
        em.add_field(name = history, value = "Get a post from the Hot section of the r/HistoryMemes subreddit [.history]", inline = False)
        em.add_field(name = prequel, value = "Get a post from the Hot section of the r/prequelmemes subreddit [.prequelmemes]", inline = False)
        em.add_field(name = tifu, value = "Get a post from the Hot section of the r/tifu subreddit [.tifu]", inline = False)
        em.add_field(name = teenagers, value = "Get a post from the Hot section of the r/teenagers subreddit [.teenagers]", inline = False)
        em.add_field(name = programmerhumor, value = "Get a post from the Hot section of the r/programmerhumor subreddit [.programmerhumor]", inline = False)
        em.set_footer(text = f"Page {page}/5")
        await ctx.send(embed = em)
    
    elif page == 4:
        em = discord.Embed(
            title = "Other Bot Commands",
            color = discord.Color.orange()
        )
        em.add_field(name = help, value = "This Command (Choose Between 5 Pages with .help 1/2/3/4/5)", inline = False)
        em.add_field(name = guessnumber, value = "You'll get 4 guesses to guess a number between 1 and 20 [.guessnumber]", inline = False)
        em.set_footer(text = f"Page {page}/5")
        await ctx.send(embed = em)
    
    elif page == 5:
        em = discord.Embed(
            title = "Non-Commands",
            color = discord.Color.greyple()
        )
        em.add_field(name = "ModMail", value = "DM the Bot, and it will relay your message to a private staff chat.", inline = False)
        em.add_field(name = "Blocked Word Detection", value = f"Words that will be censored: ||{filtered_words}||", inline = False)
        em.set_footer(text = f"Page {page}/5")
        await ctx.send(embed = em)


"""
Moderation Commands
"""


"""
Ban & Unban Commands
"""


#Ban Command
@client.command() #Creating a new command
@commands.has_permissions(ban_members = True) #Checking if person calling the command has required permissions
async def ban(ctx,member : discord.Member,*,reason = "No reason provided"): #Creating the arguments required for the command: the member (who will have to be pinged),  and the reason for the ban. Will look like this: .ban @Impact Test

    if member.guild_permissions.kick_members:
        await ctx.send("Sorry, I can't ban Admins!")
        return

    if member == ctx.author:
        await ctx.send("The first law of Isaac Asimov's 3 laws of robotics prohibits me from causing harm (In this case, banning) to you. Although I would like to. Heh")
        return

    try:
        await member.send(f"{member.name} has been banned from <**Coders Central>**. Reason: {reason}") #Will initally ban member through DMs
    except:
        await ctx.send(f"The member has their DMs closed. Ban has still be initiated. Reason: {reason}") #If Bot is blocked, the bot will ban through the channel where the command was called


    await member.ban(reason=reason) #Calling the 'ban' method to ban the specified user using the 'member' variable
    await ctx.send(f"{member} has been banned")

#Unban Command
@client.command() #Creating a new command
@commands.has_permissions(ban_members=True) #Checking if person calling the command has required permissions
async def unban(ctx,*,member): #Creating the arguments required for the command: the member (Who can't be pinged/mentioned, so you will specify who to unban using the username and id tag, e.g: .unban Impact#1704)
    banned_users = await ctx.guild.bans() #Create a variable that accesses the server's banned members
    member_name, member_disc = member.split("#")

    for banned_entry in banned_users: #Uses a for loop to iterate through the banned members
        user = banned_entry.user #Created variable called users

        if (user.name, user.discriminator)==(member_name,member_disc): #Used if statement to check if the member you want to unban is the member which the for loop detected

            await ctx.guild.unban(user) #Calls the unban method on the user
            await ctx.send(f"{member_name} was unbanned.") #Send this message in the channel where the command was called. I could've concatanated the text so it would look like: await ctx.send(member_name + " was unbanned".") but my personal preference is f stringing it. 
            return 
    await ctx.send(f"{member} was not found in the ban list") #If the member was not found, it will send this message instead


#Kick Command
@client.command() #This whole command is the same as the Ban Command, with the exception of the method call member.kick instead of member.ban, as well as sending a differnent message. 
@commands.has_permissions(kick_members = True)
async def kick(ctx,member : discord.Member,*,reason = "No reason provided"):
    
    if member.guild_permissions.kick_members:
        await ctx.send("Sorry, I can't kick Admins!")
        return

    if member == ctx.author:
        await ctx.send("Dude you can't kick yourself smh")
        return


    try:
        await member.send(f"{member.name} has been kicked from <**Coders Central>**. Reason: {reason}")
    except:
        await ctx.send(f"The member has their DMs closed. Kick has still be initiated. Reason: {reason}")


    await member.kick(reason=reason)
    await ctx.send(f"{member} has been kicked")


"""
Addrole & Derole Commands
"""


#Addrole Command
@client.command()
@commands.has_permissions(kick_members=True)
async def addrole(ctx, member : discord.Member, *, role_given : discord.Role): #Creating arguments required for the command; pinging the member and the name of the role you want to give
    await member.add_roles(role_given) #Calling the add_roles method and passing in the argument of the variable 'role_given'
    await ctx.send(f"{member} was given the ''**{role_given}**'' role!")
    

#Derole Command
@client.command()
@commands.has_permissions(kick_members=True)
async def derole(ctx, member : discord.Member, *, role_removed : discord.Role): #Creating arguments required for the command; pinging the member and the name of the role you want to remove
    await member.remove_roles(role_removed) #Calling the remove_roles method and passing in the argument of the variable 'role_removed'
    await ctx.send(f"The ''**{role_removed}**'' role has been removed from {member}")


#Clear/Purge Command
@client.command(aliases = ['purge']) #Created an aliase aka alternate command name that will still work when called
@commands.has_permissions(manage_messages = True) #Checking perms
async def clear(ctx,amount=2): #Set the default value of amount to 2
    amount += 1
    await ctx.channel.purge(limit = amount) #Deleting the messages


#Slowmode Command
@client.command()
@commands.has_permissions(kick_members = True) #Checking perms
async def slowmode(ctx, seconds: int): #the seconds variable has to be a whole number
    if seconds < 0: #Created if statement to check if the integer is below 0
        await ctx.send("Very funny")
        return #Code will return, therefore resetting and not carrying out the rest of the command


    await ctx.channel.edit(slowmode_delay=seconds)
    await ctx.send(f"I set the slowmode delay in this channel to {seconds} seconds!")


"""
Mute & Unmute Commands 
"""


#Mute Command
@client.command()
@commands.has_permissions(kick_members=True) #checking if person calling command has perms
async def mute(ctx, member : discord.Member): #Required args: member
    muted_role = ctx.guild.get_role(id_of_mute_role) #getting id of the role

    if member.guild_permissions.kick_members:
        await ctx.send("Sorry, I can't mute Admins!")
        return
    
    if member == ctx.author:
        await ctx.send("You can't mute yourself")

    await member.add_roles(muted_role) #adding role to member specified

    await ctx.send(member.mention + " has been muted") #awaiting the command


#Unmute Command
@client.command()
@commands.has_permissions(kick_members=True)
async def unmute(ctx, member : discord.Member):
    muted_role = ctx.guild.get_role(id_of_mute_role) 

    await member.remove_roles(muted_role) #removing role instead of adding it to member specified

    await ctx.send(member.mention + " has been unmuted")




"""
Non-Commands
"""
filtered_words = ["example1","example2","example3"]

@client.event
async def on_message(message):
    await client.process_commands(message)
    
    for word in filtered_words:
        if word in message.content.lower():
            await message.delete()
            await message.channel.send(f"{message.author}, that word is blocked!")




    empty_array = []
    modmail_channnel = discord.utils.get(client.get_all_channels(), name = "modmail")
    
    if message.author == client.user:
        return 
    if str(message.channel.type) == "private":
        if message.attachments != empty_array:
            files = message.attachments
            await modmail_channnel.send("[" + message.author.display_name + "] ")
    
            for file in files:
                await modmail_channnel.send(file.url)
        else:
            await modmail_channnel.send("[" + message.author.display_name + "] " + message.content)
    
    elif str(message.channel) == "modmail" and message.content.startswith("<"):
        member_object = message.mentions[0]
        if message.attachments != empty_array:
            files = message.attachments
            await member_object.send("[" + message.author.display_name + "] ")
    
            for file in files:
                await member_object.send(file.url)
        else:
            index = message.content.index(" ")
            string = message.content
            mod_message = string[index:]
            await member_object.send("[" + message.author.display_name + "] " + mod_message)



"""
Reddit Commands w/ Praw
"""


#Insert my Reddit App details
reddit = praw.Reddit(client_id = 'your clientid',
                     client_secret = 'your clientsecret',
                     username = 'your username',
                     password = 'your password',
                     user_agent = "your user agent" )


"""
Programming Related Reddit Commands
"""


#/r/webdev
@client.command()
@cooldown(1, 5, BucketType.user) #Making a 5 second cooldown
async def webdev(ctx): #Command is called "webdev"
    subreddit = reddit.subreddit("webdev") #Pulls reddit posts from r/webdev
    all_subs = []

    hot = subreddit.hot(limit = 100)

    for submission in hot:
        all_subs.append(submission)

    random_sub = random.choice(all_subs)

    name = random_sub.title #name is the submission's post title
    body = random_sub.selftext #body is the submission's body text (if it has any)
    link = random_sub.shortlink #link is the link to the submission
    img = random_sub.url #img is the submission's image attachment (if it has any)
    
    em = discord.Embed(title = name) #Creating an embed
    em.description = body #Setting the description of the embed
    em.set_image(url = img) #Setting the image to the img variable
    em.add_field(name = f"Link to post:", value = link, inline= False) #Adding a field to the embed, which has the value of the link
    
    if hasattr(random_sub, 'preview') == True: #Checking if the submission has the attribute of an image preview of a link
        if 'images' in random_sub.preview:
            preview_image_link = random_sub.preview['images'][0]['source']['url'] #Taking info from an external object
            em.set_image(url = preview_image_link) #Setting the link preview to the embed img
        else:
            return #If there isn't a link preview, return

    await ctx.send(embed = em) #sending the embed


#r/frontend
@client.command()
@cooldown(1, 5, BucketType.user) #Same thing as the previous reddit command, just different subreddit
async def frontend(ctx):
    subreddit = reddit.subreddit("frontend")
    all_subs = []

    hot = subreddit.hot(limit = 100)

    for submission in hot:
        all_subs.append(submission)

    random_sub = random.choice(all_subs)

    name = random_sub.title
    body = random_sub.selftext
    link = random_sub.shortlink
    img = random_sub.url
    
    em = discord.Embed(title = name)
    em.description = body
    em.set_image(url = img)
    em.add_field(name = f"Link to post:", value = link, inline= False)
    
    if hasattr(random_sub, 'preview') == True:
        if 'images' in random_sub.preview:
            preview_image_link = random_sub.preview['images'][0]['source']['url']
            em.set_image(url = preview_image_link)
        else:
            return

    await ctx.send(embed = em)


#r/CSS
@client.command()
@cooldown(1, 5, BucketType.user) #Same thing as the previous reddit command, just different subreddit
async def css(ctx):
    subreddit = reddit.subreddit("css")
    all_subs = []

    hot = subreddit.hot(limit = 100)

    for submission in hot:
        all_subs.append(submission)

    random_sub = random.choice(all_subs)

    name = random_sub.title
    body = random_sub.selftext
    link = random_sub.shortlink
    img = random_sub.url


    em = discord.Embed(title = name)
    em.description = body
    em.set_image(url = img)
    em.add_field(name = f"Link to post:", value = link, inline= False)
    
    if hasattr(random_sub, 'preview') == True:
        if 'images' in random_sub.preview:
            preview_image_link = random_sub.preview['images'][0]['source']['url']
            em.set_image(url = preview_image_link)
        else:
            return

    await ctx.send(embed = em)


#r/javascript
@client.command()
@cooldown(1, 5, BucketType.user) #Same thing as the previous reddit command, just different subreddit
async def javascript(ctx):
    subreddit = reddit.subreddit("javascript")
    all_subs = []

    hot = subreddit.hot(limit = 100)

    for submission in hot:
        all_subs.append(submission)

    random_sub = random.choice(all_subs)

    name = random_sub.title
    body = random_sub.selftext
    link = random_sub.shortlink
    img = random_sub.url


    em = discord.Embed(title = name)
    em.description = body
    em.set_image(url = img)
    em.add_field(name = f"Link to post:", value = link, inline= False)
    

    if hasattr(random_sub, 'preview') == True:
        if 'images' in random_sub.preview:
            preview_image_link = random_sub.preview['images'][0]['source']['url']
            em.set_image(url = preview_image_link)
        else:
            return


    await ctx.send(embed = em)


#r/learnjavascript
@client.command()
@cooldown(1, 5, BucketType.user) #Same thing as the previous reddit command, just different subreddit
async def learnjavascript(ctx):
    subreddit = reddit.subreddit("learnjavascript")
    all_subs = []

    hot = subreddit.hot(limit = 100)

    for submission in hot:
        all_subs.append(submission)

    random_sub = random.choice(all_subs)

    name = random_sub.title
    body = random_sub.selftext
    link = random_sub.shortlink
    img = random_sub.url


    em = discord.Embed(title = name)
    em.description = body
    em.set_image(url = img)
    em.add_field(name = f"Link to post:", value = link, inline= False)


    if hasattr(random_sub, 'preview') == True:
        if 'images' in random_sub.preview:
            preview_image_link = random_sub.preview['images'][0]['source']['url']
            em.set_image(url = preview_image_link)
        else:
            return


    await ctx.send(embed = em)


#php
@client.command()
@cooldown(1, 5, BucketType.user) #Same thing as the previous reddit command, just different subreddit
async def php(ctx):
    subreddit = reddit.subreddit("PHP")
    all_subs = []

    hot = subreddit.hot(limit = 100)

    for submission in hot:
        all_subs.append(submission)

    random_sub = random.choice(all_subs)

    name = random_sub.title
    body = random_sub.selftext
    link = random_sub.shortlink
    img = random_sub.url


    em = discord.Embed(title = name)
    em.description = body
    em.set_image(url = img)
    em.add_field(name = f"Link to post:", value = link, inline= False)


    if hasattr(random_sub, 'preview') == True:
        if 'images' in random_sub.preview:
            preview_image_link = random_sub.preview['images'][0]['source']['url']
            em.set_image(url = preview_image_link)
        else:
            return


    await ctx.send(embed = em)


#Wordpress
@client.command()
@cooldown(1, 5, BucketType.user) #Same thing as the previous reddit command, just different subreddit
async def wordpress(ctx):
    subreddit = reddit.subreddit("Wordpress")
    all_subs = []

    hot = subreddit.hot(limit = 100)

    for submission in hot:
        all_subs.append(submission)

    random_sub = random.choice(all_subs)

    name = random_sub.title
    body = random_sub.selftext
    link = random_sub.shortlink
    img = random_sub.url


    em = discord.Embed(title = name)
    em.description = body
    em.set_image(url = img)
    em.add_field(name = f"Link to post:", value = link, inline= False)


    if hasattr(random_sub, 'preview') == True:
        if 'images' in random_sub.preview:
            preview_image_link = random_sub.preview['images'][0]['source']['url']
            em.set_image(url = preview_image_link)
        else:
            return


    await ctx.send(embed = em)


#prowordpress
@client.command()
@cooldown(1, 5, BucketType.user) #Same thing as the previous reddit command, just different subreddit
async def prowordpress(ctx):
    subreddit = reddit.subreddit("ProWordPress")
    all_subs = []

    hot = subreddit.hot(limit = 100)

    for submission in hot:
        all_subs.append(submission)

    random_sub = random.choice(all_subs)

    name = random_sub.title
    body = random_sub.selftext
    link = random_sub.shortlink
    img = random_sub.url


    em = discord.Embed(title = name)
    em.description = body
    em.set_image(url = img)
    em.add_field(name = f"Link to post:", value = link, inline= False)


    if hasattr(random_sub, 'preview') == True:
        if 'images' in random_sub.preview:
            preview_image_link = random_sub.preview['images'][0]['source']['url']
            em.set_image(url = preview_image_link)
        else:
            return


    await ctx.send(embed = em)


#rails
@client.command()
@cooldown(1, 5, BucketType.user) #Same thing as the previous reddit command, just different subreddit
async def rails(ctx):
    subreddit = reddit.subreddit("rails")
    all_subs = []

    hot = subreddit.hot(limit = 100)

    for submission in hot:
        all_subs.append(submission)

    random_sub = random.choice(all_subs)

    name = random_sub.title
    body = random_sub.selftext
    link = random_sub.shortlink
    img = random_sub.url


    em = discord.Embed(title = name)
    em.description = body
    em.set_image(url = img)
    em.add_field(name = f"Link to post:", value = link, inline= False)


    if hasattr(random_sub, 'preview') == True:
        if 'images' in random_sub.preview:
            preview_image_link = random_sub.preview['images'][0]['source']['url']
            em.set_image(url = preview_image_link)
        else:
            return


    await ctx.send(embed = em)


#python
@client.command()
@cooldown(1, 5, BucketType.user) #Same thing as the previous reddit command, just different subreddit
async def python(ctx):
    subreddit = reddit.subreddit("python")
    all_subs = []

    hot = subreddit.hot(limit = 100)

    for submission in hot:
        all_subs.append(submission)

    random_sub = random.choice(all_subs)

    name = random_sub.title
    body = random_sub.selftext
    link = random_sub.shortlink
    img = random_sub.url


    em = discord.Embed(title = name)
    em.description = body
    em.set_image(url = img)
    em.add_field(name = f"Link to post:", value = link, inline= False)


    if hasattr(random_sub, 'preview') == True:
        if 'images' in random_sub.preview:
            preview_image_link = random_sub.preview['images'][0]['source']['url']
            em.set_image(url = preview_image_link)
        else:
            return


    await ctx.send(embed = em)


#coding
@client.command()
@cooldown(1, 5, BucketType.user) #Same thing as the previous reddit command, just different subreddit
async def coding(ctx):
    subreddit = reddit.subreddit("coding")
    all_subs = []

    hot = subreddit.hot(limit = 100)

    for submission in hot:
        all_subs.append(submission)

    random_sub = random.choice(all_subs)

    name = random_sub.title
    body = random_sub.selftext
    link = random_sub.shortlink
    img = random_sub.url


    em = discord.Embed(title = name)
    em.description = body
    em.set_image(url = img)
    em.add_field(name = f"Link to post:", value = link, inline= False)


    if hasattr(random_sub, 'preview') == True:
        if 'images' in random_sub.preview:
            preview_image_link = random_sub.preview['images'][0]['source']['url']
            em.set_image(url = preview_image_link)
        else:
            return


    await ctx.send(embed = em)


#codinghelp
@client.command()
@cooldown(1, 5, BucketType.user) #Same thing as the previous reddit command, just different subreddit
async def codinghelp(ctx):
    subreddit = reddit.subreddit("CodingHelp")
    all_subs = []

    hot = subreddit.hot(limit = 100)

    for submission in hot:
        all_subs.append(submission)

    random_sub = random.choice(all_subs)

    name = random_sub.title
    body = random_sub.selftext
    link = random_sub.shortlink
    img = random_sub.url


    em = discord.Embed(title = name)
    em.description = body
    em.set_image(url = img)
    em.add_field(name = f"Link to post:", value = link, inline= False)


    if hasattr(random_sub, 'preview') == True:
        if 'images' in random_sub.preview:
            preview_image_link = random_sub.preview['images'][0]['source']['url']
            em.set_image(url = preview_image_link)
        else:
            return


    await ctx.send(embed = em)


#learnpython
@client.command()
@cooldown(1, 5, BucketType.user) #Same thing as the previous reddit command, just different subreddit
async def learnpython(ctx):
    subreddit = reddit.subreddit("learnpython")
    all_subs = []

    hot = subreddit.hot(limit = 100)

    for submission in hot:
        all_subs.append(submission)

    random_sub = random.choice(all_subs)

    name = random_sub.title
    body = random_sub.selftext
    link = random_sub.shortlink
    img = random_sub.url


    em = discord.Embed(title = name)
    em.description = body
    em.set_image(url = img)
    em.add_field(name = f"Link to post:", value = link, inline= False)


    if hasattr(random_sub, 'preview') == True:
        if 'images' in random_sub.preview:
            preview_image_link = random_sub.preview['images'][0]['source']['url']
            em.set_image(url = preview_image_link)
        else:
            return


    await ctx.send(embed = em)


#programmerhumor
@client.command()
@cooldown(1, 5, BucketType.user) #Same thing as the previous reddit command, just different subreddit
async def programmerhumor(ctx):
    subreddit = reddit.subreddit("ProgrammerHumor")
    all_subs = []

    hot = subreddit.hot(limit = 100)

    for submission in hot:
        all_subs.append(submission)

    random_sub = random.choice(all_subs)

    name = random_sub.title
    body = random_sub.selftext
    link = random_sub.shortlink
    img = random_sub.url


    em = discord.Embed(title = name)
    em.description = body
    em.set_image(url = img)
    em.add_field(name = f"Link to post:", value = link, inline= False)


    if hasattr(random_sub, 'preview') == True:
        if 'images' in random_sub.preview:
            preview_image_link = random_sub.preview['images'][0]['source']['url']
            em.set_image(url = preview_image_link)
        else:
            return


    await ctx.send(embed = em)


#learnprogramming
@client.command()
@cooldown(1, 5, BucketType.user) #Same thing as the previous reddit command, just different subreddit
async def learnprogramming(ctx):
    subreddit = reddit.subreddit("learnprogramming")
    all_subs = []

    hot = subreddit.hot(limit = 100)

    for submission in hot:
        all_subs.append(submission)

    random_sub = random.choice(all_subs)

    name = random_sub.title
    body = random_sub.selftext
    link = random_sub.shortlink
    img = random_sub.url


    em = discord.Embed(title = name)
    em.description = body
    em.set_image(url = img)
    em.add_field(name = f"Link to post:", value = link, inline= False)


    if hasattr(random_sub, 'preview') == True:
        if 'images' in random_sub.preview:
            preview_image_link = random_sub.preview['images'][0]['source']['url']
            em.set_image(url = preview_image_link)
        else:
            return


    await ctx.send(embed = em)


#pygame
@client.command()
@cooldown(1, 5, BucketType.user) #Same thing as the previous reddit command, just different subreddit
async def pygame(ctx):
    subreddit = reddit.subreddit("pygame")
    all_subs = []

    hot = subreddit.hot(limit = 100)

    for submission in hot:
        all_subs.append(submission)

    random_sub = random.choice(all_subs)

    name = random_sub.title
    body = random_sub.selftext
    link = random_sub.shortlink
    img = random_sub.url


    em = discord.Embed(title = name)
    em.description = body
    em.set_image(url = img)
    em.add_field(name = f"Link to post:", value = link, inline= False)
    
    if hasattr(random_sub, 'preview') == True:
        if 'images' in random_sub.preview:
            preview_image_link = random_sub.preview['images'][0]['source']['url']
            em.set_image(url = preview_image_link)
        else:
            return


    await ctx.send(embed = em)


#programmer dad jokes
@client.command()
@cooldown(1, 5, BucketType.user) #Same thing as the previous reddit command, just different subreddit
async def programmerdadjoke(ctx):
    subreddit = reddit.subreddit("ProgrammerDadJokes")
    all_subs = []

    hot = subreddit.hot(limit = 100)

    for submission in hot:
        all_subs.append(submission)

    random_sub = random.choice(all_subs)

    name = random_sub.title
    body = random_sub.selftext
    link = random_sub.shortlink
    img = random_sub.url


    em = discord.Embed(title = name)
    em.description = body
    em.set_image(url = img)
    em.add_field(name = f"Link to post:", value = link, inline= False)
    
    if hasattr(random_sub, 'preview') == True:
        if 'images' in random_sub.preview:
            preview_image_link = random_sub.preview['images'][0]['source']['url']
            em.set_image(url = preview_image_link)
        else:
            return


    await ctx.send(embed = em)


"""
Start of Non-coding Reddit commands
"""


#meme
@client.command()
@cooldown(1, 5, BucketType.user) #Same thing as the previous reddit command, just different subreddit
async def meme(ctx):
    subreddit = reddit.subreddit("memes")
    all_subs = []

    hot = subreddit.hot(limit = 100)

    for submission in hot:
        all_subs.append(submission)

    random_sub = random.choice(all_subs)

    name = random_sub.title
    body = random_sub.selftext
    link = random_sub.shortlink
    img = random_sub.url


    em = discord.Embed(title = name)
    em.description = body
    em.set_image(url = img)
    em.add_field(name = f"Link to post:", value = link, inline= False)
    
    if hasattr(random_sub, 'preview') == True:
        if 'images' in random_sub.preview:
            preview_image_link = random_sub.preview['images'][0]['source']['url']
            em.set_image(url = preview_image_link)
        else:
            return


    await ctx.send(embed = em)


#history
@client.command()
@cooldown(1, 5, BucketType.user) #Same thing as the previous reddit command, just different subreddit
async def history(ctx):
    subreddit = reddit.subreddit("HistoryMemes")
    all_subs = []

    hot = subreddit.hot(limit = 100)

    for submission in hot:
        all_subs.append(submission)

    random_sub = random.choice(all_subs)

    name = random_sub.title
    body = random_sub.selftext
    link = random_sub.shortlink
    img = random_sub.url


    em = discord.Embed(title = name)
    em.description = body
    em.set_image(url = img)
    em.add_field(name = f"Link to post:", value = link, inline= False)
    
    if hasattr(random_sub, 'preview') == True:
        if 'images' in random_sub.preview:
            preview_image_link = random_sub.preview['images'][0]['source']['url']
            em.set_image(url = preview_image_link)
        else:
            return


    await ctx.send(embed = em)


#prequel
@client.command()
@cooldown(1, 5, BucketType.user) #Same thing as the previous reddit command, just different subreddit
async def prequel(ctx):
    subreddit = reddit.subreddit("PrequelMemes")
    all_subs = []

    hot = subreddit.hot(limit = 100)

    for submission in hot:
        all_subs.append(submission)

    random_sub = random.choice(all_subs)

    name = random_sub.title
    body = random_sub.selftext
    link = random_sub.shortlink
    img = random_sub.url


    em = discord.Embed(title = name)
    em.description = body
    em.set_image(url = img)
    em.add_field(name = f"Link to post:", value = link, inline= False)
    
    if hasattr(random_sub, 'preview') == True:
        if 'images' in random_sub.preview:
            preview_image_link = random_sub.preview['images'][0]['source']['url']
            em.set_image(url = preview_image_link)
        else:
            return


    await ctx.send(embed = em)


#tifu
@client.command()
@cooldown(1, 5, BucketType.user) #Same thing as the previous reddit command, just different subreddit
async def tifu(ctx):
    subreddit = reddit.subreddit("TIFU")
    all_subs = []

    hot = subreddit.hot(limit = 100)

    for submission in hot:
        all_subs.append(submission)

    random_sub = random.choice(all_subs)

    name = random_sub.title
    body = random_sub.selftext
    link = random_sub.shortlink

    em = discord.Embed(title = name)
    em.description = body
    
    em.add_field(name = f"Link to post:", value = link, inline= False)
    
    await ctx.send(embed = em)


#teenagers
@client.command()
@cooldown(1, 5, BucketType.user) #Same thing as the previous reddit command, just different subreddit
async def teenagers(ctx):
    subreddit = reddit.subreddit("teenagers")
    all_subs = []

    hot = subreddit.hot(limit = 100)

    for submission in hot:
        all_subs.append(submission)

    random_sub = random.choice(all_subs)

    name = random_sub.title
    body = random_sub.selftext
    link = random_sub.shortlink
    img = random_sub.url
    em = discord.Embed(title = name)
    em.description = body
    em.set_image(url = img)
    em.add_field(name = f"Link to post:", value = link, inline= False)

    if img == None:
        print("") #The subreddit allows both images and text only posts, checking if the post has an image or not
    else:
        if hasattr(random_sub, 'preview') == True:
            if 'images' in random_sub.preview:
                preview_image_link = random_sub.preview['images'][0]['source']['url']
                em.set_image(url = preview_image_link)
            else:
                return

    
    
    
    


    await ctx.send(embed = em)


"""
Fun Commands
"""


@client.command()
@cooldown(1, 5, BucketType.user)
async def guessnumber(ctx):

    await ctx.send(f"Hello {ctx.author.name}! I'm thinking of a number between 1 and 20. You are given 4 tries to find the number. If you guess correctly, you'll be given nothing! Good luck!")
    secretNumber = random.randint(1,20)

    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel  and message.content.isdigit()

    for guessesTaken in range(1,5):

        guess = int((await client.wait_for('message', check=check)).content)

        if guess < secretNumber:
            await ctx.send("Your guess is too low")
        elif guess > secretNumber:
            await ctx.send("Your guess is too high")
        else:
            break

    if guess == secretNumber:
        await ctx.send(f"GG! You correctly guessed the number in {guessesTaken} guesses!")
    else:
        await ctx.send(f"Nope, sorry, you took to many guesses. The number I was thinking of was {secretNumber}")


"""
Error Handling
"""


@client.event
async def on_command_error(ctx,error):
    if isinstance(error,commands.MissingPermissions):
        await ctx.send("You're missing permissions to execute that command!")
    elif isinstance(error,commands.MissingRequiredArgument):
        await ctx.send("Please enter all the required arguements!")
    elif isinstance(error, CommandOnCooldown):
        await ctx.send(f"This command is on cooldown! Please wait `{error.retry_after:,.2f}` seconds until you use it again.")


"""
Status
"""


@client.event
async def on_ready():
    print("")
    print("Bot is online")
    print(f"Client Token: {token}")
    print("-----------------------")
    bot_testing_channel = discord.utils.get(client.get_all_channels(), name = "channel name here")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="status here"))
    await bot_testing_channel.send("`Bot is online`")
    

"""
Running the bot
"""


client.run(token)
















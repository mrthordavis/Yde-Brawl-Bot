import discord
from discord.ext import commands
import asyncio #Used for asyncio.sleep()
import time #Used for ping cmd


bot = commands.Bot(command_prefix = "!", owner_id = 322449414142558208, case_insensitive=True)
bot.remove_command("help") #Used for the custom help cmd


blue_colour = 0x0098FD
log_colour = 0xF9D14A


@bot.event
async def on_ready():
    print("Bot is online")
    print("Discord Version: " + discord.__version__)
    print("Bot ID: " + str(bot.user.id))
    print("Bot Name: " + str(bot.user.name))
    print("Prefix: '!'")
    print("---------")
    await bot.change_presence(activity=discord.Activity(name="Yde - Brawl Stars", type=discord.ActivityType.watching))


#Events

@bot.event
async def on_member_join(member):
    global blue_colour
    #Sends welcome messsage in #general
    bot_count = sum(m.bot for m in member.guild.members)
    human_count = len(member.guild.members) - bot_count
    embed = discord.Embed(title="Welcome", description=f"Welcome {member.name}! Check out <#507933597785915393> and enjoy your time here!", colour=blue_colour)
    embed.set_footer(text=f"You are the {human_count}th member!")
    await bot.get_channel(507250791002931201).send(embed=embed)

    #Logs
    log = discord.Embed(title="User Joined", description=f"{member.name} joined the server!", colour=0xF9D14A)
    await bot.get_channel(542012361775513621).send(embed=log)

    #Roles to add
    sub_role = discord.utils.get(member.guild.roles, id=508210020005969921)
    achievements = discord.utils.get(member.guild.roles, id=513776818088706051)
    tenk = discord.utils.get(member.guild.roles, id=544950063487778846)
    await member.add_roles(sub_role, achievements, tenk)


@bot.event
async def on_member_leave(member):
    #Logs
    log = discord.Embed(title="User Left", description=f"{member.name} left the server!", colour=0xF9D14A)
    await bot.get_channel(542012361775513621).send(embed=log)


@bot.event
async def on_message_delete(message):
    #Logs
    if message.author.bot:
        return
    embed = discord.Embed(title="Message Deletion", description=f"{message.author} deleted a message in <#{message.channel.id}>\nContent: `{message.content}`", colour=0xF9D14A)
    await bot.get_channel(542012361775513621).send(embed=embed)


@bot.event
async def on_command_error(ctx, error):
    print(error)
    if isinstance(error, commands.CommandNotFound):
        return
    await bot.get_channel(544249107762511873).send(f"An error has occured:\nCommand: `{ctx.message.content}`\nChannel: `{ctx.message.channel}`\nAuthor: `{ctx.message.author}` ```{error}```")
    await ctx.send("Something went wrong, please try again and if you're still having issues contact <@322449414142558208>")


#Commands

@bot.command()
async def help(ctx):
    #Commands
    embed = discord.Embed(title="Commands", description="`!join <role>` - Joins the role specified\n`!social` - Displays all Yde's social media accounts\n`!ping` - Shows the bots ping in ms\n`!suggest <Suggestion>` - Creates a suggestion, which will be displayed in the sugggestions channel\n`!comment <ID> <Comment>` - Creates a comment on an existing embed\n`!help` - Displays this message", colour=0x0098FD)
    #Staff commands
    embed.add_field(name="Staff Commands", value="`!kick <@user> <reason>` - Kicks the user tagged (The reason is optional)\n`!ban <@user> <reason>` - Bans the user tagged (The reason is optional)\n`!delete <amount>` - Deletes a specified amount of messages")
    embed.set_footer(text="Please note that I'm still under development")
    await ctx.send(embed=embed)


@bot.command(aliases=["socials", "links"])
async def social(ctx):
    embed = discord.Embed(title="Yde's Socials", description="[Twitter!](https://twitter.com/YdeBrawlStars)\n[Youtube!]( https://www.youtube.com/channel/UCOuBW7wkRaMMjMt6huBtMLg)\n[Instagram!](https://www.instagram.com/ydebrawlstars/)\n[Discord Server!](https://discord.gg/XeGjz6E)", colour=0x0098FD)
    await ctx.send(embed=embed)


@bot.command(aliases=["pong", "latency"])
async def ping(ctx):
    start = time.time() * 1000
    msg = await ctx.message.channel.send("Pong!")
    end = time.time() * 1000
    await msg.edit(content=f"Pong! `{(str(int(round(end-start, 0))))}ms` :ping_pong:")


@bot.command()
async def join(ctx, role: str = None):
    if role == None:
        await ctx.send("You forgot to specify which role you would like to join.\nCorrect syntax: `!join <role>`")
    else:
        list_of_roles = ["subscriber"]
        if role.lower() in list_of_roles:
            sub_role = discord.utils.get(ctx.message.guild.roles, id=508210020005969921)
            if sub_role in ctx.message.author.roles:
                await ctx.message.author.remove_roles(sub_role)
                await ctx.send(f"You successfully left the `{sub_role}` role!")
            else:
                await ctx.message.author.add_roles(sub_role)
                await ctx.send(f"You successfully joined the `{sub_role}` role!")
        else:
            await ctx.send(f"I couldn't find the role you were looking for.\nList of available roles: `{list_of_roles}`")


#Informative Commands

@bot.command()
@commands.is_owner()
async def servers(ctx):
    embed = discord.Embed(title="Brawl Star Related Servers", description="[Jeff's Hideout](https://discord.gg/UCNcufE)\n[Tryhard Youtube](https://discord.gg/NTu8cWB)\n[TKA Brew](https://discord.gg/FhUk8wr)\n[The Coop](https://discord.gg/Nr4pJur)\n[BS World Cup](https://discord.gg/TXGUYGt)\n[Brawl Cup](https://discord.gg/2uprKmB)\n[Nova Champion League](https://discord.gg/NGbqWGk)\n[Ark - Brawl Stars](https://discord.gg/jyc36Wr)\n[Rey - Brawl Stars](https://discord.gg/M76VRuz)\n[Brawlverse's Super Secret Club!](https://discord.gg/eMKGamu)\n[Youtube Community - Ash](https://discord.gg/JD2UX3H)\n[/r/BrawlStars](https://discord.gg/P9ja3qW)\n[KariosTime Kingdom](https://discord.gg/Xyz2344)\n[Brawl Stats](https://discord.gg/PzGHeH3)\n[Coach Cory - Brawl Stats](https://discord.gg/rDT5mcs)", colour=0x0098FD)
    embed.set_footer(text="If any of the links aren't working then contact Alpha#5960")
    await ctx.message.delete()
    await ctx.send(embed=embed)


@bot.command()
@commands.is_owner()
async def achievements(ctx):
    embed = discord.Embed(title="Achievements", colour=0x0098FD)
    embed.add_field(name="Before 250 Subscribers:", value="Exclusive role to people who joined before I had 250 subscribers on my YT channel!")
    embed.add_field(name="Before 500 Subscribers:", value="Exclusive role to people who joined before I had 500 subscribers on my YT channel!")
    embed.add_field(name="Before 1000 Subscribers:", value="Exclusive role to people who joined before I had 1000 subscribers on my YT channel!")
    embed.add_field(name="Before 2500 Subscribers:", value="Exclusive role to people who joined before I had 2500 subscribers on my YT channel!")
    embed.add_field(name="Before 5000 Subscribers:", value="Exclusive role to people who joined before I had 5000 subscribers on my YT channel!")
    embed.add_field(name="Goal Accomplished", value="Reach 10k trophies in Brawl Stars")
    embed.add_field(name="Beta Player", value="Exclusive role to people who joined this discord server and claimed the role before Brawl Stars was globally released!")
    embed.set_footer(text="If you want to redeem one of the achievements then ping an admin in a text channel")
    await ctx.message.delete()
    await ctx.send(embed=embed)


@bot.command()
@commands.is_owner()
async def rules(ctx):
    #Rules
    embed = discord.Embed(title="Official Server Rules", description="1) Distribution of Malicious Software (Viruses, IP grabbers or Harmware) will result in an immediate and permanent ban.\n2) All advertising must be posted in <#508212633560678428>.\n3) Please don't spam or ping someone without a proper reason.\n4) Don't reveal personal information without permission.\n5) Keep all the channels SFW (Safe for work)\n6) Please use all channes for their intended purpose\n7) Use common sense and dont be inappropriate", colour=0x0098FD)
    embed.set_footer(text="Failure to comply with these rules will result in a punishment")
    await ctx.message.delete()
    await ctx.send(embed=embed)

    #Info
    info = discord.Embed(title="Socials", description="[Twitter!](https://twitter.com/YdeBrawlStars)\n[Youtube!]( https://www.youtube.com/channel/UCOuBW7wkRaMMjMt6huBtMLg)\n[Instagram!](https://www.instagram.com/ydebrawlstars/)\n[Discord Server!](https://discord.gg/XeGjz6E)", colour=0x0098FD)
    await ctx.send(embed=info)

    #Faq
    commands = discord.Embed(title="FAQ", colour=0x0098FD)
    commands.add_field(name="How Do I Get The Subscriber Role?", value="When you join the server you get assigned to the role. If you want to opt-out/in of the role run `!join subscriber` in <#508681422748254218>")
    commands.add_field(name="Has Yde Got A Club In Brawl Stars?", value="Yde has a club in Brawl Stars. To join the club just press [This link!](https://link.brawlstars.com/invite/band/en?tag=20YUYUJV&token=7pk3f8ej)")
    commands.add_field(name="What Commands Are There?", value="All my commands can be found by typing `!help`.")
    commands.add_field(name="Where Can I Suggest Something?", value="You can suggest stuff in <#508681422748254218>. Just run `!suggest <suggestion>`")
    commands.add_field(name="What's The Official Server Invite?", value="The official server invite is: https://discord.gg/XeGjz6E")
    commands.set_footer(text="Please note that I'm still under development and if you experience any issues please report them to Alpha#5960")
    await ctx.send(embed=commands)


#Moderation Commands

@bot.command(aliases=["delete", "nuke", "clear"])
@commands.has_permissions(manage_messages=True)
async def purge(ctx, amount: int = None):
    if amount == None:
        await ctx.send("You forgot to specify the amount of messages you would like to delete.\nCorrect syntax: `!delete <amount>`")
    else:
        await ctx.channel.purge(limit=amount+1)
        msg = await ctx.send(f"Successfully cleared {amount} messages")
        await asyncio.sleep(5)
        await msg.delete()


@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, user: discord.Member = None, *, reason: str = None):
    global log_colour
    if user == None:
        await ctx.send("You forgot to specify which user you would like to ban.\nCorrect syntax: `!ban <@user> <reason>`")
    else:
        if reason == None:
            await user.ban()
            await ctx.send(f"Successfully banned {user.name}.")
        else:
            await user.ban(reason=reason)
            await ctx.send(f"Successfully banned {user.name}.\nReason: `{reason}`")

    #Log
    if reason == None:
        embed = discord.Embed(title="Ban", description=f"{user.name} has been banned by {ctx.author.name}.\nReason: `No reason given`", colour=log_colour)
    else:
        embed = discord.Embed(title="Ban", description=f"{user.name} has been banned by {ctx.author.name}.\nReason: `{reason}`", colour=log_colour)
    await bot.get_channel(542012361775513621).send(embed=embed)


@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.Member = None, *, reason: str = None):
    global log_colour
    if user == None:
        await ctx.send("You forgot to specify which user you would like to kick.\nCorrect syntax: `!kick <@user> <reason>`")
    else:
        if reason == None:
            await user.kick()
            await ctx.send(f"Successfully kicked {user.name}")
        else:
            await user.kick(reason=reason)
            await ctx.send(f"Successfully kicked {user.name}.\nReason: `{reason}`")
    #Log
    if reason == None:
        embed = discord.Embed(title="Kick", description=f"{user.name} has been kicked by {ctx.author.name}.\nReason: `No reason given`", colour=log_colour)
    else:
        embed = discord.Embed(title="Kick", description=f"{user.name} has been kicked by {ctx.author.name}.\nReason: `{reason}`", colour=log_colour)
    await bot.get_channel(542012361775513621).send(embed=embed)


#Suggestion system

@bot.command()
async def suggest(ctx, *, suggestion: str = None):

    global log_colour

    if suggestion == None:
        await ctx.send("You didn't post a suggestion\nCorrect syntax: `!suggest <suggestion>`")
    else:
        embed = discord.Embed(colour=log_colour)
        embed.set_author(name=f"Suggestion by {ctx.message.author}")
        embed.add_field(name="Content", value=suggestion)
        msg = await bot.get_channel(546839604704182282).send(embed=embed)
        embed.set_footer(text="Sugggestion ID: " + str(msg.id))
        await msg.edit(embed=embed)
        await ctx.send("Successfully submitted your suggestion to <#546839604704182282>")


@bot.command()
async def comment(ctx, id: str, *, comment: str = None):
    if comment == None:
        await ctx.send("Wrong syntax\nCorrect syntax: `!comment <ID> <comment>`")
    else:
        suggestion_log = bot.get_channel(546839604704182282)
        async for message in suggestion_log.history():
            if id in message.embeds[0].footer.text:
                embed = message.embeds[0]
                embed.add_field(name=f"{ctx.message.author.name}'s Comment", value=comment, inline=False)
                await message.edit(embed=embed)


bot.run(TOKEN)

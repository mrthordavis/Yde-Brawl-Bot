import discord
from discord.ext import commands
import asyncio #Used for asyncio.sleep()


bot = commands.Bot(command_prefix = "!", owner_id = 322449414142558208, case_insensitive=True)
bot.remove_command("help") #Used for the custom help cmd


@bot.event
async def on_ready():
    print("Bot is online")
    print("Version: " + discord.__version__)
    print("Bot ID: " + str(bot.user.id))
    print("Bot Name: " + str(bot.user.name))
    print("Prefix: '!'")
    print("---------")
    await bot.change_presence(activity=discord.Activity(name="Yde - Brawl Stars", type=discord.ActivityType.watching))


#Events

@bot.event
async def on_member_join(member):
    #Sends welcome messsage in #general
    bot_count = sum(m.bot for m in member.guild.members)
    human_count = len(member.message.guild.members) - bot_count
    embed = discord.Embed(title="Welcome", description=f"Welcome {member.name}! Make sure to check out <#507933597785915393>. We hope you enjoy your time here!",colour=0x0098FD)
    embed.set_footer(text=f"You are the {human_count}th member!")
    await bot.get_channel(507579059547537460).send(embed=embed)

    #Logs
    log = discord.Embed(title="User Joined", description=f"{member.name} joined the server!", colour=0xF9D14A)
    await bot.get_channel(542012361775513621).send(embed=log)


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
    await ctx.send("Something went wrong, please try again and if you're still having issues contact <@322449414142558208>")


#Commands

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Commands", description="!join <role> - Joins the role specified\n!social - Displays all Yde's social media accounts\n!help - Displays this message", colour=0x0098FD)
    embed.add_field(name="Staff Commands", value="!kick <@user> <reason> - Kicks the user tagged (The reason is optional)\n!ban <@user> <reason> - Bans the user tagged (The reason is optional)\n!delete <amount> - Deletes a specified amount of messages")
    embed.set_footer(text="Please note that I'm still under development")
    await ctx.send(embed=embed)


@bot.command(aliases=["socials", "links"])
async def social(ctx):
    embed = discord.Embed(title="Yde's Socials", description="[Twitter!](https://twitter.com/YdeBrawlStars)\n[Youtube!]( https://www.youtube.com/channel/UCOuBW7wkRaMMjMt6huBtMLg)\n[Instagram!](https://www.instagram.com/ydebrawlstars/)\n[Discord Server!](https://discord.gg/XeGjz6E)", colour=0x0098FD)
    await ctx.send(embed=embed)


@bot.command()
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
async def rules(ctx):
    #Rules
    embed = discord.Embed(title="Official Server Rules", description="**1)** Distribution of Malicious Software (Viruses, IP grabbers or Harmware) will result in an immediate and permanent ban.\n**2)** All advertising must be posted in <#508212633560678428>.\n**3)** Please don't spam or ping someone without a proper reason.\n**4)** Don't reveal personal information without permission.\n**5)** Keep all the channels SFW (Safe for work)\n**6)** Please use all channes for their intended purpose\n**7)** Use common sense and dont be inappropriate", colour=0x0098FD)
    embed.set_footer(text="Failure to comply with these rules will result in a punishment")
    await ctx.message.delete()
    await ctx.send(embed=embed)

    #Info
    info = discord.Embed(title="Socials", description="[Twitter!](https://twitter.com/YdeBrawlStars)\n[Youtube!]( https://www.youtube.com/channel/UCOuBW7wkRaMMjMt6huBtMLg)\n[Instagram!](https://www.instagram.com/ydebrawlstars/)\n[Discord Server!](https://discord.gg/XeGjz6E)", colour=0x0098FD)
    await ctx.send(embed=info)

    #Faq
    commands = discord.Embed(title="FAQ", colour=0x0098FD)
    commands.add_field(name="How Do I Get The Subscriber Role?", value="To get the subscriber role all you have to do is type `!join subscriber` in <#508681422748254218>")
    commands.add_field(name="Has Yde Got A Club In Brawl Stars?", value="Yde has a club in Brawl Stars. To join the club just press [This link!](https://link.brawlstars.com/invite/band/en?tag=20YUYUJV&token=7pk3f8ej)")
    commands.add_field(name="What Commands Are There?", value="All my commands can be found by typing `!help`.")
    commands.add_field(name="Where Can I Suggest Something?", value="You can suggest discord-related stuff in <#511970909217882133> and video ideas in <#508211560158855179>")
    commands.add_field(name="What's The Official Server Invite?", value="The official server invite is: https://discord.gg/XeGjz6E")
    commands.set_footer(text="Please note that I'm still under development and if you experience any issues please report them to @Alpha#5960")
    await ctx.send(embed=commands)


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
async def ban(ctx, user: discord.Member = None, reason: str = None):
    if user == None:
        await ctx.send("You forgot to specify which user you would like to ban.\nCorrect syntax: `!ban <@user> <reason>`")
    else:
        if reason == None:
            await user.ban()
        else:
            await user.ban(reason=reason)
        await ctx.send(f"Successfully banned {user.name}")


@bot.command()
async def kick(ctx, user: discord.Member = None, reason: str = None):
    if user == None:
        await ctx.send("You forgot to specify which user you would like to kick.\nCorrect syntax: `!kick <@user> <reason>`")
    else:
        if reason == None:
            await user.kick()
        else:
            await user.kick(reason=reason)
        await ctx.send(f"Successfully kicked {user.name}")


bot.run("TOKEN")
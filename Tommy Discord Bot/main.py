from keepalive import keep_alive
import os
import discord
from datetime import datetime
from discord.ext import commands
from discord.utils import get
import asyncio

my_secret = os.environ['Secret']

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix=".", intents=intents)

@client.event
async def on_ready():
    print('{0.user} is Online'.format(client))
  

#Command for messages Ex: if user says "[Text]" then bot will respond with "[Text]"

#Temporary way to delete message history of people who left.
@client.event
async def on_member_remove(member: discord.Member):
  if Toggle:
    await member.ban()
    await member.unban()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("https://discord.gg"):
      if message.author.guild_permissions.administrator: 
        pass
      else:
        await message.delete()
        await message.channel.send("You cannot send invites. Moderators have been notified.")
        channel = get(client.get_all_channels(), guild__name='Horny Horizon', name='mod-mail')
        embed = discord.Embed(title='Warning', description=f"{message.author}, tried sending a discord link.",color=000000)
        await channel.send(embed=embed)



    await client.process_commands(message)


#.clean [amt of msgs]
@client.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def clean(ctx, amount=0):
    await ctx.channel.purge(limit=int(amount) + 1)


#This will auto-ban new accounts under a week old
@client.event
async def on_member_join(member):
    if ((datetime.now() - member.created_at).days) < 8:
        await member.kick()


#.kick [User]
@client.command(pass_context=True)
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member):
    await member.kick()
    embed=discord.Embed(title="User Kicked", description=f"{member} has been Kicked from {ctx.guild.name}.", color=000000)
    await ctx.send(embed=embed)
    message = f"You have been kicked from {ctx.guild.name}."
    await member.send(message)

#.ban [User]
@client.command(pass_context=True)
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member):
    global Toggle
    Toggle = False
    if Toggle == False:
      await member.ban()
      embed=discord.Embed(title="User Banned", description=f"{member} has been banned from {ctx.guild.name}.", color=000000)
      await ctx.send(embed=embed)
      Toggle = not Toggle


#.echo [Channel] [Msg]
@client.command(pass_context=True)
async def echo(ctx, destination: discord.TextChannel=None,*, msg: str):
  destination = ctx.message.channel if destination is None else destination
  await destination.send(msg)

#.mute [User]
@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def mute(ctx, member: discord.Member):
  role = discord.utils.get(ctx.guild.roles, name="Muted")
  await member.add_roles(role)
  embed=discord.Embed(title="User Muted", description="**{0}** was muted by **{1}**!".format(member, ctx.message.author), color=000000)
  await ctx.send(embed=embed)

#.confess [Message]
@client.command(pass_context=True)
@commands.dm_only()
async def confess(ctx,*,message: str):
    channel = get(client.get_all_channels(), guild__name='Horny Horizon', name='﹕⛩・confession')
    embed = discord.Embed(title='Anonymous Confession', description=f'{message}',color=000000)
    embed.set_footer(text='DM ".confess [Text]" to confess.')
    await channel.send(embed=embed)

#.mail [Message] Basically mails mod to a channel
@client.command(pass_context=True)
@commands.dm_only()
async def mail(ctx,*,message: str):
    channel = get(client.get_all_channels(), guild__name='Horny Horizon', name='mod-mail')
    embed = discord.Embed(title='**{0}**'.format(ctx.message.author), description=f'{message}',color=000000)
    await channel.send(embed=embed)

#.giverole [User] [Role] 
#Note - Bot rank must be higher than the rank itself
@client.command(pass_content=True)
@commands.has_permissions(administrator=True)
async def giverole(ctx, member: discord.Member, *, role: discord.Role):  
  await member.add_roles(role)

#.embed #channel [tite] | [descrip]
@client.command(pass_content=True)
async def embed (ctx,destination: discord.TextChannel=None, *, content: str):
  destination = ctx.message.channel if destination is None else destination
  title, description = content.split('|')
  embed = discord.Embed(title=title, description=description, color=000000)
  await destination.send(embed=embed)

#if isinstance(ctx.channel, discord.channel.DMChannel):
#Basically checks to see if it is in DMs

#enable or disable commands
#command = client.get_command('')
#command.update(enabled=False)

Toggle = True
@client.command(pass_content=True)
@commands.has_permissions(administrator=True)
async def toggle(ctx):
    global Toggle
    Toggle = not Toggle
    if Toggle == True:
      await ctx.message.channel.send("Ban disabled.")
    elif Toggle == False:
      await ctx.message.channel.send("Ban enabled for 30 seconds.")
      await asyncio.sleep(30)
      Toggle = not Toggle
      if Toggle == True:
        await ctx.message.channel.send("Ban is now disabled.")

snipe_message_author = {}
snipe_message_content = {}

timestamp = datetime.now()
Timeupdate = timestamp.strftime(r"%I:%M %p")

@client.event
async def on_message_delete(message):
    snipe_message_author[message.channel.id] = message.author
    snipe_message_content[message.channel.id] = message.content
    await asyncio.sleep(20)
    del snipe_message_author[message.channel.id]
    del snipe_message_content[message.channel.id]

@client.command()
async def snipe(ctx):
  channel = ctx.channel
  try:
    embed = discord.Embed(description = snipe_message_content[channel.id])
    embed.set_author(name=f"{snipe_message_author[channel.id]}", icon_url=snipe_message_author[channel.id].avatar_url)
    embed.set_footer(text = f"Today at {Timeupdate}")
    await ctx.send(embed = embed)
  except:
    await ctx.send(f"There's nothing to snipe!")





keep_alive()
client.run(my_secret)


import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import get
from discord.ext.commands import has_permissions, MissingPermissions

intents = discord.Intents.all()

# Bot
bot = commands.Bot(command_prefix="!",
                   case_insensitive=True,
                   description='a bot',
                   intents=discord.Intents.all())

@bot.command()
async def version(ctx):
  
    myEmbed = discord.Embed(title="Current Version", description="Der Bot befindet sich derweil in version 1.0.0", color=0x00ff00)
    myEmbed.add_field(name="Version", value="v1.0.0", inline=False)
    myEmbed.add_field(name="Release Date:", value="12.Dezember.2020", inline=False)
    myEmbed.set_author(name="Lurinoxi")

    await ctx.send(embed=myEmbed)

@bot.command(name='kick', pass_context = True)
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member):
    await member.kick()
    await ctx.send('User ' + member.display_name + 'has been kicked.')

@bot.command(name='ban', pass_context = True)
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member):
    await member.ban()
    await ctx.send('User ' + member.display_name + 'has been banned.')

@bot.command()
async def socials(ctx):
    await ctx.send(f'My Twitch: https://www.twitch.tv/lurinoxi')
    await ctx.send(f'My Twitter: https://www.twitch.tv/lurinoxi')
    await ctx.send(f'My Instagram: https://www.twitch.tv/lurinoxi')

@bot.event
async def on_member_join(member):
    role = member.guild.get_role(600348866679799818)
    await member.add_roles(role)
    
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game('Watching Lurinoxis Server'), status=discord.Status.online, afk=False)

@bot.event
async def on_message(message):

    if message.content == 'hurensohn':
        await message.channel.send('Fuck u!')

    if message.content == 'send me a DM Anix':
      await  message.author.send('This is a DM! Have a nice Day!')
    
    elif message.content == ('Love u AnixBot'):
        await message.channel.send('Love u too!')
    
    elif message.content ==('Ich Verkauf dich auf dem Schwarzmarkt AnixBot!'):
        await message.channel.send('Versuchs doch!')

    await bot.process_commands(message)
#Run client on server

bot.run('Token')

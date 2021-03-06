#!/usr/bin/env python3.6

import os
import configparser
import asyncio
import traceback
import json
import copy
from subprocess import call
from os import execv
from sys import argv

import discord
from discord.ext import commands

# Change to script's directory
path = os.path.dirname(os.path.realpath(__file__))
os.chdir(path)

# Create database
os.makedirs("database", exist_ok=True)
if not os.path.isfile("database/warns.json"):
    with open("database/warns.json", "w") as f:
        f.write('{}')
if not os.path.isfile("database/ignored_users.json"):
    with open("database/ignored_users.json", "w") as f:
        f.write('{"users": []}')

bot_prefix = ["."]
bot = commands.Bot(command_prefix=bot_prefix, description="SchmuckBot, a general purpose discord bot.", max_messages=10000)

# Read config.ini
config = configparser.ConfigParser()
config.read("config.ini")

@bot.event
async def on_ready():

    for guild in bot.guilds:
        bot.guild = guild

    @bot.event
    async def on_member_join(member):
        schmuck_role = discord.utils.get(guild.roles, name="Schmucks")
        #print("member join: " + member.name)
        if schmuck_role not in member.roles:
            await member.add_roles(schmuck_role)
            #print("gave " + member.name + " the " + schmuck_role + "role")
        #else:
           # print("role already given?")

    # Roles
    
    bot.owner_role = discord.utils.get(guild.roles, name="Owner Bud")
    bot.admin_role = discord.utils.get(guild.roles, name="Minions (admin)")
    bot.botdev_role = discord.utils.get(guild.roles, name="SchmuckBotAllow")
    bot.nsfw_role = discord.utils.get(guild.roles, name="mcspankies")
    bot.muted_role = discord.utils.get(guild.roles, name="No Talk")
    bot.sudo_role = discord.utils.get(guild.roles, name="sudo")
    #bot.schmuck_role = discord.utils.get(guild.roles, name="Schmucks")

    #Game Roles
    bot.fortnite_role = discord.utils.get(guild.roles, name="FortNUT")
    bot.pubg_role = discord.utils.get(guild.roles, name="PUBG")
    bot.payday2_role = discord.utils.get(guild.roles, name="Payday2")
    bot.minecraft_role = discord.utils.get(guild.roles, name="Minecraft")
    bot.overwatch_role = discord.utils.get(guild.roles, name="Overwatch")
    bot.stick_role = discord.utils.get(guild.roles, name="StickFight")
    bot.r6s_role = discord.utils.get(guild.roles, name="Rainbow6")
    bot.golf_role = discord.utils.get(guild.roles, name="Golf")
    bot.gtav_role = discord.utils.get(guild.roles, name="GTAV")
    bot.csgo_role = discord.utils.get(guild.roles, name="CSGO")
    bot.osu_role = discord.utils.get(guild.roles, name="Osu")
    bot.warthunder_role = discord.utils.get(guild.roles, name="WarThunder")
    bot.gmod_role = discord.utils.get(guild.roles, name="GMOD")

    #Game Roles Non-pingable
    bot.fortnitenp_role = discord.utils.get(guild.roles, name="FortNUT-NP")
    bot.pubgnp_role = discord.utils.get(guild.roles, name="PUBG-NP")
    bot.payday2np_role = discord.utils.get(guild.roles, name="Payday2-NP")
    bot.minecraftnp_role = discord.utils.get(guild.roles, name="Minecraft-NP")
    bot.overwatchnp_role = discord.utils.get(guild.roles, name="Overwatch-NP")
    bot.sticknp_role = discord.utils.get(guild.roles, name="StickFight-NP")
    bot.r6snp_role = discord.utils.get(guild.roles, name="Rainbow6-NP")
    bot.golfnp_role = discord.utils.get(guild.roles, name="Golf-NP")
    bot.gtavnp_role = discord.utils.get(guild.roles, name="GTAV-NP")
    bot.csgonp_role = discord.utils.get(guild.roles, name="CSGO-NP")
    bot.osunp_role = discord.utils.get(guild.roles, name="Osu-NP")
    bot.warthundernp_role = discord.utils.get(guild.roles, name="WarThunder-NP")
    bot.gmodnp_role = discord.utils.get(guild.roles, name="GMOD-NP")

    # Channels
    bot.announcements_channel = discord.utils.get(guild.channels, name="announcements")
    bot.botdev_channel = discord.utils.get(guild.channels, name="botwork")
    bot.botdms_channel = discord.utils.get(guild.channels, name="bot-dm")
    bot.logs_channel = discord.utils.get(guild.channels, name="server-log")
    bot.memberlogs_channel = discord.utils.get(guild.channels, name="join-leave-log")

    # Ignored users
    with open("database/ignored_users.json", "r") as f:
        ignored_users = json.load(f)["users"]
    bot.ignored_users = ignored_users

    # Load addons
    addons = [
        'addons.speak',
        'addons.misc',
        'addons.memes',
        'addons.mod',
        'addons.game',
        'addons.events',
       # 'addons.emojif'
     ]

    # Notify user if an addon fails to load.
    for addon in addons:
        try:
            bot.load_extension(addon)
        except Exception as e:
            print("Failed to load {} :\n{} : {}".format(addon, type(e).__name__, e))

    bot.all_ready = True

    print("Client logged in as {}, in the following guild : {}".format(bot.user.name, guild.name))

# Handle errors
# Taken from 
# https://github.com/916253/Kurisu/blob/31b1b747e0d839181162114a6e5731a3c58ee34f/run.py#L88
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CommandNotFound):
        pass
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send("{} You don't have permission to use this command.".format(ctx.message.author.mention))
    elif isinstance(error, commands.errors.MissingRequiredArgument):
        formatter = commands.formatter.HelpFormatter()
        msg = await formatter.format_help_for(ctx, ctx.command)
        await ctx.send("{} You are missing required arguments.\n{}".format(ctx.message.author.mention, msg[0]))
    elif isinstance(error, commands.errors.CommandOnCooldown):
        try:
            await ctx.message.delete()
        except discord.errors.NotFound:
            pass
        message = await ctx.message.channel.send("{} This command was used {:.2f}s ago and is on cooldown. Try again in {:.2f}s.".format(ctx.message.author.mention, error.cooldown.per - error.retry_after, error.retry_after))
        await asyncio.sleep(10)
        await message.delete()
    else:
        await ctx.send("An error occured while processing the `{}` command.".format(ctx.command.name))
        print('Ignoring exception in command {0.command} in {0.message.channel}'.format(ctx))
        botdev_msg = "Exception occured in `{0.command}` in {0.message.channel.mention}".format(ctx)
        tb = traceback.format_exception(type(error), error, error.__traceback__)
        print(''.join(tb))
        botdev_channel = bot.botdev_channel
        await botdev_channel.send(botdev_msg + '\n```' + ''.join(tb) + '\n```')

@bot.event
async def on_error(ctx, event_method, *args, **kwargs):
    if isinstance(args[0], commands.errors.CommandNotFound):
        return
    print('Ignoring exception in {}'.format(event_method))
    botdev_msg = "Exception occured in {}".format(event_method)
    tb = traceback.format_exc()
    print(''.join(tb))
    botdev_msg += '\n```' + ''.join(tb) + '\n```'
    botdev_msg += '\nargs: `{}`\n\nkwargs: `{}`'.format(args, kwargs)
    botdev_channel = bot.botdev_channel
    await botdev_channel.send(botdev_msg)
    print(args)
    print(kwargs)



    
# Core commands
@bot.command(hidden=True)
async def unload(ctx, addon: str):
    """Unloads an addon."""
    dev = ctx.message.author
    if bot.botdev_role in dev.roles or bot.owner_role in dev.roles:
        try:
            addon = "addons." + addon
            bot.unload_extension(addon)
            await ctx.send('✅ Addon unloaded.')
        except Exception as e:
            await ctx.send('💢 Error trying to unload the addon:\n```\n{}: {}\n```'.format(type(e).__name__, e))

@bot.command(name='reload', aliases=['load'], hidden=True)
async def reload(ctx, addon : str):
    """(Re)loads an addon."""
    dev = ctx.message.author
    if bot.botdev_role in dev.roles or bot.owner_role in dev.roles:
        try:
            addon = "addons." + addon
            bot.unload_extension(addon)
            bot.load_extension(addon)
            await ctx.send('✅ Addon reloaded.')
        except Exception as e:
            await ctx.send('💢 Failed!\n```\n{}: {}\n```'.format(type(e).__name__, e))

            # Will add back later

@bot.command(hidden=True, name="pull", aliases=["pacman"])
async def pull(ctx, pip=None):
    """Pull new changes from Git and restart.\nAppend -p or --pip to this command to also update python modules from requirements.txt."""
    dev = ctx.message.author
    if bot.botdev_role in dev.roles or bot.owner_role in dev.roles:
        await ctx.send("`Pulling changes...`")
        call(["git", "stash", "save"])
        call(["git", "pull"])
        call(["git", "stash", "clear"])
        pip_text = ""
        if pip == "-p" or pip == "--pip" or pip == "-Syu":
            await ctx.send("`Updating python dependencies...`")
            call(["python3.6", "-m", "pip", "install", "--user", "--upgrade", "-r",
                "requirements.txt"])
            pip_text = " and updated python dependencies"
        await ctx.send("Pulled changes{}! Restarting...".format(pip_text))
        call(["python3.6", "SchmuckBot.py"])
    else:
        if "pacman" in ctx.message.content:
            await ctx.send("`{} is not in the sudoers file. This incident will be reported.`".format(ctx.message.author.display_name))
        else:
            await ctx.send("Only bot devs and / or owners can use this command")
            

@bot.command()
async def restart(ctx):
    """Restart the bot (Staff Only)"""
    dev = ctx.message.author
    if bot.botdev_role in dev.roles or bot.owner_role in dev.roles:
        await ctx.send("`Restarting, please wait...`")
        execv("python3 SchmuckBot", argv)

@commands.has_role("SchmuckBotAllow")
@bot.command()
async def quit(ctx):
    """Shutdowns the bot"""
    await ctx.send('wew, I can drop the act that I care now!')
    print("\nBot Quit By User")
    await bot.logout()


# Run the bot
bot.run(config['Main']['token'])

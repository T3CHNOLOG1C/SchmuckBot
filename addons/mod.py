#!/usr/bin/env python3

import asyncio
import json
import time
from os import execv
from sys import argv
from subprocess import call

import discord
from discord.ext import commands

class Moderation:
    """
    Moderation commands
    """

    def __init__(self, bot):
        self.bot = bot
        print("{} addon loaded.".format(self.__class__.__name__))

    async def dm(self, member, message):
        """DM the user and catch an eventual exception."""
        try:
            await member.send(message)
        except:
            pass
        
    @commands.has_permissions(kick_members=True)
    @commands.command()
    async def kick(self, ctx, member, *, reason=""):
        """Kick a member. (Staff Only)"""
        try:
            try:
                member = ctx.message.mentions[0]
            except IndexError:
                await ctx.send("Please mention a user.")
                return
            if reason == "":
                dm_msg="You have been kicked from {}.".format(ctx.guild.name)
            else:
                dm_msg = "You have been kicked from {} for the following reason:\n{}".format(ctx.guild.name, reason)
            await self.dm(member, dm_msg)
            await member.kick()
            await ctx.send("I've kicked {}.".format(member))
            emb = discord.Embed(title="Member Kicked", colour=discord.Colour.red())
            emb.add_field(name="Member:", value=member, inline=True)
            emb.add_field(name="Mod:", value=ctx.message.author, inline=True)
            if reason == "":
                reason = "No reason specified."
            emb.add_field(name="Reason:", value=reason, inline=True)
            logchannel = self.bot.logs_channel
            await logchannel.send("", embed=emb)
        except discord.errors.Forbidden:
            await ctx.send("💢 I dont have permission to do this.")

                
    @commands.has_permissions(ban_members=True)
    @commands.command()
    async def ban(self, ctx, member, *, reason=""):
        """Ban a member. (Staff Only)"""
        owner = ctx.message.guild.owner
        if len(ctx.message.mentions) == 0:
            await ctx.send("Please mention a user.")
        else:
            try:
                member = ctx.message.mentions[0]
                if reason == "":
                    dm_msg = "You have been banned from {}.".format(ctx.guild.name)
                else:
                    dm_msg = "You have been banned from {} for the following reason:\n{}".format(ctx.guild.name, reason)
                await self.dm(member, dm_msg)
                await member.ban(delete_message_days=0)
                await ctx.send("I've banned {}.".format(member))
                emb = discord.Embed(title="Member Banned", colour=discord.Colour.red())
                emb.add_field(name="Member:", value=member.name, inline=True)
                emb.add_field(name="Mod:", value=ctx.message.author.name, inline=True)
                if reason == "":
                    reason = "No reason specified."
                emb.add_field(name="Reason:", value=reason, inline=True)
                logchannel = self.bot.logs_channel
                await logchannel.send("", embed=emb)
            except discord.errors.Forbidden:
                await ctx.send("💢 I dont have permission to do this.")
    

    @commands.has_permissions(manage_messages=True)
    @commands.command()
    async def lockdown(self, ctx, reason=""):
        """
        Lock down a channel
        """
        channel = ctx.channel
        await channel.set_permissions(ctx.guild.default_role, send_messages=False)
        if reason == "":
            await channel.send(":lock: Channel Locked")
        else:
            await channel.send(":lock: Channel locked. The given reason is: {}".format(reason))
        emb = discord.Embed(title="Lockdown", colour=discord.Colour.gold())
        emb.add_field(name="Channel:", value=ctx.channel.name, inline=True)
        emb.add_field(name="Mod:", value=ctx.message.author.name, inline=True)
        if reason == "":
            reason = "No Reason Given"
        emb.add_field(name="Reason:", value=reason, inline=True)
        logchannel = self.bot.logs_channel
        await logchannel.send("", embed=emb)
        
        
    @commands.has_permissions(manage_messages=True)
    @commands.command()
    async def unlock(self, ctx):
        """
        Unlock a channel
        """
        channel = ctx.channel
        await channel.set_permissions(ctx.guild.default_role, send_messages=True)
        await channel.send(":unlock: Channel Unlocked")
        emb = discord.Embed(title="Unlock", colour=discord.Colour.gold())
        emb.add_field(name="Channel:", value=ctx.channel.name, inline=True)
        emb.add_field(name="Mod:", value=ctx.message.author.name, inline=True)
        logchannel = self.bot.logs_channel
        await logchannel.send("", embed=emb)
        
    
    # WARN STUFF

    @commands.has_permissions(administrator=True)
    @commands.command()
    async def warn(self, ctx, member, *, reason=""):
        """
        Warn members. (Staff Only)
        A user ID can be used instead of mentionning the user.
        - First warn : nothing happens, a simple warning
        - Second warn : kick
        - Third warn : muted for a day
        - Fourth warn : time banned for 3 days
        - Fifth warn : banned
        """
        author = ctx.message.author
        try:
            member = ctx.message.mentions[0]
        except IndexError:
            return await ctx.send("Please mention a user.")

        if self.bot.admin_role in member.roles and not self.bot.owner_role in author.roles:
            return await ctx.send("You cannot warn other staff members!")
        elif self.bot.owner_role in member.roles:
            return await ctx.send("💢 I don't have the permission to do that!")
        
        with open("database/warns.json", "r") as f:
            js = json.load(f) # https://hastebin.com/ejizaxasav.scala
        
        id = str(member.id)
        if id not in js:
            amount_of_warns = 1
            js[id] = {"warns": []}
        else:
            amount_of_warns = len(js[id]["warns"]) + 1

        member_name = "{}#{}".format(member.name, member.discriminator)
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        author_name = "{}#{}".format(author.name, author.discriminator)

        js[id]["amount"] = amount_of_warns
        js[id]["warns"].append({
            "name": member_name,
            "timestamp": timestamp,
            "reason": reason,
            "author": author_name,
            "author_id": author.id,
        })
        await ctx.send("🚩 I've warned {}. The user now has {} warns.".format(member, amount_of_warns))
        await self.dm(member, "You have been warned in {} for the following reason :\n\n{}\n\n".format(ctx.guild.name, reason))
        emb = discord.Embed(title="Member Warned", colour=discord.Colour.orange())
        emb.add_field(name="Member:", value=member.name, inline=True)
        emb.add_field(name="Warning Number:", value=amount_of_warns, inline=True)
        emb.add_field(name="Mod:", value=ctx.message.author.name, inline=True)
        emb.add_field(name="Reason:", value=reason, inline=True)
        logchannel = self.bot.logs_channel
        await logchannel.send("", embed=emb)

        if amount_of_warns == 1:
            await self.dm(member, "This is your first warning. The next warning will automatically kick you from the server.")
        elif amount_of_warns == 2:
            await self.dm(member, "This is your second warning, so you've been kicked from the server. You can rejoin immediately, but please note that *the next warn will result in an automatic mute!*")
            await member.kick(reason="Second warn.")
        elif amount_of_warns == 3:
            await self.dm(member, "This is your third warning, so you are muted for 24 hours. Please note that **the next warn will result in an automatic temporary ban!")
            # Someone implement a mute command already
        elif amount_of_warns == 4:
            await self.dm(member, "This is your fourth and final warning. **__The next ban will result in an automatic permanent ban.__**")
            # Someone implement a timeban command already
            await member.ban(delete_message_days=0, reason="Fourth warn.")
        elif amount_of_warns >= 5:
            await self.dm(member, "You have reached your fifth warning. You are now permanently banned from this server. How the fuck did you even get 5 warns lmao")
            await member.ban(delete_message_days=0, reason="Fifth warn.")

        with open("database/warns.json", "w") as f:
            json.dump(js, f, indent=2, separators=(',', ':'))    

    @commands.command()
    async def listwarns(self, ctx):
        """
        List your own warns or someone else's warns.
        Only the staff can view someone else's warns
        """

        try:
            member = ctx.message.mentions[0]
            if self.bot.admin_role in ctx.message.author.roles:
                has_perms = True
            else:
                has_perms = False
        except IndexError:
            member = ctx.message.author
            has_perms = True
        if not has_perms:
            return await ctx.send("{} You don't have permission to list other member's warns!".format(ctx.message.author.mention))

        with open("database/warns.json", "r") as f:
            js = json.load(f)
        
        id = str(member.id)
        if id not in js:
            return await ctx.send("No warns found!")
        embed = discord.Embed(color=member.colour)
        embed.set_author(name="List of warns for {} :".format(member), icon_url=member.avatar_url)

        for nbr, warn in enumerate(js[id]["warns"]):
            content = "{}".format(warn["reason"])
            if ctx.message.channel in self.bot.staff_channels.channels:
                author = await self.bot.get_user_info(warn["author_id"])
                content += "\n*Warn author : {} ({})*".format(warn["author"], author.mention)
            embed.add_field(name="\n\n#{}: {}".format(nbr + 1, warn["timestamp"]), value=content, inline=False)
        
        await ctx.send("", embed=embed)
        
    @commands.has_permissions(administrator=True)
    @commands.command()
    async def clearwarns(self, ctx, member):
        """Clear all of someone's warns. (Staff only)"""
        try:
            member = ctx.message.mentions[0]
        except IndexError:
            return await ctx.send("Please mention a user.")

        with open("database/warns.json", "r") as f:
            js = json.load(f)

        try:
            js.pop(str(member.id))
            await ctx.send("Cleared all of {}'s warns!".format(member.mention))
            emb = discord.Embed(title="Member Warns Cleared", colour=discord.Colour.orange())
            emb.add_field(name="Member:", value=member.name, inline=True)
            emb.add_field(name="Mod:", value=ctx.message.author.name, inline=True)
            logchannel = self.bot.logs_channel
            await logchannel.send("", embed=emb)
            with open("database/warns.json", "w") as f:
                json.dump(js, f, indent=2, separators=(',', ':'))
        except KeyError:
            return await ctx.send("This user doesn't have any warns!")
            
    @commands.has_permissions(manage_roles=True)
    @commands.command()
    async def mute(self, ctx, member, *, reason=""):
        """Mutes a user. (Staff Only)"""
        try:
            member = ctx.message.mentions[0]
        except IndexError:
            return await ctx.send("Please mention a user.")
        
        if self.bot.muted_role in member.roles:
            return await ctx.send("{} is already muted!".format(member))
        
        try:
            await member.add_roles(self.bot.muted_role)
            await ctx.send("{} can no longer speak!".format(member))
            if reason == "":
                msg = "You have been muted in {} by {}. You will be DM'ed when a mod unmutes you.\n**Do not ask mods to unmute you, as doing so might extend the duration of the mute**".format(ctx.guild.name, ctx.message.author)
            else:
                msg = "You have been muted in {} by {}. The given reason is {}. You will be DM'ed when a mod unmutes you.\n**Do not ask mods to unmute you, as doing so might extend the duration of the mute**".format(ctx.guild.name, ctx.message.author, reason)
            await self.dm(member, msg)
            emb = discord.Embed(title="Member Muted", colour=discord.Colour.purple())
            emb.add_field(name="Member:", value=member, inline=True)
            emb.add_field(name="Mod:", value=ctx.message.author, inline=True)
            if reason == "":
                emb.add_field(name="Reason:", value="No reason specified.", inline=True)
            else:
                emb.add_field(name="Reason:", value=reason, inline=True)
            logchannel = self.bot.logs_channel
            await logchannel.send("", embed=emb)
        except discord.errors.Forbidden:
            await ctx.send("💢 I dont have permission to do this.")


    @commands.has_permissions(manage_roles=True)
    @commands.command()
    async def unmute(self, ctx, member):
        """Unmutes a user. (Staff Only)"""
        try:
            member = ctx.message.mentions[0]
        except IndexError:
            return await ctx.send("Please mention a user.")
        
        if self.bot.muted_role not in member.roles:
            return await ctx.send("{} is not muted!".format(member))
        
        try:
            await member.remove_roles(self.bot.muted_role)
            await ctx.send("{} is no longer muted!".format(member))
            msg = "You have been unmuted in {}.".format(ctx.guild.name)
            await self.dm(member, msg)
            emb = discord.Embed(title="Member Unmuted", colour=discord.Colour.purple())
            emb.add_field(name="Member:", value=member, inline=True)
            emb.add_field(name="Mod:", value=ctx.message.author, inline=True)
            logchannel = self.bot.logs_channel
            await logchannel.send("", embed=emb)
        except discord.errors.Forbidden:
            await ctx.send("💢 I dont have permission to do this.")



def setup(bot):
    bot.add_cog(Moderation(bot))
            


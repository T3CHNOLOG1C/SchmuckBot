#!/usr/bin/env python3.6

import datetime
import discord
from discord.ext import commands

class Misc:
    """
    Miscellaneous commands
    """

    def __init__(self, bot):
        self.bot = bot
        print("{} addon loaded.".format(self.__class__.__name__))
        
    @commands.command(pass_context=True)
    async def ping(self, ctx):
        """Pong!"""
        # https://github.com/appu1232/Discord-Selfbot/blob/master/cogs/misc.py#L595
        msgtime = ctx.message.created_at.now()
        await (await self.bot.ws.ping())
        now = datetime.datetime.now()
        ping = now - msgtime
        return await ctx.send(":ping_pong:! Response Time: {} ms".format(str(ping.microseconds / 1000.0)))

    @commands.command(pass_context=True, aliases=['mc'])
    async def membercount(self, ctx):
        """Prints current member count"""
        return await ctx.send(str(self.bot.guild.name)+" currently has " + str(len(self.bot.guild.members)) + " members!")
    
    @commands.command()
    async def about(self, ctx):
        """About SchmuckBot."""
        return await ctx.send("Link coming soon")

    @commands.command(pass_context=True)
    async def sudo(self, ctx, roles):
        """Gain temp mod powers, only need by PhazonicRidley to fix the bot"""

        user = ctx.message.author
        await ctx.message.delete()

        #if ctx.message.author.id == 286488483994927109:
         #   self.bot.sudo_role in user.roles
          #  await ctx.send("You are already a HalfOP")

        if ctx.message.author.id == 286488483994927109:
            await user.add_roles(self.bot.sudo_role)
            await ctx.send(":ambulance: **PhazonicRidley is now a HalfOP! Welcome to the twilight zone!**")
            emb = discord.Embed(title="Gained Temp Powers", colour=discord.Colour.orange())
            emb.set_thumbnail(url=user.avatar_url)
            emb.add_field(name="User:", value=user.name, inline=True)
            logchannel = self.bot.logs_channel
            await logchannel.send("", embed=emb)

        
        else:
           return await ctx.send("You do not have permission to use this command!")

    @commands.command(pass_context=True)
    async def unsudo(self, ctx, roles):
        """Remove temp mod powers, only needed by PhazonicRidley"""
        user = ctx.message.author
        await ctx.message.delete()

      #  if ctx.message.author.id == 286488483994927109:
      #      self.bot.sudo_role not in user.roles
      #      await ctx.send("You are not a HalfOP")
            
        if ctx.message.author.id == 286488483994927109:
            await user.remove_roles(self.bot.sudo_role)
            await ctx.send("**Problem Solved! PhazonicRidley is no longer a HalfOP!**")
            emb = discord.Embed(title="No longer HalfOP", colour=discord.Colour.orange())
            emb.set_thumbnail(url=user.avatar_url)
            emb.add_field(name="User:", value=user.name, inline=True)
            logchannel = self.bot.logs_channel
            await logchannel.send("", embed=emb)

        else:
            return await ctx.send("You do not have permission to use this command!")



        
        
    @commands.command(pass_context=True)
    async def togglechannel(self, ctx, channel):
        """Toggle access to some hidden channels"""

        user = ctx.message.author
        await ctx.message.delete()

        if channel == "nsfw":

            if self.bot.nsfw_role in user.roles:
                await user.remove_roles(self.bot.nsfw_role)
                await user.send("Access to NSFW channels revoked.")
            else:
                await user.add_roles(self.bot.nsfw_role)
                await user.send("Access to NSFW channels granted.")
        else:
            await user.send("{} is not a togglable channel.".format(channel))

    @commands.has_permissions(manage_messages=True)
    @commands.command()
    async def clear(self, ctx, amount):
        """Clears a given amount of messages. (Mods only)"""

        channel = ctx.message.channel
        try:
            n = int(amount) + 1
        except ValueError:
            return await ctx.send("Please mention a valid amount of messages!")

        try:
            await channel.purge(limit=n)
            await ctx.send("🗑️ Cleared {} messages in this channel!".format(amount))
        except discord.errors.Forbidden:
            await ctx.say("💢 I don't have permission to do this.")
       
   



            

def setup(bot):
    bot.add_cog(Misc(bot))

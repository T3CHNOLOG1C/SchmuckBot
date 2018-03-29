import datetime
import discord
from discord.ext import commands

@commands.command(pass_context=True)
async def game(self, ctx, roles):

    """toggle game roles"""
    user = ctx.message.author
    await ctx.message.delete()
        
    async def core(self, ctx, roles):
        if self.bot.pubg_role in user.roles:
            await user.remove_roles(self.bot.pubg_role)
            await user.send("Left PUBG role")
        else:
            await user.add_roles(self.bot.pubg_role)
            await user.send("Joined PUBG role.")

        list = ["PUBG", "Minecraft", "Rainbow 6 Seige", "Golf", "GTAV", "FortNUT", "Overwatch", "CSGO", "Osu!", "WarThunder", "Payday 2"]
        if roles in list: await core(self,ctx,roles)
       
        else:
            await user.send("{} is not a game role".format(roles))
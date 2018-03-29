 #!/usr/bin/env python3.6

import datetime

import discord
from discord.ext import commands



class Games:
    """
    Join/Leave role commands
    """

    def __init__(self, bot):
        self.bot = bot
        print("{} addon loaded".format(self.__class__.__name__))



    @commands.command(pass_contex=True)
    async def game(self, ctx, role):
        """Join/Leave game roles"""
        user = ctx.message.author
        await ctx.message.delete()
        if role == "PUBG":
            if self.bot.pubg_role in user.roles:
                await user.remove_roles(self.bot.pubg_role)
                await user.send("Left PUBG role")

            else:
                await user.add_roles(self.bot.pubg_role)
                await user.send("Joined PUBG role")

        elif role == "Minecraft":
            if self.bot.minecraft_role in user.roles:
                await user.remove_roles(self.bot.minecraft_role)
                await user.send("Left Minecraft role")
                
            else:
                await user.add_roles(self.bot.minecraft_role)
                await user.send("Joined Minecraft role")



def setup(bot):
    bot.add_cog(Games(bot))

        
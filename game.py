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

        elif role == "Rainbow 6 Seige":
            if self.bot.r6s_role in user.roles:
                await user.remove_roles(self.bot.r6s_role)
                await user.send("Left Rainbow 6 Seige role")

            else:
                await user.add_roles(self.bot.r6s_role)
                await user.send("Joined Rainbow 6 Seige role")

        elif role == "Golf":
            if self.bot.golf_role in user.roles:
                await user.remove_roles(self.bot.golf_role)
                await user.send("Left Golf role")

            else:
                await user.add_roles(self.bot.golf_role)
                await user.send("Joined Golf role")

        elif role == "GTAV":
            if self.bot.gtav_role in user.roles:
                await user.remove_roles(self.bot.gtav_role)
                await user.send("Left GTAV role")

            else:
                await user.add_roles(self.bot.gtav_role)
                await user.send("Joined GTAV role")
        
        elif role == "FortNUT":
            if self.bot.fornite_role in user.roles:
                await user.remove_roles(self.bot.fornite_role)
                await user.send("Left FortNUT role")

            else:
                await user.add_roles(self.bot.fornite_role)
                await user.send("Joined FortNUT role")

        elif role == "Overwatch":
            if self.bot.overwatch_role in user.role:
                await user.remove_roles(self.bot.overwatch_role)
                await user.send("Left Overwatch role")

            else:
                await user.add_roles(self.bot.overwatch_role)
                await user.send("Joined Overwatch role")

        elif role == "CSGO":
            if self.bot.csgo_role in user.roles:
                await user.remove_roles(self.bot.csgo_role)
                await user.send("Left CSGO role")

            else:
                await user.add_roles(self.bot.csgo_role)
                await user.send("Joined CSGO role")

        elif role == "Osu!":
            if self.bot.osu_role in user.role:
                await user.remove_roles(self.bot.osu_role)
                await user.send("Left Osu! role")

            else:
                await user.add_roles(self.bot.osu_role)
                await user.send("Joined Osu! role")

        elif role == "WarThunder":
            if self.bot.warthunder_role in user.roles:
                await user.remove_roles(self.bot.warthunder_role)
                await user.send("Left WarThunder role")

            else:
                await user.add_roles(self.bot.warthunder_role)
                await user.send("Joined WarThunder role")

        elif role == "Payday 2":
            if self.bot.payday2_role in user.roles:
                await user.remove_roles(self.bot.payday2_role)
                await user.send("Left Payday 2 role")

            else:
                await user.add_roles(self.bot.payday2_role)
                await user.send("Joined Payday 2 role")

        elif role == "Stick Fight":
            if self.bot.stick_role in user.roles:
                await user.remove_roles(self.bot.stick_role)
                await user.send("Left Stick Fight role")

            else:
                await user.add_roles(self.bot.stick_role)
                await user.send("Joined Stick Fight role")

        else:
            await user.send("{} is not a game role".format(role))

    @commands.command(pass_context=True)
    async def listgames(self, ctx,):
        """list game roles"""
        
        await ctx.message.delete()
        embed = discord.Embed(title="List of Game roles", color=10689279)
        embed.description = """-PUBG
-Minecraft
-Rainbow 6 Seige
-Golf
-GTAV
-Fortnite
-Overwatch
-CSGO
-Osu!
-WarThunder
-Payday 2
"""       
        await ctx.send (embed=embed)
            



def setup(bot):
    bot.add_cog(Games(bot))

        
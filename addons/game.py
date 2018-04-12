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
        if role == "FortNUT":
            if self.bot.fortnite_role in user.roles:
                await user.remove_roles(self.bot.fortnite_role)
                await user.send("Left FortNUT role")

            else:
                await user.add_roles(self.bot.fortnite_role)
                await user.send("Joined FortNUT role")

        elif role == "PUBG":
            if self.bot.pubg_role in user.roles:
                await user.remove_roles(self.bot.pubg_role)
                await user.send("Left PUBG role")

            else:
                await user.add_roles(self.bot.pubg_role)
                await user.send("Joined PUBG role")

        elif role == "Payday2":
            if self.bot.payday2_role in user.roles:
                await user.remove_roles(self.bot.payday2_role)
                await user.send("Left Payday2 role")

            else:
                await user.add_roles(self.bot.payday2_role)
                await user.send("Joined Payday2 role")

        elif role == "Minecraft":
            if self.bot.minecraft_role in user.roles:
                await user.remove_roles(self.bot.minecraft_role)
                await user.send("Left Minecraft role")

            else:
                await user.add_roles(self.bot.minecraft_role)
                await user.send("Joined Minecraft role")

        elif role == "Overwatch":
            if self.bot.overwatch_role in user.roles:
                await user.remove_roles(self.bot.overwatch_role)
                await user.send("Left Overwatch role")

            else:
                await user.add_roles(self.bot.overwatch_role)
                await user.send("Joined Overwatch role")

        elif role == "StickFight":
            if self.bot.stick_role in user.roles:
                await user.remove_roles(self.bot.stick_role)
                await user.send("Left Stick Fight role")

        elif role == "Rainbow6":
            if self.bot.r6s_role in user.roles:
                await user.remove_roles(self.bot.r6s_role)
                await user.send("Left Rainbow6 role")

            else:
                await user.add_roles(self.bot.r6s_role)
                await user.send("Joined Rainbow6 role")

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

        elif role == "CSGO":
            if self.bot.csgo_role in user.roles:
                await user.remove_roles(self.bot.csgo_role)
                await user.send("Left CSGO role")

            else:
                await user.add_roles(self.bot.csgo_role)
                await user.send("Joined CSGO role")

        elif role == "Osu":
            if self.bot.osu_role in user.roles:
                await user.remove_roles(self.bot.osu_role)
                await user.send("Left Osu role")

            else:
                await user.add_roles(self.bot.osu_role)
                await user.send("Joined Osu role")

        elif role == "WarThunder":
            if self.bot.warthunder_role in user.roles:
                await user.remove_roles(self.bot.warthunder_role)
                await user.send("Left WarThunder role")

            else:
                await user.add_roles(self.bot.warthunder_role)
                await user.send("Joined WarThunder role")
            else:
                await user.add_roles(self.bot.stick_role)
                await user.send("Joined Stick Fight role")

        elif role == "GMOD":
            if self.bot.gmod_role in user.roles:
                await user.remove_roles(self.bot.gmod_role)
                await user.send("Left GMOD role")

            else:
                await user.add_roles(self.bot.gmod_role)
                await user.send("Joined GMOD role")

    # Non Pingables
        if role == "FortNUT-NP":
            if self.bot.fortnitenp_role in user.roles:
                await user.remove_roles(self.bot.fortnitenp_role)
                await user.send("Left FortNUT-Not Pingable role")

            else:
                await user.add_roles(self.bot.fortnitenp_role)
                await user.send("No more pings from FortNUT")


        elif role == "PUBG-NP":
            if self.bot.pubgnp_role in user.roles:
                await user.remove_roles(self.bot.pubgnp_role)
                await user.send("Left PUBG-Not Pingable role")

            else:
                await user.add_roles(self.bot.pubgnp_role)
                await user.send("Joined PUBG-Not Pingable role")

        elif role == "Payday2-NP":
            if self.bot.payday2np_role in user.roles:
                await user.remove_roles(self.bot.payday2np_role)
                await user.send("Left Payday2-Not Pingable role")

            else:
                await user.add_roles(self.bot.payday2np_role)
                await user.send("Joined Payday2-Not Pingable role")


        elif role == "Minecraft-NP":
            if self.bot.minecraftnp_role in user.roles:
                await user.remove_roles(self.bot.minecraftnp_role)
                await user.send("Left Minecraft-Not Pingable role")

            else:
                await user.add_roles(self.bot.minecraftnp_role)
                await user.send("Joined Minecraft-Not Pingable role")

        elif role == "Overwatch-NP":
            if self.bot.overwatchnp_role in user.roles:
                await user.remove_roles(self.bot.overwatchnp_role)
                await user.send("Left Overwatch-Not Pingable role")

            else:
                await user.add_roles(self.bot.overwatchnp_role)
                await user.send("Joined Overwatch-Not Pingable role")

        elif role == "StickFight-NP":
            if self.bot.sticknp_role in user.roles:
                await user.remove_roles(self.bot.sticknp_role)
                await user.send("Left Stick Fight-Not Pingable role")

            else:
                await user.add_roles(self.bot.sticknp_role)
                await user.send("Joined Stick Fight-Not Pingable role")

        elif role == "Rainbow6-NP":
            if self.bot.r6snp_role in user.roles:
                await user.remove_roles(self.bot.r6snp_role)
                await user.send("Left Rainbow6-Not Pingable role")

            else:
                await user.add_roles(self.bot.r6snp_role)
                await user.send("Joined Rainbow6-Not Pingable role")

        elif role == "Golf-NP":
            if self.bot.golfnp_role in user.roles:
                await user.remove_roles(self.bot.golfnp_role)
                await user.send("Left Golf-Not Pingable role")

            else:
                await user.add_roles(self.bot.golfnp_role)
                await user.send("Joined Golf-Not Pingable role")

        elif role == "GTAV-NP":
            if self.bot.gtavnp_role in user.roles:
                await user.remove_roles(self.bot.gtavnp_role)
                await user.send("Left GTAV-Not Pingable role")

            else:
                await user.add_roles(self.bot.gtavnp_role)
                await user.send("Joined GTAV-Not Pingable role")

        elif role == "CSGO-NP":
            if self.bot.csgonp_role in user.roles:
                await user.remove_roles(self.bot.csgonp_role)
                await user.send("Left CSGO-Not Pingable role")

            else:
                await user.add_roles(self.bot.csgonp_role)
                await user.send("Joined CSGO-Not Pingable role")

        elif role == "Osu-NP":
            if self.bot.osunp_role in user.roles:
                await user.remove_roles(self.bot.osunp_role)
                await user.send("Left Osu-Not Pingable role")

            else:
                await user.add_roles(self.bot.osunp_role)
                await user.send("Joined Osu-Not Pingable role")

        elif role == "WarThunder-NP":
            if self.bot.warthundernp_role in user.roles:
                await user.remove_roles(self.bot.warthundernp_role)
                await user.send("Left WarThunder-Not Pingable role")

            else:
                await user.add_roles(self.bot.warthundernp_role)
                await user.send("Joined WarThunder-Not Pingable role")

        elif role == "GMOD-NP":
            if self.bot.gmodnp_role in user.roles:
                await user.remove_roles(self.bot.gmodnp_role)
                await user.send("Left GMOD-Not Pingable role")

            else:
                await user.add_roles(self.bot.gmodnp_role)
                await user.send("Joined GMOD-Not Pingable role")

        else:
            await user.send("{} is not a game role".format(role))

    @commands.command(pass_context=True)
    async def listgames(self, ctx,):
        """list game roles"""

        await ctx.message.delete()
        embed = discord.Embed(title="List of Game roles", color=10689279)
        embed.description = """-PUBG
-Minecraft
-Rainbow6
-Golf
-GTAV
-FortNUT
-Overwatch
-CSGO
-Osu
-WarThunder
-Payday2
-StickFight
-GMOD

You can get a non-pingable role by adding "-NP" to the end of the game so you don't get @mentioned when someone wants to play

If you want a game added to the bot you can fill out [this](https://goo.gl/forms/F5XZmnQBQfhRxmmx1) fourm here.
"""
        await ctx.send (embed=embed)




def setup(bot):
    bot.add_cog(Games(bot))

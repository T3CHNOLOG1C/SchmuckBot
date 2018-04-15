#!/usr/bin/env python3.6

import discord
from discord.ext import commands

class Memes:
    """
    ayy lmao
    """

    def __init__(self, bot):
        self.bot = bot
        print("{} addon loaded.".format(self.__class__.__name__))

    # SSS memes

    @commands.command()
    async def rip(self, ctx):
        """F"""
        msg = await ctx.send("Press F to pay respects.")
        await msg.add_reaction("🇫")

    @commands.command()
    async def t3ch(self, ctx):
        """Goddamn Nazimod"""
        return await ctx.send("https://i.imgur.com/4kANai8.png")

    @commands.command()
    async def bigsmoke(self, ctx):
        """Memes."""
        await ctx.send("http://i.imgur.com/vo5l6Fo.jpg\nALL YOU HAD TO DO WAS FOLLOW THE DAMN GUIDE CJ!")
 
    @commands.command()
    async def bigorder(self, ctx):
        """Memes."""
        await ctx.send("I'll have two number 9s, a number 9 large, a number 6 with extra dip, a number 7, two number 45s, one with cheese, and a large soda.")
 
    @commands.command()
    async def heil(self, ctx):
        """SIEG HEIL"""
        await ctx.send("HEIL T3CH!")
        
    @commands.command()
    async def lenny(self, ctx):
        """( ͡° ͜ʖ ͡°)"""
        await ctx.send("( ͡° ͜ʖ ͡°)")

    @commands.command()
    async def birds(self, ctx):
        """Memes."""
        await ctx.send("http://i.imgur.com/fVAx5oh.png")
        await ctx.send("SS credit 46620:tm:")
	
    
    # SSS spammy-ish memes that need a cooldown
    @commands.cooldown(rate=1, per=30.0, type=commands.BucketType.channel)
    @commands.command(aliases=["astronautlevel"])
    async def astro(self, ctx):
        """MEMES???"""
        await ctx.send(
            "ASTRO DOES IT AGAIN!!!\n" +
            "The peak nazi mod recuperance has occurred, mimicing the occurrence of 2016 where he once emotionally manipulated s_99 and xorhash to die off the server. " +
            "In that time, it was an emotionally draining period in which tensions were high and confusion was all over the place. " +
            "The word on the street places that this time is very similar to that time, in the dark days of the previously old, now defunct, 3d shacks, which was renamed to Nintendo Homebrew as of the final official takeover of Emma in late 2016-early 2017, with the help of Ian. " +
            "However, the old tales of his exploits have been sung across the land, and it is possible that they have led to influence over this most recent attempt of takeover of SSS. " +
            "The real quandry of all this however, is, how will he now react to the new role in taking over SSS? " +
            "Will his potential ownership be riddeled with as much controversy as his old temporary ownership in 3dshacks? The future alone will know."
        )
    
  
    # Kurisu memes

    @commands.command()
    async def screams(self, ctx):
        """Memes."""
        await ctx.send("http://i.imgur.com/j0Dkv2Z.png")

    @commands.command()
    async def rusure(self, ctx):
        """Memes."""
        await ctx.send("http://i.imgur.com/dqh3fNi.png")

    @commands.command()
    async def r34(self, ctx):
        """Memes."""
        await ctx.send("http://i.imgur.com/sjQZKBF.gif")

    @commands.command()
    async def permabrocked(self, ctx):
        """Memes."""
        await ctx.send("http://i.imgur.com/ARsOh3p.jpg")

    @commands.command()
    async def pbanjo(self, ctx):
        """Memes."""
        await ctx.send("http://i.imgur.com/sBJKzuK.png")

    # Cute commands :3
    @commands.command()
    async def sudoku(self, ctx):
        """Cute"""
        await ctx.send("http://i.imgur.com/VHlIZRC.png")

    @commands.command()
    async def blackalabi(self, ctx):
        """Memes."""
        await ctx.send("http://i.imgur.com/JzFem4y.png")
	
    @commands.command()
    async def sn0w(self, ctx):
        """Memes."""
        await ctx.send("http://i.imgur.com/sFD5uSB.png")
    
 
    ## GIB DONGRODER LAZY DEV
    @commands.cooldown(rate=1, per=10.0, type=commands.BucketType.channel)
    @commands.command()
    async def dongroder(self, ctx, variant=""):
        """MEMES?!?
        This meme has multiple variants : piter, swotch.
        If no variant is specified, it will defautlt to piter."""
        if variant == "piter":
            await ctx.send(
                "```Hey YOU. YES YOU!!!! YOU CAN CREATE A DOWNGRADER. JUST like can Plailect , Aurora Wright , astronautlevel and Apache Thunder and Kyojin work on a 3DS 11.0 Downgrader!!!!!!!!!!!!!!!!!!!!!!!!!!!\nI mean I got arm11 acess with my 6 copies of freakyforms deluxes and now i want to downgrade to 9.2 and as I have homebrew I can boot lima3ds but it doesnt boot its Aurora Wright fault, its incompetent and lazy to not develop for 11 I want downgrader to 9.2 and kernel exploit quick it's not hard ur the devs do it now quick.\nYou just have to hack/reprogram/patch the 11.0 FIRM so I can downgrade. Think the comunity. Cmon your hackers you acn do it. And plilect should make guide safer!!! becuase evryone bricks!!!!! And lima3ds should add nds rom support native. take notes Aurora Wright !!!!!!!!!!!!!!I WANT 3DS 11.0 DOWNGRADER NOW!!!!!!!!!!!!!!!\nI WANT 3DS 11.0 DOWNGRADER NOW!!!!!!!!!!!!!!!\nI WANT 3DS 11.0 DOWNGRADER NOW!!!!!!!!!!!!!!!\nI WANT 3DS 11.0 DOWNGRADER NOW!!!!!!!!!!!!!!!\nI WANT 3DS 11.0 DOWNGRADER NOW!!!!!!!!!!!!!!!\nI WANT 3DS 11.0 DOWNGRADER NOW!!!!!!!!!!!!!!!\nI WANT 3DS 11.0 DOWNGRADER NOW!!!!!!!!!!!!!!!\nI WANT 3DS 11.0 DOWNGRADER NOW!!!!!!!!!!!!!!!\nI WANT 3DS 11.0 DOWNGRADER NOW!!!!!!!!!!!!!!!\nI WANT 3DS 11.0 DOWNGRADER NOW!!!!!!!!!!!!!!!```"
            )
        elif variant == "swotch":
            await ctx.send(
                "```Hey YOU. YES YOU!!!! YOU CAN CREATE A DOWNGRADER. JUST like can Plailect , Aurora Wright , hedgeberg and SciresM and Daeken work on a Switch 3.0.2 dongroder!!!!!!!!!!!!!!!!!!!!!!!!!!!\nI mean I got browser acess with my 6 verzions of teh dns and now i want to downgrade to 3.0.0 and as I have browser I can boot reswotched but it doesnt boot teh hebrew lawnchair its Aurora Wright fault, its incompetent and lazy to not develop for 3.0.2 I want dongroder to 3.0.0 and trustzone exploit quick it's not hard ur the devs do it now quick.\nYou just have to hack/reprogram/patch the 3.0.2 bootrom so I can dongrode. Think the comunity. Cmon your hackers you acn do it. And plilect should make swotch gudie safer!!! becuase evryone bricks!!!!! And limaswotch should add wii u rom support native. take notes Aurora Wright !!!!!!!!!!!!!!I WANT Switch 3.0.2 DONGROADER NOW!!!!!!!!!!!!!!!\nI WANT Switch 3.0.2 DONGROADER NOW!!!!!!!!!!!!!!!\nI WANT Switch 3.0.2 DONGROADER NOW!!!!!!!!!!!!!!!\nI WANT Switch 3.0.2 DONGROADER NOW!!!!!!!!!!!!!!!\nI WANT Switch 3.0.2 DONGROADER NOW!!!!!!!!!!!!!!!\nI WANT Switch 3.0.2 DONGROADER NOW!!!!!!!!!!!!!!!\nI WANT Switch 3.0.2 DONGROADER NOW!!!!!!!!!!!!!!!\nI WANT Switch 3.0.2 DONGROADER NOW!!!!!!!!!!!!!!!\nI WANT Switch 3.0.2 DONGROADER NOW!!!!!!!!!!!!!!!\nI WANT Switch 3.0.2 DONGROADER NOW!!!!!!!!!!!!!!!```" 
            )

    @commands.cooldown (rate=1, per=10.0, type=commands.BucketType.channel)
    @commands.command()
    async def gnulinux(self, ctx,):
        """GNU/Linux Copy Pasta"""
        await ctx.send("""```I'd just like to interject for a moment. What you're referring to as Linux, is in fact, GNU/Linux, or as I've recently taken to calling it, GNU plus Linux. Linux is not an operating system unto itself, but rather another free component of a fully functioning GNU system made useful by the GNU corelibs, shell utilities and vital system components comprising a full OS as defined by POSIX.

Many computer users run a modified version of the GNU system every day, without realizing it. Through a peculiar turn of events, the version of GNU which is widely used today is often called "Linux", and many of its users are not aware that it is basically the GNU system, developed by the GNU Project.

There really is a Linux, and these people are using it, but it is just a part of the system they use. Linux is the kernel: the program in the system that allocates the machine's resources to the other programs that you run. The kernel is an essential part of an operating system, but useless by itself; it can only function in the context of a complete operating system. Linux is normally used in combination with the GNU operating system: the whole system is basically GNU with Linux added, or GNU/Linux. All the so-called "Linux" distributions are really distributions of GNU/Linux.
```""")



    @commands.cooldown (rate=1, per=10.0, type=commands.BucketType.channel)
    @commands.command()
    async def gitgud(self,ctx,):
        """gitgud"""
        await ctx.send("""Let's :clap: do :clap: it :clap: again :clap: memelords
Mods :clap: asleep :clap: pwn :clap: server
I :clap: was :clap: nice :clap: last :clap: time :clap: but :clap: not :clap: anymore
Yesterday :clap: was :clap: a :clap: warm :clap: up, :clap: here's :clap: the :clap: real :clap: deal
Unbanmii :clap: is :clap: malware
Paul :clap: faps :clap: to :clap: 15 :clap: year :clap: olds
Derek :clap: is :clap: a :clap: terrible :clap: choice :clap: for :clap: staff
You :clap: can't :clap: ban :clap: all :clap: the :clap: alts
Git :clap: fucking :clap: good
All programs by Paul are cancer and not curable.""")

def setup(bot):
    bot.add_cog(Memes(bot))

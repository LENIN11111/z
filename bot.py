import discord
from discord.ext import commands 
import praw
import logging
import os
import random
client = commands.Bot(command_prefix = "~")
@client.command()
async def hentai(ctx):
    if 5 == 5:
        if ctx.channel.nsfw == False:
            await ctx.send("This command can be used only in NSFW channels!")
        else:
            reddit = praw.Reddit(client_id='CeDBvaI-EoNQyw',
            client_secret='jmtJ3foXUUPzKby1CFtNdVQ-Ovc',
            user_agent='hi')
            sub = random.choice(['hentai', 'thick_hentai', 'officelady', 'oppailove'])
            memes_submissions = reddit.subreddit(sub).hot()
            post_to_pick = random.randint(1, 100)
            for i in range(0, post_to_pick):
                submission = next(x for x in memes_submissions)

            await ctx.send(submission.url)
@client.command()
async def hentaibomb(ctx):
    if 5 == 5:
        if ctx.channel.nsfw == False:
            await ctx.send("This command can be used only in NSFW channels!")
        else:
            reddit = praw.Reddit(client_id='CeDBvaI-EoNQyw',
            client_secret='jmtJ3foXUUPzKby1CFtNdVQ-Ovc',
            user_agent='hi')
            sub = random.choice(['hentai', 'thick_hentai', 'officelady', 'oppailove'])
            memes_submissions = reddit.subreddit(sub).hot()
            z = 0
            post_to_end = random.randint(10,125)
            for i in range(1, post_to_end):
                sendz = []
                shouldwe = random.randint(1,2)
                submission =   next(x for x in memes_submissions)
                if shouldwe == 2:
                    if z < 11:
                        z += 1
                        await ctx.send(str(submission.url))
                    else:
                        break
                else:
                    pass
client.run()
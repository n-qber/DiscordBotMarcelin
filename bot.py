from credentials import TOKEN
import discord
import discord.message
import discord.ext.commands.bot
from meme import Meme


if __name__ == '__main__':
    client = discord.ext.commands.bot.Bot(command_prefix="!")
    channels = {}


    @client.event
    async def on_ready():
        print("i am ready lol")


    @client.command()
    async def clear(ctx: discord.ext.commands.context.Context, **kwargs):
        messages = await ctx.channel.history(limit=None).flatten()
        for message in messages:
            await message.delete()

    @client.command()
    async def control(ctx: discord.ext.commands.context.Context):
        await ctx.message.delete()
        while True:
            message = input(">>>  ")
            if message != "quit":
                await ctx.send(message)
            else:
                break

    @client.command()
    async def meme(ctx:  discord.ext.commands.context.Context, get_set, name, url=""):
        if get_set.lower().startswith("get"):
            file = Meme.getter(name)
            if file:
                await ctx.send(ctx.author, file=file)
            else:
                await ctx.message.delete()
                await ctx.send(f"Couldn't get {name}\nIf you want to save {name} you should use\n!meme set {name} {name}_url",
                               delete_after=5)
        elif get_set.lower().startswith('set'):
            await ctx.send("Function to be made tururu")


    client.run(TOKEN)


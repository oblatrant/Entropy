import discord
from discord.ext import commands
import time
import logging
from config import TOKEN

logging.basicConfig(level=logging.INFO)

def boot_sequence():
    print('''
          
 ███████╗███╗   ██╗████████╗██████╗  ██████╗ ██████╗ ██╗   ██╗
██╔════╝████╗  ██║╚══██╔══╝██╔══██╗██╔═══██╗██╔══██╗╚██╗ ██╔╝
█████╗  ██╔██╗ ██║   ██║   ██████╔╝██║   ██║██████╔╝ ╚████╔╝ 
██╔══╝  ██║╚██╗██║   ██║   ██╔══██╗██║   ██║██╔═══╝   ╚██╔╝  
███████╗██║ ╚████║   ██║   ██║  ██║╚██████╔╝██║        ██║   
╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝        ╚═╝   
                                                             
                                                 

 discord utility framework
 version 1.0 
 ''')
    print('> initializing core modules...')
    time.sleep(0.5)
    print('> verifying Discord API environment...')
    time.sleep(0.6)
    print('> status: all systems nominal.')
    time.sleep(0.4)
    print("=" * 60)
    print("AVALIABLE COMMANDS:")
    print("!nuke - Deletes all channels in the server.")
    print("!mass_ban - Bans all members in the server.")
    print("!spam <message> - Spams a message in the server.")
    print("=" * 60)

boot_sequence()

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    print('Ready to cause some chaos.')

class ServerCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def nuke(self, ctx):
        """Deletes all channels."""
        try:
            for channel in ctx.guild.channels:
                await channel.delete()
            await ctx.send('Nuked all channels.')
        except Exception as e:
            logging.error(f"Failed to delete channels: {e}")
            await ctx.send("Error deleting channels.")

class DestructiveCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def mass_ban(self, ctx):
        """Bans all members."""
        try:
            for member in ctx.guild.members:
                if not member.bot:
                    await member.ban()
            await ctx.send('Banned all members.')
        except Exception as e:
            logging.error(f"Failed to ban members: {e}")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def spam(self, ctx, message):
        """Spams a message."""
        try:
            for _ in range(100):
                await ctx.send(message)
            await ctx.send("Spam complete.")
        except Exception as e:
            logging.error(f"Failed to spam messages: {e}")

if __name__ == '__main__':
    from config import TOKEN
    
    async def setup_bot():
        await bot.add_cog(ServerCommands(bot))
        await bot.add_cog(DestructiveCommands(bot))
        await bot.start(TOKEN)

    import asyncio
    asyncio.run(setup_bot())
 

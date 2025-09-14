import discord
from discord.ext import commands
from mcstatus import  JavaServer
import asyncio



# Ativando intents
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True  # Necessário para ler mensagens

# criando o bot com prefixo !
bot = commands.Bot(command_prefix="!", intents=intents)



# evento quando o bot fica on
@bot.event
async def on_ready():
    print(f" Bot conectado como {bot.user}")

#iniciar 
@bot.command()
async def iniciar(ctx):
    cargo = discord.utils.get(ctx.author.roles, name="Admin")  # nome do cargo q podera iniciar o comando 
    if cargo:
     while True: #loop
        CANAL_ID = 1234567890 #id do canal q ele trocara o nome pra "👥Jogadores: "
        guild = ctx.guild
        canal = guild.get_channel(CANAL_ID)
        server = JavaServer.lookup("exemplo.com:25565")#ip do servidor
        status = server.status()
        await canal.edit(name=f"👥Jogadores: {status.players.online}") #ele vai trocar o nome pra quantos players tão on
        await asyncio.sleep (120) # atualiza quantos players ta no servidor a cada 120s, se colocar tempo menor vc vai levar rate limited do discord
    else: #sem cargo ele n vai funcionar
        await ctx.send("❌ Você não tem permissão para usar este comando!")


# token
bot.run("")

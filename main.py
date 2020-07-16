import discord
from discord.ext import commands
import random
import time 
import asyncio 

client = commands.Bot(command_prefix = "!")
vecesNicoleCancelada = 0 # !nicole
vecesGabrielCancelado = 0 # !gabriel
vecesShalomCancelada = 0 # !shalom  
beeMovieScript = open("beeMovieScript/movieScript.txt","r")

@client.command() # add phrase to element.txt
async def agregar(ctx, *arg1):
    addSpace = [word + ' ' for word in arg1]
    stringPhrase = ''.join(addSpace)
    openAppendTXT = open("element.txt", "a") # if not in directory it will create file 
    openAppendTXT.write(stringPhrase + "\n")
    await ctx.send('" '+stringPhrase+'" ha sido agregado!') # "phrase" has been added!

@client.command()
async def frase(ctx):
    try:
        randomPhrases = open("element.txt", "r")
        listFile = randomPhrases.readlines()

        rPhrase = random.choice(listFile) # chooses random element from element.txt
        await ctx.send(rPhrase)
    except IndexError:
        await ctx.send("No hay frases disponibles...")

@client.command()
async def beeMovie(ctx):
    if ctx.author.id == 194152947808993280: # if author do command
        for e in beeMovieScript.readlines():
            if e == "":
                pass
            await ctx.send(e)
            await asyncio.sleep(2)
    else: await ctx.send("Perdón, pero no puedes hacer eso")
     
@client.command()
async def commandList(ctx):
    await ctx.send("""\n
    **!agregar** | Agregar frases a lista
    **!beeMovie** | Toda la pelicula de beeMovie en texto
    **!borrarUltimo** | Borra el ultimo elemento de la lista de frases
    **!ping** | Prueba de latencia
    **!todo**| Lista completa de todas las frases
    **!borrarLista** | Borra lista completa de frases
    **!logout** | Apaga el bot (SOLO ADMIN)
    **!nicole** | ???
    """)

@client.command()
async def borrarUltimo(ctx):
    phraseList = open("element.txt","w")
    print(type(phraseList))

@client.command()
async def ping(ctx): # get a response in miliseconds
    await ctx.send("Pong! {:.2f}".format(client.latency)) # round to an integer and a decimal 

@client.command()
async def todo(ctx):
    phraseList = open("element.txt", "r")
    readPhraseList = phraseList.readlines()
    await ctx.send(readPhraseList)

@client.command()
async def borrarLista(ctx):
    if ctx.author.id == 194152947808993280:
        open('element.txt', 'w').close()
    else: 
        await ctx.send("Perdón, pero tú no puedes hacer esto...")

'''COMANDOS ABAJO VECES CANCELADOS GABRIEL / SHALOM / NICOLE'''

@client.command()
async def nicole(ctx):
    global vecesNicoleCancelada
    vecesNicoleCancelada += 1
    if vecesNicoleCancelada == 1: await ctx.send("¡Nicole ha sido cancelada" + " " + str(vecesNicoleCancelada) + " vez!")
    else: await ctx.send("¡Nicole ha sido cancelada" + " " + str(vecesNicoleCancelada) + " veces!")

@client.command()
async def gabriel(ctx):
    global vecesGabrielCancelado
    vecesGabrielCancelado += 1
    if vecesGabrielCancelado == 1: await ctx.send("Gabriel ha sido cancelado" + " " + str(vecesGabrielCancelado) + " vez!")
    else: await ctx.send("¡Gabriel ha sido cancelado" + " " + str(vecesGabrielCancelado) + " veces!")

@client.command()
async def shalom(ctx):
    global vecesShalomCancelada
    vecesShalomCancelada += 1
    if vecesShalomCancelada == 1: await ctx.send("¡Shalom ha sido cancelada" + " " + str(vecesShalomCancelada) + " vez!")
    else: await ctx.send("Shalom ha sido cancelada" + " " + str(vecesShalomCancelada) + " veces!")

@client.command()
async def borrarContadores(ctx):
    global vecesGabrielCancelado
    global vecesNicoleCancelada
    global vecesShalomCancelada
    if ctx.author.id == 194152947808993280:
        vecesGabrielCancelado = 0 
        vecesNicoleCancelada = 0
        vecesShalomCancelada = 0
        await ctx.send("¡Contadores reiniciados desde 0!")

'''COMANDOS ARRIBA VECES CANCELADOS GABRIEL / SHALOM / NICOLE'''

@client.command()
async def logout(ctx):
    print("DISCONNECT! \n")
    if ctx.author.id == 194152947808993280 or ctx.author.id == 692158701255131178:
        await ctx.send("¡Desconectad@!")
        await ctx.bot.logout()
    else: await ctx.send("Perdón... no puedes desconectarme! Eso sería muy grosero de tu parte :open_mouth:")


client.run("token")

import discord
from discord.ext import commands
import random
import time 

client = commands.Bot(command_prefix = "!")
vecesNicoleCancelada = 0 # para el !nicole  

@client.command() # add phrase to element.txt
async def agregar(ctx, *arg1):
    addSpace = [word + ' ' for word in arg1]
    stringPhrase = ''.join(addSpace)
    openAppendTXT = open("element.txt", "a") # if not in directory it will create file 
    openAppendTXT.write(stringPhrase + "\n")
    await ctx.send('" '+stringPhrase+'" ha sido agregado!') # "phrase" has been added!

@client.command()
async def frase(ctx):
    randomPhrases = open("element.txt", "r")
    listFile = randomPhrases.readlines()

    rPhrase = random.choice(listFile) # chooses random element from element.txt
    await ctx.send(rPhrase)

@client.command()
async def ping(ctx): # get a response in miliseconds
    await ctx.send("Pong! {:.2f}".format(client.latency)) # round to an integer and a decimal 

@client.command()
async def todo(ctx):
    phraseList = open("element.txt", "r")
    readPhraseList = phraseList.readlines()
    await ctx.send(readPhraseList)

@client.command()
async def clearPhrases(ctx):
    if ctx.author.id == 194152947808993280:
        open('element.txt', 'w').close()
    else: ctx.send("Perdón, pero tú no puedes hacer esto...")

@client.command()
async def nicole(ctx):
    global vecesNicoleCancelada
    vecesNicoleCancelada += 1
    if vecesNicoleCancelada == 1: await ctx.send("¡Nicole ha sido cancelada" + " " + str(vecesNicoleCancelada) + " vez!")
    else: await ctx.send("¡Nicole ha sido cancelada" + " " + str(vecesNicoleCancelada) + " veces!")

@client.command()
async def logout(ctx):
    print("DISCONNECT! \n")
    if ctx.author.id == 194152947808993280:
        await ctx.send("Disconnect!!!")
        await ctx.bot.logout()
    else: await ctx.send("Perdón... no puedes desconectarme! Eso sería muy grosero de tu parte :open_mouth:")

client.run("token")

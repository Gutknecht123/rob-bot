import discord
import os
import requests
import json
import random
from keep_alive import keep_alive
from datetime import datetime

client = discord.Client()

pozycje = []




def strike(text):
    result = ''
    for c in text:
        result = result + c + '\u0336'
    return result

@client.event
async def on_ready():
  print('Zalogowany {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$helpme'):

    await message.channel.send('KOMENDY: \n bingo$create + 12 pozycji do bingo = Tworzy bingo \n bingo$show = Pokazuje aktualne bingo \n bingo$hit + nazwa pozycji = Skreślenie pozycji z bingo \n bingo$delete = Usuwa bingo \n $brek + @użytkownik = Przyzwanie Breka \n $pwbrek = Przyzwanie Breka na pw \n $dailybrek = Dzienne przyzwanie Breka na pw')
  
  if message.content.startswith('bingo$show'):
    if pozycje==[]:

      await message.channel.send('Nie utworzono jeszcze BINGO :(')
      return

    else:

      await message.channel.send('DISCORDOWE BINGO :PeepoGlad: :call_me:'+'\n'+'\n'+'[ '+pozycje[0]+' ]       [ '+pozycje[1]+' ]       [ '+pozycje[2]+' ] '+'\n'+'\n'+
       ' [ '+pozycje[3]+' ]       [ '+pozycje[4]+' ]       [ '+pozycje[5]+' ] '+'\n'+'\n'+
       ' [ '+pozycje[6]+' ]       [ '+pozycje[7]+' ]       [ '+pozycje[8]+' ] '+'\n'+'\n'+
       ' [ '+pozycje[9]+' ]       [ '+pozycje[10]+' ]       [ '+pozycje[11]+' ] '+'\n')
  
  if message.content.startswith('bingo$create'):

    if await message.channel.send(':+1:')==False:
      return

    mess = message.content
    
    x = mess[13:].split(';')

    if len(x)!=12:
      await message.channel.send('Podano nieprawidłową ilość pól! Musi być 12 :)')
      return

    pozycje.clear()  
    for i in range(0,len(x),1):
      pozycje.append(x[i])

    await message.channel.send(message.author.name+' - Bingo utworzone :call_me: ')
  
  if message.content.startswith('bingo$hit'):

    if await message.channel.send(':+1:')==False:
      return

    if pozycje==[]:

      await message.channel.send('Nie utworzono jeszcze BINGO :(')
      return

    else:
      mess = message.content

      x = mess[10:]

      for i in range(len(pozycje)):
        if x.upper()==pozycje[i].upper():
          pozycje[i]=strike(pozycje[i])
          await message.channel.send('Pole skreślone :)')
          blad=0
          break
        else:
          blad=1
        
      if blad==1:
        await message.channel.send('Podano złe pole!')

  if message.content.startswith('bingo$delete'):
    pozycje.clear()
    await message.channel.send('BINGO wyczyszczone')

  if message.content.startswith('$brek'):
    
    mess = message.content
    pom = mess[6:]
    await message.channel.send("Widzisz mnie? "+pom)
    await message.channel.send('https://tenor.com/view/brek-widzisz-mnie-gif-22339630')

 # elif "brek" in message.content.lower():

   # await message.channel.send("Widzisz mnie? "+message.author.mention)
   # await message.channel.send('https://tenor.com/view/brek-widzisz-mnie-gif-22339630')

  if message.content.startswith('$pwbrek'):
    
    await message.author.send("Widzisz mnie?")
    await message.author.send('https://tenor.com/view/brek-widzisz-mnie-gif-22339630')

  if message.content.startswith('$dailybrek'):

    daily = []
    data = []

    linki =[['Neutralny Brek ','https://cdn.discordapp.com/attachments/797142278652035096/871954688893923358/PZffziV.png'],
    ['Szczęśliwy Brek ','https://cdn.discordapp.com/attachments/797142278652035096/871954705239117874/mF17VgI.png'],
    ['Srebrny Brek ','https://cdn.discordapp.com/attachments/797142278652035096/871954727754149978/NeubI2a.png'],
    ['Cursed Brek ','https://cdn.discordapp.com/attachments/797142278652035096/871954744296489030/deJCgyN.png'],
    ['Smutny Brek ','https://cdn.discordapp.com/attachments/797142278652035096/871954767910408242/wctUfX2.png'],
    ['Zaskoczony Brek ','https://cdn.discordapp.com/attachments/797142278652035096/871954782770835466/HOyu6ZB.png'],
    ['Niewidzialny Brek','https://cdn.discordapp.com/attachments/797142278652035096/871954792128339978/mXD7NDK.png'],
    ['Thanos Brek ','https://cdn.discordapp.com/attachments/797142278652035096/871954828811730984/5F5abi6.png'],
    ['Matrix Brek','https://cdn.discordapp.com/attachments/797142278652035096/871954847212130365/H2TBU1h.png'],
    ['Vader Brek ','https://cdn.discordapp.com/attachments/797142278652035096/871954867168620595/6fCo0O4.png'],
    ['To nawet nie jest Brek! ','https://cdn.discordapp.com/attachments/797142278652035096/871954918309761035/poetciH.png'],
    ['USA Brek','https://cdn.discordapp.com/attachments/797142278652035096/871954937419010099/vQIjOQ3.png'],
    ['Niewyraźny Brek','https://cdn.discordapp.com/attachments/797142278652035096/871954974542819358/fmipNNu.png'],
    ['Jabolowy Brek','https://cdn.discordapp.com/attachments/797142278652035096/871954988841185320/l2K4syi.png'],
    ['Minecraft Brek','https://cdn.discordapp.com/attachments/797142278652035096/871954150282371082/KBbH0WX.png']]


    rand = random.randint(0, 14)

    file2 = open("date.txt","a+")
    file2.seek(0)
    Lines = file2.readlines()
    count = 0
    
    for line in Lines:
      count += 1
      print(line.strip())
      data.append(line.strip())

    

    

    #file2.write(message.created_at.strftime('%Y-%m-%d'))


    file1 = open("acc.txt","a+")
    file1.seek(0)
    Lines = file1.readlines()


    count = 0
    
    for line in Lines:
      count += 1
      #print(line.strip())
      daily.append(line.strip())
    




    if message.created_at.strftime('%Y-%m-%d') not in data or message.author.name not in daily:

      if message.created_at.strftime('%Y-%m-%d') not in data:
        open('acc.txt', 'w').close()
        open('date.txt', 'w').close()

        file2 = open("date.txt","a+")
        file2.seek(0)

        file2.write(message.created_at.strftime('%Y-%m-%d'))

        file2.close()

      file2.close()

      #daily.append(message.author.name)

      file1.write(message.author.name+"\n")
    
      await message.author.send("Twój daily Brek to: "+linki[rand][0])

      await message.author.send(linki[rand][1])

      #await message.author.send(message.created_at)

      #file1.seek(0)

      #await message.author.send(daily)
    elif message.author.name in daily and message.created_at.strftime('%Y-%m-%d') in data:

      #await message.author.send(message.created_at)
      await message.author.send("Już brałeś dzisiaj!")
    file2.close()  
    file1.close()
    



keep_alive()
client.run(os.getenv('TOKEN'))
















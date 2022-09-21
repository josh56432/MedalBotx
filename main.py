CODE IS DISABLED
import keepalive
keepalive.keep_alive()
import os
import discord
import discord.utils
import psutil
import io
import time
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


intents = discord.Intents.default()
intents.members = True
intents.messages = True
client = discord.Client(intents=intents)

from PIL import Image

def split(word):
    return [char for char in word]

def merge(medals,caps,coats,roleimg,speclist,SCC):
  print('RAM memory % used:', psutil.virtual_memory()[2])
  xpadding = 20 #padding between medals (px)
  ypadding=20
  images = [Image.open(x) for x in medals]
  capimages = [Image.open(x) for x in caps]
  coatimages = [Image.open(x) for x in coats]
  specimages = [Image.open(x) for x in speclist]
  new_im = Image.new('RGBA', (0, 800))
  x_offset = 0
  y_offset=0
  column=0
  row=0
  if(len(medals)+len(caps)+len(coats)<7):
    limit=3
  else:
    limit=6
  for im in images:
    #crops png
    bbox = im.getbbox()
    image = im.crop(bbox)
    (width, height) = image.size
    cropped_image = Image.new("RGBA", (width, height), (0,0,0,0))
    cropped_image.paste(image, (0, 0))
    #rescales to 800 px tall
    targetHeight = 400
    heightPercent = (targetHeight/float(cropped_image.size[1]))
    targetWidth = int((float(cropped_image.size[0])*float(heightPercent)))
    img = cropped_image.resize((targetWidth,targetHeight))
    #increments and adds new image
    if column<limit:
      holder=new_im
      new_width=holder.width+img.width
      new_im = Image.new('RGBA', (new_width+xpadding, holder.height))
      new_im.paste(holder,(0,0))
      new_im.paste(img, (x_offset, y_offset))
      x_offset += img.width+xpadding
      column+=1
      holder.close()
    else: #new row
      bbox = new_im.getbbox()
      image = new_im.crop(bbox)
      (width, height) = image.size
      new_im = Image.new("RGBA", (width, height), (0,0,0,0))
      new_im.paste(image, (0, 0))
      holder=new_im
      column=1
      x_offset = img.width+xpadding
      new_height=holder.height+img.height+ypadding
      new_im = Image.new('RGBA', (holder.width, new_height))
      new_im.paste(holder,(0,0))
      new_im.paste(img, (0, new_height-img.height))
      y_offset += img.height+ypadding
      row+=1
      holder.close()

  
  print("Done")
  if column>1 and len(coatimages)>1:
    column=limit
  for im in coatimages:
    #crops png
    bbox = im.getbbox()
    image = im.crop(bbox)
    (width, height) = image.size
    cropped_image = Image.new("RGBA", (width, height), (0,0,0,0))
    cropped_image.paste(image, (0, 0))
    #rescales to 800 px tall
    targetHeight = 400
    heightPercent = (targetHeight/float(cropped_image.size[1]))
    targetWidth = int((float(cropped_image.size[0])*float(heightPercent)))
    img = cropped_image.resize((targetWidth,targetHeight))
    #increments and adds new image
    if column<limit:
      holder=new_im
      new_width=holder.width+img.width
      new_im = Image.new('RGBA', (new_width, holder.height))
      new_im.paste(holder,(0,0))
      new_im.paste(img, (x_offset, y_offset))
      x_offset += img.width+xpadding
      column+=1
      holder.close()
    else: #new row
      bbox = new_im.getbbox()
      image = new_im.crop(bbox)
      (width, height) = image.size
      new_im = Image.new("RGBA", (width, height), (0,0,0,0))
      new_im.paste(image, (0, 0))
      holder=new_im
      column=1
      x_offset = img.width+xpadding
      new_height=holder.height+img.height+ypadding
      new_im = Image.new('RGBA', (holder.width, new_height))
      new_im.paste(holder,(0,0))
      new_im.paste(img, (0, new_height-img.height))
      y_offset += img.height+ypadding
      row+=1
      holder.close()
  print('RAM memory % used:', psutil.virtual_memory()[2])
  print("Done")
  if column>1 and len(capimages)>1:
    column=limit
  for im in capimages:
    #crops png
    bbox = im.getbbox()
    image = im.crop(bbox)
    (width, height) = image.size
    cropped_image = Image.new("RGBA", (width, height), (0,0,0,0))
    cropped_image.paste(image, (0, 0))
    #rescales to 800 px tall
    targetHeight = 400
    heightPercent = (targetHeight/float(cropped_image.size[1]))
    targetWidth = int((float(cropped_image.size[0])*float(heightPercent)))
    img = cropped_image.resize((targetWidth,targetHeight))
    #increments and adds new image
    if column<limit:
      holder=new_im
      new_width=holder.width+img.width+xpadding
      new_im = Image.new('RGBA', (new_width+xpadding, holder.height))
      new_im.paste(holder,(0,0))
      new_im.paste(img, (x_offset, y_offset))
      x_offset += img.width+xpadding
      column+=1
    else: #new row
      bbox = new_im.getbbox()
      image = new_im.crop(bbox)
      (width, height) = image.size
      new_im = Image.new("RGBA", (width, height), (0,0,0,0))
      new_im.paste(image, (0, 0))
      holder=new_im
      column=1
      x_offset = img.width+xpadding
      new_height=holder.height+img.height+ypadding
      new_im = Image.new('RGBA', (holder.width, new_height))
      new_im.paste(holder,(0,0))
      new_im.paste(img, (0, new_height-img.height))
      y_offset += img.height+ypadding
      row+=1
  print('RAM memory % used:', psutil.virtual_memory()[2])
  print("Done")
  im.close()
  image.close()
  holder.close()
  cropped_image.close()
  img.close()
  bbox = new_im.getbbox()
  image = new_im.crop(bbox)
  (width, height) = image.size
  new_im = Image.new("RGBA", (width, height), (0,0,0,0))
  time.sleep(1)
  new_im.paste(image, (0, 0))
  out_im=new_im
  
  targetHeight = 1080
  heightPercent = (targetHeight/float(out_im.size[1]))
  targetWidth = int((float(out_im.size[0])*float(heightPercent)))
  out_im = out_im.resize((targetWidth,targetHeight))
  
  print(speclist)

  if len(specimages)<9:
    targetHeight = int(round(out_im.height/6))
  else:
    targetHeight = int(round(out_im.height/8))
  holder=Image.new('RGBA', (100,100))
  x_offset=holder.width
  targety=holder.height
  y_offset=targety+holder.height
  new_width=0
  x=0
  y_place=0
  holder =Image.new('RGBA', (0,0))
  for im in specimages:
    bbox = im.getbbox()
    image = im.crop(bbox)
    (width, height) = image.size
    im = Image.new("RGBA", (width, height), (0,0,0,0))
    im.paste(image, (0, 0))

    heightPercent = (targetHeight/float(im.size[1]))
    targetWidth = int((float(im.size[0])*float(heightPercent)))
    im = im.resize((targetWidth,targetHeight))

    new_img = Image.new('RGBA', (im.width*(len(speclist)),y_offset+20))
    new_img.paste(holder,(0,0))
    new_img.paste(im,(int((x*im.width)),y_place))
   # print(int((x*im.width)))
    new_width=new_img.width+im.width 
    holder=new_img
    x+=1
    if(x==3):
      y_offset+= im.height+20
      y_place += im.height+20
      x_offset = im.width
      x=0
  
  SCC_im=Image.new("RGBA",(0,0), (0,0,0,0))
  if(SCC==True):
    im = Image.open("Storm Cannon Certified.png")
    bbox = im.getbbox()
    image = im.crop(bbox)
    (width, height) = image.size
    cropped_image = Image.new("RGBA", (width, height), (0,0,0,0))
    cropped_image.paste(image, (0, 0))
    targetHeight = int(1/6*out_im.height)
    heightPercent = (targetHeight/float(cropped_image.size[1]))
    targetWidth = int((float(cropped_image.size[0])*float(heightPercent)))
    SCC_im = cropped_image.resize((targetWidth,targetHeight))
    


  if(len(speclist)>0):
    bbox = new_img.getbbox()
    image = new_img.crop(bbox)
    (width, height) = image.size
    new_img = Image.new("RGBA", (width, height), (0,0,0,0))
    new_img.paste(image, (0, 0))

  print('RAM memory % used:', psutil.virtual_memory()[2])
  print("Done")
  im = Image.open(roleimg)
  #crops png
  bbox = im.getbbox()
  image = im.crop(bbox)
  (width, height) = image.size
  cropped_image = Image.new("RGBA", (width, height), (0,0,0,0))
  cropped_image.paste(image, (0, 0))
  #rescales to 800 px tall
  targetHeight = int(1/2*out_im.height)
  heightPercent = (targetHeight/float(cropped_image.size[1]))
  targetWidth = int((float(cropped_image.size[0])*float(heightPercent)))
  new_img2 = cropped_image.resize((targetWidth,targetHeight))
  # #adds to right#
  output_im = new_img2

  column=0
  rolemove=0
  try:
    rolemove=int(0.5*new_img.width-0.5*output_im.width)
  except:
    x=x
  
  im = Image.open("Dotted-line.png")

  try:
    if((output_im.height+new_img.height+SCC_im.height+20)>out_im.height):
      targetHeight = int(output_im.height+new_img.height+SCC_im.height+20)
    else:
      targetHeight = int(out_im.height)
  except:
    targetHeight = int(out_im.height)
  heightPercent = (targetHeight/float(im.size[1]))
  targetWidth = int((float(im.size[0])*float(heightPercent)))
  dotted = im.resize((targetWidth,targetHeight))

  bbox = dotted.getbbox()
  image = dotted.crop(bbox)
  (width, height) = image.size
  dotted = Image.new("RGBA", (width, height), (0,0,0,0))
  dotted.paste(image, (0, 0))


  #medalim = Image.open("out.png")
  if(roleimg=="COL.png"):
    coloffset=20
  else:
    coloffset=0
  holder=out_im
  if(len(speclist)>0):
    new_width=holder.width+500+output_im.width+int(0.35*holder.width)
  else:
    new_width=holder.width+int(0.4*holder.width)+output_im.width
  try:
    if((output_im.height+new_img.height+SCC_im.height+20)>holder.height):
      out_im1 = Image.new('RGBA', (new_width, output_im.height+new_img.height+SCC_im.height+20))
    else:
      out_im1 = Image.new('RGBA', (new_width, round(holder.height*1.2)))
  except:
    out_im1 = Image.new('RGBA', (new_width, round(holder.height*1.2)))
  out_im1.paste(holder,(0,0))
  out_im1.paste(dotted,(holder.width+int(0.1*holder.width),0))
  out_im1.paste(output_im,(holder.width+int(0.25*out_im.width)+rolemove+coloffset, 0))
  #+int(round(1/3*len(speclist)*targetHeight)
  yplus=0
  try:
    out_im1.paste(new_img, (holder.width+int(0.25*out_im.width)+coloffset, output_im.height+20))
    yplus+=new_img.height
  except:
    x=x
  out_im1.paste(SCC_im, (holder.width+int(0.25*out_im.width)+coloffset, output_im.height+yplus+20))


  bbox = out_im1.getbbox()
  image = out_im1.crop(bbox)
  (width, height) = image.size
  cropped_image = Image.new("RGBA", (width, height), (0,0,0,0))
  cropped_image.paste(image, (0, 0))
  print('RAM memory % used:', psutil.virtual_memory()[2])
  print("Processed Image")
  return cropped_image




@client.event
async def on_ready():
    print("Ready!")
    file1 = open("prefix.txt","r")
    prefix=file1.readline()
    file1.close()
    file1 = open("Maintenance.txt","r")
    maintain=file1.readline()
    file1.close()
    if maintain == "0":
      await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="for "+prefix))
    else:
      await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="Maintenance mode"))






@client.event
async def compiler(message, user, role):  
  spec = ["Armor","Artillery","Engineering","Grenadier","Heavy Weapons Operator","Logistics","Marine","Medic","Partisan","Pirate","Recon","Infantry"]
  medals = []
  x=0
  try:
      Image.open(role+".png")
      roleimg = (role+".png")
  except:
      roleimg = "Colonial.png"
  for i in range(len(user.roles)):
    try:
      if(str(user.roles[i])=="Strategic/Recon"):
        medals.append("Recon.png")
      elif(str(user.roles[i].id)=="905474494536228885"):
        medals.append("Korn Capture Prize.png")
      else:
        Image.open(str(user.roles[i])+".png")
        medals.append(str(user.roles[i])+".png")
      x+=1
    except:
      x=x
  speclist=[]
  z=0
  SCC=False
  for i in range(len(medals)):
      try:
        print((medals[z].split(".")[0]))
        if(medals[z].split(".")[0] in spec):
          speclist.append(medals[z])
          del medals[z]
          z=z-1
        elif(medals[z].split(".")[0] == "Storm Cannon Certified"):
          SCC=True
          del medals[z]
          z=z-1
        z+=1
      except:
        z+=1
  if len(medals)==0:
    medals.append("youtried.png")
  medalsOut=sorted(medals, key=str.lower,reverse=True)
  z=0
  for i in range(len(medalsOut)):
    try:
      if(medalsOut[z].split(" ")[len(medalsOut[z].split(" "))-1]!="Class.png" and medalsOut[z].split(" ")[len(medalsOut[z].split(" "))-1]!="class.png"):
        medalsOut.append(medalsOut[z])
        del medalsOut[z]
        z=z-1
      z+=1
    except Exception as e:
      z+=1
      print(e)
  coatlist=[]
  z=0
  for i in range(len(medalsOut)):
    try:
      if(medalsOut[z].split(" ")[1]=="Coat"):
        coatlist.append(medalsOut[z])
        del medalsOut[z]
        z=z-1
      z+=1
    except:
      z+=1
  coatlist= sorted(coatlist, key=str.lower)
  if len(coatlist)==3:
    hold = coatlist[1]
    coatlist[1]=coatlist[2]
    coatlist[2]=hold
  if len(coatlist)==4:
    hold = coatlist[1]
    coatlist[1]=coatlist[3]
    coatlist[3]=hold
    hold = coatlist[2]
    coatlist[2]=coatlist[3]
    coatlist[3]=hold
  z=0
  caplist=[]
  for i in range(len(medalsOut)):
    try:
      if(medalsOut[z].split(" ")[1]=="Cap"):
        caplist.append(medalsOut[z])
        del medalsOut[z]
        z=z-1
      z+=1
    except:
      z+=1
  z=0
  for i in range(len(medalsOut)):
    try:
      if(medalsOut[z].split(" ")[1]=="Capture"):
        caplist.append(medalsOut[z])
        del medalsOut[z]
        z=z-1
      z+=1
    except:
      z+=1
  z=0
  tablist=[]
  for i in range(len(medalsOut)):
    try:
      if(medalsOut[z].split(" ")[1]=="Tab.png"):
        tablist.append(medalsOut[z])
        del medalsOut[z]
        z=z-1
      z+=1
    except:
      z+=1
  tablist= sorted(tablist, key=str.lower)
  if len(tablist)==3:
    tablist.append(tablist[2])
    tablist[2]=tablist[1]
    tablist[1]=tablist[0]
    tablist[0]=tablist[3]
    del tablist[3]
  for i in range(len(tablist)):
    medalsOut.append(tablist[i])
  z=0
  for i in range(len(medalsOut)):
    try:
      if(medalsOut[z].split(" ")[0]=="Commendation"):
        coatlist.append(medalsOut[z])
        del medalsOut[z]
        z=z-1
      z+=1
    except:
      z+=1
  
  image = merge(medalsOut,caplist,coatlist,roleimg,speclist,SCC)
  title1 = "Medal Cabinet for: "+user.display_name
  embedVar = discord.Embed(title=title1, color=user.color)
  with io.BytesIO() as output:
    image.save(output, format="PNG")
    im = output.getvalue()
  f = io.BytesIO(im)
  file = discord.File(f, filename="output.png")
  embedVar.set_image(url="attachment://output.png")
  embedVar.set_footer(text="-Made by Stolas")
  embedVar.set_author(name="MedalCabinetBot",icon_url="https://cdn.discordapp.com/attachments/867837759518146583/899405909531447346/141.png")
  await message.channel.send(file=file, embed=embedVar)
  print('RAM memory % used:', psutil.virtual_memory()[2])
  print("Image Sent")







@client.event
async def on_message(message, user=discord.Member):
  file1 = open("prefix.txt","r")
  prefix=file1.readline()
  file1.close()
  file1 = open("Maintenance.txt","r")
  maintain=file1.readline()
  file1.close()
  role=""
  if message.content.split(" ")[0] == prefix+"cabinet":
    if message.channel.id == 992061915322925126 and message.author.id != 897838899584442418:
      message2 = await message.channel.send("Loading Medals")
      file = discord.File("loading-bar.gif",       filename="roadwork.gif")
      message3 = await message.channel.send(file=file)
     
      if maintain == "1":
        await message.channel.send("Bot under maintainence")
        file = discord.File("roadwork.png", filename="output.png")
        await message.channel.send(file=file)
     
      if len(message.content.split(" "))>1:
        username=message.content.split(" ")[1]
        username=username.replace("<","")
        username=username.replace(">","")
        username=username.replace("@","")
        username=username.replace("!","")
        try:
          user = message.guild.get_member(int(username))
          uname=user.display_name
          uname=uname.split("]")
          role=uname[0].replace("[","")
          if(user.id == 514789033176596482):
            role="GEN"
          await compiler(message, user, role)
          await message2.delete()
          await message3.delete()
        except Exception as e:
          await message.channel.send("Invalid User!")
          await message2.delete()
          await message3.delete()
          print(e)
      else:
        user= message.author
        uname=user.display_name
        uname=uname.split("]")
        role=uname[0].replace("[","")
        await compiler(message, user,role)
        await message2.delete()
        await message3.delete()
   
    else:
      await message.channel.send("Go to <#992061915322925126> to use this.")

      
  if message.content.split(" ")[0] == prefix+"stats":
    list1=[]
    x=0
    for i in range(len(message.guild.roles)):
      try:
          Image.open(str(message.guild.roles[i])+".png")
          if len(str(message.guild.roles[i]).split(" "))>1: 
            list1.append(message.guild.roles[i].id)
          x+=1
      except:
          x=x
    if x == 0:
        await message.channel.send("Error!")
    rep=int(str(len(list1)/25).split(".")[0])+1
    for x in range(rep):
      embed = discord.Embed(title="All time medal awards #"+str(x+1), color=message.author.color)
      for i in range(25):  
        try:
          rolename=str(message.guild.get_role(list1[i+(25*x)]))+":"
          role = message.guild.get_role(list1[i+(25*x)])
          rolelength = len(role.members)
        except Exception as e:
          print(e)
          break;
        embed.add_field(name=rolename, value=rolelength, inline=True)
      embed.set_author(name="MedalCabinetBot",icon_url="https://cdn.discordapp.com/attachments/867837759518146583/899405909531447346/141.png")
      await message.channel.send(embed=embed)
  
  if message.content.split(" ")[0] == prefix+"display":
    text=""
    for i in range(1,len(message.content.split(" "))-1):
      text += message.content.split(" ")[i]+" "
    text += message.content.split(" ")[len(message.content.split(" "))-1]
    try:
      memberlist=""
      Image.open(text+".png")
      for member in message.guild.members:
        for role in member.roles:
          if member.id != 897838899584442418 and role.name == text or (text == "Korn Capture Prize" and role.id == 905474494536228885):
            memberlist+=member.display_name+"\n"
      embed = discord.Embed(title=text, color=message.author.color)
      file = discord.File(text+".png", filename="output.png")
      embed.set_image(url="attachment://output.png")
      mem=split(memberlist)
      if len(mem)<=1024:
        embed.add_field(name="Recipients:", value="```"+memberlist+"```", inline=True)
      else:
        memberlist = memberlist.replace("\n","\n~")
        memberlist = memberlist.split("~")
        for x in range(len(memberlist)):
          memlist = memberlist[0:20]
          del memberlist[0:20]
          print(memlist)
          memberout=""
          for i in range(len(memlist)):
            memberout+=memlist[i]
          if len(split(memberout)) ==0:
            break;
          if x<1:
            embed.add_field(name="Recipients:", value="```"+memberout+"```", inline=True)
          else:
            embed.add_field(name="‎", value="```"+memberout+"```", inline=True)

      embed.set_author(name="MedalCabinetBot",icon_url="https://cdn.discordapp.com/attachments/867837759518146583/899405909531447346/141.png")
      await message.channel.send(file=file,embed=embed)
    except Exception as e:
      print(e)
      await message.channel.send("Invalid medal name!")
  
  if message.content.split(" ")[0] == prefix+"maintenance":
    if message.author.id == 352829345863303168:
      if maintain == "0":
        file1 = open("Maintenance.txt","w")
        file1.write("1")
        file1.close()
        message1=await message.channel.send("Maintenance mode activated")
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="Maintenance mode"))
      else:
        file1 = open("Maintenance.txt","w")
        file1.write("0")
        file1.close()
        message1=await message.channel.send("Maintenance mode deactivated")
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="for "+prefix))
      time.sleep(2)
      await message.delete()
      await message1.delete()


  
  listmes = message.content.split(" ")
  role = discord.utils.find(lambda r: r.name == 'Senior Officer', message.guild.roles)
  if listmes[0]==prefix+"prefix":
      if role in message.author.roles:
          if len(listmes)>1:
              prefix = listmes[1]
              file1 = open("prefix.txt","w")
              file1.write(prefix)
              file1.close()
              await message.channel.send("Prefix is now "+'"'+prefix+'"')
              await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="for "+prefix))
          else:
              await message.channel.send("Prefix is still "+'"'+prefix+'"'+" this is because input error occured.")
      else:
          await message.channel.send("You do not have the 'Senior Officer' role please get this role before doing settings commands")



client.run(TOKEN)
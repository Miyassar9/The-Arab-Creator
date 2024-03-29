
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
import telebot
from telebot import *
from telebot import types

from PIL import Image, ImageDraw,ImageFont

user_data={}

text1_pos=(280,292)
text2_pos=(130,350)
text3_pos=(95,390)
text4_pos=(550,392)
text5_pos=(100,450)
text6_pos=(400,450)
image=Image.open("template.jpg")
d=ImageDraw.Draw(image)
font=ImageFont.truetype("arial.ttf",26)
text_pos=[(280,292),(130,350),(95,390),(550,392),(100,450),(400,450)]
item = 0
course=''
hour=0
name=''
date=''
manger=''
coach=''
text_color=(0,0,0)
c =True

# Replace 'YOUR_TOKEN' with your actual bot token

bot=telebot.TeleBot('7139140547:AAE7oe_3nN6WJs7XOnGfbW32LLOJDqhU-Oc')

@bot.message_handler(commands=["start"])
def question(message):
   
    markup=types.InlineKeyboardMarkup(row_width=2)
    command1=types.InlineKeyboardButton('إصدار شهادة',callback_data='creat')
    command2=types.InlineKeyboardButton('تعديل المعلومات الإدارية',callback_data='edit')
   
    markup.add(command1,command2)
    bot.send_message(message.chat.id,'Welcome to The Arab Creator bot',reply_markup=markup)

   
    


@bot.callback_query_handler(func=lambda call:True)
def button_click(call):
     global c
     if call.message:
       if call.data=='creat':
         
         bot.send_message(call.message.chat.id,'اسم الطالب:')
         chat_id = call.message.chat.id
         user_data[chat_id] = {}
         c=False
       
       elif  call.data=='edit':
         c=True
         global item,course,hour
         item=0
         course=''
         hour=0
         bot.send_message(call.message.chat.id,'اسم الكورس')
@bot.message_handler(func=lambda message:True)       
def ed(message):
   
   print (message.text)
   global item,course,hour,name,date,manger,coach
   chat_id = message.chat.id
   if c==True:
     if item==0:
      course=message.text
       
     
      bot.send_message(message.chat.id,'عدد الساعات:')
     if item==1:
      hour=message.text
      bot.send_message(message.chat.id,'التاريخ:')
     if item==2:
      date=message.text
      bot.send_message(message.chat.id,'اسم المدير:') 
     if item==3:
      manger=message.text
      bot.send_message(message.chat.id,'اسم المدرب:') 
     if item==4:
       coach=message.text
     
       image=Image.open("template.jpg")
       d=ImageDraw.Draw(image)
   
       d.text(text2_pos,text=course,fill=text_color,font=font)
       d.text(text3_pos,text=hour,fill=text_color,font=font)
       d.text(text4_pos,text=date,fill=text_color,font=font)
       d.text(text5_pos,text=manger,fill=text_color,font=font)
       d.text(text6_pos,text=coach,fill=text_color,font=font)
       image.save(f"{course}_img.jpg")
       photo_path=f'{course}_img.jpg'
       bot.send_photo(chat_id,photo=open(photo_path,'rb'))
       
       markup=types.InlineKeyboardMarkup(row_width=2)
       command1=types.InlineKeyboardButton('إصدار شهادة',callback_data='creat')
       command2=types.InlineKeyboardButton('تعديل المعلومات الإدارية',callback_data='edit')
   
       markup.add(command1,command2)
       bot.send_message(message.chat.id,'Welcome to The Arab Creator bot',reply_markup=markup)
     item+=1
   else:
       name=message.text
       image=Image.open(f"{course}_img.jpg")
       d=ImageDraw.Draw(image)
   
       d.text(text1_pos,text=name,fill=text_color,font=font)
       image.save(f"{name}_img.jpg")
       photo_path=f'{name}_img.jpg'
       bot.send_photo(chat_id,photo=open(photo_path,'rb'))
       markup=types.InlineKeyboardMarkup(row_width=2)
       command1=types.InlineKeyboardButton('إصدار شهادة',callback_data='creat')
       command2=types.InlineKeyboardButton('تعديل المعلومات الإدارية',callback_data='edit')
   
       markup.add(command1,command2)
       bot.send_message(message.chat.id,'Welcome to The Arab Creator bot',reply_markup=markup)
      



def main():
   


    bot.poll_handler(CommandHandler("start",question))
   
   
    bot.polling()

if __name__ == '__main__':
    main()
#-*- coding:utf-8 -*-

# 모듈 임포트
import telegram
import os
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters
import logging
import random
import urllib
import urllib3
import re
from requests import get
import urllib.request
import urllib.parse
import time
import datetime
from bs4 import BeautifulSoup

# 정상적으로 모듈임포트 완료/기본설정 시작 안내
print("\n모듈 임포트 완료!\n기본 설정중. . .")

#토큰을 변수에 저장
meal_token = '토큰'

#봇 선언
bot = telegram.Bot(token = meal_token)

#커스텀 키보드 설정
custom_keyboard = [
        ["/help",  "공유하기!"],
        ["Winsub 상태", "Winsub 링크"],
        ]
reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)

#시간설정
n = time.localtime().tm_wday
now = datetime.datetime.now()

# 윈섭 xml 리스트 확인
file = open(filename, 'w')
xml=file.read()
file.close()
soup = BeautifulSoup(xml, 'html.parser')winsubxml
winsubxml = soup.find("winsubxml")
url = winsubxml.get_text()
while True:

    #1
    service1name = soup.find("service1name")
    service1name = service1name.get_text()
    if service1name == "x":
        service=1
        break
    service1tag = soup.find("service1tag")
    service1tag = service1tag.get_text()
    if service1tag == "x":
        service=1
        break
            
    #2
    service2name = soup.find("service2name")
    service2name = service2name.get_text()
    if service2name == "x":
        service=2
        break
    service2tag = soup.find("service2tag")
    service2tag = service2tag.get_text()
    if service2tag == "x":
        service=2
        break

    #3
    service3name = soup.find("service3name")
    service3name = service3name.get_text()
    if service3name == "x":
        service=3
        break
    service3tag = soup.find("service3tag")
    service3tag = service3tag.get_text()
    if service3tag == "x":
        service=3
        break

    #4
    service4name = soup.find("service4name")
    service4name = service4name.get_text()
    if service4name == "x":
        service=4
        break
    service4tag = soup.find("service4tag")
    service4tag = service4tag.get_text()
    if service4tag == "x":
        service=4
        break

    #5
    service5name = soup.find("service5name")
    service5name = service5name.get_text()
    if service5name == "x":
        service=5
        break
    service5tag = soup.find("service5tag")
    service5tag = service5tag.get_text()
    if service5tag == "x":
        service=5
        break

    #6
    service6name = soup.find("service6name")
    service6name = service4name.get_text()
    if service6name == "x":
        service=6
        break
    service6tag = soup.find("service6tag")
    service6tag = service6tag.get_text()
    if service6tag == "x":
        service=6
        break

    #7
    service7name = soup.find("service7name")
    service7name = service7name.get_text()
    if service7name == "x":
        service=7
        break
    service7tag = soup.find("service7tag")
    service7tag = service7tag.get_text()
    if service7tag == "x":
        service=7
        break

    #8
    service8name = soup.find("service8name")
    service8name = servicename.get_text()
    if service8name == "x":
        service=8
        break
    service8tag = soup.find("service8tag")
    service8tag = service8tag.get_text()
    if service8tag == "x":
        service=8
        break

    #9
    service9name = soup.find("service9name")
    service9name = service9name.get_text()
    if service9name == "x":
        service=9
        break
    service9tag = soup.find("service9tag")
    service9tag = service7tag.get_text()
    if service9tag == "x":
        service=9
        break

    #10
    service10name = soup.find("service10name")
    service10name = service10name.get_text()
    if service10name == "x":
        service=10
        break
    service10tag = soup.find("service10tag")
    service10tag = service10tag.get_text()
    if service10tag == "x":
        service=10
        break

    #11
    service11name = soup.find("service11name")
    service11name = service11name.get_text()
    if service11name == "x":
        service=11
        break
    service11tag = soup.find("service11tag")
    service11tag = service11tag.get_text()
    if service11tag == "x":
        service=11
        break

    #12
    service12name = soup.find("service12name")
    service12name = service12name.get_text()
    if service12name == "x":
        service=12
        break
    service12tag = soup.find("service12tag")
    service12tag = service12tag.get_text()
    if service12tag == "x":
        service=12
        break

    #13
    service13name = soup.find("service13name")
    service13name = service13name.get_text()
    if service13name == "x":
        service=13
        break
    service13tag = soup.find("service13tag")
    service13tag = service13tag.get_text()
    if service13tag == "x":
        service=13
        break

    #14
    service14name = soup.find("service14name")
    service14name = service14name.get_text()
    if service14name == "x":
        service=14
        break
    service14tag = soup.find("service14tag")
    service14tag = service14tag.get_text()
    if service14tag == "x":
        service=14
        break

    #15
    service15name = soup.find("service15name")
    service15name = service15name.get_text()
    if service15name == "x":
        service=15
        break
    service15tag = soup.find("service15tag")
    service15tag = service15tag.get_text()
    if service15tag == "x":
        service=15
        break

    break

#커스텀 키보드 설정/봇 시작 알림
bot.send_message(chat_id=79673869, text="Start Winsub 봇, 커스텀 키보드 설정완료!",  reply_markup=reply_markup)
bot.send_message(chat_id=564590318, text="Start Winsub 봇, 커스텀 키보드 설정완료!",  reply_markup=reply_markup)
#초기설정 성공 안내
print("Start Winsub 봇")

#도움말
def help_command(bot, update) :
    update.message.reply_text("""Winsub 봇 도움말\n이 봇은 Winsub 을 위한 Winsub 에 관한 정보를 알려주는 봇입니다.""", reply_markup=reply_markup)

# 시작 메시지
def start_command(bot, update) :
    update.message.reply_text("안녕하세요! Winsub 봇입니다.\n도움말을 보시려면 /help << 이 문자를 눌러주세요!", reply_markup=reply_markup)

# 메인 루프
def get_message(bot, update) :

    if update.message.text[7:9]=="상태":

        with urllib.request.urlopen(url) as response:
            html = response.read()
            soup = BeautifulSoup(html, 'html.parser')

        service1status = soup.find(service1tag)
        service1status=service1status.get_text()

        service2status = soup.find(service2tag)
        year = soup.find("year")
        mainpagesay = soup.find("mainpagesay")
        cloudsay = soup.find("cloudsay")
        linksay = soup.find("linksay")
        myipsay = soup.find("myipsay")
        bksay = soup.find("bksay")

        update.message.reply_text("""%s
%s %s
메인 페이지 상태 : %s
윈섭 클라우드 상태 : %s
링크단축 상태 : %s
내 아이피 상태 : %s
복마이크(북마크) 상태 : %s""" %(domain.get_text(), copyname.get_text(), year.get_text(), mainpagesay.get_text(), cloudsay.get_text(), linksay.get_text(), myipsay.get_text(), bksay.get_text()))


    if update.message.text[7:9]=="링크":

        with urllib.request.urlopen(url) as response:
            html = response.read()
            soup = BeautifulSoup(html, 'html.parser')

        domain = soup.find("domain")
        update.message.reply_text("Winsub\n%s" %domain)



    # 날짜와 시간
    if update.message.text[0:2]=="날짜":
        now = datetime.datetime.now()
        update.message.reply_text("오늘의 날짜 : \n%s년 %s월 %s일 입니다." %(now.year,now.month, now.day))

    if update.message.text[0:2]=="시간":
        now = datetime.datetime.now()
        update.message.reply_text("현재 시간 : \n%s시 %s분 %s초 입니다." %(now.hour,now.minute, now.second))

    # 봇 공유링크
    if update.message.text[0:2]=="공유":
        update.message.reply_text("아래 링크를 복사하여 친구에게 공유하세요.\n상대방이 Telegram이 설치된 상태여야 합니다.\n\nhttps://t.me/winsubbot")

updater = Updater(meal_token)

message_handler = MessageHandler(Filters.text, get_message)
updater.dispatcher.add_handler(message_handler)

help_handler = CommandHandler('help', help_command)
updater.dispatcher.add_handler(help_handler)

start_handler = CommandHandler('start', start_command)
updater.dispatcher.add_handler(start_handler)

updater.start_polling()
updater.idle()

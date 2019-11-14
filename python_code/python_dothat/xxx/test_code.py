# a=[1,2,3]
# b=[4,5,6]
# c={1:2,2:3}
# e={3:4,4:5}
# # c[4]=6
# # for i in c.items():
# #     print(i)
# #     print(i[1])
# # print()
# print(c)
# for ai,bi in zip(a,b):
#     print(type(ai),bi)
import ctypes
import inspect
import pymssql
# import PyQt5
import random
import time
# from PIL import Image
import threading
import tkinter
from tkinter import Label, Tk, Entry, Scrollbar, RIGHT, Text, LEFT, END, INSERT, Button, Toplevel, mainloop, Y, \
    Radiobutton, IntVar
from tkinter import ttk
import time
import pygame
import datetime
# import os
import win32api
from aip import AipSpeech
# import itchat
import os
# import cv2
# from PIL import ImageGrab
# import sys
from  docx import  Document
# from  docx.shared import  Pt
# from  docx.oxml.ns import  qn
# from docx.shared import Inches
# 导入tkinter模块的所有内容
from aip import AipFace
import base64
import cv2
import os
# 首先导入email模块构造邮件
from email.mime.text import MIMEText
# 然后是导入smtplib模块发送邮件
import smtplib

from mutagen.mp3 import MP3
import time, datetime
# 字符类型的时间
print('软件启动中....')
server = 'SC-201903271457'
user = 'sa'
password = 'sqlserver_li'
database = 'aibinghaus'
conn = pymssql.connect(server, user, password, database)
cur1 = conn.cursor()
sql_arrow='select start_time from aibinghaus_use'
cur1.execute(sql_arrow)

def  give_timearray(datetime_my):
    tss1 = datetime_my
      # 转为时间数组
    timeArray = time.strptime(tss1, "%Y-%m-%d %H:%M:%S")
    timeStamp = int(time.mktime(timeArray))
    # print ('时间戳是：'+str(timeStamp))
    return timeStamp
a=[]
for i in cur1:
    # print(i[0])
    my_time=give_timearray(i[0])
    print(type(my_time))
    sql_arrow = "update aibinghaus_use set time_wait='%s' where start_time='%s'"%(str(my_time),i[0])
    # print(sql_arrow)
    a.append(sql_arrow)
for i in a:
    print(i)
    cur1.execute(i)
    conn.commit()


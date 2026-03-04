from ctypes import alignment
import tkinter as tk
from tkinter import *
from tkinter import messagebox as mb
from tkinter.tix import COLUMN
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import csv
import datetime  
import time
import subprocess


def dawei():
    myurl = url.get()
    mytid = tid.get()
    mb.showinfo(title="Message", message=myurl + "\n" + mytid)
    print("URL =", myurl, ", Table filter =", mytid)
    
    driver = webdriver.Chrome()
    driver.get(myurl)
    driver.implicitly_wait(30)
    time.sleep(5)
 
    with open('dawei.csv', 'w', newline='') as f:
        mytid = "//*[@id='ContentPlaceHolder1_ContentPlaceHolder1_GridView1']"  
        myrow = driver.find_elements(By.XPATH, mytid + "/tbody/tr")
        mycol = driver.find_elements(By.XPATH, mytid + "/tbody/tr/th")
        writer = csv.writer(f)
        myheads = [cell.text for cell in mycol]
        writer.writerow(myheads)
        
        while True:
            for row in range(2, len(myrow) + 1):
                myrecord = []
                for col in range(1, len(mycol)):
                    cell = driver.find_element(By.XPATH, mytid + "/tbody/tr[" + str(row) + "]/td[" + str(col) + "]")
                    myrecord.append(cell.text)
                writer.writerow(myrecord)
                print("Row:", myrecord[0], "... written.")
            
            thispage = 0
            try:
                mylink = driver.find_element(By.LINK_TEXT, str(thispage))
                mylink.click()
                driver.implicitly_wait(30)
                time.sleep(5)
                myrow = driver.find_elements(By.XPATH, mytid + "/tbody/tr")
            except Exception as e:
                print(str(e))
                break


first = Tk()
first.title("dawei")
first.geometry('700x500')

custom_font = ("TkDefaultFont", 20)
label_url = tk.Label(first, text="URL:")
label_filter = tk.Label(first, text="Table filter:")


label_url.config(font=custom_font)
label_filter.config(font=custom_font)


label_url.grid(row=0)
label_filter.grid(row=1)


url = Entry(first, width=60)
tid = Entry(first, width=60)



url.insert(0, "https://ap.usc.edu.tw/STU1/STU1/SC0103.aspx")
tid.insert(0, "id='ContentPlaceHolder1_ContentPlaceHolder1_GridView1'")


url.grid(row=0, column=1)
tid.grid(row=1, column=1)


btn = Button(first, text='Click me!', command = dawei)
btn.grid(row=3, column=0, columnspan=2)

custom_font = ("TkDefaultFont", 20)
btn =Button(first, text= 'Open excel', command = dawei)
btn.grid(row=4,column=0,columnspan=2)

first.mainloop()

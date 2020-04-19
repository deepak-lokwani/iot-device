'''
Created on 04-Apr-2020

@author: deepa
'''
from labs.common import ConfigUtil
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

class SMTPClientConnector(object):
    
    def __init__(self):
        
        '''
        Constructor
        '''
        self.configUtil =   ConfigUtil.ConfigUtil()
        self.configUtil.loadConfig()
        
    def publishMessage(self, topic, data):
        '''
        defining a method to push email with sensor data as the text body
        '''
        #gets the host, port, fromAddr, toAddr, authToken from the config file
        host    =   self.configUtil.getProperty(self.configUtil.configConst.SMTP_CLOUD_SECTION, self.configUtil.configConst.HOST_KEY)
        port    =   self.configUtil.getProperty(self.configUtil.configConst.SMTP_CLOUD_SECTION, self.configUtil.configConst.PORT_KEY)
        fromAddr=   self.configUtil.getProperty(self.configUtil.configConst.SMTP_CLOUD_SECTION, self.configUtil.configConst.FROM_ADDRESS_KEY)
        toAddr  =   self.configUtil.getProperty(self.configUtil.configConst.SMTP_CLOUD_SECTION, self.configUtil.configConst.TO_ADDRESS_KEY)
        authToken=  self.configUtil.getProperty(self.configUtil.configConst.SMTP_CLOUD_SECTION, self.configUtil.configConst.USER_AUTH_TOKEN_KEY)
        
        
        msg             =   MIMEMultipart()     #Creating the email attributes
        msg['From']     =   fromAddr            #sender's email ID
        msg['To']       =   toAddr              #Recepient's email ID
        msg['Subject']  =   topic               #subject of the email
        msgBody         =   str(data)           #message body of the email
        msg.attach(MIMEText(msgBody))           #bringing everything together
        msgText         =   msg.as_string()
        
        #email procedure through ehlo for SMTP
        smtpServer      =   smtplib.SMTP_SSL(host, port)        
        smtpServer.ehlo()
        smtpServer.login(fromAddr, authToken)
        smtpServer.sendmail(fromAddr, toAddr, msgText)
        smtpServer.close()
        
        return True
        #closing the SMTP Connection
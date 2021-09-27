#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  2 21:14:51 2020

@author: elliott
"""

# from PyPDF2 import PdfFileReader

# def sfEMSProtocols():# to organize protocols into text files for Socrates
#     path = 'EMS_ProtocolManual_020320.pdf'
#     protocol = "1.1" 
#     with open(path, 'rb') as f:
#         pdf = PdfFileReader(f)
#         for i in range(5,pdf.getNumPages()):
# #            I'm skipping the first 5 pages as they are a
# #            glossary and updates to the last manual
#             page = pdf.getPage(i) 
#             text = page.extractText()
#             pNum = text[0:6]
#             print('just indexed', pNum)
#             if protocol in pNum:
#                 f = open(pNum+".txt", "a")
#                 f.write(text)
#                 f.close()
#             else:
#                 protocol = pNum
#                 f = open(pNum+".txt", "a")
#                 f.write(text)
#                 f.close()
                
            
"""
Простой скрипт парсинга с фортата flask-wiki на git-book
"""

import os
import codecs
posts=os.listdir('posts')

for i in  posts:
     page=codecs.open('posts/%s' %i, "r", "utf_8_sig")
     strings=[]
     strings = page.readlines()
     page.close()
     if "title:" in strings[0]:
         b=str(strings[0])
         b = b[7:-1]
         file = codecs.open('SUMMARY.md', 'a', "utf_8_sig")
         c ='* [%s](/posts/%s)\n' %(b, i)
         file.write('* [%s](/posts/%s)\n' %(b, i))
         print(c)
         del strings[0:3]
         page=codecs.open('posts/%s' %i, "w", "utf_8_sig")
         string='\n'.join(strings)
         page.write(string)
         page.close()

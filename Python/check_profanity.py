import urllib

def read_text():
    link = open('/Users/jinzegu/Desktop/sample_text.txt')
    content = link.read()
    link.close()
    profanity_check(content)
   
    

def profanity_check(text):
    connection = urllib.urlopen('http://www.wdylike.appspot.com/?q='+text)
    result = connection.read()
    connection.close()
    if 'true' in result:
        print('Profanity alert, please double check your e-mail')
    elif 'false' in result:
        print('You are fine to send the e-mail')
    else:
        print('Could not scan the text information')
        

read_text()
    

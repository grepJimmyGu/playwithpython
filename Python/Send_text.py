from twilio.rest import TwilioRestClient

# Your Account SID from twilio.com/console
account_sid = "AC0271aaa1b03ec52fa589645848894ceb"
# Your Auth Token from twilio.com/console
auth_token  = "6fac79463d35f26bc2075c0d3deeaa38"

client = TwilioRestClient(account_sid, auth_token)

stored_text = ('There are setbacks and mistakes in your life...',
               'but no one achieves his/her goal with one attempt, and sometime it takes a dramatic amount of efforts..',
               'what distinguishes common man and leaders is the determination and persistance',
               'JINZE, you are great, just keep doing what you are doing, you will become who you want to be.',
               'https://www.youtube.com/watch?v=SevHZgBnfF0')

i = 0
while i <= 4:
    message = client.messages.create(
    to="+14156942769", 
    from_="+14159695123", # Twilio number
    body= stored_text[i])
    i = i+1

print(message.sid)

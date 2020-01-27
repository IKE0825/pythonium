import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate
import pdb

pdb.set_trace()

account = "itoken0825@gmail.com"
password = "potenz@0825"

to_email = "itoken0825@gmail.com"
from_email = "itoken0825@gmail.com"

subject = "解析結果"
message = "テストメール"
msg = MIMEText(message,"html")
msg["Subject"] = subject
msg["To"] = to_email
msg["From"] = from_email

server = smtplib.SMTP('smtp.gmail.com', 587)
#smtpobj.set_debuglevel(True)
server.starttls()
server.login(account,password)
server.send_message(msg)
server.quit()
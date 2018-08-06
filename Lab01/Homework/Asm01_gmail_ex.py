from gmail import GMail, Message

from datetime import datetime
hour_now = datetime.today().hour
time_period = 7
html_content ="""
<p>Dear Mrs. Stark,</p>
<p>I&rsquo;m emailing to inform you that I can&rsquo;t make it to work today,&nbsp;as I&rsquo;ve come down with a fever.</p>
<p>I'll be available to answer emails if you need urgent help, but Pete&nbsp;Park will handle my workload today to ensure all deadlines are met.</p>
<p>Thank you for understanding,</p>
"""

gmail = GMail("Minh<minhnt13@gmail.com>","someknownow")
msg = Message(
    "Minh - Absent From Work",
    to="imrichaf@gmail.com",
    html=html_content)

if hour_now > time_period:
    gmail.send(msg)

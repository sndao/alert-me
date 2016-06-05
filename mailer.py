import smtplib

GMAIL_SMTP = 'smtp.gmail.com'
WF_SMTP = 'smtp.webfaction.com:587'

SMTP_SERVER = WF_SMTP

class mailer:
    def __init__(self):

    def sendemail(self, from_addr, to_addr_list, cc_addr_list,
                  subject, message,
                  login, password,
                  smtpserver=SMTP_SERVER):
        header  = 'From: %s\n' % from_addr
        header += 'To: %s\n' % ','.join(to_addr_list)
        header += 'Cc: %s\n' % ','.join(cc_addr_list)
        header += 'Subject: %s\n\n' % subject
        message = header + message

        server = smtplib.SMTP(smtpserver)
        server.starttls()
        server.login(login,password)
        problems = server.sendmail(from_addr, to_addr_list, message)
        server.quit()

    def compose(self, subj, message, to_list):
        self.sendemail(from_addr    = self.from_address,
                              to_addr_list = to_list,
                              cc_addr_list = to_list,
                              subject      = subj,
                              message      = message,
                              login        = self.login,
                              password     = self.password)

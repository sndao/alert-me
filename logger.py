import environment
import timekeeper
import os

class logger:
    def __init__(self, env, module):
        self.env = env
        self.module = module
        self.tk = None

    def log(self, tk):
        self.tk = tk
        if int(tk.minute) < 10:
            tk.minute = '0' + str(tk.minute)
        self.tk.timing = str(self.tk.timing)[:6]

        file = open(self.env.logdir + self.module + '_log.html', 'a')
        log_str = str(self.tk.hour) + ':' + str(self.tk.minute) + "&#160;&#160;&#160;&#160;&#160;" + str(self.tk.timing) + "&#160;&#160;&#160;&#160;&#160;" + str(self.tk.now) + ' ' + self.module + '<br>\n'
        file.write(log_str)
        file.close()
        file = open(self.env.logdir + 'all_log.html', 'a')
        log_str = str(self.tk.hour) + ':' + str(self.tk.minute) + "&#160;&#160;&#160;&#160;&#160;" + str(self.tk.timing) + "&#160;&#160;&#160;&#160;&#160;" + str(self.tk.now) + ' ' + self.module + '<br>\n'
        file.write(log_str)
        file.close()

    def deletelog(self):
        pass
        #delete = raw_input("deltee")
        #os.remove(self.env.logdir + self.module + '_log.html')


import sys
import os
import random
import win32con, time, random, win32api

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import *
 

class Get_Password():
    """
    num_of_symbols = int, char_v = bool int_v = bool, uchar_v = bool,
    winfsuss_v = bool, winfsss_v = bool
    num_of_sympols define count of symbols in password; 
    char_v allow to include letters into password; 
    int_v allow to include numbers into password; 
    uchar_v allow to include upper letters into password;
    winfsuss allow to include windows filesystem unsupported symbols;
    winfsss allow to include windows filesystem supported symbols;
    """
    
    def __init__(self, num_of_symbols, char_v, int_v, uchar_v, winfsuss_v, winfsss_v):

        self.num_of_symbols = num_of_symbols 
        self.char_v = char_v 
        self.int_v = int_v 
        self.uchar_v = uchar_v 
        self.winfsuss_v = winfsuss_v 
        self.winfsss_v = winfsss_v
        self.chosen_parameter = None
        self.available_parameter = []
        self.outputstring = ""

    
    def pw_gen(self):
        
        char_list = [
            'q','w','e','r','t',
            'y','u','i','o','p',
            'a','s','d','f','g',
            'h','j','k','l','z',
            'x','c','v','b','n',
            'm'
            ]
        int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
        winfsuss_list = ["/",":",">","<","'","|","*","?"]
        winfsss_list = [
            ",",".",";","&","^",
            "!","@","#","$","%",
            "+","=","-","_","}",
            "{","~","`","[","]",
            "(",")"
            ]

        Get_Password.add_available_parameter_to_list(self)
        if self.available_parameter != []:

            for i in range(self.num_of_symbols):
            
                self.chosen_parameter = random.choice(self.available_parameter)

                if (self.char_v == True) and (self.chosen_parameter == 0):
                    self.outputstring += random.choice(char_list)

                elif (self.int_v == True) and (self.chosen_parameter == 1):
                    self.outputstring += str(random.choice(int_list))


                elif (self.uchar_v == True) and (self.chosen_parameter == 2):
                    chosen_letter =  random.choice(char_list)
                    self.outputstring += str(chosen_letter).upper()

                elif (self.winfsuss_v == True) and (self.chosen_parameter == 3):
                    self.outputstring += random.choice(winfsuss_list)


                elif (self.winfsss_v == True) and (self.chosen_parameter == 4):
                    self.outputstring += random.choice(winfsss_list)
        
            return self.outputstring

    
    
    def add_available_parameter_to_list(self):
        if self.char_v:
            self.available_parameter.append(0)
        if self.int_v:
            self.available_parameter.append(1)
        if self.uchar_v:
            self.available_parameter.append(2)
        if self.winfsuss_v:
            self.available_parameter.append(3)
        if self.winfsss_v:
            self.available_parameter.append(4)
        if self.available_parameter.count == 0:
            __name__ = '__main__'
        return self.available_parameter


class Work_sim():
    """Simulates hard work"""


    def __init__(self, defenition = (win32api.GetSystemMetrics(0), win32api.GetSystemMetrics(1)), delay = 5, destinations = []):
        self.defenitionx = defenition[0]
        self.defenitiony = defenition[1]
        self.delay = delay
        self.cursorposx = (win32api.GetCursorPos()[0])
        self.cursorposy = (win32api.GetCursorPos()[1])
        self.destinations = destinations
        self.it = 1
        self.run = True

    
    def move_mouse(self):
        
        
        for destination in self.destinations:

            while self.cursorposx % 10 != 0:
                self.cursorposx += 1
                print(self.cursorposx)
            while self.cursorposy % 10 != 0:
                self.cursorposy += 1
                print(self.cursorposy)
                win32api.SetCursorPos((self.cursorposx, self.cursorposy))
            

            while (self.cursorposx, self.cursorposy) != destination:
            
                self.it += 1
            
                if self.cursorposx < destination[0]:
                    self.cursorposx += 10
                elif self.cursorposy < destination[1]:
                    self.cursorposy += 10
                elif self.cursorposx > destination[0]:
                    self.cursorposx -= 10
                elif self.cursorposy > destination[1]:
                    self.cursorposy -= 10

                win32api.SetCursorPos((self.cursorposx, self.cursorposy))
                time.sleep(0.01)
                print((win32api.GetCursorPos()))
            

                if self.it % random.randint(20, 100) == 0:
                    time.sleep(float(f"0.{random.randint(4, 6)}"))
            
                if (self.cursorposx, self.cursorposy) >= (self.defenitionx, self.defenitiony):
                    break
                elif (self.cursorposx, self.cursorposy) < (0, 0):
                    break
            
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, self.cursorposx, self.cursorposy, 0, 0)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, self.cursorposx, self.cursorposy, 0, 0)
            time.sleep(int(random.randint(1, 20)))
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, self.cursorposx, self.cursorposy, 0, 0)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, self.cursorposx, self.cursorposy, 0, 0)


        """a"""
    def keyboard_input(self):
        win32api.keyboard_event(win32con.q)

    def program_stop(self):
        self.run = False

    
    def main(self):
        sttime = time.time()
        time.sleep(self.delay)
        while self.run:
            self.move_mouse()
            entime = time.time()
            print("runing for",entime - sttime,"seconds")


class PC_action_manager(QWidget):

    
    def __init__(self):
        super().__init__()

        self.initGUI()

        
    def initGUI(self):
        self.delay = 0
        self.pw_symbols_count = 0


        self.sd_label = QLabel("To shutdown device press button -->", self)
        self.sd_label.move(15, 10)

        self.sdr_label = QLabel("To restart device press button -->", self)
        self.sdr_label.move(15, 40)

        self.sda_label = QLabel("To cancel device shutdown press button -->", self)
        self.sda_label.setStyleSheet("color: rgb(232,0,0)")
        self.sda_label.move(15, 80)

        self.d_label = QLabel("To set delay in seconds -->", self)
        self.d_label.move(355, 10)

        self.pwsc_label = QLabel("Include letters", self)
        self.pwsc_label.move(15, 180)

        self.pwsi_label = QLabel("Include numbers", self)
        self.pwsi_label.move(15, 200)

        self.pwsuc_label = QLabel("Include upper case letters", self)
        self.pwsuc_label.move(15, 220)

        self.pwsss_label = QLabel("Include Windows filesystem\nunsuported symbols", self)
        self.pwsss_label.move(15, 240)

        self.pwsns_label = QLabel("Include Windows filesystem\nsuported symbols", self)
        self.pwsns_label.move(15, 280)

        self.pwc_label = QLabel("Set count of symbols", self)
        self.pwc_label.move(15, 318)

        self.apwc_label = QLabel("Admin password:", self)
        self.apwc_label.move(550, 50)

        self.gdtof_label = QLabel("Chosen directory:", self)
        self.gdtof_label.move(550, 160)

        self.sw_label = QLabel("Work simulation destinations", self)
        self.sw_label.move(355, 40)

        self.pw_char_in_tum = QCheckBox(self)
        self.pw_char_in_tum.move(160, 182)
        self.pw_char_in_tum.setCheckable(True)
        self.pw_char_in_tum.setChecked(True)

        self.pw_int_in_tum = QCheckBox(self)
        self.pw_int_in_tum.move(160, 202)
        self.pw_int_in_tum.setCheckable(True)
        self.pw_int_in_tum.setChecked(True)

        self.pw_uchar_in_tum = QCheckBox(self)
        self.pw_uchar_in_tum.move(160, 222)
        self.pw_uchar_in_tum.setCheckable(True)
        self.pw_uchar_in_tum.setChecked(True)

        self.pw_winfsuss_in_tum = QCheckBox(self)
        self.pw_winfsuss_in_tum.move(160, 258)
        self.pw_winfsuss_in_tum.setCheckable(True)
        self.pw_winfsuss_in_tum.setChecked(True)

        self.pw_winfsss_in_tum = QCheckBox(self)
        self.pw_winfsss_in_tum.move(160, 298)
        self.pw_winfsss_in_tum.setCheckable(True)
        self.pw_winfsss_in_tum.setChecked(True)

        self.sd_button = QPushButton("Shutdown", self)
        self.sd_button.resize(100, 20)
        self.sd_button.move(250, 10)
        self.sd_button.setCheckable(True)
        self.sd_button.clicked.connect(self.shutdown)

        self.sdr_button = QPushButton("Restart", self)
        self.sdr_button.resize(100, 20)
        self.sdr_button.move(250, 40)
        self.sdr_button.setCheckable(True)
        self.sdr_button.clicked.connect(self.restart)

        self.sda_button = QPushButton("Cancel", self)
        self.sda_button.resize(100, 100)
        self.sda_button.move(250, 70)
        self.sda_button.setStyleSheet(
            "background: rgb(232,0,0);"
            "font: bold 20px;"
            "border-style: outset;"
            "border-radius: 50px;"
            "padding: 6px;"
        )
        self.sda_button.setCheckable(True)
        self.sda_button.clicked.connect(self.cancel_shutdown)

        self.pwc_button = QPushButton("Create password", self)
        self.pwc_button.resize(100, 30)
        self.pwc_button.move(170, 315)
        self.pwc_button.setCheckable(True)
        self.pwc_button.clicked.connect(self.generate_password)

        self.cpc_button = QPushButton("Call command prompt", self)
        self.cpc_button.resize(135, 40)
        self.cpc_button.move(0, 355)
        self.cpc_button.setCheckable(True)
        self.cpc_button.clicked.connect(self.command_prompt_call)

        self.cp_button = QPushButton("Call powershell", self)
        self.cp_button.resize(135, 40)
        self.cp_button.move(140, 355)
        self.cp_button.setCheckable(True)
        self.cp_button.clicked.connect(self.call_powershell)

        self.clp_button = QPushButton("Call local politics", self)
        self.clp_button.resize(135, 40)
        self.clp_button.move(420, 355)
        self.clp_button.setCheckable(True)
        self.clp_button.clicked.connect(self.call_local_politics)

        self.cre_button = QPushButton("Call register editor", self)
        self.cre_button.resize(135, 40)
        self.cre_button.move(280, 355)
        self.cre_button.setCheckable(True)
        self.cre_button.clicked.connect(self.call_register_editor)

        self.cs_button = QPushButton("Call services", self)
        self.cs_button.resize(135, 40)
        self.cs_button.move(560, 355)
        self.cs_button.setCheckable(True)
        self.cs_button.clicked.connect(self.call_servises)

        self.sapwc_button = QPushButton("Save password", self)
        self.sapwc_button.resize(100, 25)
        self.sapwc_button.move(550, 120)
        self.sapwc_button.setCheckable(True)
        self.sapwc_button.clicked.connect(self.save_password)

        self.gdtof_button = QPushButton("Open directory", self)
        self.gdtof_button.resize(100, 25)
        self.gdtof_button.move(550, 325)
        self.gdtof_button.setCheckable(True)
        self.gdtof_button.clicked.connect(self.getdirectory)

        self.idf_button = QPushButton("Execute files", self)
        self.idf_button.resize(100, 25)
        self.idf_button.move(655, 325)
        self.idf_button.setCheckable(True)
        self.idf_button.clicked.connect(self.executeall)

        self.cws_button = QPushButton("Start", self)
        self.cws_button.resize(100, 25)
        self.cws_button.move(380, 325)
        self.cws_button.setCheckable(True)
        self.cws_button.clicked.connect(self.destinations_apply)

        self.sdd_spinbox = QSpinBox(self)
        self.sdd_spinbox.setValue(10)
        self.sdd_spinbox.setMaximum(99999)
        self.sdd_spinbox.resize(60,20)
        self.sdd_spinbox.move(500,10)
        self.sdd_spinbox.textChanged.connect(self.delay_change)

        self.pwc_spinbox = QSpinBox(self)
        self.pwc_spinbox.move(130,315)
        self.pwc_spinbox.textChanged.connect(self.count_of_symbols_in_pw_change)

        self.pwchar_rtextbox = QTextBrowser(self)
        self.pwchar_rtextbox.move(15, 120)
        self.pwchar_rtextbox.setText("")
        self.pwchar_rtextbox.resize(230, 55)

        self.gdtof_rtextbox = QTextBrowser(self)
        self.gdtof_rtextbox.move(550, 180)
        self.gdtof_rtextbox.setText("")
        self.gdtof_rtextbox.resize(200, 140)

        self.apwchar_textbox = QTextEdit(self)
        self.apwchar_textbox.move(550, 70)
        self.apwchar_textbox.setText("")
        self.apwchar_textbox.resize(200, 45)
        self.apwchar_textbox.textChanged.connect(self.admin_password_change)

        self.chdes_textbox = QTextEdit(self)
        self.chdes_textbox.move(380, 55)
        self.chdes_textbox.setText("")
        self.chdes_textbox.resize(100, 180)
        self.chdes_textbox.textChanged.connect(self.destinations_change)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Pam - assistaint')
        self.setFixedSize(QSize(800, 400))
        self.setStyleSheet("background: rgb(128, 128, 128)")
        
        self.show()


    
    def delay_change(self):
        self.delay = self.sdd_spinbox.value()

    
    def count_of_symbols_in_pw_change(self):
        self.pw_symbols_count = self.pwc_spinbox.value()
    
    
    def admin_password_change(self):
        self.admin_password = self.apwchar_textbox.toPlainText()
        print(self.admin_password)

    
    def shutdown(self):
        if self.sd_button.isChecked():
            self.sd_button.setChecked(False)
            os.system(f'mshta.exe vbscript:Execute("msgbox""Shutdown in {self.delay} seconds"",48,""Session shutting down"":close")')
            os.system(f"shutdown /s /t {self.delay}")

    
    def restart(self):
        if self.sdr_button.isChecked():
            self.sdr_button.setChecked(False)
            os.system(f'mshta.exe vbscript:Execute("msgbox""Sysrem restart in {self.delay} seconds"",48,""Session shutting down"":close")')
            os.system(f"shutdown /r /t {self.delay}")

    
    def cancel_shutdown(self):
        if self.sda_button.isChecked():
            self.sda_button.setChecked(False)
            os.system('mshta.exe vbscript:Execute("msgbox""Shutdown was canceled"",262192,""Session shutting down"":close")')
            os.system("shutdown /a")

    
    def command_prompt_call(self):
        if self.cpc_button.isChecked():
            self.cpc_button.setChecked(False)
            os.system("START cmd.exe")

    
    def call_powershell(self):
        if self.cp_button.isChecked():
            self.cp_button.setChecked(False)
            user = win32api.GetUserName()
            os.system(f"START powershell.exe")
            

    
    def call_local_politics(self):
        if self.clp_button.isChecked():
            self.clp_button.setChecked(False)
            os.system('FOR %F IN ("%SystemRoot%\servicing\Packages\Microsoft-Windows-GroupPolicy-ClientTools-Package~*.mum") DO (DISM /Online /NoRestart /Add-Package:"%F")')
            os.system('FOR %F IN ("%SystemRoot%\servicing\Packages\Microsoft-Windows-GroupPolicy-ClientExtensions-Package~*.mum") DO (DISM /Online /NoRestart /Add-Package:"%F")')
            os.system("START secpol")
            os.system("START gpedit")

    
    def call_register_editor(self):
        if self.cre_button.isChecked():
            self.cre_button.setChecked(False)
            os.system("START regedit")

    
    def call_servises(self):
        if self.cs_button.isChecked():
            self.cs_button.setChecked(False)
            os.system("START services.msc")

    
    def generate_password(self):
        if self.pwc_button.isChecked():
            self.pwc_button.setChecked(False)
            
            password_subclass_example = Get_Password(
                self.pw_symbols_count, 
                self.pw_char_in_tum.isChecked(),
                self.pw_int_in_tum.isChecked(),
                self.pw_uchar_in_tum.isChecked(),
                self.pw_winfsuss_in_tum.isChecked(),
                self.pw_winfsss_in_tum.isChecked())
            
            password = Get_Password.pw_gen(password_subclass_example)
            self.pwchar_rtextbox.setText(password)
    
    
    def save_password(self):
        if self.sapwc_button.isChecked():
            self.sapwc_button.setChecked(False)
            with open("admin_password/password.txt", "r+") as pwtxtfile:
                pwtxtfile.write(self.admin_password)

    
    def getdirectory(self):
        if self.gdtof_button.isChecked():
            self.gdtof_button.setChecked(False)
            self.dirpath = QFileDialog.getExistingDirectory(self,"Choose directory",".")
            self.dirpath = self.dirpath
            self.gdtof_rtextbox.setText(self.dirpath)

    
    def executeall(self):
        if self.idf_button.isChecked():
            self.idf_button.setChecked(False)
            os.system(f"FOR /R {self.dirpath} %F IN (/*) DO START %F")

    
    def destinations_change(self):
        self.destination_list = [(0, 0)]
        raw_destination_values = self.chdes_textbox.toPlainText()
        firsttuplemember = ""
        tuplememberlist = []
        i = 0

        for symbol in raw_destination_values:
            if ((symbol == ",") or (symbol == " ")):
                try:
                    firsttuplemember = int(firsttuplemember)
                    while firsttuplemember % 10 != 0:
                        firsttuplemember += 1
                    tuplememberlist.append(int(firsttuplemember))
                except ValueError:
                    pass
                firsttuplemember = ""
            else:
                try:
                    int(symbol)
                    firsttuplemember += symbol
                except ValueError:
                    pass
        
        for member in tuplememberlist:
            
            if len(self.destination_list) % 2 != 0:
                pass
            try:
                if i % 2 == 0:
                    self.destination_list.append((tuplememberlist[i], tuplememberlist[i+1]))
                    print(self.destination_list)
                else:
                    pass
            except IndexError:
                break
            i += 1
    
    
    def destinations_apply(self):
        if self.cws_button.isChecked():
            self.cws_button.setChecked(False)
            destination_list = self.destination_list
            start = Work_sim(destinations = destination_list)
            start.main()

            
            

if __name__ == '__main__':

    app = QApplication(sys.argv)
    Pam = PC_action_manager()
    sys.exit(app.exec())



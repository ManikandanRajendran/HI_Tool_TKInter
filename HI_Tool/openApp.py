import traceback
from tkinter import *
import clipboard
import webbrowser
import platform
from PIL import Image, ImageTk
import firstPage, commonFunction, run_page

# from lettuce.terrain import after

window = Tk()
window.geometry("600x900")
window.title("Home Insurance")
window.configure(background='honeydew3')
chrome_path = ''
postcode1 = StringVar()
quotePage_Url = ''
text = ''
path = "/home/manikandan/Documents/HI_Tool/chrome.png"
image = Image.open(path)
img = image.resize((30, 30), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)
result = Entry
copy_link1 = Button
linkLabel = Label


# this function is just for reference
def loadEntry(value, col, align):
    global result
    result.delete(0, END)
    result.config(bg="honeydew3", fg=col, justify=align)
    result.insert(END, value)
    result.place(x=150, y=500, width=300, height=150)


def loadingLable(value, col):
    Label(window, text=value, fg="black", bg=col, justify=CENTER, wraplength=200).place(x=150, y=550, width=300,
                                                                                        height=150)


def loadingCopyLink():
    global copy_link1
    copy_link1 = Button(window, text="copy", fg="white", bg="green", width=8, font=("arial", 7, "bold"))


def loadBrowser(value):
    global linkLabel
    linkLabel = Label(window, image=img, bg="honeydew3")
    linkLabel.bind('<Button-1>', value)
    linkLabel.place(x=520, y=640)


def define_os():
    global chrome_path
    osDetails = platform.system()
    if osDetails == 'Windows':
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    elif osDetails == 'Linux':
        chrome_path = '/usr/bin/google-chrome %s'
    elif osDetails == 'Darvin':
        chrome_path = 'open -a /Applications/Google\ Chrome.app %s'


def open_browser(event=None):
    define_os()
    webbrowser.get(chrome_path).open(quotePage_Url)


def open_retrieveQuote(event=None):
    define_os()
    webbrowser.get(chrome_path).open(
        "https://www2.bgo.bgdigitaltest.co.uk/home-services/insurance/home-insurance/retrieve-quote?branch=57d5091ed079e185b57361b7026b446c95b3f97b")


def open_retrieveDoc(event=None):
    define_os()
    webbrowser.get(chrome_path).open(
        "https://www2.bgo.bgdigitaltest.co.uk/home-services/insurance/home-insurance/your-portal?branch=57d5091ed079e185b57361b7026b446c95b3f97b")


def copy_quoteUrl():
    clipboard.copy(quotePage_Url)


def readValue(value):
    # global postcode1
    string = value.get()
    return string


def quoteDetails():
    global result, copy_link1, linkLabel, text
    promocode = readValue(promoCodeField)
    commonFunction.applyPromo(promocode)
    commonFunction.check_accidentalDamage_b(var1)
    commonFunction.check_accidentalDamage_c(var2)
    commonFunction.check_opex(var3, var4, var5)
    commonFunction.check_coverDetails(var6, var7, var8)
    pc = readValue(postcode1)
    env = var9.get()
    results = firstPage.getQuoteDetails(pc, env)
    if 'error' in results:
        loadingLable("Sorry !!! we are unable to help you this time :( \n due to the error :  " + results, "red")
    elif 'failed' in results:
        loadingLable("Sorry !!! we are unable to help you this time :( \n due to the error :  " + results, "red")
    else:
        text = run_page.get_details()
        loadingLable(text, "honeydew3")
        loadingCopyLink()
        copy_link1.config(command=clipboard.copy(text))
        copy_link1.place(x=500, y=600)
        loadBrowser(open_retrieveQuote)


def quotePageLink():
    global quotePage_Url, img, result, copy_link1, linkLabel
    promocode = readValue(promoCodeField)
    commonFunction.applyPromo(promocode)
    commonFunction.check_accidentalDamage_b(var1)
    commonFunction.check_accidentalDamage_c(var2)
    commonFunction.check_opex(var3, var4, var5)
    commonFunction.check_coverDetails(var6, var7, var8)
    pc = readValue(postcode1)
    env = var9.get()
    quotePage_Url = firstPage.getQuoteLink(pc, env)
    if 'error' in quotePage_Url:
        loadingLable("Sorry !!! we are unable to help you this time :( \n due to the error :  " + quotePage_Url, "red")
    elif 'failed' in quotePage_Url:
        loadingLable("Sorry !!! we are unable to help you this time :( \n due to the error :  " + quotePage_Url, "red")
    else:
        loadingLable(quotePage_Url, "honeydew3")
        loadingCopyLink()
        copy_link1.config(command=copy_quoteUrl)
        copy_link1.place(x=500, y=600)
        loadBrowser(open_browser)


def retDocDetails():
    global img, result, copy_link1, linkLabel
    promocode = readValue(promoCodeField)
    commonFunction.applyPromo(promocode)
    commonFunction.check_accidentalDamage_b(var1)
    commonFunction.check_accidentalDamage_c(var2)
    commonFunction.check_opex(var3, var4, var5)
    commonFunction.check_coverDetails(var6, var7, var8)
    pc = readValue(postcode1)
    env = var9.get()
    marketing = firstPage.getDetailsforRetDocs(pc, env)
    if 'error' in marketing:
        loadingLable("Sorry !!! we are unable to help you this time :( \n due to the error :  " + marketing, "red")
    elif 'failed' in marketing:
        loadingLable("Sorry !!! we are unable to help you this time :( \n due to the error :  " + marketing, "red")
    else:
        loadingLable(marketing, "honeydew3")
        loadingCopyLink()
        copy_link1.config(command=clipboard.copy(marketing))
        copy_link1.place(x=500, y=600)
        loadBrowser(open_retrieveDoc)


def exit1():
    exit()


def clear1():
    # countdown1(self)
    postcode1.delete(0, 'end')
    promoCodeField.delete(0, 'end')
    loadingLable("Your result will be displayed here...", "honeydew3")
    checkButBuildingCover.deselect()
    checkButContentCover.deselect()
    checkButHas.deselect()
    checkButKey.deselect()
    checkButLec.deselect()
    checkButBuilding.deselect()
    checkButContent.deselect()
    checkButBoth.deselect()
    try:
        copy_link1.destroy()
        linkLabel.destroy()
    except SystemExit as msg:
        raise SystemExit(msg)
    except:
        traceback.print_exc(file=open('test.log', 'a'))


title = Label(window, text="Test data generator", fg="navy", bg="honeydew3", font=("arial", 16, "bold")).place(x=160,
                                                                                                               y=20)
lblPostcode = Label(window, text='Enter the postcode : ', fg="RoyalBlue4", bg="honeydew3",
                    font=("arial", 11, "bold")).place(x=10, y=80)
lblPromoCode = Label(window, text='Enter Promo code : ', fg="RoyalBlue4", bg="honeydew3",
                     font=("arial", 11, "bold")).place(x=10, y=320)

postcode1 = Entry(window)
postcode1.focus_set()
postcode1.place(x=200, y=80)

promoCodeField = Entry(window)
promoCodeField.place(x=200, y=320)

title1 = Label(window, text="Not mandatory", fg="Red", bg="honeydew3", font=("arial", 7, "bold")).place(x=380, y=90)

# check boxes of Building and contents cover
lblAccidentalDamage = Label(window, text='Accidental damage cover :', fg="RoyalBlue4", bg="honeydew3",
                            font=("arial", 11, "bold")).place(x=10, y=200)
var1 = IntVar()
checkButBuildingCover = Checkbutton(window, text="Building-AD", variable=var1, bg="honeydew3")
checkButBuildingCover.place(x=200, y=200)
var2 = IntVar()
checkButContentCover = Checkbutton(window, text="Content-AD", variable=var2, bg="honeydew3")
checkButContentCover.place(x=350, y=200)

# check boxes of optional extras
lblOpex = Label(window, text='Optional extras cover :', fg="RoyalBlue4", bg="honeydew3",
                font=("arial", 11, "bold")).place(x=10, y=260)
var3 = IntVar()
checkButHas = Checkbutton(window, text="HAS", variable=var3, bg="honeydew3")
checkButHas.place(x=200, y=260)
var4 = IntVar()
checkButLec = Checkbutton(window, text="LEC", variable=var4, bg="honeydew3")
checkButLec.place(x=300, y=260)
var5 = IntVar()
checkButKey = Checkbutton(window, text="Key", variable=var5, bg="honeydew3")
checkButKey.place(x=400, y=260)

# check boxes of cover details
lblCoverDetails = Label(window, text='Select the cover :', fg="RoyalBlue4", bg="honeydew3",
                        font=("arial", 11, "bold")).place(x=10, y=140)
var6 = IntVar()
checkButBuilding = Checkbutton(window, text="Building", variable=var6, bg="honeydew3")
checkButBuilding.place(x=200, y=140)
var7 = IntVar()
checkButContent = Checkbutton(window, text="Content", variable=var7, bg="honeydew3")
checkButContent.place(x=300, y=140)
var8 = IntVar()
checkButBoth = Checkbutton(window, text="Both", variable=var8, bg="honeydew3")
checkButBoth.place(x=400, y=140)

# Select environment
title1 = Label(window, text="Select Environment : ", fg="RoyalBlue4", bg="honeydew3", font=("arial", 11, "bold")).place(
    x=10, y=380)
var9 = StringVar()
var9.set("QA1")
environments = ["Stage", "QA1"]
selectEnv = OptionMenu(window, var9, *environments)
selectEnv.place(x=200, y=380)

# Buttons to trigger the journeys
title1 = Label(window, text="Data you need for : ", fg="RoyalBlue4", bg="honeydew3", font=("arial", 11, "bold")).place(
    x=10, y=440)
gaq = Button(window, text="Retrieve A Quote", fg="black", bg="honeydew3", width=18, command=quoteDetails)
gaq.place(x=10, y=480)
gaq = Button(window, text="Retrieve Documents", fg="black", bg="honeydew3", width=18, command=retDocDetails)
gaq.place(x=200, y=480)
gaq = Button(window, text="Link to see Quote Summary", fg="black", bg="honeydew3", width=20, command=quotePageLink)
gaq.place(x=400, y=480)

loadingLable("Your result will be displayed here...", "honeydew3")

# Buttons to clear the postcode and exit
clear2 = Button(window, text="Clear", fg="white", bg="brown", width=10, command=clear1)
clear2.place(x=150, y=750)
exit2 = Button(window, text="Exit", fg="white", bg="brown", width=10, command=exit1)
exit2.place(x=300, y=750)  # GROOVE, RIDGE, SUNKEN, RAISED

window.mainloop()

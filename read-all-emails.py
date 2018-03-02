import imapclient
import getpass

""" sets the server imap list """
serverList = {
    'outlook': 'imap-mail.outlook.com',
    'gmail': ''
}

""" Asks the user for their email client """
try:
    print('') #Astetic Space
    serverInput = input("What email client do you use? (i.e outlook, gmail...)") #get user email client
    imapServer = serverList[serverInput.lower()] #check if input is in the serverList dict
except:
    exit("Couldn't find your email client") #on failure, quit


email = str(input("What is your email address?")) #get target email address from user
password = getpass.getpass()
readOnly = False #False: enabes read, True: debug mode


imapObj = imapclient.IMAPClient(imapServer, ssl=True) #init connection to imap server


""" Attempt Login to email client """
try:
    imapObj.login(email, password) #login with credentials
    print('') #Astetic Space
except:
    quit('Login failure, please check you login details...)') #on failure, quit


""" Find folder """
folderList = imapObj.list_folders()

try:
    for x in range(len(folderList)): #iterate over folder list
        print(str(folderList[x][2])) #print folders
    print('') #Astetic Space

    folder = str(input("What folder would you like to read all files for?")) #get folder name from user
    imapObj.select_folder(folder, readonly=readOnly) #Tries to navigate to folder
    print(str(folder) + ' Folder selected.')
except:
    quit("Folder doesn't exist") #on failure, quit


""" Get all messages """
try:
    msgs = imapObj.search(['UNSEEN']) #gets all unread messages
    print('') #Astetic Space
    print("Imported " + str(len(msgs)) + " unseen messages!")
    print('') #Astetic Space
    read = input('Do you want to read these emails? (y/n)') #asks user to proceed
except:
    quit("Couldn't get unseen list.") #on failure, quit


""" Read all messages """
if read == 'y': #if users presses 'y'
    try:
        print('') #Astetic Space
        print("Reading Messages...")
        rawMessages = imapObj.fetch(msgs,['BODY[]']) #fetches and reads the emails
        print("Reading " + str(len(msgs)) + " unseen messages!")
    except:
        quit("Couldn't Read.") #on failure, quit
else: #if user types anything else
    quit('No action taken...') #on failure, quit



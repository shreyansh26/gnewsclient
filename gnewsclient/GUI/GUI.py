from tkinter import *
from gnewsclient import gnewsclient
from gnewsclient import utils
from tkinter import ttk


# function to set attributes(language, location, topic), and then fetch news accordingly
# we have variables topic_query, language_query, location_query for storing attributes
def news():
    global location_query, language_query,topic_query,edition_query,client,status
    client.query=None # because search query overrides all other parameters
    client.topic=topic_query.get()
    if(client.topic=="Select topic"):
        client.topic = "top stories"

    client.language=language_query.get()
    if(client.language=="Select language"):
        client.language="english"
    client.edition=edition_query.get()
    if(client.edition == "Select edition"):
        client.edition = "United States (English)"

    client.location= location_query.get()
    if(client.location==""):
        client.location = None

    update_status(client,status)
    for i in client.get_news():
        print(i)
        print("\n")
    return


# to search news related to a search string
def search():
    global search_query,client,status
    client.query= search_query.get()
    update_status(client,status)
    print(client.get_news())
    return

# helper function for status bar
def getstatus(clientX):
    x = clientX.get_config()
    y=sorted(x)
    text = ""
    for i in y:
        text += str(i) + ": " + str(x[i]) + "                         "
    return text

# set status bar text
def update_status(client, status):
    status['text']=getstatus(client)
    return



#initializing window
root = Tk()
root.title("GNEWSCLIENT")

#object making and packing
client = gnewsclient()
status = Label(root, text=getstatus(client), bd=1, relief=SUNKEN)
status.pack(side=BOTTOM, fill=X)


# implementing searching news
search_frame=Frame(root)
search_frame.pack()
search_query = StringVar()
query = Entry(search_frame, textvariable=search_query).grid(row=1, column=0)
search_button = Button(search_frame,text= "search", command=search).grid(row=1, column = 1)

west_frame = Frame(root)
west_frame.pack(side=LEFT)


# frame for topic, location, and edition filters
tle_frame=Frame(west_frame)
tle_frame.pack()

# implementing edition filter
edition_label = Label(tle_frame, text="Edition: ").grid(row=1, column=0,pady=50,sticky=W)
edition_query=StringVar()
edition_dropdown = ttk.Combobox(tle_frame, textvariable=edition_query, values=sorted(list(utils.editionMap))).grid(row=1, column=1,pady=50)
edition_query.set("Select edition")

# implementing topic filter
topic_label = Label(tle_frame, text="Topic: ").grid(row=2, column=0,pady=50,sticky=W)
topic_query=StringVar()
topic_dropdown = ttk.Combobox(tle_frame, textvariable=topic_query, values=sorted(list(utils.topicMap))).grid(row=2, column=1,pady=50)
topic_query.set("Select topic")


# implementing language filter
language_label = Label(tle_frame, text="Language: ").grid(row=3, column=0,pady=50,sticky=W)
language_query=StringVar()
language_dropdown = ttk.Combobox(tle_frame, textvariable=language_query, values=sorted(list(utils.langMap))).grid(row=3, column=1,pady=50)
language_query.set("Select language")



# implementing location filter
location_label= Label(tle_frame,text="Location: ").grid(row=4,column=0,pady=50,sticky=W)
location_query = StringVar()
location = Entry(tle_frame, textvariable=location_query).grid(row=4, column=1,pady=50)



# button to fetch news
getnews = Button(tle_frame, command=news,text = "Get News!").grid(row=6,column=0,columnspan=2, pady=25)




root.mainloop()

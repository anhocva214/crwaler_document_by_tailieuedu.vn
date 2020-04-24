import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

data = open("input.txt", "r")
string_data = data.readline()
# key = "15717"

print("Nhap key: ")
key = input()

list = []
def search_id(stop, string):
    if stop == True: return True
    s = string
    start = s.find(key)
    end = s.find(".pdf")

    while end<start :
        s  = s.replace(".pdf", "****", 1)
        end = s.find(".pdf")
        # print(end)

    id = s[start:end]+".pdf"
    s = s.replace(id, ' ')
    # print(start, " ", end)
    # print(id)
    if start == -1:
        search_id(True, s)
    else:
        # print(id[-1])
        if id!="" and len(id)>10:
            # if id[len(id)-1]=="." : id = id[0:len(name)-1]
            list.append(id)
            search_id(False, s)

search_id(False, string_data.replace(".doc", ".pdf"))
# print(len(list))

# driver = webdriver.Chrome()
# for id in list:
#     # driver.implicitly_wait(3)
#     link = "http://tailieuedu.vn/storage/previews/{}"
#     driver.get(link.format(id))

# driver.close()


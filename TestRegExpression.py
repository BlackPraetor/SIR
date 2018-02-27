import MySQLdb, re
Actcon=MySQLdb.connect(host="localhost", user="root", passwd="Bp040931", db="actordatabase")
cursor = Actcon.cursor()
Actcon.set_character_set('utf8mb4')
cursor.execute('SET NAMES utf8mb4;')
cursor.execute('SET CHARACTER SET utf8mb4;')
cursor.execute('SET character_set_connection=utf8mb4;')
for i in range(1,30,1):
    Actorsearch="SELECT Snippet, Searchkey FROM Snippet WHERE ActorID=%d"%i
    cursor.execute(Actorsearch)
    for (Snippet, Searchkey) in cursor:
        search_term="%s %s\n" %(Snippet, Searchkey)
        Age=re.search('อายุ\S+(.\d+)',Snippet)
      #Age2=re.search('อายุ(.\d?)',Snippet)
        Dir=re.search('กำกับโดย (.\S+)',Snippet)
        DOB=re.search('เกิดเมื่อ\S+(.\d+)(.\S+).?\S+(...\d+)',Snippet)
        Height=re.search('ส่วนสูง (.\d+)',Snippet)
        Weight=re.search('น้ำหนัก\S(.\d+)',Snippet)
        Heri=re.search('ลูกครึ่ง(.\S+)-(.\S+)',Snippet)
        if Heri:
            print(Searchkey)
            print("Heritage:",Heri.group(1),"-",Heri.group(2))
            print(Snippet)

        
        if DOB:
            print(Searchkey)
            print("DOB:", DOB.group(1))
            print("DOB:", DOB.group(2))
            print("DOB:", DOB.group(3))
            print(search_term)     
        if Age:
            print("Age", Age.group(1))
            print(search_term)
      #  if Age2:
      #      print("Age2", Age2.group(1))
      #      print(search_term)
        if Height:
            print("Height", Height.group(1))
            print(search_term)
        if Weight:
            print("Weight", Weight.group(1))
            print(search_term)
        if Dir:
            print("กำกับโดย", Dir.group(1))
            print(search_term)
        
        

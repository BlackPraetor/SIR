import MySQLdb, re
Actcon=MySQLdb.connect(host="localhost", user="root", passwd="Bp040931", db="actordatabase")
cursor = Actcon.cursor()
Actcon.set_character_set('utf8mb4')
cursor.execute('SET NAMES utf8mb4;')
cursor.execute('SET CHARACTER SET utf8mb4;')
cursor.execute('SET character_set_connection=utf8mb4;')
for i in range(30,31,1):
    Actorsearch="SELECT Snippet, Searchkey FROM Snippet WHERE ActorID=%d"%i
    cursor.execute(Actorsearch)
    HeriStr="NA"
    DOBStr="NA"
    AgeStr="0"
    HStr="0"
    WStr="0"
    DirStr="NA"
    SStr="NA"
    RStr="NA"
    for (Snippet, Searchkey) in cursor:
        search_term="%s %s\n" %(Snippet, Searchkey)
        Age=re.search('อายุ\S+(.\d+)',Snippet)
        Dir=re.search('กำกับโดย (.\S+) (.\S+)',Snippet)
        DOB=re.search('เกิดเมื่อ\S+(.\d+)(.\S+).?\S+(...\d+)',Snippet)
        Height=re.search('ส่วนสูง\S+(.\d+)',Snippet)
        Weight=re.search('น้ำหนัก\S(.\d+)',Snippet)
        Heri=re.search('ลูกครึ่ง(.\S+)-(.\S+)',Snippet)
        FilmName=re.search('เรื่อง\s(.\S+)',Snippet)
        FilmRole=re.search('รับบท(.\S+)',Snippet)
        if Heri:
            print(Searchkey)
            HeriStr=Heri.group(1)+"-"+Heri.group(2)
            print("Heritage:",HeriStr)
            print(Snippet)
        if DOB:
            print(Searchkey)
            DOBStr=DOB.group(1)+DOB.group(2)+DOB.group(3)
            DOBStr.strip()
            print("DOB:", DOBStr)
            print(search_term)
        if Age:
            AgeStr=Age.group(1)
            print("Age", AgeStr)
            print(search_term)
        if Height:
            print("Height", Height.group(1))
            HStr=Height.group(1)
            print(search_term)
        if Weight:
            print("Weight", Weight.group(1))
            WStr=Weight.group(1)
            print(search_term)
        if Dir:
            print("กำกับโดย", Dir.group(1)+" "+Dir.group(2))
            DirStr=Dir.group(1)+" "+Dir.group(2)
            print(search_term)
        if FilmName:
             print("เรื่อง", FilmName.group(1))
             SStr=FilmName.group(1)
             print(search_term)
        if FilmRole:
             print("รับบท", FilmRole.group(1))
             RStr=FilmRole.group(1)
             print(search_term)
    ActProAdd="INSERT INTO actorprofile (ActorName, Age, DOB, Height, Weight, Heritage, FilmRole, FilmName) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
    #ActProAdd="INSERT INTO actorprofile (ActorName, Age, DOB, Height, Weight, Heritage, FilmRole, FilmName) VALUES ('1','2','3','4','5','6','7','8')"
    print(Searchkey, AgeStr, DOBStr, HStr, WStr, HeriStr, RStr, SStr)
    print(ActProAdd)
    data=(Searchkey, AgeStr, DOBStr, HStr, WStr, HeriStr, RStr, SStr)
    #data=("ดิว นัทธพงศ์ พรมสิงห์","N/A","31 ตุลาค 2535","N/A","N/A","N/A","N/A","N/A")
    cursor.execute(ActProAdd,data)
    #cursor.execute(ActProAdd)
    Actcon.commit()
Actcon.close()

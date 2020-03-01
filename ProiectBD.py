from tkinter import *
import mysql.connector
from PIL import Image
import datetime

#conexiune la server
prj=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="ProiectBD",
    database="ProiectBD"
)
cursor=prj.cursor()

#fereastra pentru actiunile valabile pentru un angajat`
def WindowAngajat():
    #functie ce arata salariul
    def arataSalariu():
        #accesare date de la entryboxuri
        entryNume = entryAng.get()
        entryPrenum=entryPren.get()
        #construire query
        sql="select Salariu from Angajat where Nume= %s AND Prenume= %s"
        cursor.execute(sql,(entryNume,entryPrenum ))
        #colectare date
        result = cursor.fetchall()
        #afisare date
        labelSal = Label(angajat, text=result, fg='blue', relief='solid', font=('arial', 16, 'bold'))
        labelSal.place(x=100, y=100)
    #functie ce updateaza baza de date pentru coloana Finalizat
    def finalizareTask():
        #colectare date din entrybox
        entryID = entryAng.get()
        entryPrenum=entryPren.get()
        #construire query
        sql="UPDATE ProiectBD.Lucreaza  L INNER JOIN ProiectBD.Angajat A ON L.AngajatID=A.AngajatID set L.Finalizat=1 Where A.Nume= %s AND A.Prenume= %s"
        cursor.execute(sql, (entryID,entryPrenum))
        #commit pentru a actualiza baza de date
        prj.commit()
    #functie ce afiseaza proiectele unui angajat
    def arataProiecte():
        #functie ce actualizeaza orele de lucru ale unui angajat
        def actualizareOre():
            #colectare date
            entryID = entryAng.get()
            entryPrenum = entryPren.get()
            entryOrele=entryOre.get()
            #construire query
            sql = "UPDATE ProiectBD.Lucreaza  L INNER JOIN ProiectBD.Angajat A ON L.AngajatID=A.AngajatID set L.NumarOre= %s Where A.Nume= %s AND A.Prenume= %s"
            cursor.execute(sql, (entryOrele, entryID, entryPrenum))
            #commit pentru a salva modificarile in baza de date
            prj.commit()

        #functie ce arata serviciile unde sunt echipamente ce au nevoie de revizie in viitorul apropiat
        def ajutorRevizie():
            sql="SELECT S.NumeServiciu, E.DataRevizie from ProiectBD.Servicii S INNER JOIN ProiectBD.Echipamente E on S.ServiciuID=E.ServiciuID WHERE E.DataRevizie > 2020-10-10"
            cursor.execute(sql)
            #formare rezultat pe baza pe informatiilor colectate
            result=cursor.fetchall()
            text=""
            for i in range(len(result)):
                serv=result[i][0]
                data=result[i][1]
                text=text + "{}".format(serv) + " " + "{}".format(data) + "\n"
            #plasare raspuns pe interfata grafica
            labelRevizie = Label(angajat, text=text, fg='blue', relief='solid', font=('arial', 16, 'bold'))
            labelRevizie.pack()
            labelRevizie.place(x=50, y=400)
        #colectare date
        entryID = entryAng.get()
        entryPrenum=entryPren.get()
        entryOre = IntVar(angajat)

        #definire drop down menu pentru update ore
        list=['1','2','3','4','5','6']
        entryOre.set(list[0])
        entryOreUpdated=OptionMenu(angajat,entryOre,*list)
        entryOreUpdated.pack()
        entryOreUpdated.place(x=250, y=250)
        #formare query pentru a afla ora de incepere a unui proiect
        sql = "SELECT L.DataIncepere from ProiectBD.Lucreaza L INNER JOIN ProiectBD.Angajat A on L.AngajatID=A.AngajatID WHERE A.Nume= %s AND A.Prenume= %s"
        cursor.execute(sql, (entryID,entryPrenum))
        result = cursor.fetchall()
        #afisare rezultat
        labelSal = Label(angajat, text=result[0][0], fg='blue', relief='solid', font=('arial', 16, 'bold'))
        labelSal.place(x=100, y=150)

        #colectare date pentru query
        entryID = entryAng.get()
        entryPrenum = entryPren.get()
        #construire query ce afiseaza adresa, orasul, ora si judetul unde se afla un proiect
        sql = "select A.Adresa, A.Oras, A.Judet from ProiectBD.Proiecte A INNER JOIN ProiectBD.Lucreaza B ON A.ProiectID=B.ProiectID INNER JOIN ProiectBD.Angajat C ON B.AngajatID=C.AngajatID WHERE C.Nume= %s AND C.Prenume= %s"
        cursor.execute(sql, (entryID, entryPrenum))
        result = cursor.fetchall()
        print(result)
        #formatare rezultat pentru a putea fi afisat
        result="{}".format(result[0][0]) + " " +"{}".format(result[0][1]) + " " + "{}".format(result[0][2])
        #afisare query
        labelSal = Label(angajat, text=result, fg='blue', relief='solid', font=('arial', 16, 'bold'))
        labelSal.place(x=100, y=200)

        #selectare date
        entryID = entryAng.get()
        entryPrenum = entryPren.get()
        #selectare numar ore pe care trebuie sa le lucreze un angajat la un proiect
        sql = "SELECT L.NumarOre from ProiectBD.Lucreaza L INNER JOIN ProiectBD.Angajat A on L.AngajatID=A.AngajatID WHERE A.Nume= %s AND A.Prenume= %s"
        cursor.execute(sql, (entryID, entryPrenum))
        result = cursor.fetchall()
        #afisare rezultat
        labelSal = Label(angajat, text=result, fg='blue', relief='solid', font=('arial', 16, 'bold'))
        labelSal.place(x=100, y=250)

        labelNrOre=Label(angajat, text="Numar Ore", fg='blue', relief='solid', font=('arial', 16, 'bold'))
        labelNrOre.place(x=10,y=250)
        #buton ce face trimite la functia actualizareOre ce schimba numarul de ore lucrat de un angajat la un proiect
        buttonActualizare = Button(angajat, text="Actualizare Ore", fg="blue", relief='solid', font=('arial', 16, 'bold'),
                                command=actualizareOre)
        buttonActualizare.place(x=120, y=250)

        #afisare serviciu asociat proiectului la care trebuie un angajat sa lucreze
        sqlaux2= "SELECT S.NumeServiciu FROM ProiectBD.Servicii S INNER JOIN ProiectBD.Lucreaza L ON S.ServiciuID=L.ServiciuID INNER JOIN ProiectBD.Angajat A on L.AngajatID=A.AngajatID WHERE A.Nume= %s AND A.Prenume= %s "
        cursor.execute(sqlaux2, (entryID, entryPrenum))
        result=cursor.fetchall()
        #afisare rezultat
        labelNumeServ = Label(angajat, text=result, fg='blue', relief='solid', font=('arial', 16, 'bold'))
        labelNumeServ.place(x=10, y=300)

        #buton ce face trimitere la functia ajutorRevizie ce ofera angajatilor informatii despre echipamentele ce au nevoie de revizie
        buttonRev= Button(angajat, text="Ajutor Revizie", fg="blue", relief='solid',
                                   font=('arial', 16, 'bold'),
                                   command=ajutorRevizie)
        buttonRev.place(x=10, y=350)

        #verificare daca un proiect este sau nu finalizat
        sqlaux = "SELECT L.Finalizat FROM ProiectBD.Lucreaza L INNER JOIN ProiectBD.Angajat A on L.AngajatID=A.AngajatID where Nume= %s AND Prenume= %s"
        cursor.execute(sqlaux, (entryID,entryPrenum))
        result2 = cursor.fetchall()
        if result2[0][0] == 0:
            #se face trimitere la functia finalizareTask intrucat task-ul apare ca fiind nefinalizat
            labelNefinal = Label(angajat, text="Nefinalizat", fg='blue', relief='solid', font=('arial', 16, 'bold'))
            labelNefinal.place(x=270, y=150)
            buttonFinalizare = Button(angajat, text="Finalizare", fg="blue", relief='solid', font=('arial', 16, 'bold'),
                      command=finalizareTask)
            buttonFinalizare.place(x=360, y=150)
        else:
            #se afiseaza faptul ca taskul este terminat
            labelFinal = Label(angajat, text="Finalizat", fg='blue', relief='solid', font=('arial', 16, 'bold'))
            labelFinal.place(x=270, y=150)




    #definire entrybox uri pentru nume si prenume angajat
    entryAng=StringVar()
    entryPren=StringVar()
    #definire window de angajat
    angajat=Tk()
    angajat.title("Angajat")
    angajat.geometry("500x800")

    #formare window angajat cu label-urile necesare
    labelNume = Label(angajat, text="Nume", fg='blue',relief='solid', font=('arial', 16, 'bold'))
    labelNume.place(x=10,y=20)
    entryAng=Entry(angajat,textvar=entryAng)
    entryAng.place(x=100,y=20)

    labelPren=Label(angajat,text="Prenume",fg='blue',relief='solid',font=('arial',16, 'bold'))
    labelPren.place(x=10,y=60)
    entryPren = Entry(angajat, textvar=entryPren)
    entryPren.place(x=100, y=60)


    buttonAng = Button(angajat, text="Salariu", fg="blue",relief='solid', font=('arial', 16, 'bold'),command=arataSalariu)
    buttonAng.place(x=10,y=100)

    buttonProiecte =Button(angajat, text="Proiecte", fg="blue",relief='solid', font=('arial', 16, 'bold'),command=arataProiecte)
    buttonProiecte.place(x=10,y=150)


#fereastra aferenta actiunilor valabile pentru un administrator
def WindowAdmin():
    #definire functie ce va introduce un angajat
    def inserareAngajat():

        #comanda ce introduce angajatul
        def insertAngajat():
            #colectare date necesare din entrybox-uri
            nume= entryNume.get()
            prenume = entryPreNume.get()
            cnp = entryCNP.get()
            strada = entryStrada.get()
            oras = entryOras.get()
            judet=entryJudet.get()
            dnas=entryDNas.get()
            dang=entryDAng.get()
            salariu=entrySalariu.get()
            sex=entrySex.get()
            user=entryUser.get()
            passwd=entryPass.get()

            sql = "SET FOREIGN_KEY_CHECKS=0"
            cursor.execute(sql)
            #introducere date in baza de date
            sql = "INSERT INTO `ProiectBD`.`Angajat` (`Nume`, `Prenume`, `CNP`, `Strada`, `OrasResedinta`, `JudetResedinta`, `DataNasterii`, `DataAngajarii`, `Salariu`, `Sex`, `Username`, `Password`) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
            cursor.execute(sql, (nume, prenume, cnp, strada, oras, judet, dnas, dang, salariu, sex, user, passwd))
            sql = "SET FOREIGN_KEY_CHECKS=1"
            cursor.execute(sql)
            #salvare schimbari in baza de date in functie de schema personala modificata
            prj.commit()
            succes = Tk()
            #fereastra de succes
            succes.title("Succes")
            succes.geometry("400x200")

            labelPren = Label(succes, text="Comanda executata cu succes", fg='blue', relief='solid',
                              font=('arial', 16, 'bold'))
            labelPren.place(x=10, y=60)



        #definire window de inserare date pentru introducere angajat
        inserare=Tk()
        inserare.title("Adaugare angajat")
        inserare.geometry("500x700")

        # definire labeluri si entrybox uri pentru toate informatiile necesare unui angajat
        labelNume = Label(inserare, text="Nume: ", fg='blue', relief='solid',
                         font=('arial', 16, 'bold'))
        labelNume.place(x=10, y=10)

        entryNume = StringVar(inserare)
        entryNumeE = Entry(inserare, textvar=entryNume)
        entryNumeE.place(x=200, y=10)

        labelPreNume = Label(inserare, text="Prenume: ", fg='blue', relief='solid',
                          font=('arial', 16, 'bold'))
        labelPreNume.place(x=10, y=60)

        entryPreNume = StringVar(inserare)
        entryPreNumeE = Entry(inserare, textvar=entryPreNume)
        entryPreNumeE.place(x=200, y=60)

        labelCNP = Label(inserare, text="CNP: ", fg='blue', relief='solid',
                          font=('arial', 16, 'bold'))
        labelCNP.place(x=10, y=110)

        entryCNP = StringVar(inserare)
        entryCNPE = Entry(inserare,textvar=entryCNP)
        entryCNPE.place(x=200, y=110)

        labelStrada = Label(inserare, text="Strada: ", fg='blue', relief='solid',
                          font=('arial', 16, 'bold'))
        labelStrada.place(x=10, y=160)

        entryStrada = StringVar(inserare)
        entryStradaE = Entry(inserare, textvar=entryStrada)
        entryStradaE.place(x=200, y=160)

        labelOras = Label(inserare, text="Oras: ", fg='blue', relief='solid',
                          font=('arial', 16, 'bold'))
        labelOras.place(x=10, y=210)

        entryOras = StringVar(inserare)
        entryOrasE = Entry(inserare, textvar=entryOras)
        entryOrasE.place(x=200, y=210)

        labelJudet = Label(inserare, text="Judet: ", fg='blue', relief='solid',
                          font=('arial', 16, 'bold'))
        labelJudet.place(x=10, y=260)

        entryJudet = StringVar(inserare)
        entryJudetE = Entry(inserare, textvar=entryJudet)
        entryJudetE.place(x=200, y=260)

        labelDNas = Label(inserare, text="Data nasterii: ", fg='blue', relief='solid',
                          font=('arial', 16, 'bold'))
        labelDNas.place(x=10, y=310)

        entryDNas = StringVar(inserare)
        entryDNasE = Entry(inserare, textvar=entryDNas)
        entryDNasE.place(x=200, y=310)

        labelDAng = Label(inserare, text="Data angajarii: ", fg='blue', relief='solid',
                          font=('arial', 16, 'bold'))
        labelDAng.place(x=10, y=360)

        entryDAng = StringVar(inserare)
        entryDAngE = Entry(inserare, textvar=entryDAng)
        entryDAngE.place(x=200, y=360)

        labelSalariu = Label(inserare, text="Salariu: ", fg='blue', relief='solid',
                      font=('arial', 16, 'bold'))
        labelSalariu.place(x=10, y=410)

        entrySalariu=IntVar(inserare)
        entrySalariuE=OptionMenu(inserare,entrySalariu,'2000','3000','4000')
        entrySalariuE.pack()
        entrySalariuE.place(x=200,y=410)

        labelSex = Label(inserare, text="Sex: ", fg='blue', relief='solid',
                             font=('arial', 16, 'bold'))
        labelSex.place(x=10, y=460)

        entrySex = StringVar(inserare)
        entrySexE = OptionMenu(inserare, entrySex,'M','F')
        entrySexE.pack()
        entrySexE.place(x=200, y=460)

        labelUser = Label(inserare, text="Username: ", fg='blue', relief='solid',
                          font=('arial', 16, 'bold'))
        labelUser.place(x=10, y=510)

        entryUser = StringVar(inserare)
        entryUserE = Entry(inserare, textvar=entryUser)
        entryUserE.place(x=200, y=510)

        labelPass = Label(inserare, text="Password: ", fg='blue', relief='solid',
                          font=('arial', 16, 'bold'))
        labelPass.place(x=10, y=560)

        entryPass = StringVar(inserare)
        entryPassE = Entry(inserare,show='*', textvar=entryPass)
        entryPassE.place(x=200, y=560)

        buttonExec = Button(inserare, text="Execute ", fg="blue", relief='solid', font=('arial', 16, 'bold'),
                            command=insertAngajat)
        buttonExec.place(x=10, y=610)

    #functie de inserare locatie
    def inserareLocatie():
        #functie ce insereaza in baza de date locatia noua
        def adaugareProiect():
            #colectare date
            adr=entryAdr.get()
            oras=entryOrs.get()
            jud=entryJud.get()
            od=entryOD.get()
            oi=entryOI.get()
            print(adr)
            print(oras)
            print(jud)
            print(od)
            print(oi)
            sql = "SET FOREIGN_KEY_CHECKS=0"
            cursor.execute(sql)
            #construire query pe baza informatiilor colectate
            sql="INSERT INTO `ProiectBD`.`Locatii` (`AdresaLocatie`, `Oras`, `Judet`, `OraDeschidere`, `OraInchidere`) VALUES (%s , %s, %s, %s, %s)"
            cursor.execute(sql,(adr,oras,jud,od,oi))
            sql = "SET FOREIGN_KEY_CHECKS=1"
            cursor.execute(sql)
            #salvare in baza de date a schimbarilor
            prj.commit()
            succes = Tk()
            #fereastra ce arata ca datele s-au introdus corect
            succes.title("Succes")
            succes.geometry("400x200")

            labelPren = Label(succes, text="Comanda executata cu succes", fg='blue', relief='solid',
                          font=('arial', 16, 'bold'))
            labelPren.place(x=10, y=60)


        #definire labeluri si entryboxuri pentru informatiile necesare inserarii
        labelAdr = Label(admin, text="Adresa: ", fg='blue', relief='solid',
                          font=('arial', 16, 'bold'))
        labelAdr.place(x=10, y=180)

        entryAdr=StringVar(admin)
        entryAdresa = Entry(admin, textvar=entryAdr)
        entryAdresa.place(x=10, y=210)

        labelOras=Label(admin, text="Oras: ", fg='blue', relief='solid',
                          font=('arial', 16, 'bold'))
        labelOras.place(x=200, y=180)
        entryOrs=StringVar(admin)
        entryOras=Entry(admin,textvar=entryOrs)
        entryOras.place(x=200,y=210)

        labelJudet=Label(admin, text="Judet: ", fg='blue', relief='solid',
                          font=('arial', 16, 'bold'))
        labelJudet.place(x=10, y=240)

        entryJud=StringVar(admin)
        entryJudet=Entry(admin,textvar=entryJud)
        entryJudet.place(x=10,y=270)

        labelOD=Label(admin, text="Ora deschidere: ", fg='blue', relief='solid',
                          font=('arial', 16, 'bold'))
        labelOD.place(x=10, y=300)

        entryOD=StringVar(admin)
        entryOraD=Entry(admin,textvar=entryOD)
        entryOraD.place(x=10,y=330)

        labelOI = Label(admin, text="Ora inchidere: ", fg='blue', relief='solid',
                    font=('arial', 16, 'bold'))
        labelOI.place(x=200, y=300)

        entryOI = StringVar(admin)
        entryOraI = Entry(admin, textvar=entryOI)
        entryOraI.place(x=200, y=330)

        buttonExec = Button(admin, text="Execute ", fg="blue", relief='solid', font=('arial', 16, 'bold'),
                                 command=adaugareProiect)
        buttonExec.place(x=10, y=360)

    #definire functie de stergere proiect
    def stergereProiect():
        #executia stergerii in baza de date
        def execStergere():
            #colectare date
            entrySt=entryPrj.get()
            sql="SET FOREIGN_KEY_CHECKS=0"
            cursor.execute(sql)
            #construire query
            sql="Delete from ProiectBD.Proiecte WHERE NumeProiect= %s"

            cursor.execute(sql, (entrySt, ))
            sql="SET FOREIGN_KEY_CHECKS=1"
            cursor.execute(sql)
            prj.commit()
            succes = Tk()
            succes.title("Succes")
            succes.geometry("400x200")

            labelPren = Label(succes, text="Comanda executata cu succes", fg='blue', relief='solid',
                              font=('arial', 16, 'bold'))
            labelPren.place(x=10, y=60)

        #construire dropdown menu folosind numele de proiect aflate printr-un query
        entryPrj = StringVar(admin)
        sql = "SELECT NumeProiect FROM ProiectBD.Proiecte"
        cursor.execute(sql)
        result = cursor.fetchall()

        #formare dropdown menu
        options=[None]*len(result)

        for i in range(len(result)):
            options[i]=result[i][0]

        entryPrj.set(options[0])
        entryProjects = OptionMenu(admin, entryPrj, *options)
        entryProjects.pack()

        entryProjects.place(x=10, y=500)

        #buton executie ce duce la comanda execStergere
        buttonExec=Button(admin, text="Executare", fg="blue",relief='solid', font=('arial', 16, 'bold'),command=execStergere)
        buttonExec.place(x=200,y=450)




    #definire functie de stergere serviciu
    def stergereServiciu():
        #functie de executie a stergerii prin query
        def execStergere():
            #colectare date
            entrySt=entryPrj.get()
            sql="SET FOREIGN_KEY_CHECKS=0"
            cursor.execute(sql)
            #construire query
            sql="Delete from ProiectBD.Servicii WHERE NumeServiciu= %s"

            cursor.execute(sql, (entrySt, ))
            sql="SET FOREIGN_KEY_CHECKS=1"
            cursor.execute(sql)
            #salvare in baza de date
            prj.commit()
            #fereastra ce afiseaza ca s-a executat cu succes comanda
            succes = Tk()
            succes.title("Succes")
            succes.geometry("400x200")

            labelPren = Label(succes, text="Comanda executata cu succes", fg='blue', relief='solid', font=('arial', 16, 'bold'))
            labelPren.place(x=10, y=60)


        #label si dropdown menu creat pe baza unui query ce gaseste toate numele serviciilor disponibile
        entryPrj = StringVar(admin)
        sql = "SELECT NumeServiciu FROM ProiectBD.Servicii"
        cursor.execute(sql)
        result = cursor.fetchall()
        #formare dropdown menu pe baza inforamtiilor obtine din query
        options=[None]*len(result)

        for i in range(len(result)):
            options[i]=result[i][0]

        entryPrj.set(options[0])
        entryProjects = OptionMenu(admin, entryPrj, *options)
        entryProjects.pack()

        entryProjects.place(x=10, y=600)
        #buton de executie ce face trimitere la functia execStergere
        buttonExec=Button(admin, text="Executare", fg="blue",relief='solid', font=('arial', 16, 'bold'),command=execStergere)
        buttonExec.place(x=200,y=550)

    #definire interogare complexa 1
    #se afiseaza toti angajatii care nu lucreaza la niciun proiect
    def query1():
        entrySal=entrySalarii.get()
        sql = "SELECT Nume, Prenume from ProiectBD.Angajat where Salariu > %s AND AngajatID not in ( SELECT AngajatID from ProiectBD.Lucreaza)"
        cursor.execute(sql,(entrySal, ))
        result = cursor.fetchall()
        text=""
        for i in range(len(result)):
            nume=result[i][0]
            prenume=result[i][1]
            text=text + "{}".format(nume) + " " + "{}".format(prenume) + " \n"

        succes = Tk()
        succes.title("Succes")
        succes.geometry("400x200")

        labelPren = Label(succes, text=text, fg='blue', relief='solid',
                          font=('arial', 16, 'bold'))
        labelPren.pack()
        labelPren.place(x=10, y=60)
    #definire interogara complexa 2
    #se afiseaza angajatul cu cel mai mare salariu
    def query2():
        sql = "SELECT Nume, Prenume from ProiectBD.Angajat where Salariu = (SELECT MAX(Salariu) from ProiectBD.Angajat)"
        cursor.execute(sql)
        result = cursor.fetchall()
        text= "{}".format(result[0][0]) + " " + "{}".format(result[0][1])
        succes = Tk()
        succes.title("Succes")
        succes.geometry("400x200")

        labelPren = Label(succes, text=text, fg='blue', relief='solid',
                          font=('arial', 16, 'bold'))
        labelPren.pack()
        labelPren.place(x=10, y=60)
    #definire interogara complexa 3
    #Se afiseaza numele serviciilor si locatiile servicilor unde echipamentul detinut este peste media numarului de echipamente
    def query3():
        sql = "select S.NumeServiciu , L.AdresaLocatie, SUM(E.Cantitate) from ProiectBD.Servicii S "
        sql= sql + "INNER JOIN ProiectBD.Locatii L on S.LocatieID=L.LocatieID "
        sql = sql + "INNER JOIN ProiectBD.Echipamente E on S.ServiciuID=E.ServiciuID "
        sql=sql + "GROUP BY S.NumeServiciu, L.AdresaLocatie "
        sql=sql + "HAVING SUM(E.Cantitate) > ( SELECT AVG(Cantitate) from ProiectBD.Echipamente)"

        cursor.execute(sql)
        result = cursor.fetchall()
        text = ""
        for i in range(len(result)):
            serv = result[i][0]
            loc = result[i][1]
            cant=result[i][2]
            text = text + "{}".format(serv) + " " + "| {} |".format(loc) + " " + "{}".format(cant) + "\n"

        succes = Tk()
        succes.title("Succes")
        succes.geometry("400x200")

        labelPren = Label(succes, text=text, fg='blue', relief='solid',
                          font=('arial', 16, 'bold'))
        labelPren.pack()
        labelPren.place(x=10, y=60)
    #definire interogare complexa 4
    #se afiseaza toti angajatii care vor lucra la un proiect inainte de ziua lor de nastere
    def query4():
        sql = "select A.Nume, A.Prenume , DATE_FORMAT(DataNasterii, '%m-%d') as data, P.NumeProiect from ProiectBD.Angajat A "
        sql = sql + "INNER JOIN ProiectBD.Lucreaza  L on A.AngajatID=L.AngajatID  "
        sql = sql + "INNER JOIN ProiectBD.Proiecte P on L.ProiectID=P.ProiectID "
        sql = sql + "HAVING data < ( SELECT DATE_FORMAT(DataIncepere, '%m-%d') FROM ProiectBD.Lucreaza LL where A.AngajatID=LL.AngajatID)"

        cursor.execute(sql)
        result = cursor.fetchall()
        text = ""
        for i in range(len(result)):
            nume = result[i][0]
            prenume = result[i][1]
            data = result[i][2]
            prj=result[i][3]
            text = text + "{}".format(nume) + " " + "{}".format(prenume) + " " + "{} ".format(data) + "{}".format(prj) +  "\n"

        succes = Tk()
        succes.title("Succes")
        succes.geometry("400x200")

        labelPren = Label(succes, text=text, fg='blue', relief='solid',
                          font=('arial', 16, 'bold'))
        labelPren.pack()
        labelPren.place(x=10, y=60)



    #definire window administrator
    admin=Tk()
    admin.title("Admin")
    admin.geometry("600x900")
    #definire butoane din window administrator
    buttonInsAng = Button(admin, text="Inserare Angajat", fg="blue", relief='solid', font=('arial', 16, 'bold'),
                       command=inserareAngajat)
    buttonInsAng.place(x=10, y=50)

    buttonLocatie= Button(admin, text="Inserare Locatie", fg="blue", relief='solid', font=('arial', 16, 'bold'),
                       command=inserareLocatie)
    buttonLocatie.place(x=10, y=150)

    buttonStProiect=Button(admin, text="Stergere Proiect ", fg="blue", relief='solid', font=('arial', 16, 'bold'),
                       command=stergereProiect)
    buttonStProiect.place(x=10,y=450)

    buttonStServiciu=Button(admin, text="Stergere Serviciu", fg="blue", relief='solid', font=('arial', 16, 'bold'),
                       command=stergereServiciu)
    buttonStServiciu.place(x=10,y=550)

    buttonQ1=Button(admin, text="Info 1", fg="blue", relief='solid', font=('arial', 16, 'bold'),
                       command=query1)
    buttonQ1.place(x=10,y=650)

    #dropdown menu pentru query 2
    entrySalarii=StringVar()
    list = ['1500', '2000', '2500', '3000']
    entrySalarii.set(list[0])
    entrySalar = OptionMenu(admin, entrySalarii, *list)
    entrySalar.pack()
    entrySalar.place(x=10, y=700)

    buttonQ2 = Button(admin, text="Info 2", fg="blue", relief='solid', font=('arial', 16, 'bold'),
                  command=query2)
    buttonQ2.place(x=350, y=650)

    buttonQ3 = Button(admin, text="Info 3", fg="blue", relief='solid', font=('arial', 16, 'bold'),
                      command=query3)
    buttonQ3.place(x=10, y=750)

    buttonQ4 = Button(admin, text="Info 4", fg="blue", relief='solid', font=('arial', 16, 'bold'),
                      command=query4)
    buttonQ4.place(x=350, y=750)




#alegere tip de utilizator: admin/angajat pe baza credentialelor
def alegereWindow():
    entryUsername = entryUser.get()
    entryPassword = entryPass.get()
    sql="SELECT AngajatID from ProiectBD.Angajat Where Username= %s and Password= %s"
    cursor.execute(sql, (entryUsername,entryPassword))
    result=cursor.fetchall()
    print(result)
    #login
    if entryUsername == "admin":
        if entryPassword == "admin":
            WindowAdmin()
    else:
        if result != [] :
            WindowAngajat()
        else:
            succes = Tk()
            succes.title("Logare nereusita")
            succes.geometry("400x200")

            labelPren = Label(succes, text="Username sau parola introduse gresit.", fg='blue', relief='solid',
                              font=('arial', 16, 'bold'))
            labelPren.place(x=10, y=60)
#definire window initial de login
root=Tk()
root.title('Proiect BD')
root.geometry("300x300")

#adaugare poza fundal
canvas=Canvas(root,width=1597,height=561)
image=PhotoImage(file="/Users/hakanmeva/Downloads/Casa-din-Povesti-fatada-dreapta-Cartierul-Buna-Ziua-Tartasesti-nord-vest-Bucuresti.png/")
canvas.create_image(0,0,anchor=NW,image=image)
canvas.pack()

#definire labeluri si entryboxuri din window de login
labelPrincipal=Label(root,text="Credentials",fg='blue',font=('arial',16,'bold'))
labelPrincipal.place(x=50,y=10)

labelUser=Label(root,text="User:",fg="blue",font=('arial',16,'bold'))
labelUser.place(x=30,y=100)

labelPass=Label(root,text="Parola:",fg="blue",font=('arial',16,'bold'))
labelPass.place(x=30,y=150)

entryUser=StringVar()
entryPass=StringVar()
entryUser=Entry(root, textvar=entryUser)
entryUser.place(x=100,y=100)
entryPass=Entry(root,show='*',textvar=entryPass)
entryPass.place(x=100,y=150)


buttonAuten =Button(root, text="Autentificare", fg="blue",relief='solid', font=('arial', 16, 'bold'),command=alegereWindow)
buttonAuten.place(x=150,y=200)


root.mainloop()




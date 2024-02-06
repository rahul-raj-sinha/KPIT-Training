
import xml.dom.minidom

DOMTree = xml.dom.minidom.parse("C:\\Training\\PycharmProjects\\KPIT2024\\Data\\stud.xml")
collection = DOMTree.documentElement

std = collection.getElementsByTagName('stud')

for st in std:
    print(f"Student Name :", st.getAttribute('name'))

    dob = st.getElementsByTagName('dob')[0]
    print("DOB :", dob.childNodes[0].data)

    cls = st.getElementsByTagName('class')[0]
    print("Class :", cls.childNodes[0].data)

    gen = st.getElementsByTagName('gender')[0]
    print("Gender :", gen.childNodes[0].data)

    con = st.getElementsByTagName('contact')[0]
    print("Contact No :", con.childNodes[0].data)

    ret = st.getElementsByTagName('rettype')[0]
    print("ReturnType :", ret.childNodes[0].data)

    print('\n', "-" * 60, "\n")

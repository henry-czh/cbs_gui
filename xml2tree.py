
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtXml import *

def create_dict(tdict,inst_list):
    if len(inst_list)==1:
        tdict[inst_list[0]]=dict()
        tdict[inst_list[0]]['star']=True
    else:
        if not inst_list[0] in tdict:
            tdict[inst_list[0]] = {}
        create_dict(tdict[inst_list[0]],inst_list[1:])
    return tdict


def genDesignTree():
    tree_dict = dict()
    doc = QDomDocument("mydocument")
    file = QFile("example.xml")
    if not file.open(QIODevice.ReadOnly):
        print ("file type error")
    if not doc.setContent(file):
        file.close()

    docElem = doc.documentElement()
    #print (docElem.nodeName())

    root = docElem.firstChild()
    #print (root.nodeName())
    while not root.isNull():
        e = root.toElement() # try to convert the node to an element.
        if not e.isNull():
            if e.tagName() == "tb_top":
                top_tb=e.text()

            if e.tagName() == "dut_top":
                dut_top=e.text()

            if e.tagName() == "config_item":
                item=e.attribute('name')
                if e.attribute('type')=="instance":
                    ii = e.firstChild()
                    while not ii.isNull():
                        inst_e = ii.toElement()
                        if inst_e.tagName() == "hdl_path":
                            print (inst_e.text())                                       
                            tree_dict = create_dict(tree_dict,inst_e.text().strip().split('.'))
                        ii = ii.nextSibling() 
        root = root.nextSibling()
    print (tree_dict)
    return tree_dict


if __name__=="__main__":
    genDesignTree()




## Here we append a new element to the end of the document
#elem = doc.createElement("img")
#elem.setAttribute("src", "myimage.png")
#docElem.appendChild(elem)
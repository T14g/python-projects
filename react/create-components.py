##
# Create a new component folder and files with default code in the current folder
# Author: T14g (https://github.com/t14g)
##
import os
import pathlib

BASE_PATH = str(pathlib.Path(__file__).parent.absolute()) + '/'

def createFolder(pathName):
    try:
        os.mkdir(pathName)
    except OSError:
        print ("Creation of the directory  failed")
        return False
    else:
        print ("Successfully created the directory ")
        return True

def createJSX(full_path ,name):
    COMPONENT_DEFAULT_CODE = """import React from 'react';

export const """ + name.capitalize() + """ = () => {
    return(
        <div>Hello world</div>
    );
}""" 

    file = open(full_path + "/" + name +".component.jsx","w")
    file.write(COMPONENT_DEFAULT_CODE)
    file.close()

def createComp():
    name = input("Qual o nome do novo componente?")
    full_path = BASE_PATH + name

    if(createFolder(full_path)):
        createJSX(full_path, name)
        print("Component successfully created")
    else:
        print("Fail")

createComp()

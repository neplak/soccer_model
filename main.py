# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import easygui as eg
from dataclasses import dataclass,field
from anytree import AnyNode,NodeMixin, RenderTree,PreOrderIter, PostOrderIter
from anytree.exporter import JsonExporter
import ref
import json


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    eg.msgbox(f'Hi, {name}',title='UUUUu',ok_button='AGA')  # Press Ctrl+F8 to toggle the breakpoint.
def test2():
    with open("data/rifleman_squad.json") as fp:
        q=json.load(fp)

    root=ref.NodeUnit('squad',11,**q)
    print(root)

def test1():
    squads=[]
    root=ref.NodeUnit('infantry batalion',1,men=4,rifle=2,smg=1,handgun=2)
    commands=[ref.NodeUnit('infantry command',i,parent=root,men=8,rifle=6,handgun=2) for i in range(1,4)]
    for command in commands:
        squads+=[ref.NodeUnit('infantry platoon',i,parent=command,men=47,lmg=4,rifle=35,smg=8) for i in range(1,4)]
    squads.append(ref.NodeUnit('communications platoon ',1,parent=root,men=34,smg=1,rifle=33))
    print(RenderTree(root))
    print(root.descendants)
    for node in  squads:
        print(node)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    test1()
    test2()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/


from dataclasses import dataclass,field
import random as rnd
from anytree import AnyNode,NodeMixin, RenderTree,PreOrderIter, PostOrderIter
from anytree.exporter import JsonExporter

class BaseUnit:
    def __init__(self,unitType,number,**kwargs):
        self.unitType=unitType
        self.number=number
        self.directStaff={}
        self.directStaff.update(kwargs)
    @property
    def name(self):
        return f'{self.number} {self.unitType}'

    def __repr__(self):
        return self.name

class NodeUnit(BaseUnit,NodeMixin):
    def __init__(self,unitType,number,parent=None,children=None,**kwargs):
        super(NodeUnit,self).__init__(unitType,number,**kwargs)
        self.parent=parent
        if children:
            self.children=children

    @property
    def fullName(self):
        if not self.parent:
            return self.name
        return self.name+' '+self.parent.fullName

    def __str__(self):
        return f'{self.fullName} \n {self.directStaff}'


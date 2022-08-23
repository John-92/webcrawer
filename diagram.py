# -*- coding=utf-8 -*-
# @Time: 2022/8/21 15:01
# @Author: John
# @File: diagram.py
# @Software: PyCharm
from xml.etree import ElementTree as ET
import csv


class Node():
  def __init__(self,id,startpoint):
    self.id = id
    self.startpoint=startpoint
    self.name = self.id + "_di"
    self.width = 0
    self.height = 0
    self.startpoint_x, self.startpoint_y = self.startpoint
    self.endpoint = (int(self.startpoint_x + self.width / 2), int(self.startpoint_y + self.height))
    self.width = 54
    self.height = 100


class sequenceFlow(Node):
  #流水线类，用于时间之间的连接
  def __init__(self,id,startpoint):
    super(sequenceFlow, self).__init__(id,startpoint)
    self.width = 54
    # self.startpoint = (236, 168)

  def process_xml(self,root,sourceRef,targetRef):
    attrib={}
    attrib["id"]=self.id
    attrib["name"]=self.name
    attrib["sourceRef"]=sourceRef
    attrib["targetRef"]=targetRef
    lastmod = ET.SubElement(root, "sequenceFlow", attrib=attrib)
    # print(lastmod)
    return lastmod

class Activity(Node):
  #特殊的活动类
  def __init__(self,id,startpoint):
    super(Activity, self).__init__(id,startpoint)
    self.width =100
    self.height=80

  def process_xml(self,root,incoming,outgoing):
    attrib={}
    attrib["id"]=self.id
    attrib["name"]=self.name
    lastmod = ET.SubElement(root, "task", attrib=attrib)
    innode=ET.SubElement(lastmod, "incoming")
    innode.text=incoming
    newnode=ET.SubElement(lastmod, "outgoing")
    newnode.text=outgoing
    # print(lastmod)
    return newnode

class task(Node):
  #起止节点类
  def __init__(self,id,startpoint):
    super(task, self).__init__(id,startpoint)
    self.width = 36
    self.height = 36

class startNode(task):
  #起始节点
  def __init__(self,id,startpoint):
    super(startNode, self).__init__(id,startpoint)
    self.id="StartEvent_1"
    self.startpoint=(190,136)

  def process_xml(self,root,outgoing):
    attrib={}
    attrib["id"]=self.id
    attrib["name"]=self.name
    attrib["outgoing"]=outgoing
    lastmod = ET.SubElement(root, "startEvent", attrib=attrib)
    return lastmod

class endNode(task):
    # 终止节点
    def __init__(self, id, startpoint):
      super(endNode, self).__init__( id, startpoint)
      self.id = "endEvent_1"
      self.startpoint = (190, 136)

    def process_xml(self, root, incoming):
      attrib = {}
      attrib["id"] = self.id
      lastmod = ET.SubElement(root, "endEvent", attrib=attrib)
      # print(lastmod)
      return lastmod

class Csv_to_dict():
  def __init__(self):
    self.csv_list = []


  def get_csv(self, filename,pipeline):
    with open(filename) as f:
      for row in csv.DictReader(f, skipinitialspace=True):
        if row["process-id"] == pipeline:
          self.csv_list.append(row)


class xmlhandle():
  def __init__(self):
    definition_attr = {}
    definition_attr["xmlns"] = "http://hhhhhh"
    definition_attr["xmlns:xsi"] = "http://hhhhkkkkk"
    definition_attr["xmlns:omgdi"] = "http://ffff"
    definition_attr["xmlns:omgdc"] = "http://hhhhkkffkkk"
    definition_attr["xmlns:flowable"] = "http://fffff"
    definition = ET.Element("definition", attrib=definition_attr)
    self.rootElement = definition
    tree1 = ET.ElementTree(self.rootElement)
    tree1.write("test.xml")

  def inert_node(self,pre_node, node,incoming,outgoing):
    node.process_xml(pre_node,incoming,outgoing)
    tree1 = ET.ElementTree(self.rootElement)
    tree1.write("test.xml")
    ET.dump(tree1)
    return node
    # node = ET.SubElement(pre_node, id, tag="yyy", attrib={"1": "8"})

  def csv_to_xml(self,process_id):
    csvhandle=Csv_to_dict()
    csvhandle.get_csv("test1.csv","aaaa-test")
    csv_lists=csvhandle.csv_list
    process_attr = {}
    process_attr["id"] = process_id
    process = ET.SubElement(self.rootElement, "process", attrib=process_attr)
    BPMNDiagram_attr = {}
    BPMNDiagram_attr["id"] = "hhhh"
    ET.SubElement(self.rootElement, "bpmndi:BPMNDiagram-id", attrib=BPMNDiagram_attr)
    tree1 = ET.ElementTree(self.rootElement)
    tree1.write("test.xml")
    for csv_dict in csv_lists:
      print(csv_dict['event-id'])
      if csv_dict['event-id'].startswith("StartEvent"):
        startnode = startNode(csv_dict['event-id'], (136, 136))
        startnode.process_xml(process,  csv_dict['outgoing'])
      elif csv_dict['event-id'].startswith("process"):
        startnode = startNode(csv_dict['event-id'], (136, 136))
        startnode.process_xml(process,  csv_dict['outgoing'])
      elif csv_dict['event-id'].startswith("Flow"):
        l1 = sequenceFlow(csv_dict['event-id'], (136, 136))
        l1.process_xml( process, csv_dict['incoming'], csv_dict['outgoing'])
      elif csv_dict['event-id'].startswith("Activity"):
        act=Activity(csv_dict['event-id'], (136, 136))
        act.process_xml(process, csv_dict['incoming'], csv_dict['outgoing'])
      elif csv_dict['event-id'].startswith("event"):
        endnode = endNode(csv_dict['event-id'], (136, 136))
        endnode.process_xml(process,  csv_dict['incoming'])

    tree1 = ET.ElementTree(self.rootElement)
    tree1.write("test.xml")
    ET.dump(tree1)
    # return node


if __name__ == '__main__':

  xmltest=xmlhandle()
  xmltest.csv_to_xml("oooooooooooooooooo")







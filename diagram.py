# -*- coding=utf-8 -*-
# @Time: 2022/8/21 15:01
# @Author: John
# @File: diagram.py
# @Software: PyCharm
from xml.etree import ElementTree as ET
import csv
def build_sitemap():
  urlset = ET.Element("urlset")  #设置一个根节点，标签为urlset
  url = ET.SubElement(urlset,"url")  #在根节点urlset下建立子节点
  loc = ET.SubElement(url,"loc")
  loc.text = "http://www/baidu.com"
  lastmod = ET.SubElement(url,"lastmod", attrib={"checked": "no"})
  lastmod.text = "2017-10-10"
  changefreq = ET.SubElement(url,"changefreq")
  changefreq.text = "daily"
  priority = ET.SubElement(url,"priority")
  priority.text = "1.0"
  tree = ET.ElementTree(urlset)
  tree.write("sitemap.xml")


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
    print(lastmod)




class diagramShape(Node):
  def __init__(self,id,startpoint):
    super(diagramShape, self).__init__(id,startpoint)
    self.width =100
    self.height=80


class task(Node):
  def __init__(self,id,startpoint):
    super(task, self).__init__(id,startpoint)

    self.width = 36
    self.height = 36




class startNode(task):
  def __init__(self,id,startpoint):
    super(startNode, self).__init__(id,startpoint)
    self.id="StartEvent_1"
    self.startpoint=(190,136)

  def start_xml(self,root,outgoing):
    attrib={}
    attrib["id"]=self.id
    attrib["name"]=self.name
    lastmod = ET.SubElement(root, "startEvent", attrib=attrib)
    print(lastmod)



class HandleCsv():
  csv_list = []

  def __init__(self, filename):
    self.filename = filename
    with open(self.filename) as fp:
      self.csv_list = list(csv.reader(fp))
      print(self.csv_list)


class xmlhandle():
  def __init__(self,rootElement):
    self.rootElement=rootElement


  def init_xml(self,startNode,flow_id):
    process_attr = {}
    process_attr["id"]="uu"
    process_attr["name"]="uu"
    process = ET.Element("process", attrib=process_attr)
    diagram=startNode.start_xml(process,flow_id)
    # ET.SubElement(process, flow_id)
    tree1 = ET.ElementTree(process)
    tree1.write("test.xml")

  def inert_node(self):
    pass




if __name__ == '__main__':
  # start=task("start_",(100,136))
  # l1=sequenceFlow("ii",(136,136))
  # b=diagramShape("test",(290,136))
  # l2= sequenceFlow("ii", (390, 136))
  # end=task("start_",(450,136))
  # c=HandleCsv("test1.csv")
  #
  # print(c.csv_list[1][0])
  # process_attr={}
  # process_attr["id"]="uu"
  # process_attr["name"]="uu"
  # urlset = ET.Element("process",attrib=process_attr)
  # diagram = ET.Element("bpmndi:BPMNDiagram")
  # l1 = sequenceFlow("ii", (136, 136))
  #
  # l1.process_xml(urlset,"yy","bb")
  # l1.process_xml(diagram, "yyuuu", "bb")
  # tree1 = ET.ElementTree(urlset)
  # print(tree1)
  # # tree2 = ET.ElementTree(diagram)
  # tree1.write("test.xml")
  # tree2.write("test.xml")
  process_attr = {}
  process_attr["id"] = "uu"
  process_attr["name"] = "uu"
  process = ET.Element("process", attrib=process_attr)

  xmltest=xmlhandle(process)
  start_node=startNode("1",(1,2))
  # start_node.start_xml()
  flow_id="flow_test"
  xmltest.init_xml(start_node,flow_id)
  l1 = sequenceFlow("ii", (136, 136))






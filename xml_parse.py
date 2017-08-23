# -*- coding: utf-8 -*-
from xml.etree import ElementTree as ET
import os

#tree = ET.parse("2-s2.0-34848815009.xml")
unique_id = 1

def walk_data(root_node, level, result_list):
    '''遍历节点 '''
    global unique_id #全句变量
    temp = [unique_id, level, root_node.tag, root_node.attrib]
    result_list.append(temp)
    unique_id += 1
	
    children_node = root_node.getchildren()  #遍历子节点
    if len(children_node) == 0:
	    return
    
    for child in children_node:
        walk_data(child, level+1, result_list)
    return

def getXmlData(file_path):
    ''' '''
    level = 1
    result_list = []
    root = ET.parse(file_path).getroot()
    walk_data(root, level, result_list)
    return result_list
	
if __name__ == "__main__":
    for dirpath, dirnames, filenames in os.walk(os.getcwd()):
        file_path = os.path.join(dirpath, filenames[0]) #xml文件路径
        print file_path
        text_file_name = filenames[0].replace("xml", "text")
        if not file_path.endswith(".xml"):
            continue
        ret = getXmlData(file_path)
        new_list = []
        for i in ret:
            node_level = str(i[1]) + " " + i[2]
            new_list.append(node_level)
        print(len(new_list))
        list1 = list(set(new_list)) #去重，节点名和深度
        print(len(list1))
        sorted(list1)

        with open(text_file_name, "w+") as s:
            for i in list1:
                s.write(i)
                s.write("\n")
    
    
            


    
        
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, argparse
from datetime import datetime,date
import random, json
import os


class Task():
    
    def __init__(self, name="", priority=1, due_date =""):
        self.created = date.today().strftime("%m/%d/%Y")
        self.name = name
        self.priority = priority
        self.dueDate = due_date
        self.uniqueId = random.randint(1, 10000000)
        self.completed = ""
        

class Tasks():
    def __init__(self):
        self.tasks=[]
        self.filename="pickle"
    
    def add(self):
        with open (self.filename, 'w') as myfile:
            for t in self.tasks:
                myfile.write(json.dumps({t.uniqueId:{'created':t.created, 'task':t.name, 'priority':t.priority, 'dueDate': t.dueDate, 'completed': ""}}))
    
    def listed(self):
        print("{:<10} {:<10} {:<10} {:<10} {:<10}".format('ID', 'AGE', 'Due Date', 'Priority', 'Task'))
        with open(self.filename, 'r') as myfile:
            d = myfile.read()
            js = json.loads(d)
            for k,v in js.items():
               print("{:<10} {:<10} {:<10} {:<10} {:<10}".format(k,"0", v['dueDate'], v['priority'], v['task']))
               
    def report(self):
        print("{:<10} {:<10} {:<10} {:<10} {:<10}".format('ID', 'AGE', 'Due Date', 'Priority', 'Task'))
        with open(self.filename, 'r') as myfile:
            d = myfile.read()
            js = json.loads(d)
            for k,v in js.items():
               print("{:<10} {:<10} {:<10} {:<10} {:<10}".format(k,"0", v['dueDate'], v['priority'], v['task']))

    def done(self, id):
        with open(self.filename, 'r+') as myfile:
            d = myfile.read()
            js = json.loads(d)
        os.remove(self.filename)
        with open (self.filename, 'w') as myfile:
            js[id]['completed']= date.today().strftime("%m/%d/%Y")
            myfile.write(json.dumps(js))
            
                
        
        
    
def main(args):
    ts = Tasks()
    parse = argparse.ArgumentParser("add args to func")
    
    parse.add_argument('--add', type=str)
    parse.add_argument('--due', type=str)
    parse.add_argument('--priority', type=int)
    parse.add_argument('--report', action='store_true')
    parse.add_argument('--list', action='store_true')
    parse.add_argument('--h', action='store_true')
    parse.add_argument('--done', type=str)
    
    args = vars(parse.parse_args())
    print(args)
    if args['add'] is not None:
        t=Task(name=args['add'], due_date=args['due'], priority = args['priority'])
        ts.tasks.append(t)
        ts.add()
    
    if args['done'] is not None:
        ts.done(args['done'])
    if args['list'] is True:
        ts.listed()
    if args['report'] is True:
        ts.listed()
    

    


    

if __name__ == "__main__":
    main(sys.argv[1:])
    
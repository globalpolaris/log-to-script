import sys
import csv

fields = ['rulesID', 'srcintf', 'dstintf', 'srcaddr', 'dstaddr', 'action', 'schedule', 'service', 'logtraffic', 'comments']
words = ['edit', 'srcintf', 'dstintf', 'srcaddr', 'dstaddr', 'action', 'schedule', 'service', 'logtraffic', 'comments']

def reset_dict():
    result = {
        'rulesID' : '',
        'srcintf' : '',
        'dstintf' : '',
        'srcaddr' : '',
        'dstaddr' : '',
        'action' : '',
        'schedule' : '',
        'service': '',
        'logtraffic' : '',
        'comments' : ''
    }
    return result

def create_csv(filename):
    src = ""
    res = reset_dict()
    with open('FWCORE Policy.log') as log:
        with open('output.csv', 'w') as csv_file:
            w = csv.DictWriter(csv_file, lineterminator='\n', delimiter=';', fieldnames=fields)
            # w.writerow(dict((f,f) for f in fields))
            w.writeheader()
            res = reset_dict()
            for l in log:
                if "next" in l:
                        w.writerow(res)
                        res = reset_dict()
                for i in words:
                    if i in l:
                        if "edit" in l:
                            src = l.split(' ')[5].strip('\n')
                            res['rulesID'] = src
                            # print(res)
                        if "srcintf" in l:
                            src = l.split(' ')[10:]
                            
                            src = [i.strip('"') for i in src]
                            src[-1] = src[-1].strip('\n')
                            src[-1] = src[-1].strip('"')
                            res['srcintf'] = ",".join(src)
                        if "dstintf" in l:
                            src = l.split(' ')[10:]
                            
                            src = [i.strip('"') for i in src]
                            src[-1] = src[-1].strip('\n')
                            src[-1] = src[-1].strip('"')
                            res['dstintf'] = ",".join(src)
                        if "srcaddr" in l:
                            src = l.split(' ')[10:]
                            
                            src = [i.strip('"') for i in src]
                            src[-1] = src[-1].strip('\n')
                            src[-1] = src[-1].strip('"')
                            res['srcaddr'] = ",".join(src)
                        if "dstaddr" in l:
                            src = l.split(' ')[10:]
                            
                            src = [i.strip('"') for i in src]
                            src[-1] = src[-1].strip('\n')
                            src[-1] = src[-1].strip('"')
                            res['dstaddr'] = ",".join(src)
                        if "action" in l:
                            src = l.split(' ')[10].strip('\n').strip('"')
                            res['action'] = src
                        if "schedule" in l:
                            src = l.split(' ')[10].strip('\n').strip('"')
                            res['schedule'] = src
                        if "service" in l:
                            src = l.split(' ')[10:]
                            
                            src = [i.strip('"') for i in src]
                            src[-1] = src[-1].strip('\n')
                            src[-1] = src[-1].strip('"')
                            res['service'] = ",".join(src)
                        if "logtraffic" in l:
                            src = l.split(' ')[10].strip('\n').strip('"')
                            res['logtraffic'] = src

                        if "comments" in l:
                            src = l.split(' ')[10:]
                            
                            src = [i.strip('"') for i in src]
                            src[-1] = src[-1].strip('\n')
                            src[-1] = src[-1].strip('"')
                            res['comments'] = " ".join(src)

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("Usage: log_to_csv.py logfile")
        sys.exit()
    filename = sys.argv[1]
    create_csv(filename)
#! /usr/bin/python
# python3 -m pip install scapy
# python3 -m pip install ipaddr
 
from scapy.all import *
from sys import argv
from ipaddr import IPv4Network
from time import sleep
from threading import Thread, RLock


def SynScanThread(dstIP, firstPort, lastPort, timeLen, scan_res, myLock):
    if (timeLen == 0):
        ans, unans = sr(IP(dst=dstIP)/TCP(sport=RandShort(), dport=(firstPort, lastPort), flags="S"), retry=0, timeout=1, verbose=False)  
        for snd, rcv in ans:
            with myLock:
                if (scan_res.get(snd[IP].dst) == None):
                    scan_res[snd[IP].dst] = dict()
                if(rcv[TCP].flags == 0x12):
                    sr(IP(dst=snd[IP].dst)/TCP(sport=RandShort(), dport=snd[TCP].dport, flags="R"), timeout=1, verbose=False)
                    scan_res[snd[IP].dst][snd[TCP].dport] = "Open"
                elif (rcv[TCP].flags == 0x14):
                    scan_res[snd[IP].dst][snd[TCP].dport] = "Closed"        
    else:
        for p in range(firstPort, lastPort+1):
            ans, unans = sr(IP(dst=dstIP)/TCP(sport=RandShort(), dport=p, flags="S"), retry=0, timeout=1, verbose=False)   
            for snd, rcv in ans:
                with myLock:
                    if (scan_res.get(snd[IP].dst) == None):
                        scan_res[snd[IP].dst] = dict()
                    if (rcv[TCP].flags == 0x12):
                        sr(IP(dst=snd[IP].dst)/TCP(sport=RandShort(), dport=snd[TCP].dport, flags="R"), timeout=1, verbose=False)
                        scan_res[snd[IP].dst][snd[TCP].dport] = "Open"
                    elif (rcv[TCP].flags == 0x14):
                        scan_res[snd[IP].dst][snd[TCP].dport] = "Closed"
            sleep(timeLen)


def SynScan(dstIP, firstPort, lastPort, timeLen, threadCount):
    scan_res = dict()
    myLock = RLock()

    ans, unans = sr(IP(dst=dstIP)/ICMP(), retry=0, timeout=1, verbose=False)
    for snd, rcv in ans:
        scan_res[snd[IP].dst] = dict()
    
    t = list()
    f = firstPort
    portAdder = (lastPort - firstPort + 1) // threadCount
    for i in range(threadCount):
        if (i == threadCount - 1):
            l = lastPort
        else:
            l = f + portAdder - 1 
        t.append(Thread(target=SynScanThread, args=(dstIP, f, l, timeLen, scan_res, myLock,)))
        t[-1].start()
        f = l + 1
    for tr in t:
        tr.join()

    for curIP in scan_res.keys():
        for p in range(firstPort, lastPort+1):
            if (scan_res[curIP].get(p) == None):
                scan_res[curIP][p] = "Filtered"
    
    return scan_res


def FinScanThread(dstIP, firstPort, lastPort, timeLen, scan_res, myLock):
    if (timeLen == 0):
        ans, unans = sr(IP(dst=dstIP)/TCP(sport=RandShort(), dport=(firstPort, lastPort), flags="F"), retry=0, timeout=1, verbose=False)  
        for snd, rcv in ans:
            with myLock:
                if (scan_res.get(snd[IP].dst) == None):
                    scan_res[snd[IP].dst] = dict()
                if (rcv[TCP].flags == 0x14):
                    scan_res[snd[IP].dst][snd[TCP].dport] = "Closed"        
    else:
        for p in range(firstPort, lastPort+1):
            ans, unans = sr(IP(dst=dstIP)/TCP(sport=RandShort(), dport=p, flags="F"), retry=0, timeout=1, verbose=False)   
            for snd, rcv in ans:
                with myLock:
                    if (scan_res.get(snd[IP].dst) == None):
                        scan_res[snd[IP].dst] = dict()
                    if (rcv[TCP].flags == 0x14):
                        scan_res[snd[IP].dst][snd[TCP].dport] = "Closed"
            sleep(timeLen)


def FinScan(dstIP, firstPort, lastPort, timeLen, threadCount):
    scan_res = dict()
    myLock = RLock()

    ans, unans = sr(IP(dst=dstIP)/ICMP(), retry=0, timeout=1, verbose=False)
    for snd, rcv in ans:
        scan_res[snd[IP].dst] = dict()

    t = list()
    f = firstPort
    portAdder = (lastPort - firstPort + 1) // threadCount
    for i in range(threadCount):
        if (i == threadCount - 1):
            l = lastPort
        else:
            l = f + portAdder - 1 
        t.append(Thread(target=FinScanThread, args=(dstIP, f, l, timeLen, scan_res, myLock,)))
        t[-1].start()
        f = l + 1
    for tr in t:
        tr.join()

    for curIP in scan_res.keys():
        for p in range(firstPort, lastPort+1):
            if (scan_res[curIP].get(p) == None):
                scan_res[curIP][p] = "Open|Filtered"

    return scan_res


def AckScanThread(dstIP, firstPort, lastPort, timeLen, scan_res, myLock):
    if (timeLen == 0):
        ans, unans = sr(IP(dst=dstIP)/TCP(sport=RandShort(), dport=(firstPort, lastPort), flags="A"), retry=0, timeout=1, verbose=False)  
        for snd, rcv in ans:
            with myLock:
                if (scan_res.get(snd[IP].dst) == None):
                    scan_res[snd[IP].dst] = dict()
                scan_res[snd[IP].dst][snd[TCP].dport] = "Unfiltered"        
    else:
        for p in range(firstPort, lastPort+1):
            ans, unans = sr(IP(dst=dstIP)/TCP(sport=RandShort(), dport=p, flags="A"), retry=0, timeout=1, verbose=False)   
            for snd, rcv in ans:
                with myLock:
                    if (scan_res.get(snd[IP].dst) == None):
                        scan_res[snd[IP].dst] = dict()
                    scan_res[snd[IP].dst][snd[TCP].dport] = "Unfiltered"
            sleep(timeLen)


def AckScan(dstIP, firstPort, lastPort, timeLen, threadCount):
    scan_res = dict()
    myLock = RLock()

    ans, unans = sr(IP(dst=dstIP)/ICMP(), retry=0, timeout=1, verbose=False)
    for snd, rcv in ans:
        scan_res[snd[IP].dst] = dict()

    t = list()
    f = firstPort
    portAdder = (lastPort - firstPort + 1) // threadCount
    for i in range(threadCount):
        if (i == threadCount - 1):
            l = lastPort
        else:
            l = f + portAdder - 1 
        t.append(Thread(target=AckScanThread, args=(dstIP, f, l, timeLen, scan_res, myLock,)))
        t[-1].start()
        f = l + 1
    for tr in t:
        tr.join()

    for curIP in scan_res.keys():
        for p in range(firstPort, lastPort+1):
            if (scan_res[curIP].get(p) == None):
                scan_res[curIP][p] = "Filtered"

    return scan_res


funcs = dict(SYN=SynScan, FIN=FinScan, ACK=AckScan)
if (len(argv) == 1):
    print("No arguments passed")
    print("Use scanner.py -h for help")
elif (argv[1] == "-h"):
    print("Port scanner usage: scanner.py [-thr threads] [-m mode] [-p ports] [-t time] IP")
    print("threads - number of threads in scanning; threads diapason 1-4; default = 1")
    print("mode - SYN, FIN or ACK scan; default = SYN")
    print("ports - single port (80) or ports range (53-80); ports diapason 0-65535; default = 0-1023")
    print("time - timeout (in seconds) between sendings; default = 0")
    print("IP - single IP (8.8.8.8) or IPs range (192.168.1.0/24)")
else:
    scanFunc = SynScan
    mode = "SYN"
    firstPort = 0
    lastPort = 1023
    timeLen = 0
    threadCount = 1
    for i in range(1, len(argv)):
        if (argv[i] == "-thr"):
            if (argv[i+1].isdigit() == True):
                if (int(argv[i+1]) >=1 and int(argv[i+1]) <= 4):
                    threadCount = int(argv[i+1])
                else:
                    print("Wrong parameter \"" + argv[i+1] + "\" for threads")
                    exit()
            else:
                print("Wrong parameter \"" + argv[i+1] + "\" for threads")
                exit()
        if (argv[i] == "-m"):
            if (argv[i+1] in funcs.keys()):
                scanFunc = funcs[argv[i+1]]
                mode = argv[i+1]
            else:
                print("Wrong parameter \"" + argv[i+1] + "\" for mode")
                exit()
        if (argv[i] == "-p"):
            if (argv[i+1].find("-") > 0):
                f, l = argv[i+1].split("-", 1)
                if (f.isdigit() == True and l.isdigit() == True):
                    if (int(f) <= 65535 and int(l) <= 65535 and int(f) <= int(l)):
                        firstPort = int(f)
                        lastPort = int(l)
                    else:
                        print("Wrong parameter \"" + argv[i+1] + "\" for ports")
                        exit()
                else:
                    print("Wrong parameter \"" + argv[i+1] + "\" for ports")
                    exit()
            elif (argv[i+1].isdigit() == True):
                if (int(argv[i+1]) <= 65535):
                    firstPort = int(argv[i+1])
                    lastPort = int(argv[i+1])
                else:
                    print("Wrong parameter \"" + argv[i+1] + "\" for ports")
                    exit()
            else:
                print("Wrong parameter \"" + argv[i+1] + "\" for ports")
                exit()
        if (argv[i] == "-t"):
            if (argv[i+1].isdigit() == True):
                timeLen = int(argv[i+1])
            else:
                print("Wrong parameter \"" + argv[i+1] + "\" for time")
                exit()
    try:
        try_ip = IPv4Network(argv[-1])
        dstIP = argv[-1]
    except ValueError:
        print("Wrong parameter \"" + argv[-1] + "\" for IP")
        exit()
    print(mode, "scanning", dstIP, "with port range", str(firstPort) + "-" + str(lastPort), "and timeout", timeLen, "with", threadCount, "thread(s)")
    print()
    res = scanFunc(dstIP, firstPort, lastPort, timeLen, threadCount)
    for ip in res.keys():
        print("Scan results for ip:", ip)
        for port in sorted(res[ip].keys()):
            print(port, "->", res[ip][port])
        print()
    print("Other hosts seems down")     

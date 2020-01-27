#!/usr/bin/env python3

import os
import time
import subprocess

routers={"r00":"10.251.251.100","r01":"10.251.251.101","r02":"10.251.251.102",
"r05":"10.251.251.105","r06":"10.251.251.106","r71":"","r72":""}

for router in routers:
        ip =routers[router]
        print("\n[Starting] router ", router)
        if router == "r71":
                os.system("sudo virsh start r71")
                time.sleep(60)
                print("[Starting] router r72")
                os.system("sudo virsh start r72")
                break
        response = -1
        os.system("sudo virsh start " + router)
        while response !=0:
                print(".",  end=" ", flush=True)
                response = os.system("ping -c 1 "+ ip + " > /dev/null 2>&1")
                time.sleep(20)

print("\nThat's it!\n")
print(subprocess.check_output(["sudo","virsh","list"]).decode())

# log-to-script

This script is used to convert log files to csv

### Usage:  
> python log-to-script.py logfile

Example:
> python log-to-script.py Log-10-10-2022.log

### Output:
Currently, output will be saved in directory where the script is located, named as **output.csv**.

If you are converting more than one log file, please rename the previous output as it will get overwritten

#### Compatible log example:
```
sh firewall policy
config firewall policy
    edit 420
        set uuid aaaaaa-aaaaa-aaaaaa-aaaaaaaa
        set srcintf "any"
        set dstintf "any"
        set srcaddr "all"
        set dstaddr "all"
        set schedule "always"
        set service "ALL"
        set logtraffic all
    next
    edit 1082
        set uuid bbbbbb-aaaabbbbba-aabbbaaaa-aaaaabbaaa
        set srcintf "any"
        set dstintf "any"
        set srcaddr "Host_123.123.123"
        set dstaddr "all"
        set action accept
        set schedule "always"
        set service "ssh"
        set logtraffic all
        set comments "Comments"
    next
end```

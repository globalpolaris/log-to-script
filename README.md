# log-to-script

This script is used to convert log files to csv

Compatible log example:
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
end

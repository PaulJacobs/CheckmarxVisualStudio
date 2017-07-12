import os
import xml.etree.ElementTree
from collections import Counter

runScan = 0

l= []

if runScan == 1:
    print("Scan")
    os.system('C:\\CxConsolePlugin-7.5.0-20160719-1414\\runCxConsole.cmd scan -v -CxServer https://cxprivatecloud.checkmarx.net ' \
          '-ProjectName "CxServer\SP\America\Rob-Sandbox\PaulCLI" -CxUser paul.r.jacobs@gmail.com -CxPassword "MADiba2778^^" ' \
          '-locationtype folder -locationpath "C:\Users\paul.jacobs\workspace\Checkmarx" ' \
          '-ReportXML "c:\\temp\\results.xml"'
          )

e = xml.etree.ElementTree.parse('c:\\temp\\results.xml').getroot()

for child in e:
     print(child.get("name"))
     print(child.get("Severity"))
     l.append(child.get("Severity"))

c = Counter(l)

print c

for  t in c:
    print (t,c[t])

print("Done")



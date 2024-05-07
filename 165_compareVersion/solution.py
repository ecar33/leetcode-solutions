def compareVersion(version1: str, version2: str) -> int:  
    # Turn version 1 and version 2 into arrays with leading 0's removed
    version1 =  [int(x) for x in version1.split(".")]
    version2 =  [int(x) for x in version2.split(".")]
    

        
    for i in range(0, max(len(version1), len(version2))):
        v1 = version1[i] if i < len(version1) else 0
        v2 = version2[i] if i < len(version2) else 0
        if v1 > v2:
            return 1
        elif v2 > v1:
            return -1
    return 0
    
    
    
version1 = "1.0.0.0.5"
version2 = "1.2.3.4"

print(compareVersion(version1, version2))
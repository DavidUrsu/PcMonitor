import json
import psutil
import platform
import cpuinfo
import GPUtil


def getSoftware():
    functionList = {}
    functionList["platform"] = platform.system()
    functionList["userName"] = platform.node()
    return functionList


def getProccesor():
    functionList = {}
    functionList["name"] = cpuinfo.get_cpu_info()["brand_raw"]
    functionList["frequency"] = psutil.cpu_freq()[0]
    functionList["proccent"] = psutil.cpu_percent()
    return functionList


def getGPU():
    functionList = {}
    myGpus = GPUtil.getGPUs()
    gpuNumber = 0
    gpuList = {}
    for gpu in myGpus:
        gpuList["id"] = gpu.id
        gpuList["name"] = gpu.name
        gpuList["load"] = gpu.load*100
        gpuList["usedMemory"] = gpu.memoryUsed
        gpuList["totalMemory"] = gpu.memoryTotal
        gpuList["temperature"] = gpu.temperature
        functionList[gpuNumber] = gpuList
        gpuNumber = gpuNumber+1
    return functionList


if __name__ == '__main__':
    with open('data.json', 'w') as jsonFile:
        informationList = {}
        informationList["software"] = getSoftware()
        informationList["proccesor"] = getProccesor()
        informationList["gpu"] = getGPU()
        informationList = json.dumps(informationList, indent=4)
        print(informationList)

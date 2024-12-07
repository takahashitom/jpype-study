import jpype
import jpype.imports

jpype.startJVM(classpath=["./java-production/"])

class Jpype:
    def __init__(self):
        pass

    def hello(self):
        helloWorld = jpype.JClass('com.dir_1.Hello')
        args = jpype.JArray(jpype.JString)(["arg1", "arg2"])
        helloWorld.main(args)

    def goodMorning(self, send):
        GoodMorning = jpype.JClass("com.dir_2.GoodMorning")
        sendInstance = GoodMorning(send)
        result = sendInstance.sendMorning()
        return result

if __name__ == "__main__":
    pype = Jpype()
    pype.hello()
    result = pype.goodMorning("World")
    print(result)

jpype.shutdownJVM()
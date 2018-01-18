from stack import YowsupSendStack

credentials = ("554196805910","CRR1t/LTW3WifveO/lb4uohQUyQ=")
messages = [("554199205589","ola tudo bem")]

whats_app = YowsupSendStack(credentials,messages,True)

whats_app.start()
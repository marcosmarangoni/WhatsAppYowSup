from stack import YowsupEchoStack

credentials = ("554196805910","CRR1t/LTW3WifveO/lb4uohQUyQ=")
messages = [("554199205589","Testando mais uma vez YowSup")]

whats_app = YowsupEchoStack(credentials,True)

whats_app.start()
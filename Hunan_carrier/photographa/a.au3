ControlFocus("�ļ��ϴ�", "","Edit1")
WinWait("[CLASS:#32770]","",10)
ControlSetText("�ļ��ϴ�", "", "Edit1", $CmdLine[1])
Sleep(2000)
ControlClick("�ļ��ϴ�", "","Button1");
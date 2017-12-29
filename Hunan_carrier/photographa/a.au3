ControlFocus("文件上传", "","Edit1")
WinWait("[CLASS:#32770]","",10)
ControlSetText("文件上传", "", "Edit1", $CmdLine[1])
Sleep(2000)
ControlClick("文件上传", "","Button1");
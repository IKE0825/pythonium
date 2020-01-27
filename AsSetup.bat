rem 変数初期化
set ORIGINEXECUTIONPOLICY=RemoteSigned
set TARGETEXECUTIONPOLICY=unrestricted

REM set target execution policy
powershell -Command Set-ExecutionPolicy %TARGETEXECUTIONPOLICY%
powershell -Command Get-ExecutionPolicy

echo 'AS400エミュレータの設定'
set ASCOPY=\\des-plt-svr\setup\PCsetup\src\Copy_AS.ps1
powershell -File %ASCOPY%
set JAVAEXE=C:\Java\JavaSetup8u191.exe
set CONFIG=C:\Java\install.cfg
call %JAVAEXE% INSTALLCFG=%CONFIG% 
start C:\ACS\ACS端末.lnk
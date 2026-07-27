#define Publisher "DeepThoughtt"
#define AppName "PyProGen"

[Setup]
AppName={#AppName}
AppVersion=0.2.0
AppVerName={#AppName}
AppPublisher={#Publisher}
DefaultDirName={pf}\{#AppName}
UninstallDisplayIcon={app}\ppg.exe
DefaultGroupName={#AppName}
LanguageDetectionMethod=locale

OutputDir=output
OutputBaseFilename=PyProGen-Windows-Installer
SetupIconFile=..\assets\icons\pyprogen.ico
Compression=lzma
SolidCompression=yes
ArchitecturesInstallIn64BitMode=x64

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"
Name: "italian"; MessagesFile: "compiler:Languages\Italian.isl"

[Files]
Source: "..\dist\ppg.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\PyProGen"; Filename: "{app}\ppg.exe"

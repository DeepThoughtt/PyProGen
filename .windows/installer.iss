#define Publisher "DeepThoughtt"
#define AppName "PyProGen"

[Setup]
AppName={#AppName}
AppVersion=1.0.2
AppVerName={#AppName}
AppPublisher={#Publisher}
DefaultDirName={commonpf}\{#AppName}
UninstallDisplayIcon={app}\ppg.exe
DefaultGroupName={#AppName}
LanguageDetectionMethod=locale

OutputDir=output
OutputBaseFilename=PyProGen-Windows-Installer
SetupIconFile=..\assets\icons\pyprogen.ico
LicenseFile=..\LICENSE
Compression=lzma
SolidCompression=yes
ArchitecturesInstallIn64BitMode=x64compatible

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"
Name: "italian"; MessagesFile: "compiler:Languages\Italian.isl"

[Files]
Source: "..\dist\PyProGen\*"; DestDir: "{app}"; Flags: recursesubdirs

[Icons]
Name: "{group}\PyProGen"; Filename: "{app}\ppg.exe"

[UninstallDelete]
Type: filesandordirs; Name: "{app}"

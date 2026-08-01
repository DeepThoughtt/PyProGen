#define Publisher "$publisher"
#define AppName "$app_name"

[Setup]
AppName={#AppName}
AppVersion=0.1.0
AppVerName={#AppName}
AppPublisher={#Publisher}
DefaultDirName={commonpf}\{#AppName}
UninstallDisplayIcon={app}\$app_name.exe
DefaultGroupName={#AppName}
LanguageDetectionMethod=locale

OutputDir=output
OutputBaseFilename=$app_name-Windows-Installer
SetupIconFile=..\assets\icons\icon.ico
Compression=lzma
SolidCompression=yes
ArchitecturesInstallIn64BitMode=x64compatible

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"
Name: "italian"; MessagesFile: "compiler:Languages\Italian.isl"

[Files]
Source: "..\dist\$app_name\*"; DestDir: "{app}"; Flags: recursesubdirs

[Icons]
Name: "{group}\$app_name"; Filename: "{app}\$app_name.exe"

[UninstallDelete]
Type: filesandordirs; Name: "{app}"

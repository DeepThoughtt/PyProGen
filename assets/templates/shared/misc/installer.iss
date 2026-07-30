#define Publisher "$publisher"
#define AppName "$app_name"
#define Exe "$app_name.exe"

[Setup]
AppName={#AppName}
AppVersion=0.1.0
AppVerName={#AppName}
AppPublisher={#Publisher}
DefaultDirName={pf}\{#AppName}
DefaultGroupName={#AppName}

OutputDir=output
OutputBaseFilename=$app_name-Windows-Installer
SetupIconFile=..\assets\icons\icon.ico
UninstallDisplayIcon={app}\$app_name.exe
Compression=lzma
SolidCompression=yes
ArchitecturesInstallIn64BitMode=x64
LanguageDetectionMethod=locale

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"
Name: "italian"; MessagesFile: "compiler:Languages\Italian.isl"

[CustomMessages]
english.CreateDesktopIcon=Create a desktop icon
italian.CreateDesktopIcon=Crea un'icona sul desktop
english.AdditionalOptions=Additional options:
italian.AdditionalOptions=Opzioni aggiuntive:
english.Run$app_name=Run $app_name
italian.Run$app_name=Avvia $app_name
english.DeleteUserData=Do you want to delete the saved user data?
italian.DeleteUserData=Vuoi cancellare i dati utente salvati?

[Files]
Source: "..\dist\$app_name\*"; DestDir: "{app}"; Flags: recursesubdirs

[Icons]
Name: "{group}\$app_name"; Filename: "{app}\{#Exe}"
Name: "{commondesktop}\$app_name"; Filename: "{app}\{#Exe}"; Tasks: desktopicon

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalOptions}"; Flags: unchecked

; This code is used to delete the data saved in AppData when uninstalling the software
[Code]
procedure CurUninstallStepChanged (CurUninstallStep: TUninstallStep);
var
    mres : integer;
begin
  case CurUninstallStep of
    usPostUninstall:
      begin
        mres := MsgBox(CustomMessage('DeleteUserData'), mbConfirmation, MB_YESNO or MB_DEFBUTTON2)
        if mres = IDYES then
          DelTree(ExpandConstant('{userappdata}\$app_name'), True, True, True);
      end;
  end;
end;

[UninstallDelete]
Type: filesandordirs; Name: "{app}"

[Run]
Filename: "{app}\{#Exe}"; Description: "{cm:Run$app_name}"; Flags: nowait postinstall skipifsilent

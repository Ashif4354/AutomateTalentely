; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

#define MyAppName "Automate Talentely"
#define MyAppVersion "8.12"
#define MyAppPublisher "DG"
#define MyAppURL "automatetalentely.netlify.app"
#define MyAppExeName "Automate_Talentely.exe"

[Setup]
; NOTE: The value of AppId uniquely identifies this application. Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{5E4252E3-7533-4CFC-A860-E82A7A614260}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
;AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName={autopf}\{#MyAppName}
DisableProgramGroupPage=yes
LicenseFile=D:\PROGRAMMING\PROJECTS\AutomateTalentely\text files\licence.txt
InfoBeforeFile=D:\PROGRAMMING\PROJECTS\AutomateTalentely\text files\info.txt
InfoAfterFile=D:\PROGRAMMING\PROJECTS\AutomateTalentely\text files\after_info.txt
; Uncomment the following line to run in non administrative install mode (install for current user only.)
;PrivilegesRequired=lowest
OutputDir=D:\PROGRAMMING\React apps\AutomateTalentelySite\public
OutputBaseFilename=Automate_Talentely
SetupIconFile=D:\PROGRAMMING\PROJECTS\AutomateTalentely\images\talentelyicon.ico
Compression=lzma
SolidCompression=yes
WizardStyle=modern

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "D:\PROGRAMMING\PROJECTS\AutomateTalentely\output\{#MyAppExeName}"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\PROGRAMMING\PROJECTS\AutomateTalentely\jsonFiles\Answers.json"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\PROGRAMMING\PROJECTS\AutomateTalentely\jsonFiles\Ctests.json"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\PROGRAMMING\PROJECTS\AutomateTalentely\jsonFiles\Qtests.json"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\PROGRAMMING\PROJECTS\AutomateTalentely\jsonFiles\Rtests.json"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\PROGRAMMING\PROJECTS\AutomateTalentely\jsonFiles\tests.json"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\PROGRAMMING\PROJECTS\AutomateTalentely\jsonFiles\Vtests.json"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\PROGRAMMING\PROJECTS\AutomateTalentely\text files\_README.txt"; DestDir: "{app}"; Flags: ignoreversion
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
Name: "{autoprograms}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent


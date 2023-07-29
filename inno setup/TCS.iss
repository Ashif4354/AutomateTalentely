; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

#define MyAppName "Automate Talentely"
#define MyAppVersion "7.6"
#define MyAppPublisher "DG"
#define MyAppURL "https://automatetalentely.netlify.app/"
#define MyAppExeName "Automate_Talentely.exe"

[Setup]
; NOTE: The value of AppId uniquely identifies this application. Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{1B88D635-C828-4F5D-B05A-395FD5E4822F}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
;AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName={autopf}\{#MyAppName}
DefaultGroupName={#MyAppName}
AllowNoIcons=yes
LicenseFile=D:\PROGRAMMING\PROJECTS\AutomateTalentely\licence.txt
InfoBeforeFile=D:\PROGRAMMING\PROJECTS\AutomateTalentely\info.txt
InfoAfterFile=D:\PROGRAMMING\PROJECTS\AutomateTalentely\after_info.txt
; Uncomment the following line to run in non administrative install mode (install for current user only.)
;PrivilegesRequired=lowest
OutputBaseFilename=Automate_Talentely
SetupIconFile=D:\PROGRAMMING\PROJECTS\AutomateTalentely\talentelyicon.ico
Compression=lzma
SolidCompression=yes
WizardStyle=modern

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "D:\PROGRAMMING\PROJECTS\AutomateTalentely\output\Automate Talentely by DG\{#MyAppExeName}"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\PROGRAMMING\PROJECTS\AutomateTalentely\output\Automate Talentely by DG\_README.txt"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\PROGRAMMING\PROJECTS\AutomateTalentely\output\Automate Talentely by DG\Answers.json"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\PROGRAMMING\PROJECTS\AutomateTalentely\output\Automate Talentely by DG\Ctests.json"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\PROGRAMMING\PROJECTS\AutomateTalentely\output\Automate Talentely by DG\Qtests.json"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\PROGRAMMING\PROJECTS\AutomateTalentely\output\Automate Talentely by DG\Rtests.json"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\PROGRAMMING\PROJECTS\AutomateTalentely\output\Automate Talentely by DG\select_tests.html"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\PROGRAMMING\PROJECTS\AutomateTalentely\output\Automate Talentely by DG\styles.css"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\PROGRAMMING\PROJECTS\AutomateTalentely\output\Automate Talentely by DG\tests.json"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\PROGRAMMING\PROJECTS\AutomateTalentely\output\Automate Talentely by DG\Vtests.json"; DestDir: "{app}"; Flags: ignoreversion
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
Name: "{group}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{group}\{cm:ProgramOnTheWeb,{#MyAppName}}"; Filename: "{#MyAppURL}"
Name: "{group}\{cm:UninstallProgram,{#MyAppName}}"; Filename: "{uninstallexe}"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent


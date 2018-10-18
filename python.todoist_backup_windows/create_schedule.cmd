% create C:\Softwares\Schedules\todoist_backup_windows.cmd as a scheduled task and name it TodoistBackup, run once at every 1st monthly %
schtasks /create /tn TodoistBackup /tr "C:\Softwares\Schedules\todoist_backup_windows.cmd" /sc MONTHLY /mo 1 /d 1

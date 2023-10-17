@echo off
set /p msg="Enter message: "
git add -A && git commit -m"%msg%" && git push --all
pause
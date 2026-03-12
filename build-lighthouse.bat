@echo off
echo Lighthouse OS Builder

docker --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
  echo Docker Desktop must be installed first.
  pause
  exit /b
)

docker build -t lighthouse-builder .
docker run -v %cd%\output:/output lighthouse-builder

echo Build complete. ISO is in the output folder.
pause

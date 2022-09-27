Get-ChildItem -Path *.html | Compress-Archive -DestinationPath deploy.zip -Force
Compress-Archive -Path posts -Update -DestinationPath deploy.zip

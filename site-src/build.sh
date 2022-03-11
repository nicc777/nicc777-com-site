#!/bin/sh

mkdocs build

#cp -vf site/404.html site/error.html

cat << EOF > site/error.html
<html>
<head>
<meta http-equiv="refresh" content="2;url=http://www.nicc777.com/" />
<title>Page Moved</title>
</head>
<body>
This page has moved. Click <a href="http://www.nicc777.com/">here</a> to go to the new page.
</body>
</html>
EOF

# cd site
# aws s3 sync ./ s3://www.nicc777.com/ --profile nicc777
# cd ../

python3 prepare_deployment.py --bucket-name="www.nicc777.com" --debug

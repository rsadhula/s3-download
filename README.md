# s3-download
This code allows user to download the file from s3 bucket

It contains
1)downloadfileS3.py script to download the file from s3
2)Dockerfile [Custom docker image]
3).boto file [where acces & secret key added]

For security reasons i have not added AWS Access key & Secret key in .boto file.Please add it & run the docker image.Its working fine & downloading the file from s3 bucket & printing the number of times a keyword is repeated in file

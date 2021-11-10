start:
	docker build -t "aws_test" . && docker run -ti --name aws_test -p 8080:8080 aws_test
start-bg:
	docker build -t "aws_test" . && docker run -tid --name aws_test -p  8080:8080 aws_test
restart:
	docker restart aws_test
build:
	docker build -t "aws_test" .
stop:
	docker stop aws_test
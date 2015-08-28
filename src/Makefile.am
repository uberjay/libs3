AM_CPPFLAGS = 				\
	-Werror				\
	-I$(top_srcdir)/inc

bin_PROGRAMS = s3

s3_SOURCES = s3.c
s3_LDADD = libs3.la

lib_LTLIBRARIES = libs3.la

libs3_la_CFLAGS =			\
	$(LIBCURL_CFLAGS)		\
	$(LIBXML_CFLAGS)

libs3_la_SOURCES = 			\
	acl.c				\
	bucket.c			\
	error_parser.c			\
	general.c			\
	object.c			\
	request.c			\
	request_context.c		\
	response_headers_handler.c	\
	service_access_logging.c	\
	service.c			\
	simplexml.c			\
	util.c

libs3_la_LIBADD = 			\
	$(LIBCURL_LIBS)			\
	$(LIBXML_LIBS)

libs3_la_LDFLAGS =			\
	-no-undefined 			\
	-export-symbols-regex '^S3' 	\
	-version-info 2:0:0

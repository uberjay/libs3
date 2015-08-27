AC_PREREQ([2.60])
AC_INIT([libs3], [2.0], [], [],
        [https://github.com/bji/libs3])
AM_INIT_AUTOMAKE([foreign])
AM_SILENT_RULES([yes])
LT_INIT

AC_CONFIG_SRCDIR([inc/libs3.h])
AC_CONFIG_MACRO_DIR([m4])

AC_PROG_CC
AC_PROG_LIBTOOL

PKG_CHECK_MODULES(LIBCURL, libcurl)
PKG_CHECK_MODULES(LIBXML, libxml-2.0)

AC_DEFINE([LIBS3_VER_MAJOR], [2], [libs3 major version])
AC_DEFINE([LIBS3_VER_MINOR], [0], [libs3 minor version])

AC_OUTPUT([
libs3.pc
Makefile
src/Makefile
inc/Makefile
inc/mingw/Makefile
inc/mingw/sys/Makefile
])

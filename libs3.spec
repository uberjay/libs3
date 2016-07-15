Summary: C Library and Tools for Amazon S3 Access
Name: libs3
Version: 2.0
Release: 1%{?dist}
License: LGPL
Group: Networking/Utilities
URL: http://sourceforge.net/projects/reallibs3
Source: %{name}-%{version}.tar.gz
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root
# Want to include curl dependencies, but older Fedora Core uses curl-devel,
# and newer Fedora Core uses libcurl-devel ... have to figure out how to
# handle this problem, but for now, just don't check for any curl libraries
# Buildrequires: curl-devel
Buildrequires: libxml2-devel
Buildrequires: openssl-devel
Buildrequires: make
# Requires: libcurl
Requires: libxml2
Requires: openssl

%define debug_package %{nil}

%description
This package includes the libs3 shared object library, needed to run
applications compiled against libs3, and additionally contains the s3
utility for accessing Amazon S3.

%package devel
Summary: Headers and documentation for libs3
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This library provides an API for using Amazon's S3 service (see
http://s3.amazonaws.com).  Its design goals are:

 - To provide a simple and straightforward API for accessing all of S3's
   functionality
 - To not require the developer using libs3 to need to know anything about:
     - HTTP
     - XML
     - SSL
   In other words, this API is meant to stand on its own, without requiring
   any implicit knowledge of how S3 services are accessed using HTTP
   protocols.
 - To be usable from multithreaded code
 - To be usable by code which wants to process multiple S3 requests
   simultaneously from a single thread
 - To be usable in the simple, straightforward way using sequentialized
   blocking requests


%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install
rm %{buildroot}/%{_libdir}/*.la

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_libdir}/libs3.so*

%files devel
%defattr(-,root,root,-)
%{_includedir}/*
%{_libdir}/*.a
%{_libdir}/pkgconfig/*.pc

%changelog
* Tue Sep 15 2015  <huber@paradoxical.net> Josh Huber 2.0-1
- Converted build process over to autotools.

* Sat Aug 09 2008  <bryan@ischo,com> Bryan Ischo
- Split into regular and devel packages.

* Tue Aug 05 2008  <bryan@ischo,com> Bryan Ischo
- Initial build.

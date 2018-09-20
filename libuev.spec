#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libuev
Version  : 2.1.3
Release  : 1
URL      : https://github.com/troglobit/libuev/releases/download/v2.1.3/libuev-2.1.3.tar.xz
Source0  : https://github.com/troglobit/libuev/releases/download/v2.1.3/libuev-2.1.3.tar.xz
Summary  : Simple event loop for Linux
Group    : Development/Tools
License  : MIT
Requires: libuev-lib
Requires: libuev-license

%description
libuEv | Simple event loop for Linux
====================================
[![Travis Status][]][Travis] [![Coverity Status][]][Coverity Scan]

%package dev
Summary: dev components for the libuev package.
Group: Development
Requires: libuev-lib = %{version}-%{release}
Provides: libuev-devel = %{version}-%{release}

%description dev
dev components for the libuev package.


%package doc
Summary: doc components for the libuev package.
Group: Documentation

%description doc
doc components for the libuev package.


%package lib
Summary: lib components for the libuev package.
Group: Libraries
Requires: libuev-license = %{version}-%{release}

%description lib
lib components for the libuev package.


%package license
Summary: license components for the libuev package.
Group: Default

%description license
license components for the libuev package.


%prep
%setup -q -n libuev-2.1.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1537475278
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1537475278
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/libuev
cp LICENSE %{buildroot}/usr/share/doc/libuev/LICENSE
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/uev/private.h
/usr/include/uev/queue.h
/usr/include/uev/uev.h
/usr/lib64/libuev.so
/usr/lib64/pkgconfig/libuev.pc

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/libuev/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libuev.so.2
/usr/lib64/libuev.so.2.0.2

%files license
%defattr(-,root,root,-)
/usr/share/doc/libuev/LICENSE

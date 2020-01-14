#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libuev
Version  : 2.3.0
Release  : 4
URL      : https://github.com/troglobit/libuev/releases/download/v2.3.0/libuev-2.3.0.tar.xz
Source0  : https://github.com/troglobit/libuev/releases/download/v2.3.0/libuev-2.3.0.tar.xz
Summary  : Simple event loop for Linux
Group    : Development/Tools
License  : MIT
Requires: libuev-lib = %{version}-%{release}
Requires: libuev-license = %{version}-%{release}

%description
µEv | Simple event loop for Linux
==================================
[![Travis Status][]][Travis] [![Coverity Status][]][Coverity Scan]

%package dev
Summary: dev components for the libuev package.
Group: Development
Requires: libuev-lib = %{version}-%{release}
Provides: libuev-devel = %{version}-%{release}
Requires: libuev = %{version}-%{release}

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
%setup -q -n libuev-2.3.0
cd %{_builddir}/libuev-2.3.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1579038516
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1579038516
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libuev
cp %{_builddir}/libuev-2.3.0/LICENSE %{buildroot}/usr/share/package-licenses/libuev/a40fd030b84039b440f824fda22dad3e3bd411ce
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/uev/private.h
/usr/include/uev/uev.h
/usr/lib64/libuev.so
/usr/lib64/pkgconfig/libuev.pc

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/libuev/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libuev.so.2
/usr/lib64/libuev.so.2.2.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libuev/a40fd030b84039b440f824fda22dad3e3bd411ce

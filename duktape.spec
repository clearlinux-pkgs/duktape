#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : duktape
Version  : 2.7.0
Release  : 6
URL      : https://duktape.org/duktape-2.7.0.tar.xz
Source0  : https://duktape.org/duktape-2.7.0.tar.xz
Summary  : Embeddable Javascript engine
Group    : Development/Tools
License  : MIT
Requires: duktape-lib = %{version}-%{release}
Requires: duktape-license = %{version}-%{release}
Patch1: libm.patch

%description
=======
Duktape
=======
Duktape is a small and portable ECMAScript E5/E5.1 implementation.  It is
intended to be easily embeddable into C programs, with a C API similar in
spirit to Lua's.

%package dev
Summary: dev components for the duktape package.
Group: Development
Requires: duktape-lib = %{version}-%{release}
Provides: duktape-devel = %{version}-%{release}
Requires: duktape = %{version}-%{release}

%description dev
dev components for the duktape package.


%package lib
Summary: lib components for the duktape package.
Group: Libraries
Requires: duktape-license = %{version}-%{release}

%description lib
lib components for the duktape package.


%package license
Summary: license components for the duktape package.
Group: Default

%description license
license components for the duktape package.


%prep
%setup -q -n duktape-2.7.0
cd %{_builddir}/duktape-2.7.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1664558198
unset LD_AS_NEEDED
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
make  %{?_smp_mflags}  -f Makefile.sharedlibrary INSTALL_PREFIX=%{_prefix} LIBDIR=%{_lib}


%install
export SOURCE_DATE_EPOCH=1664558198
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/duktape
cp %{_builddir}/duktape-%{version}/LICENSE.txt %{buildroot}/usr/share/package-licenses/duktape/c441a7053b67826081e515f8e52a10950e20f315 || :
%makeinstall -f Makefile.sharedlibrary DESTDIR=%{buildroot} INSTALL_PREFIX=%{_prefix} LIBDIR=/%{_lib}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/duk_config.h
/usr/include/duktape.h
/usr/lib64/libduktape.so
/usr/lib64/libduktaped.so
/usr/lib64/pkgconfig/duktape.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libduktape.so.207
/usr/lib64/libduktape.so.207.20700
/usr/lib64/libduktaped.so.207
/usr/lib64/libduktaped.so.207.20700

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/duktape/c441a7053b67826081e515f8e52a10950e20f315

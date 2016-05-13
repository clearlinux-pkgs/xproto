#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : xproto
Version  : 7.0.29
Release  : 8
URL      : http://xorg.freedesktop.org/releases/individual/proto/xproto-7.0.29.tar.gz
Source0  : http://xorg.freedesktop.org/releases/individual/proto/xproto-7.0.29.tar.gz
Summary  : Xproto headers
Group    : Development/Tools
License  : MIT
Requires: xproto-doc
BuildRequires : libxslt-bin
BuildRequires : pkgconfig(xorg-macros)
BuildRequires : xmlto

%description
X Window System Core Protocol
This package provides the headers and specification documents defining
the X Window System Core Protocol, Version 11.

%package dev
Summary: dev components for the xproto package.
Group: Development
Provides: xproto-devel

%description dev
dev components for the xproto package.


%package doc
Summary: doc components for the xproto package.
Group: Documentation

%description doc
doc components for the xproto package.


%prep
%setup -q -n xproto-7.0.29

%build
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/X11/DECkeysym.h
/usr/include/X11/HPkeysym.h
/usr/include/X11/Sunkeysym.h
/usr/include/X11/X.h
/usr/include/X11/XF86keysym.h
/usr/include/X11/XWDFile.h
/usr/include/X11/Xalloca.h
/usr/include/X11/Xarch.h
/usr/include/X11/Xatom.h
/usr/include/X11/Xdefs.h
/usr/include/X11/Xfuncproto.h
/usr/include/X11/Xfuncs.h
/usr/include/X11/Xmd.h
/usr/include/X11/Xos.h
/usr/include/X11/Xos_r.h
/usr/include/X11/Xosdefs.h
/usr/include/X11/Xpoll.h
/usr/include/X11/Xproto.h
/usr/include/X11/Xprotostr.h
/usr/include/X11/Xthreads.h
/usr/include/X11/Xw32defs.h
/usr/include/X11/Xwindows.h
/usr/include/X11/Xwinsock.h
/usr/include/X11/ap_keysym.h
/usr/include/X11/keysym.h
/usr/include/X11/keysymdef.h
/usr/lib64/pkgconfig/*.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/xproto/*

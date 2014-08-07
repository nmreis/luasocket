Name:		luasocket
Version:	scm
Release:	1%{?dist}
Summary:	Network support for the Lua language

License:	MIT
URL:		https://github.com/diegonehab/luasocket
Source0:	%{name}-%{version}.tar.gz

BuildRequires: lua52-devel
Requires: lua52

%description
LuaSocket is a Lua extension library that is composed by two parts: a C core
that provides support for the TCP and UDP transport layers, and a set of Lua
modules that add support for functionality commonly needed by applications
that deal with the Internet.

%prep
%setup -q

%build
#make %{?_smp_mflags}
bash make.sh

%install
mkdir -p %{buildroot}/%{_libdir}/lua/5.2
cp -r socket/ %{buildroot}/%{_libdir}/lua/5.2/


%post -p /sbin/ldconfig


%postun -p /sbin/ldconfig


%files
%{_libdir}/lua/5.2/socket/core.so
%{_libdir}/lua/5.2/socket/unix.so
%{_libdir}/lua/5.2/socket/serial.so


%changelog
* Tue Jul 29 2014 FSCloud Release Engineering <nreis@wavecom.pt> - 0.4.4
- First version

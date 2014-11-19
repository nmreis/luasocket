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
make %{?_smp_mflags} linux
bash make.sh

%install
mkdir -p %{buildroot}/%{_libdir}/lua/5.2
mkdir -p %{buildroot}/%{_datadir}/lua/5.2/socket
cp src/ftp.lua %{buildroot}/%{_datadir}/lua/5.2/socket/
cp src/headers.lua %{buildroot}/%{_datadir}/lua/5.2/socket/
cp src/http.lua %{buildroot}/%{_datadir}/lua/5.2/socket/
cp src/smtp.lua %{buildroot}/%{_datadir}/lua/5.2/socket/
cp src/tp.lua %{buildroot}/%{_datadir}/lua/5.2/socket/
cp src/url.lua %{buildroot}/%{_datadir}/lua/5.2/socket/
cp src/socket.lua %{buildroot}/%{_datadir}/lua/5.2/
cp src/mime.lua %{buildroot}/%{_datadir}/lua/5.2/
cp src/ltn12.lua %{buildroot}/%{_datadir}/lua/5.2/
cp -r socket/ %{buildroot}/%{_libdir}/lua/5.2/
cp src/mime.so.1.0.3 %{buildroot}/%{_libdir}/lua/5.2/mime.so


%post -p /sbin/ldconfig


%postun -p /sbin/ldconfig


%files
%{_libdir}/lua/5.2/mime.so
%{_libdir}/lua/5.2/socket/core.so
%{_libdir}/lua/5.2/socket/unix.so
%{_libdir}/lua/5.2/socket/serial.so
%{_datadir}/lua/5.2/socket/*.lua
%{_datadir}/lua/5.2/*.lua


%changelog
* Tue Jul 29 2014 FSCloud Release Engineering <nreis@wavecom.pt> - 0.4.4
- First version

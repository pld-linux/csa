#
# TODO:
# - %%files - FHS compliance (/var/csa is invalid)
# 
Summary:	System job accounting
Summary(pl):	Rozliczanie zada� systemowych
Name:		csa
Version:	2.2.0
Release:	0.1
License:	GPL
Group:		Applications/System
# .src.rpm at ftp://oss.sgi.com/projects/csa/download/
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	8a0f4a052cd9a6a6ad7227fc0b750345
URL:            http://oss.sgi.com/projects/csa/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Linux Comprehensive System Accounting (CSA) is a combination of a
Linux kernel patch, a loadable csa kernel module, and a set of C
programs and shell scripts. CSA provides methods for collecting
per-process resource usage data, monitoring disk usage, and charging
fees to specific login accounts. CSA takes this per-process accounting
information and combines it by job identifier (jid) within system boot
uptime periods.

%description -l pl
Linux Comprehensive System Accounting (CSA) to po��czenie �aty na
j�dro Linuksa, �adowalnego modu�u j�dra csa oraz zbioru program�w w C
i skrypt�w pow�oki. CSA dostarcza metody do gromadzenia danych o
wykorzystaniu zasob�w przez ka�dy proces, monitorowania wykorzystania
dysku oraz pobierania op�at za konkretne konta. CSA pobiera te
informacje rozrachunkowe dla ka�dego procesu i ��czy je po
identyfikatorze zadania (jid - job identifier) w ramach czasu
dzia�ania systemu.

%package libs
Summary:	CSA library
Summary(pl):	Biblioteka CSA
Group:		Libraries

%description libs
CSA library.

%description libs -l pl
Biblioteka CSA.

%package devel
Summary:	Header files for CSA library
Summary(pl):	Pliki nag��wkowe biblioteki CSA
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Header files for CSA library.

%description devel -l pl
Pliki nag��wkowe biblioteki CSA.

%package static
Summary:	Static CSA library
Summary(pl):	Statyczna biblioteka CSA
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static CSA library.

%description static -l pl
Statyczna biblioteka CSA.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR="$RPM_BUILD_ROOT" \
	csainstalluser=$(id -u) \
	csainstallgroup=$(id -g)

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
# COPYING contains additional notes
%doc AUTHORS COPYING ChangeLog NEWS README
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/csa.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/csa.holidays
%attr(754,root,root) /etc/rc.d/init.d/csa
%attr(755,root,root) %{_sbindir}/acctdisk
%attr(755,root,root) %{_sbindir}/acctdusg
%attr(755,root,root) %{_sbindir}/csaaddc
%attr(755,root,root) %{_sbindir}/csachargefee
%attr(755,root,root) %{_sbindir}/csacms
%attr(755,root,root) %{_sbindir}/csacon
%attr(755,root,root) %{_sbindir}/csacrep
%attr(755,root,root) %{_sbindir}/csadrep
%attr(755,root,root) %{_sbindir}/csaedit
%attr(755,root,root) %{_sbindir}/csagetconfig
%attr(755,root,root) %{_sbindir}/csajrep
%attr(755,root,root) %{_sbindir}/csarecy
%attr(755,root,root) %{_sbindir}/csaswitch
%attr(755,root,root) %{_sbindir}/csaverify
%attr(755,root,root) %{_sbindir}/csackpacct
%attr(755,root,root) %{_sbindir}/csaperiod
%attr(755,root,root) %{_sbindir}/csarun
%attr(755,root,root) %{_sbindir}/dodisk
%attr(755,root,root) %{_sbindir}/lastlogin
%attr(755,root,root) %{_sbindir}/nulladm
%attr(755,root,root) %{_sbindir}/csabuild
%attr(755,root,root) %{_bindir}/csacom
%attr(755,root,root) %{_bindir}/ja
%{_mandir}/*/*
# Below here should be owned by csaacct
FIXME FIXME
%defattr(-,csaacct,csaacct)
/var/csa/nite/statefile
%dir /var/csa
%dir /var/csa/day
%dir /var/csa/fiscal
%dir /var/csa/nite
%dir /var/csa/sum
%dir /var/csa/work

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcsa.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcsa.so
%{_libdir}/libcsa.la
%{_includedir}/csa.h
%{_includedir}/csa_api.h
%{_includedir}/csaacct.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libcsa.a

#
# TODO:
# - %%files
# - libs/devel/static subpackages
# 
Name:		csa
Version:	2.2.0
Release:	0.1
Summary:	System job accounting
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	8a0f4a052cd9a6a6ad7227fc0b750345
URL:            http://oss.sgi.com/projects/csa/
License:	GPL
Group:		Applications/System
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Linux Comprehensive System Accounting (CSA) is a combination of a
Linux kernel patch, a loadable csa kernel module, and a set of C
programs and shell scripts. CSA provides methods for collecting
per-process resource usage data, monitoring disk usage, and charging
fees to specific login accounts. CSA takes this per-process accounting
information and combines it by job identifier (jid) within system boot
uptime periods.

%prep
rm -rf $RPM_BUILD_ROOT
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

%files
FIXME FIXME
%defattr(644,root,root,755)
%config %{_sysconfdir}/csa.conf
%config %{_sysconfdir}/csa.holidays
%attr(754,root,root) /etc/rc.d/init.d/csa
%{_includedir}/csa.h
%{_includedir}/csa_api.h
%{_includedir}/csaacct.h
%{_prefix}/lib/libcsa.la
%attr(755,root,root) %{_prefix}/lib/libcsa.so
%attr(755,root,root) %{_prefix}/lib/libcsa.so.1
%attr(755,root,root) %{_prefix}/lib/libcsa.so.1.0.0
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
%doc AUTHORS COPYING INSTALL ChangeLog NEWS README ABOUT-NLS
%{_mandir}/*/*
# Below here should be owned by csaacct
%defattr(-,csaacct,csaacct)
%attr(755,root,root) %{_sbindir}/csabuild
%attr(755,root,root) %{_bindir}/csacom
%attr(755,root,root) %{_bindir}/ja
/var/csa/nite/statefile
%dir /var/csa
%dir /var/csa/day
%dir /var/csa/fiscal
%dir /var/csa/nite
%dir /var/csa/sum
%dir /var/csa/work

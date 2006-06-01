Summary:	Enterprise Audit Shell (EAS)
Name:		eas
Version:	2.0.00
Release:	0.1
License:	Open Software License v2.0
Group:		Applications/Shells
Source0:	http://download.strchr.net/%{name}-%{version}.tar.gz
# Source0-md5:	1fda6b60ad9ac9ea2a40bbb6efeb18d2
Patch0:		%{name}-DESTDIR.patch
URL:		http://download.strchr.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	openssl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/%{name}

%description
EAS allows organizations to centrally audit and report UNIX shell
access. Unlike Sudosh, the audit logs are sent to a centralized
archive and reporting server. Client server authentication and
encryption is handled by SSL. EAS was specifically designed for
enterprise, commercial use.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/var/log/%{name}

%{__make} install -j1 \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog
%doc EAS_Admin_Guide.pdf user.sql
%dir %{_sysconfdir}
%dir %{_sysconfdir}/certs
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/certs/client.pem
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/certs/root.pem
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/certs/server.pem
%dir %{_sysconfdir}/css
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/css/detailed.css
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/css/report.css
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/easd_config
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/eash_config
%attr(755,root,root) %{_bindir}/eas_play
%attr(755,root,root) %{_bindir}/eas_test_pty
%attr(755,root,root) %{_bindir}/eas_version
%attr(755,root,root) %{_bindir}/eash
%attr(755,root,root) %{_sbindir}/eas_dbtool
%attr(755,root,root) %{_sbindir}/eas_replay
%attr(755,root,root) %{_sbindir}/eas_report
%attr(755,root,root) %{_sbindir}/easd

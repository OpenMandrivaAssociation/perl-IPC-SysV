%define upstream_name    IPC-SysV
%define upstream_version 2.04

Name:       perl-%{upstream_name}
Version:    %perl_convert_version 2.04
Release:	2

Summary:    System V shared memory, semaphores, messages
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/IPC/IPC-SysV-2.04.tar.gz

BuildRequires: perl(Test::More)
BuildRequires: perl-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
A class providing an object based interface to SysV IPC message queues.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README Changes
%{_mandir}/man3/*
%perl_vendorlib/*




%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 2.30.0-5
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Sat Nov 13 2010 Jérôme Quelin <jquelin@mandriva.org> 2.30.0-4mdv2011.0
+ Revision: 597099
- rebuild

* Wed Jul 28 2010 Jérôme Quelin <jquelin@mandriva.org> 2.30.0-3mdv2011.0
+ Revision: 562427
- rebuild

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 2.30.0-2mdv2011.0
+ Revision: 555966
- rebuild for perl 5.12

* Mon Jul 12 2010 Jérôme Quelin <jquelin@mandriva.org> 2.30.0-1mdv2011.0
+ Revision: 551223
- update to 2.03

* Mon Mar 08 2010 Jérôme Quelin <jquelin@mandriva.org> 2.20.0-1mdv2010.1
+ Revision: 515653
- update to 2.02

* Sun Jul 12 2009 Jérôme Quelin <jquelin@mandriva.org> 2.10.0-1mdv2010.0
+ Revision: 395359
- import perl-IPC-SysV


* Sun Jul 12 2009 cpan2dist 2.01-1mdv
- initial mdv release, generated with cpan2dist


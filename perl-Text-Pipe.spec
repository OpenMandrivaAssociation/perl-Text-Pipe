%define upstream_name    Text-Pipe
%define upstream_version 0.10

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Common text filter API
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Text/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Class::Accessor)
BuildRequires:	perl(Class::Accessor::Complex)
BuildRequires:	perl(Class::Accessor::Constructor)
BuildRequires:	perl(Class::Accessor::Installer)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(List::Util)
BuildRequires:	perl(Sub::Name)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(UNIVERSAL::require)
BuildArch:	noarch

%description
This class is a factory for text pipes. A pipe has a 'filter()' method
through which input can pass. The input can be a string or a reference to
an array of strings. Pipes can be stacked together using the
Text::Pipe::Stackable manpage.

The problem that this distribution tries to solve is that there are several
distributions on CPAN which use text filtering in some way or other, for
example the Template Toolkit. But each distribution is somewhat different,
and they have to reimplement the same text filters over and over again.

This distribution aims at offering a common text filter API. So if you want
to use text pipes with Template Toolkit, you just need to write an adapter.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
# wants to download junk from Internet
rm -f inc/Module/AutoInstall.pm

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 25 2011 Funda Wang <fwang@mandriva.org> 0.100.0-2mdv2011.0
+ Revision: 658410
- rebuild for updated rpm-setup

* Sat Sep 19 2009 Jérôme Quelin <jquelin@mandriva.org> 0.100.0-1mdv2010.0
+ Revision: 444616
- update to 0.10
- import perl-Text-Pipe


* Thu Sep 17 2009 cpan2dist 0.08-1mdv
- initial mdv release, generated with cpan2dist

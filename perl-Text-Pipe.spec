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
BuildRequires:	perl(Module::AutoInstall)
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
